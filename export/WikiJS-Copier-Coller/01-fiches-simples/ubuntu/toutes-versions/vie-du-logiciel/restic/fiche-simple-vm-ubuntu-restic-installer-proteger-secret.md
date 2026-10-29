# Fiche_Simple_-_VM_Ubuntu_Restic_Installer_Proteger_Secret.md

- **Environnement** : VM Ubuntu Server avec destination de sauvegarde indépendante
- **OS / Version** : Ubuntu Server (toutes versions supportées); paquet restic des dépôts Ubuntu
- **Catégorie** : sauvegarde / restauration

---

## Problème précis à résoudre

Installer Restic et créer le mot de passe du dépôt dans un fichier protégé.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la source puis installer :
   ```bash
   sudo apt update
   apt-cache policy restic
   sudo apt install restic
   ```
   👉 Explication : le paquet doit venir des dépôts approuvés.

2. Créer le fichier de mot de passe (en session root, via `sudo -i`) :
   ```bash
   sudo -i
   install -d -m 0700 /root/.config/restic
   umask 077
   openssl rand -base64 48 > /root/.config/restic/password
   chmod 0600 /root/.config/restic/password
   ```
   👉 Explication : le mot de passe n'est jamais passé en argument ni affiché.

3. Conserver une copie sécurisée du mot de passe dans le coffre de secrets.
   👉 Explication : sans lui, les données chiffrées sont irrécupérables.

## 2. Production — Contrôles

Limiter l'accès au coffre aux administrateurs de la sauvegarde.

## 3. Production — Sécurité

- Fichier de mot de passe en 0600 dans un répertoire 0700.
- Ne jamais placer le mot de passe dans un script versionné.

## Validation et retour arrière

- **Validation** : `restic version` répond et le fichier de mot de passe existe avec les droits restreints.
- **Retour arrière** : `sudo apt remove restic` et suppression du fichier de mot de passe seulement si aucun dépôt ne l'utilise.

## Si le problème n'est pas résolu

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)
- [Guide complet sauvegarde Ubuntu Server Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic#2-installer-restic-et-proteger-le-secret)