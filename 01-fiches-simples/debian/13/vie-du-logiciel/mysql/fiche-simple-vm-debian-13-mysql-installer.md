# Fiche_Simple_-_VM_Debian_13_MySQL_Installer

- **Environnement** : [[Glossary:VM]] Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Installer
- **Tags** : `debian13`, `mysql`, `installation`

---

## Problème précis à résoudre

Installer MySQL Community (version [[Glossary:LTS]]) depuis le dépôt [[Glossary:APT]] officiel Oracle avec vérification de la source.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le paquet de configuration du dépôt :
   ```bash
   cd ~ && curl -fLO https://dev.mysql.com/get/mysql-apt-config_VERSION_all.deb
   ```
   👉 Explication : remplacer `VERSION` par le numéro publié sur la page de téléchargement MySQL APT repository (à vérifier) ; contrôler la somme MD5/SHA publiée.

2. Installer le dépôt (choisir la série LTS) :
   ```bash
   sudo apt install ./mysql-apt-config_VERSION_all.deb
   sudo apt update
   ```
   👉 Explication : l'assistant propose la série du serveur : retenir la LTS (8.4).

3. Vérifier l'origine puis installer :
   ```bash
   apt-cache policy mysql-server
   sudo apt install mysql-server
   ```
   👉 Explication : le candidat doit provenir de `repo.mysql.com` ; l'installation demande ou génère le mot de passe `root` (le saisir, ne pas le noter en clair).

4. Vérifier le service et la version :
   ```bash
   systemctl status mysql --no-pager
   mysql --version
   ```
   👉 Explication : service actif.

## 2. Production — Contrôles

Consigner la version, l'origine du dépôt et la cadence de mise à jour.

## 3. Production — Sécurité

- Ne jamais installer de binaire d'origine inconnue.
- Mot de passe `root` stocké dans le coffre du pack.
- Ne pas ouvrir le port 3306 à ce stade.

## Validation et retour arrière

- **Validation** : `mysql --version` et `systemctl is-active mysql` confirment l'installation.
- **Retour arrière** : `sudo apt purge mysql-server mysql-community-server` après sauvegarde de `/var/lib/mysql` si des données existent.

## Si le problème n'est pas résolu

- [MySQL — Prérequis et limites](fiche-simple-vm-debian-13-mysql-prerequis-limites.md)
- [MySQL — Configurer](fiche-simple-vm-debian-13-mysql-configurer.md)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](fiche-simple-vm-debian-13-mysql-securiser.md)
- [MySQL — Valider (recette)](fiche-simple-vm-debian-13-mysql-valider.md)
- [MySQL — Sauvegarder et restaurer](fiche-simple-vm-debian-13-mysql-sauvegarder-restaurer.md)
- [MySQL — Mise à jour et retour arrière](fiche-simple-vm-debian-13-mysql-mettre-a-jour.md)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](../mariadb/fiche-simple-vm-debian-13-mariadb-prerequis-limites.md)
