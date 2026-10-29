---
title: "Fiche Simple - VM Ubuntu 26.04 Pile Web Validation Sauvegarde Retour"
description: "Valider la pile, la sauvegarder et préparer le retour arrière."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2604", "nginx", "php8.5", "postgresql18", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Validation_Sauvegarde_Retour.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / validation
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Valider la pile, la sauvegarder et préparer le retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Tester :
   ```bash
   curl -I https://app.example.net/
   php8.5 -v
   ```
   👉 Explication : Teste HTTPS (nom d'exemple à remplacer) et la version PHP.

2. Sauvegarder la base :
   ```bash
   sudo -u postgres pg_dump appdb > appdb.sql
   ```
   👉 Explication : Dump de la base (`appdb` est un exemple), à copier dans une cible distincte.

3. Sauvegarder les fichiers :
   ```bash
   sudo tar czf app-files.tar.gz /var/www/app /etc/nginx/sites-available
   ```
   👉 Explication : Archive fichiers et configuration (chemins à adapter).

4. Tester la restauration dans un environnement isolé.
   👉 Explication : vérifie que la sauvegarde est exploitable.

## 2. Production — Contrôles

Tester parcours applicatif, connexion à la base et journaux.

## 3. Production — Sécurité

- Chiffrer et protéger dump et archive.

## Validation et retour arrière

- **Validation** : HTTPS, base et application répondent; sauvegarde restaurable.
- **Retour arrière** : restaurer le server block précédent, `nginx -t`, recharger; restaurer aussi la base si son schéma a changé.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 7](/02-fiches-completes/ubuntu/26-04/installation-deploiement/21-pile-web-ubuntu-server-26-04-nginx-php85-postgresql18#7-validation-sauvegarde-et-retour-arriere)