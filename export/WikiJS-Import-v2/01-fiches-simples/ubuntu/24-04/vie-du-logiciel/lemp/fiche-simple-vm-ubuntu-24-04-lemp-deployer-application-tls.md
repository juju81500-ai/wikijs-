---
title: "Fiche Simple - VM Ubuntu 24.04 LEMP Deployer Application TLS"
description: "Déployer l'application, valider PHP-FPM sans exposer d'information et activer TLS."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu24.04", "nginx", "php8.3", "mariadb", "lemp", "tls", "acme"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_LEMP_Deployer_Application_TLS.md

- **Environnement** : VM Ubuntu Server 24.04 dédiée à une application Web PHP
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble); Nginx, PHP 8.3, MariaDB 10.11
- **Catégorie** : web / TLS
- **Tags** : `ubuntu24.04`, `nginx`, `php8.3`, `mariadb`, `lemp`, `tls`, `acme`

---

## Problème précis à résoudre

Déployer l'application, valider PHP-FPM sans exposer d'information et activer TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Créer temporairement un endpoint de test (affiche uniquement `OK`) :
   ```bash
   printf '<?php echo "OK";\n' | sudo tee /var/www/app/public/health-tmp.php
   ```
   👉 Explication : vérifie la chaîne Nginx vers PHP-FPM.

2. Le tester via Nginx (FQDN d'exemple à remplacer) :
   ```bash
   curl -fsS http://app.example.net/health-tmp.php
   ```
   👉 Explication : la réponse doit être `OK`.

3. Le supprimer immédiatement :
   ```bash
   sudo rm /var/www/app/public/health-tmp.php
   ```
   👉 Explication : ne pas laisser de fichier de test accessible.

4. Configurer TLS avec l'autorité ou l'outil ACME retenu et vérifier le renouvellement :
   ```bash
   curl -fsSI https://app.example.net/
   ```
   👉 Explication : la procédure dépend de l'outil choisi (voir la fiche Certbot du même OS).

## 2. Production — Contrôles

Déployer une version applicative prise en charge et protéger son fichier de configuration.

## 3. Production — Sécurité

- Ne jamais exposer `phpinfo()`.
- Surveiller l'expiration des certificats.

## Validation et retour arrière

- **Validation** : HTTPS répond et le fichier de test est supprimé.
- **Retour arrière** : retirer le certificat ou revenir au server block HTTP précédent, tester et recharger Nginx.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [Ubuntu 24.04 — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Guide complet LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb#5-deployer-lapplication-et-tls)