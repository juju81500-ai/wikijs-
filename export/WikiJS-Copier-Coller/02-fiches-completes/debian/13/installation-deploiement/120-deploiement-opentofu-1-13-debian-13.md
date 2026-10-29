# Déployer OpenTofu 1.13 sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; OpenTofu 1.13.2
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : poste ou serveur d'administration IaC, dépôt APT officiel, projet pilote sans fournisseur cloud, état et sauvegarde
- **Catégorie** : automatisation / infrastructure as code

## 1. Version et périmètre

Fiche simple : [cadrer version et périmètre](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-cadrer-version).

Au 29 octobre 2026, la dernière version stable publiée par le projet est OpenTofu 1.13.2 (branche documentaire 1.13.x). Le dépôt amont contient un fichier `LICENSE` (MPL-2.0, avec copyright OpenTofu Authors et HashiCorp, Inc. pour l'héritage); le valider avant redistribution. Le binaire s'appelle `tofu`.

Cette fiche installe l'outil CLI et valide un cycle complet `init`, `plan`, `apply`, `destroy` avec la ressource intégrée `terraform_data`, donc sans compte cloud ni fournisseur externe. Elle ne décrit aucun fournisseur (Proxmox, Azure, AWS, GCP...) : chaque fournisseur exige sa propre fiche, ses identifiants et son modèle de droits. Terraform de HashiCorp n'est pas couvert ici.

## 2. Installer depuis le dépôt APT officiel

Fiche simple : [installer OpenTofu](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-installer).

Le projet documente un dépôt Debian générique (`any`). Un script `install-opentofu.sh` existe aussi; les étapes manuelles ci-dessous évitent d'exécuter en root un script non relu.

```bash
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://get.opentofu.org/opentofu.gpg | sudo tee /etc/apt/keyrings/opentofu.gpg >/dev/null
curl -fsSL https://packages.opentofu.org/opentofu/tofu/gpgkey | sudo gpg --no-tty --batch --dearmor -o /etc/apt/keyrings/opentofu-repo.gpg >/dev/null
sudo chmod a+r /etc/apt/keyrings/opentofu.gpg /etc/apt/keyrings/opentofu-repo.gpg
```

```bash
echo "deb [signed-by=/etc/apt/keyrings/opentofu.gpg,/etc/apt/keyrings/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main" | sudo tee /etc/apt/sources.list.d/opentofu.list >/dev/null
echo "deb-src [signed-by=/etc/apt/keyrings/opentofu.gpg,/etc/apt/keyrings/opentofu-repo.gpg] https://packages.opentofu.org/opentofu/tofu/any/ any main" | sudo tee -a /etc/apt/sources.list.d/opentofu.list >/dev/null
sudo chmod a+r /etc/apt/sources.list.d/opentofu.list
sudo apt-get update
sudo apt-get install -y tofu
```

Vérifier la version et l'origine du paquet :

```bash
tofu version
apt-cache policy tofu
```

Pour figer la version en production, installer explicitement la version retenue (`apt-cache madison tofu` liste les versions) puis la placer en `apt-mark hold tofu` jusqu'à la fenêtre de mise à jour.

## 3. Compte et répertoire de travail à droits minimaux

Fiche simple : [préparer le compte et les droits](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-droits-minimaux).

Ne pas exécuter `tofu` en root. Utiliser un compte nominatif ou de service sans `sudo`, propriétaire d'un répertoire dédié, par exemple `~/iac/pilote`. Les identifiants des futurs fournisseurs doivent être portés par des variables d'environnement ou un gestionnaire de secrets, jamais écrits dans les fichiers `.tf`.

## 4. Valider avec un projet pilote sans fournisseur

Fiche simple : [valider le projet pilote](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-projet-pilote).

```bash
mkdir -p ~/iac/pilote && cd ~/iac/pilote
```

Créer `main.tf` :

```hcl
terraform {
  required_version = ">= 1.13.0, < 1.14.0"
}

variable "service_name" {
  type        = string
  description = "Nom logique du service de test"
  default     = "pilote-iac"
}

resource "terraform_data" "pilote" {
  input = {
    nom  = var.service_name
    etat = "valide"
  }
}

output "pilote" {
  value = terraform_data.pilote.output
}
```

Puis exécuter :

```bash
tofu fmt -check
tofu init -input=false
tofu validate
tofu plan -input=false -out=pilote.tfplan
tofu apply -input=false pilote.tfplan
tofu state list
tofu plan -detailed-exitcode
```

Résultats attendus : `Success! The configuration is valid.`, une ressource `terraform_data.pilote` dans l'état et un second `plan` avec le code de sortie `0` (aucun changement; `2` signale une dérive). Le fichier `.terraform.lock.hcl` n'est créé que lorsqu'un fournisseur externe est utilisé; il doit alors être versionné.

Nettoyer le pilote :

```bash
tofu destroy -auto-approve
```

`-auto-approve` convient à ce pilote jetable. En production, relire chaque plan et n'appliquer qu'un plan enregistré ou approuvé.

## 5. Gérer l'état, les verrous et les secrets

Fiche simple : [protéger l'état et les secrets](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-proteger-etat).

Par défaut, l'état est un fichier local `terraform.tfstate`. Il peut contenir des valeurs sensibles en clair. Pour un usage partagé, choisir un backend distant avec verrouillage (voir documentation des backends) et limiter l'accès à l'état aux seuls exécutants autorisés.

OpenTofu sait chiffrer l'état et les plans (bloc `terraform { encryption { ... } }` ou variable `TF_ENCRYPTION`). La documentation précise les limites : le chiffrement ne protège pas contre la perte de données ni contre le rejeu d'un ancien état, et l'état devient illisible sans la clé. Avant activation, faire une copie temporaire non chiffrée de l'état, sauvegarder les clés séparément et tester la restauration. Avec un KMS, utiliser une clé distincte par état.

Ne jamais committer `terraform.tfstate`, `*.tfplan` ni les fichiers de variables contenant des secrets; ajouter ces motifs au `.gitignore`.

## 6. Vérifier

Fiche simple : [vérifier le projet et le plan](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-verifier).

- `tofu version` affiche la version attendue et `apt-cache policy tofu` montre le dépôt `packages.opentofu.org`.
- `tofu validate` réussit et `tofu fmt -check` ne renvoie aucun écart.
- Le plan pilote est reproductible et le second plan ne montre aucun changement.
- Aucun secret n'apparaît dans les fichiers du projet, l'historique du shell ou les journaux de CI.

## 7. Mettre à jour, sauvegarder et revenir en arrière

Fiche simple : [mettre à jour et préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-mise-a-jour-rollback).

Sauvegarder l'état (et sa clé de chiffrement si activée) avant chaque mise à niveau d'OpenTofu ou de fournisseur. Tester d'abord sur une copie du projet, lire les notes de version, puis comparer `tofu plan` avant/après : un plan inattendu bloque la mise à niveau. Après une montée de version, un état peut ne plus être lisible par la version précédente : conserver la sauvegarde pour le retour arrière.

Retour arrière du binaire : réinstaller la version précédente (`apt-get install tofu=<version>`) et restaurer la sauvegarde d'état correspondante. Retrait complet : `sudo apt-get remove tofu`, puis suppression de `/etc/apt/sources.list.d/opentofu.list` et de `/etc/apt/keyrings/opentofu*.gpg`.

## 8. Limites

Fiche simple : [vérifier les limites et dépendances](/01-fiches-simples/debian/13/vie-du-logiciel/opentofu/fiche-simple-vm-debian-13-opentofu-limites).

- Aucun fournisseur d'infrastructure n'est configuré ni validé par cette fiche.
- Le pilote ne prouve pas la compatibilité d'un module ou d'un fournisseur écrit pour Terraform.
- La gestion multi-équipes (CI, revue, états distants, approbations) reste à définir par l'organisation.

## Sources

- [OpenTofu — Installation sur Debian/Ubuntu](https://opentofu.org/docs/intro/install/deb/)
- [OpenTofu — Chiffrement de l'état](https://opentofu.org/docs/language/state/encryption/)
- [OpenTofu — Commande init](https://opentofu.org/docs/cli/commands/init/)
- [OpenTofu — Commande plan](https://opentofu.org/docs/cli/commands/plan/)
- [OpenTofu — Verrouillage de l'état](https://opentofu.org/docs/language/state/locking/)
- [OpenTofu — Fichier de verrouillage des dépendances](https://opentofu.org/docs/language/files/dependency-lock/)
- [OpenTofu — Backends](https://opentofu.org/docs/language/settings/backends/configuration/)
- [OpenTofu — Licence](https://github.com/opentofu/opentofu/blob/main/LICENSE)
- [OpenTofu — Versions publiées](https://github.com/opentofu/opentofu/releases)