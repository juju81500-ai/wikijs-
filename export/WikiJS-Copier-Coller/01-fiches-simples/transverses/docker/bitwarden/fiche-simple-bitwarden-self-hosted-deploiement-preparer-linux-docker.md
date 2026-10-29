# Fiche_Simple_-_Bitwarden_Self_Hosted_Deploiement_Preparer_Linux_Docker.md

- **Environnement** : Serveur Linux x86-64 avec Docker Engine et Compose (déploiement standard Bitwarden)
- **OS / Version** : Linux x86-64 supporté; Docker Engine 26+
- **Catégorie** : coffre de mots de passe / secrets

---

## Problème précis à résoudre

Préparer l'hôte, Docker et le compte de service Bitwarden.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour le système (Debian/Ubuntu; adapter au gestionnaire de paquets de votre distribution) :
   ```bash
   sudo apt update
   sudo apt full-upgrade
   ```
   👉 Explication : applique les correctifs; configurer aussi DNS et NTP.

2. Vérifier Docker Engine et Compose :
   ```bash
   docker --version
   docker compose version
   ```
   👉 Explication : Docker Engine 26+ avec Compose est requis.

3. Créer le compte de service et le répertoire persistant :
   ```bash
   sudo adduser --disabled-password --gecos "" bitwarden
   sudo mkdir -p /opt/bitwarden
   sudo chown bitwarden:bitwarden /opt/bitwarden
   sudo chmod 0700 /opt/bitwarden
   ```
   👉 Explication : compte `bitwarden` dédié et répertoire à permissions strictes.

4. Donner au compte l'accès à Docker selon le modèle approuvé : `sudo usermod -aG docker bitwarden`.
   👉 Explication : attention: appartenir au groupe `docker` équivaut généralement à root sur l'hôte; ne pas l'accorder aux utilisateurs ordinaires.

## 2. Production — Contrôles

Appliquer le modèle d'accès Docker approuvé et documenter les membres du groupe `docker`.

## 3. Production — Sécurité

- Aucun utilisateur ordinaire dans le groupe `docker`.
- Permissions strictes sur `/opt/bitwarden`.

## Validation et retour arrière

- **Validation** : Docker fonctionne et `/opt/bitwarden` appartient à `bitwarden`.
- **Retour arrière** : retirer le compte (`sudo deluser bitwarden`) et supprimer `/opt/bitwarden` s'il est encore vide.

## Si le problème n'est pas résolu

- [Docker — installer Docker Engine](https://docs.docker.com/engine/install/)
- [Bitwarden — déploiement Linux](https://bitwarden.com/help/install-on-premise-linux/)
- [Guide complet](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker#2-preparer-linux-et-docker)