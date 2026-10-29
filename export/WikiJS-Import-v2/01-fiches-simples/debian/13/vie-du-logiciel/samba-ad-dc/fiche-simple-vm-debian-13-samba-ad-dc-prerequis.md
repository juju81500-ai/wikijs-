---
title: "Fiche Simple - VM Debian 13 Samba AD DC Prerequis"
description: "Cadrer ce que couvre un domaine Samba AD DC de laboratoire avant de l'installer."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "samba", "active-directory", "lab", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Samba_AD_DC_Prerequis.md

- **Environnement** : VM Debian 13 de laboratoire, contrôleur de domaine Samba AD DC (DNS SAMBA_INTERNAL)
- **OS / Version** : Debian 13 Trixie; Samba 4.22 (dépôts Debian)
- **Catégorie** : annuaire / cadrage
- **Tags** : `debian13`, `samba`, `active-directory`, `lab`, `prerequis`

---

## Problème précis à résoudre

Cadrer ce que couvre un domaine Samba AD DC de laboratoire avant de l'installer.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir et noter le domaine DNS, le nom NetBIOS et l'adresse statique (exemples : `AD.LAB.TEST`, `ADLAB`, `192.0.2.10`, à remplacer par vos valeurs).
   👉 Explication : après création de la forêt, ces noms ne se changent pas facilement.

2. Vérifier la matrice de compatibilité Samba et les applications visées.
   👉 Explication : Samba n'est pas compatible avec tous les rôles et GPO Microsoft.

3. Confirmer que le domaine est neuf.
   👉 Explication : la procédure ne couvre pas la migration d'une forêt Microsoft existante.

## 2. Production — Contrôles

Pour une mise en service réelle : plusieurs DC dans des domaines de panne distincts, sauvegardes testées, supervision, NTP, reprise et revue de sécurité. Une seule VM sert uniquement à l'apprentissage.

## 3. Production — Sécurité

- Ne pas utiliser une seule VM DC en production.
- Choisir un domaine DNS contrôlé par l'organisation.
- Ne pas rendre le DC accessible depuis Internet.

## Validation et retour arrière

- **Validation** : noms, adresse et périmètre sont validés par écrit.
- **Retour arrière** : aucune modification; abandonner la VM de lab si le cadrage est refusé.

## Si le problème n'est pas résolu

- [Debian 13 — samba-ad-dc(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html)
- [Debian 13 — samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html)
- [Guide complet Déployer un contrôleur de domaine Samba AD DC sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13#1-limites-et-prerequis)