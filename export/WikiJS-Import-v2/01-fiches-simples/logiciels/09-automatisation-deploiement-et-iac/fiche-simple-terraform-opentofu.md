---
title: "Terraform / OpenTofu"
description: "Installer Terraform ou OpenTofu sur Debian 13, valider le cycle init, plan, apply sur une configuration de test qui ne crée aucune ressource réelle, puis préparer un usage d'équipe : version figée, état distant protégé, aucun secret dans le code. Un apply lancé sans plan relu peut modifier une infra"
published: true
date: 2026-10-29T11:50:26Z
tags: ["[debian-13]", "[terraform]", "[opentofu]", "[iac]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T11:50:26Z
dateModified: 2026-10-29T11:50:26Z
---

# 📄 Terraform / OpenTofu

- **Environnement** : Poste d'administration (Debian 13)
- **OS / Version** : Debian 13 (trixie)
- **Version** : Terraform 1.x (`<version_terraform>`) ou OpenTofu 1.x (`<version_opentofu>`), à vérifier sur la version déployée
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `[debian-13]`, `[terraform]`, `[opentofu]`, `[iac]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Terraform ou OpenTofu sur Debian 13, valider le cycle `init`, `plan`, `apply` sur une configuration de test qui ne crée aucune ressource réelle, puis préparer un usage d'équipe : version figée, état distant protégé, aucun secret dans le code. Un `apply` lancé sans plan relu peut modifier une infrastructure de production : la procédure impose de relire le plan avant chaque application.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des outils de téléchargement et de décompression :
```bash
sudo apt update
sudo apt install -y unzip curl
```
👉 Explication : `unzip` décompresse les binaires officiels, `curl` les télécharge.

2. Installation de Terraform (binaire officiel HashiCorp, vérifié par empreinte) :
```bash
cd /tmp
curl -LO https://releases.hashicorp.com/terraform/<version_terraform>/terraform_<version_terraform>_linux_amd64.zip
curl -LO https://releases.hashicorp.com/terraform/<version_terraform>/terraform_<version_terraform>_SHA256SUMS
sha256sum -c --ignore-missing terraform_<version_terraform>_SHA256SUMS
unzip terraform_<version_terraform>_linux_amd64.zip
sudo install -o root -g root -m 0755 terraform /usr/local/bin/terraform
terraform version
```
👉 Explication : `<version_terraform>` est le numéro de version publié sur `releases.hashicorp.com/terraform/` (à vérifier sur la version déployée). `sha256sum -c` doit répondre `OK` : un `FAILED` impose de ne pas installer le binaire. La dernière commande affiche la version installée.

3. Installation facultative d'OpenTofu (alternative libre, mêmes commandes avec `tofu`) :
```bash
cd /tmp
curl -LO https://github.com/opentofu/opentofu/releases/download/v<version_opentofu>/tofu_<version_opentofu>_linux_amd64.zip
curl -LO https://github.com/opentofu/opentofu/releases/download/v<version_opentofu>/tofu_<version_opentofu>_SHA256SUMS
sha256sum -c --ignore-missing tofu_<version_opentofu>_SHA256SUMS
unzip tofu_<version_opentofu>_linux_amd64.zip
sudo install -o root -g root -m 0755 tofu /usr/local/bin/tofu
tofu version
```
👉 Explication : Même principe que pour Terraform. `<version_opentofu>` est la version publiée sur la page des releases du projet OpenTofu (à vérifier sur la version déployée). Le nom des archives suit le modèle habituel du projet ; si le téléchargement échoue, vérifier le nom exact sur la page des releases.

4. Création d'un projet de test sans ressource réelle :
```bash
mkdir -p ~/tf-lab
nano ~/tf-lab/main.tf
```
Contenu du fichier :
```hcl
terraform {
  required_version = ">= 1.5.0"
}

resource "terraform_data" "lab" {
  input = "test-lab"
}

output "valeur_lab" {
  value = terraform_data.lab.output
}
```
👉 Explication : `terraform_data` est une ressource intégrée, qui ne crée rien chez un fournisseur : elle permet de tester le cycle complet sans compte cloud. Le bloc `terraform` fixe la version minimale du moteur.

5. Initialisation, mise en forme et validation :
```bash
cd ~/tf-lab
terraform init
terraform fmt -check
terraform validate
```
👉 Explication : `init` prépare le répertoire de travail (plugins, état). `fmt -check` vérifie la mise en forme sans modifier les fichiers. `validate` contrôle la syntaxe et la cohérence de la configuration. Avec OpenTofu, remplacer `terraform` par `tofu`.

6. Calcul du plan, relecture, puis application :
```bash
terraform plan -out=tfplan
terraform apply tfplan
terraform output valeur_lab
```
👉 Explication : `plan -out` enregistre le plan exact dans le fichier `tfplan`. `apply tfplan` applique ce plan relu, sans recalcul. `terraform output valeur_lab` affiche la valeur attendue `"test-lab"` (guillemets inclus, comportement d'affichage à vérifier sur la version déployée).

7. Destruction du test :
```bash
terraform destroy
```
👉 Explication : Supprime les ressources créées par le test. Le fichier `terraform.tfstate` reste dans le dossier : il contient l'état du lab et ne doit pas être réutilisé ailleurs.

---

## ⚡ 2. Production — Façon Simplifiée
1. Version figée et fournisseurs verrouillés. Ajouter au bloc `terraform` du projet :
```hcl
terraform {
  required_version = "~> <version_terraform>"

  required_providers {
    <nom_fournisseur> = {
      source  = "<espace_fournisseur>/<nom_fournisseur>"
      version = "~> <version_fournisseur>"
    }
  }
}
```
Puis :
```bash
terraform init
```
👉 Explication : `required_version` empêche d'exécuter le projet avec une version non testée. `<nom_fournisseur>`, `<espace_fournisseur>` et `<version_fournisseur>` désignent le fournisseur utilisé (par exemple un hyperviseur ou un fournisseur cloud) et sa version validée. `init` crée le fichier `.terraform.lock.hcl` qui fige les versions : il doit être versionné.

2. Séparation des valeurs de configuration. Créer `~/tf-prod/prod.tfvars` avec les valeurs propres à l'environnement :
```hcl
environnement = "<nom_environnement>"
```
Puis :
```bash
terraform plan -var-file=prod.tfvars -out=tfplan
```
👉 Explication : Les paramètres d'environnement restent hors du code, ce qui permet de réutiliser la même configuration pour le test et la production. La variable `environnement` doit être déclarée dans le code (`variable "environnement" { type = string }`). `<nom_environnement>` est par exemple `lab` ou `prod`.

3. Relecture obligatoire du plan avant application :
```bash
terraform show tfplan
terraform apply tfplan
```
👉 Explication : `show tfplan` affiche les créations, modifications et suppressions prévues. Le plan doit être relu et validé par une seconde personne avant `apply`. `apply tfplan` n'applique que ce plan, sans recalcul.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. État distant avec verrouillage. Ajouter dans le bloc `terraform` :
```hcl
  backend "s3" {
    bucket       = "<nom_bucket_etat>"
    key          = "<chemin_fichier_etat>"
    region       = "<region>"
    encrypt      = true
    use_lockfile = true
  }
```
Puis :
```bash
terraform init -migrate-state
```
👉 Explication : L'état (qui contient des valeurs sensibles) est stocké dans un bucket chiffré côté serveur plutôt que sur le poste. `use_lockfile` évite deux applications simultanées (fonction disponible à partir de Terraform 1.10, à vérifier sur la version déployée et pour OpenTofu). `<nom_bucket_etat>`, `<chemin_fichier_etat>` et `<region>` sont à remplacer par les valeurs du stockage choisi. Le compte d'accès doit avoir uniquement les droits sur ce bucket.

2. Aucun secret dans le code. Déclarer les variables sensibles :
```hcl
variable "mot_de_passe_admin" {
  type      = string
  sensitive = true
}
```
Fournir la valeur par l'environnement, sans l'écrire dans un fichier :
```bash
export TF_VAR_mot_de_passe_admin='<valeur_secrete>'
terraform plan -out=tfplan
```
👉 Explication : `sensitive = true` masque la valeur dans les sorties. `TF_VAR_` est le préfixe reconnu pour lire une variable depuis l'environnement. `<valeur_secrete>` doit provenir du coffre de l'entreprise (Passbolt ou Vaultwarden du pack). Ne jamais écrire de secret dans `.tf` ou `.tfvars`.

3. Exclusion des fichiers sensibles du dépôt Git. Créer `~/tf-prod/.gitignore` :
```
.terraform/
*.tfstate
*.tfstate.backup
*.tfvars
tfplan
```
👉 Explication : Ces fichiers contiennent l'état, les plans et les valeurs d'environnement. Le fichier `.terraform.lock.hcl`, lui, doit rester versionné. Si un secret a déjà été commité, il faut le révoquer et le retirer de l'historique.

4. Protection des fichiers locaux :
```bash
chmod 600 ~/tf-prod/prod.tfvars
chmod 600 ~/tf-prod/tfplan
ls -l ~/tf-prod
```
👉 Explication : Réserve la lecture des fichiers de valeurs et de plan à leur propriétaire. Un plan enregistré peut révéler des valeurs sensibles.

5. Vérification de l'intégrité du binaire et version figée de l'outil : reprendre la vérification d'empreinte de la fiche Packer (`sha256sum -c`) et la vérification GPG du fichier SHA256SUMS. Consigner la version de Terraform ou OpenTofu utilisée dans le dépôt, par exemple dans le bloc `required_version`.
👉 Explication : Le binaire qui applique l'infrastructure a les mêmes droits que son administrateur : il doit être authentifié comme n'importe quel logiciel d'administration (commandes exactes de vérification GPG à vérifier sur la version déployée).

6. Chiffrement de l'état côté outil (OpenTofu uniquement) : dans un projet OpenTofu, un bloc `encryption` permet de chiffrer le fichier d'état avant son envoi au backend. Terraform ne propose pas ce chiffrement : dans ce cas, le chiffrement au repos du bucket et les droits d'accès restrictifs sont obligatoires.
👉 Explication : Ce point est une recommandation : la syntaxe exacte du bloc `encryption` dépend de la version d'OpenTofu et doit être vérifiée sur la version déployée avant mise en œuvre.

---