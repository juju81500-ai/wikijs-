# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Verifier_Prerequis_Versions.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / prérequis

---

## Problème précis à résoudre

Contrôler le système et les versions candidates avant d'installer la pile LEMP.

## 1. Hors-Production (Lab / Test / POC)

1. Lire la version d'Ubuntu et actualiser l'index :
   ```bash
   cat /etc/os-release
   sudo apt update
   ```
   👉 Explication : confirme Ubuntu 24.04 et des sources APT à jour.

2. Contrôler les versions candidates :
   ```bash
   apt-cache policy nginx php8.3-fpm mariadb-server
   ```
   👉 Explication : Ubuntu 24.04 fournit PHP 8.3 et MariaDB 10.11; les révisions de sécurité évoluent.

## 2. Production — Contrôles

Réserver hostname/FQDN, IP stable, volumes, accès SSH, sauvegarde et flux avant l'installation.

## 3. Production — Sécurité

- Ne pas ajouter de dépôt tiers sans validation.

## Validation et retour arrière

- **Validation** : versions candidates conformes aux attendus.
- **Retour arrière** : lecture seule: rien à annuler.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb#1-prerequis-et-versionnement)