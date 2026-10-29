---
title: "Fiche Simple - VM Rocky 9 Pile Web Deployer Verifier"
description: "Déployer l'application et vérifier toute la chaîne avant l'ouverture."
published: true
date: 2026-10-29T20:14:10Z
tags: ["rocky9", "nginx", "php-fpm", "mariadb", "selinux"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_Pile_Web_Deployer_Verifier.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / recette
- **Tags** : `rocky9`, `nginx`, `php-fpm`, `mariadb`, `selinux`

---

## Problème précis à résoudre

Déployer l'application et vérifier toute la chaîne avant l'ouverture.

## 1. Hors-Production (Lab / Test / POC)

1. Déployer une version applicative compatible avec la version PHP réellement installée.
   👉 Explication : évite les incompatibilités.

2. Vérifier :
   ```bash
   curl -I http://127.0.0.1/
   sudo journalctl -u nginx -u php-fpm -u mariadb --no-pager -n 30
   sudo ausearch -m avc -ts recent
   ```
   👉 Explication : Teste la réponse HTTP, lit les journaux et cherche des refus SELinux.

3. Supprimer les pages de test (par exemple `phpinfo`) avant d'ouvrir le service.
   👉 Explication : elles divulguent la configuration.

## 2. Production — Contrôles

Tester application, base, socket FPM, HTTPS, logs, droits et services.

## 3. Production — Sécurité

- Aucune page de diagnostic ne doit rester accessible.

## Validation et retour arrière

- **Validation** : application, base et HTTPS répondent sans erreur ni AVC.
- **Retour arrière** : retirer le déploiement et restaurer la version précédente.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 6](/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb#6-deployer-et-verifier)