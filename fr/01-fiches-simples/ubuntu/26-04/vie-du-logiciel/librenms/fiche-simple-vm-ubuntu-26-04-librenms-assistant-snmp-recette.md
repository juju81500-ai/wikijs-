---
title: "fiche-simple-vm-ubuntu-26-04-librenms-assistant-snmp-recette"
description: "Terminer l'assistant web, ajouter des appareils en SNMPv3 et valider l'installation."
published: true
date: 2026-11-03T09:36:13Z
tags: ["ubuntu2604", "librenms", "snmpv3", "nginx", "mariadb"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# fiche-simple-vm-ubuntu-26-04-librenms-assistant-snmp-recette.md

- **Environnement** : [[Glossary:VM]] Ubuntu Server 26-04 dédiée à LibreNMS (Nginx, PHP-FPM, MariaDB, [[Glossary:SNMP]])
- **OS / Version** : Ubuntu Server 26-04 [[Glossary:LTS]]; LibreNMS 26.10.2; PHP 8.5
- **Catégorie** : supervision / recette
- **Tags** : `ubuntu2604`, `librenms`, `snmpv3`, `nginx`, `mariadb`

---

## Problème précis à résoudre

Terminer l'assistant web, ajouter des appareils en SNMPv3 et valider l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **https://librenms.example.net/install** depuis le réseau d'administration (remplacer par le vrai nom) et terminer l'assistant avec la base dédiée.
   👉 Explication : crée la configuration initiale; vérifier ensuite le propriétaire de `config.php`.

2. Ajouter `localhost` puis un appareil de test autorisé : **Devices > Add Device**.
   👉 Explication : vérifie la collecte sur une cible connue.

3. Sur chaque équipement, préférer SNMPv3 `authPriv` en lecture seule, définir l'[[Glossary:IP]] du serveur LibreNMS comme source autorisée et n'ouvrir [[Glossary:UDP]]/161 que depuis le poller.
   👉 Explication : évite la communauté `public` et toute écriture SNMP.

4. Valider :
   ```bash
   sudo -u librenms /opt/librenms/validate.php
   sudo systemctl --no-pager status nginx php8.5-fpm mariadb librenms-scheduler.timer
   ```
   👉 Explication : Contrôle officiel de l'installation et état des services.

## 2. Production — Contrôles

Confirmer collecte, graphes, journaux, alertes de test et fuseau horaire avant d'ajouter d'autres cibles.

## 3. Production — Sécurité

- Pas de SNMPv2c `public` ni d'écriture SNMP.
- Secrets SNMPv3 saisis dans l'interface, jamais en argument de commande.

## Validation et retour arrière

- **Validation** : `validate.php` sans erreur et appareil de test collecté.
- **Retour arrière** : supprimer l'appareil de test dans l'interface; restaurer le snapshot si l'assistant a mal configuré l'instance.

## Si le problème n'est pas résolu

- [LibreNMS — Validation](https://docs.librenms.org/Support/Install-Validation/)
- [LibreNMS — Ajouter un appareil](https://docs.librenms.org/Support/Adding-a-Device/)
- [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/)
- [Guide complet — étape 7](/fr/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04#7-assistant-snmp-et-recette)