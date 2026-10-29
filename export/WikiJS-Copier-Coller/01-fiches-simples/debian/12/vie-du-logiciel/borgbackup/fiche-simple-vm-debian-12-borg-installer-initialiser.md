# Fiche_Simple_-_VM_Debian_12_Borg_Installer_Initialiser.md

- **Environnement** : Debian 12 Bookworm, dépôt local ou distant préalablement validé
- **OS / Version** : Debian 12; BorgBackup du dépôt Debian
- **Catégorie** : sauvegarde / installation et dépôt

---

## Problème précis à résoudre

Installer Borg et initialiser une seule fois un dépôt chiffré sans risquer d'écraser un dépôt existant.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Borg :
   ```bash
   sudo apt update
   sudo apt install borgbackup
   borg --version
   ```
   👉 Explication : consigner la version; client et serveur doivent être compatibles.

2. Créer un compte dédié côté destination (dépôt distant) :
   ```bash
   sudo adduser --disabled-password --gecos "" borgbackup
   sudo install -d -o borgbackup -g borgbackup -m 0700 /srv/borg/depot
   ```
   👉 Explication : un compte sans mot de passe, limité à la sauvegarde (restreindre la clé SSH avec `borg serve --restrict-to-path`).

3. Initialiser une seule fois le dépôt chiffré (saisie de la phrase de passe à l'invite) :
   ```bash
   borg init --encryption=repokey-blake2 ssh://borgbackup@sauvegarde.example.net/srv/borg/depot
   ```
   👉 Explication : remplacer par le dépôt réel; `repokey-blake2` stocke la clé chiffrée dans le dépôt.

4. Exporter la clé :
   ```bash
   borg key export ssh://borgbackup@sauvegarde.example.net/srv/borg/depot /root/borg-key.txt
   chmod 0600 /root/borg-key.txt
   ```
   👉 Explication : ranger la clé et la phrase de passe hors du serveur; une clé perdue rend les archives irrécupérables.

## 2. Production — Contrôles

Documenter version, propriétaire, destination, mode de chiffrement, procédure d'accès distant et responsabilités de conservation des clés.

## 3. Production — Sécurité

- Ne pas réinitialiser un dépôt existant ni réutiliser son chemin sans validation.
- Ne pas conserver la seule clé ou phrase de passe sur le serveur sauvegardé.
- Ne pas transmettre de secret dans l'historique shell, les logs ou un ticket.
- Une clé perdue peut rendre les archives chiffrées irrécupérables.

## Validation et retour arrière

- **Validation** : dépôt initialisé, mode de chiffrement confirmé et clé de récupération conservée hors serveur.
- **Arrêt** : ne pas initialiser si le chemin, la cible ou la méthode de sauvegarde de clé sont ambigus.

## Si le problème n'est pas résolu

- [BorgBackup — installation](https://borgbackup.readthedocs.io/en/stable/installation.html)
- [BorgBackup — chiffrement](https://borgbackup.readthedocs.io/en/stable/usage/init.html)
- [Guide complet BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)