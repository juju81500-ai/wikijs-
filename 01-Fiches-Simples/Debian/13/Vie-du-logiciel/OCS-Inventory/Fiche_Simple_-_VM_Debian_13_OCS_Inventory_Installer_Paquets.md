# Fiche_Simple_-_VM_Debian_13_OCS_Inventory_Installer_Paquets.md

- **Environnement** : VM Debian 13 dédiée, OCS Inventory 3.0 (Nginx, uWSGI, PostgreSQL local)
- **OS / Version** : Debian 13 Trixie; OCS Inventory 3.0; PostgreSQL 17
- **Catégorie** : inventaire de parc / ITSM
- **Tags** : `debian13`, `ocs-inventory`, `ocs3`, `postgresql`, `nginx`, `apt`

---

## Problème précis à résoudre

Ajouter le dépôt officiel OCS Inventory 3 pour trixie et installer le serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Importer la clé de signature et déclarer le dépôt :
   ```bash
   curl -fsSL https://deb-v3.ocsinventory-ng.org/repo-signing-key.gpg \
     | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/ocs-archive-keyring.gpg
   echo "deb https://deb-v3.ocsinventory-ng.org/ trixie main" \
     | sudo tee /etc/apt/sources.list.d/ocsinventory.list
   ```
   👉 Explication : la clé permet à APT de vérifier les paquets; le dépôt cible la suite `trixie`.

2. Mettre à jour l'index et contrôler l'origine du paquet :
   ```bash
   sudo apt update
   apt-cache policy ocsinventory-server
   ```
   👉 Explication : le candidat doit provenir de `deb-v3.ocsinventory-ng.org`.

3. Installer le serveur :
   ```bash
   sudo apt install ocsinventory-server
   ```
   👉 Explication : installe le backend, la console et les services Nginx/uWSGI.

## 2. Production — Contrôles

Figer la version installée, documenter la source du dépôt et prévoir un miroir interne si nécessaire.

## 3. Production — Sécurité

- Confirmer l'origine du paquet avant installation.
- Ne pas ajouter d'autres dépôts tiers sur cette VM.

## Validation et retour arrière

- **Validation** : `apt-cache policy ocsinventory-server` montre le paquet installé depuis le dépôt officiel.
- **Retour arrière** : `sudo apt remove ocsinventory-server`, puis supprimer `/etc/apt/sources.list.d/ocsinventory.list` si le dépôt n'est plus voulu.

## Si le problème n'est pas résolu

- [OCS Inventory — Dépôts officiels](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/installation-methods/using-official-repositories.md)
- [Guide complet OCS Inventory 3 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/41_Deploiement_OCS_Inventory_3_Debian_13.md#3-ajouter-le-depot-officiel-et-installer-ocs)
