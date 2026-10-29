---
title: "Fiche Simple - VM Ubuntu 26.04 Pile Web Deployer Application TLS"
description: "Déployer l'application, la relier à PostgreSQL et activer TLS."
published: true
date: 2026-10-29T20:14:10Z
tags: ["ubuntu2604", "nginx", "php8.5", "postgresql18", "tls"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Pile_Web_Deployer_Application_TLS.md

- **Environnement** : VM ou serveur dédié Ubuntu Server hébergeant une application PHP avec PostgreSQL local et TLS
- **OS / Version** : Ubuntu Server 26.04 LTS (Resolute); Nginx, PHP 8.5, PostgreSQL 18
- **Catégorie** : services web / déploiement
- **Tags** : `ubuntu2604`, `nginx`, `php8.5`, `postgresql18`, `tls`

---

## Problème précis à résoudre

Déployer l'application, la relier à PostgreSQL et activer TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Déployer une version applicative compatible PHP 8.5, renseigner l'accès PostgreSQL via un secret protégé (fichier en droits restreints) et limiter l'écriture aux répertoires nécessaires.
   👉 Explication : évite les secrets en clair et les écritures inutiles.

2. Configurer TLS avec l'outil ACME approuvé par l'organisation et tester le renouvellement.
   👉 Explication : un certificat non renouvelé provoque une panne.

3. Pour un essai FPM, créer un endpoint temporaire affichant `OK`, le tester via Nginx puis le supprimer immédiatement.
   👉 Explication : ne jamais exposer `phpinfo()`.

## 2. Production — Contrôles

Tester le renouvellement du certificat.

## 3. Production — Sécurité

- Pas de `phpinfo()` ni de page de test conservée.

## Validation et retour arrière

- **Validation** : application accessible en HTTPS et renouvellement validé.
- **Retour arrière** : retirer le déploiement et restaurer la version précédente.

## Si le problème n'est pas résolu

- [Nginx — documentation](https://nginx.org/en/docs/)
- [PostgreSQL 18 — documentation](https://www.postgresql.org/docs/18/)
- [Guide complet — étape 5](/02-fiches-completes/ubuntu/26-04/installation-deploiement/21-pile-web-ubuntu-server-26-04-nginx-php85-postgresql18#5-deployer-lapplication-et-tls)