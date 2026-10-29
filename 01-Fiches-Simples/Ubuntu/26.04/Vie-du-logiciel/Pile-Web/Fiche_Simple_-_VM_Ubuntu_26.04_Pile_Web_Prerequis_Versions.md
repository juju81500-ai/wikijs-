# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Prerequis_Versions.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / prérequis
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Vérifier les versions disponibles avant d'installer la pile web.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les versions :
   ```bash
   cat /etc/os-release
   sudo apt update
   apt-cache policy nginx php8.5-fpm postgresql-18
   ```
   👉 Explication : Affiche la version d'Ubuntu et les candidats Nginx, PHP 8.5 et PostgreSQL 18.

2. Réserver hostname/FQDN, IP stable, volumes, accès SSH et méthode de sauvegarde.
   👉 Explication : à figer avant l'installation.

3. Vérifier que l'application prend en charge PHP 8.5 et PostgreSQL 18.
   👉 Explication : Ubuntu 26.04 fournit une base différente de Noble.

## 2. Production — Contrôles

Confirmer la compatibilité applicative par écrit.

## 3. Production — Sécurité

- N'utiliser que les dépôts Ubuntu approuvés.

## Validation et retour arrière

- **Validation** : versions candidates correctes et compatibles.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Ubuntu 26.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/26.04/summary-for-lts-users/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 1](../../../../../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/21_Pile_Web_Ubuntu_Server_26.04_Nginx_PHP85_PostgreSQL18.md#1-prerequis-et-versions)
