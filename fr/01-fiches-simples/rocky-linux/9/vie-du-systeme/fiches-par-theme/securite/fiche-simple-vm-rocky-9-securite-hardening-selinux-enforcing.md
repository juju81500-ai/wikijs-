---
title: "fiche-simple-vm-rocky-9-securite-hardening-selinux-enforcing"
description: "Maintenir SELinux en mode Enforcing et traiter les refus."
published: true
date: 2026-11-03T09:36:13Z
tags: ["rocky9", "rhel9", "hardening", "selinux", "avc"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# fiche-simple-vm-rocky-9-securite-hardening-selinux-enforcing.md

- **Environnement** : [[Glossary:VM]] ou serveur dédié Rocky Linux 9 avant ouverture en production
- **OS / Version** : Rocky Linux 9 / famille [[Glossary:RHEL]] 9
- **Catégorie** : sécurité / SELinux
- **Tags** : `rocky9`, `rhel9`, `hardening`, `selinux`, `avc`

---

## Problème précis à résoudre

Maintenir SELinux en mode Enforcing et traiter les refus.

## 1. Hors-Production (Lab / Test / POC)

1. Lire le mode :
   ```bash
   getenforce
   sestatus
   ```
   👉 Explication : doit afficher `Enforcing`.

2. Rechercher les refus récents :
   ```bash
   sudo ausearch -m AVC -ts recent
   ```
   👉 Explication : un AVC indique un contexte ou une politique à corriger finement.

## 2. Production — Contrôles

Corriger le contexte ou la politique minimale pour chaque refus.

## 3. Production — Sécurité

- Ne pas passer en permissif ni générer automatiquement une règle large.

## Validation et retour arrière

- **Validation** : `getenforce` renvoie `Enforcing` et aucun AVC inexpliqué.
- **Retour arrière** : lecture seule; en cas de changement de contexte, restaurer avec `sudo restorecon -Rv chemin` (remplacer `chemin`).

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Red Hat — SELinux sur RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Guide complet hardening Rocky Linux 9](/fr/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9#4-conserver-selinux-en-application)