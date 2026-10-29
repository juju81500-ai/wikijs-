# Fiche_Simple_-_VM_Debian_12_Bacula_Preparer_Debian12_Version.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / installation

---

## Problème précis à résoudre

Installer Bacula 15.0.3 depuis bookworm-backports sans mélanger les versions.

## 1. Hors-Production (Lab / Test / POC)

1. Mettre à jour l'index et contrôler la version candidate (le dépôt `bookworm-backports` doit déjà être configuré selon la documentation Debian) :
   ```bash
   sudo apt update
   apt-cache policy bacula-director-pgsql bacula-sd bacula-client bacula-console
   ```
   👉 Explication : le candidat doit venir de Bookworm Backports et valoir `15.0.3-3~bpo12+1`; sinon arrêter et revoir les sources APT.

2. Installer les composants depuis les backports :
   ```bash
   sudo apt install -t bookworm-backports postgresql bacula-director-pgsql bacula-sd bacula-client bacula-console
   ```
   👉 Explication : `-t bookworm-backports` force la version 15.0.3; choisir le catalogue PostgreSQL et garder la configuration générée.

3. Confirmer paquets et PostgreSQL :
   ```bash
   dpkg-query -W 'bacula*' postgresql
   systemctl --no-pager status postgresql
   ```
   👉 Explication : vérifie les versions installées et l'état de la base du catalogue.

## 2. Production — Contrôles

Figer la version par la politique de mise à jour et tester toute montée de version en laboratoire d'abord.

## 3. Production — Sécurité

- Ne pas remplacer les fichiers `.conf` par des exemples d'une autre distribution.
- Ne pas lancer de scripts de schéma d'une version différente si le catalogue n'a pas été initialisé: suivre la documentation du paquet Debian.

## Validation et retour arrière

- **Validation** : les paquets `bacula*` sont en 15.0.3 et PostgreSQL est actif.
- **Retour arrière** : `sudo apt remove bacula-director-pgsql bacula-sd bacula-client bacula-console` (sans `purge`) retire les paquets en gardant les configurations.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Debian Backports](https://backports.debian.org/Instructions/)
- [Guide complet Bacula Debian 12](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports#2-preparer-debian-12-et-verifier-la-version)