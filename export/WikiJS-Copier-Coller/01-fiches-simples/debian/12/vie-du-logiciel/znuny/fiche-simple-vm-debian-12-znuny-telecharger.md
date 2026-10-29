# Fiche_Simple_-_VM_Debian_12_Znuny_Telecharger.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing

---

## Problème précis à résoudre

Télécharger l'archive officielle, l'installer dans `/opt` et créer le compte de service.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'archive officielle :
   ```bash
   cd /tmp
   curl -fLO https://download.znuny.org/releases/znuny-7.3.8.tar.gz
   ```
   👉 Explication : on récupère la version 7.3.8 depuis le site officiel.

2. Vérifier le contenu de l'archive avant extraction :
   ```bash
   tar -tzf znuny-7.3.8.tar.gz | head
   ```
   👉 Explication : on contrôle que les fichiers sont bien dans le répertoire `znuny-7.3.8/`.

3. Extraire dans `/opt` et créer le lien stable :
   ```bash
   sudo tar -xzf znuny-7.3.8.tar.gz -C /opt
   sudo ln -sfn /opt/znuny-7.3.8 /opt/znuny
   ```
   👉 Explication : le lien `/opt/znuny` permet de changer de version sans modifier les configurations.

4. Créer le compte de service :
   ```bash
   sudo useradd --system --home-dir /opt/znuny --shell /usr/sbin/nologin \
     --gid www-data znuny
   ```
   👉 Explication : un compte système sans shell exécute l'application, dans le groupe d'Apache.

5. Si le compte `znuny` existe déjà, vérifier ses attributs au lieu de le recréer :
   ```bash
   id znuny
   ```
   👉 Explication : on contrôle UID, groupe et répertoire existants.

## 2. Production — Contrôles

Vérifier l'origine de l'archive (site officiel, HTTPS) et conserver la version déployée dans la documentation.

## 3. Production — Sécurité

- Ne pas exécuter Znuny avec un compte interactif ou `root`.
- Vérifier l'origine du téléchargement avant extraction.

## Validation et retour arrière

- **Validation** : `ls -l /opt/znuny` pointe vers `/opt/znuny-7.3.8` et `id znuny` répond.
- **Retour arrière** : `sudo rm /opt/znuny`, `sudo rm -r /opt/znuny-7.3.8` et `sudo userdel znuny` si l'installation n'est pas utilisée.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — télécharger et préparer Znuny](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12#4-telecharger-et-preparer-znuny)