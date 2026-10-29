# 📄 Packer

- **Environnement** : Poste d'administration ou VM de build (Debian 13)
- **OS / Version** : Debian 13 (trixie)
- **Version** : Packer 1.x (`<version_packer>`, binaire officiel HashiCorp, à vérifier sur la version déployée)
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `[debian-13]`, `[packer]`, `[hashicorp]`, `[image-template]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Packer sur Debian 13, valider un modèle de construction d'image (format HCL) sans VM réelle, puis préparer un build reproductible : version figée, variables externalisées, binaire vérifié par empreinte. Packer construit des images (template de VM) à partir d'un modèle ; une image mal construite se déploie ensuite partout, d'où l'importance de la vérification.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des outils de téléchargement et de décompression :
```bash
sudo apt update
sudo apt install -y unzip curl
```
👉 Explication : `unzip` décompresse l'archive officielle de Packer, `curl` la télécharge.

2. Téléchargement de Packer et de son fichier d'empreintes SHA256 :
```bash
cd /tmp
curl -LO https://releases.hashicorp.com/packer/<version_packer>/packer_<version_packer>_linux_amd64.zip
curl -LO https://releases.hashicorp.com/packer/<version_packer>/packer_<version_packer>_SHA256SUMS
sha256sum -c --ignore-missing packer_<version_packer>_SHA256SUMS
```
👉 Explication : `<version_packer>` est le numéro de version publié sur `releases.hashicorp.com/packer/` (à vérifier sur la version déployée). La commande `sha256sum -c` compare l'empreinte de l'archive à celle publiée : la réponse attendue est `OK`. Un `FAILED` signifie que le fichier est altéré : ne pas l'installer.

3. Installation du binaire dans le chemin système :
```bash
unzip packer_<version_packer>_linux_amd64.zip
sudo install -o root -g root -m 0755 packer /usr/local/bin/packer
packer version
```
👉 Explication : Décompresse le binaire `packer`, le copie dans `/usr/local/bin` avec les droits `root` en lecture et exécution pour tous, puis affiche la version installée.

4. Création d'un projet de test avec un modèle minimal (builder `null`, sans VM) :
```bash
mkdir -p ~/packer-lab
nano ~/packer-lab/lab.pkr.hcl
```
Contenu du fichier :
```hcl
packer {
  required_plugins {
    null = {
      source  = "github.com/hashicorp/null"
      version = ">= 1.0.0"
    }
  }
}

source "null" "lab" {
  communicator = "none"
}

build {
  sources = ["source.null.lab"]

  provisioner "shell-local" {
    inline = ["echo Build de test OK"]
  }
}
```
👉 Explication : Le builder `null` ne crée aucune VM : il permet de tester la chaîne `init`, `validate` et `build` sur le poste. Les blocs `packer` et `required_plugins` déclarent le plugin nécessaire. Le modèle réel (builder `qemu`, `vsphere-iso` ou autre) remplacera ce bloc `source` plus tard.

5. Téléchargement des plugins, formatage et validation du modèle :
```bash
cd ~/packer-lab
packer init .
packer fmt -check .
packer validate .
```
👉 Explication : `packer init` télécharge le plugin déclaré. `packer fmt -check` vérifie la mise en forme sans rien modifier : un code de retour non nul signale un écart (corriger avec `packer fmt .`). `packer validate` contrôle la cohérence du modèle. Les sorties attendues sont des messages sans erreur, `The configuration is valid.` à vérifier sur la version déployée.

6. Exécution du build de test :
```bash
packer build .
```
👉 Explication : Lance le build : le provisioner `shell-local` affiche `Build de test OK` sur le poste. Un build sans erreur confirme que la chaîne fonctionne avant de passer à un vrai builder.

---

## ⚡ 2. Production — Façon Simplifiée
1. Séparation du modèle et des variables. Ajouter ces déclarations au début de `~/packer-lab/lab.pkr.hcl` :
```hcl
variable "nom_image" {
  type    = string
  default = "lab-image"
}

variable "version_image" {
  type    = string
  default = "0.0.1"
}
```
La valeur par défaut permet de garder le test de lab (`packer validate .`) fonctionnel ; le fichier de variables de production la remplace.
Créer ensuite `~/packer-lab/prod.pkrvars.hcl` avec les valeurs :
```hcl
nom_image     = "<nom_image>"
version_image = "<version_image>"
```
Puis valider et construire avec ce fichier :
```bash
packer validate -var-file=prod.pkrvars.hcl .
packer build -var-file=prod.pkrvars.hcl .
```
👉 Explication : `<nom_image>` et `<version_image>` sont des valeurs propres au projet (par exemple `debian13-base` et `2026.10.1`). Les valeurs variables restent hors du modèle, ce qui permet de réutiliser le même modèle pour plusieurs environnements.

2. Version figée des plugins. Dans le bloc `required_plugins` du modèle, remplacer `">= 1.0.0"` par une version précise, puis relancer `init` :
```bash
packer init .
```
👉 Explication : Une contrainte `>= 1.0.0` peut installer une version différente à chaque exécution. Une version figée garantit des builds reproductibles. Le fichier de verrouillage généré par `packer init` (à vérifier sur la version déployée) doit être versionné.

3. Contrôle avant build, dans cet ordre :
```bash
packer fmt -check .
packer validate -var-file=prod.pkrvars.hcl .
```
👉 Explication : Ces deux contrôles doivent passer avant tout `packer build` en production. Les intégrer dans le dépôt Git ou la chaîne CI de l'équipe.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérification de l'authenticité du fichier d'empreintes (signature GPG) avant installation :
```bash
curl -LO https://releases.hashicorp.com/packer/<version_packer>/packer_<version_packer>_SHA256SUMS.sig
curl -fsSL https://www.hashicorp.com/.well-known/pgp-key.txt | gpg --import
gpg --verify packer_<version_packer>_SHA256SUMS.sig packer_<version_packer>_SHA256SUMS
sha256sum -c --ignore-missing packer_<version_packer>_SHA256SUMS
```
👉 Explication : La première vérification (`gpg --verify`) confirme que le fichier d'empreintes est bien signé par HashiCorp. La seconde contrôle l'archive. Ne pas installer Packer si l'une des deux échoue. L'URL de la clé publique HashiCorp est à vérifier sur la version déployée.

2. Variables sensibles hors des fichiers. Dans le modèle, déclarer la variable comme confidentielle :
```hcl
variable "mot_de_passe_build" {
  type      = string
  sensitive = true
}
```
Fournir la valeur par l'environnement, sans l'écrire dans un fichier :
```bash
export PKR_VAR_mot_de_passe_build='<valeur_secrete>'
packer build .
```
👉 Explication : `sensitive = true` masque la valeur dans les journaux. `PKR_VAR_` est le préfixe reconnu par Packer pour lire une variable depuis l'environnement. `<valeur_secrete>` doit venir du coffre de l'entreprise (Passbolt ou Vaultwarden, voir le pack), jamais d'un fichier versionné.

3. Protection du fichier de variables et exclusion de Git :
```bash
chmod 600 ~/packer-lab/prod.pkrvars.hcl
printf '%s\n' '*.pkrvars.hcl' '.env' >> ~/packer-lab/.gitignore
```
👉 Explication : Réserve la lecture du fichier de variables à son propriétaire. Les motifs ajoutés au fichier `.gitignore` empêchent d'envoyer ces fichiers dans le dépôt. Si un fichier de ce type a déjà été commité, il faut le retirer de l'historique et changer les secrets concernés.

4. Build reproductible avec traçabilité :
```bash
cd ~/packer-lab
packer build -var-file=prod.pkrvars.hcl -on-error=cleanup .
```
👉 Explication : `-on-error=cleanup` supprime automatiquement les ressources temporaires créées pendant le build en cas d'erreur, ce qui évite les machines orphelines. C'est le comportement par défaut ; `-on-error=abort` les laisserait en place pour diagnostic (options à vérifier sur la version déployée). Consigner la version de Packer, la version des plugins et la date du build dans le journal de l'équipe.

5. Contrôle de la surface d'accès des images produites : ajouter un provisioner final dans le modèle qui supprime les mots de passe par défaut, les clés SSH de build et les jetons temporaires, puis tester l'image produite avant publication.
👉 Explication : Une image de référence ne doit contenir aucun identifiant de construction, sinon chaque machine déployée à partir d'elle l'hérite. Le contenu exact du provisioner dépend de l'hyperviseur et de l'OS cible (à compléter selon le cas, à vérifier sur la version déployée).

---
