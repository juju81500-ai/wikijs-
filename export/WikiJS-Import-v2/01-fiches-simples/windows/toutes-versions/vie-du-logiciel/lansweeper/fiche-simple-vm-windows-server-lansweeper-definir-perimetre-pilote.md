---
title: "Fiche Simple - VM Windows Server Lansweeper Definir Perimetre Pilote"
description: "Limiter la découverte à une plage autorisée avec des identifiants minimaux."
published: true
date: 2026-10-29T20:14:10Z
tags: ["lansweeper", "windows-server-2022", "inventaire", "wmi", "snmp"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_Lansweeper_Definir_Perimetre_Pilote.md

- **Environnement** : Serveur Windows x64 avec Lansweeper Classic (SQL LocalDB ou SQL Server selon l'échelle)
- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic selon la matrice officielle
- **Catégorie** : inventaire de parc / découverte réseau
- **Tags** : `lansweeper`, `windows-server-2022`, `inventaire`, `wmi`, `snmp`

---

## Problème précis à résoudre

Limiter la découverte à une plage autorisée avec des identifiants minimaux.

## 1. Hors-Production (Lab / Test / POC)

1. Dans le **First Run Wizard**, saisir une petite plage IP appartenant à l'organisation et validée par l'équipe réseau.
   👉 Explication : ne jamais scanner de réseau tiers ou non approuvé.

2. Créer des identifiants de découverte distincts : **Scanning > Scanning Credentials**.
   👉 Explication : un compte par usage, à privilèges minimaux.

3. Pour Windows, préférer un compte de lecture/découverte dédié plutôt qu'administrateur de domaine; limiter WMI et lecture AD aux systèmes concernés.
   👉 Explication : réduit l'impact d'une compromission.

4. Pour SNMP, utiliser SNMPv3 en lecture seule si disponible.
   👉 Explication : évite les communautés en clair.

5. Limiter la portée de chaque identifiant par domaine ou plage; garder les secrets dans le coffre du produit.
   👉 Explication : empêche leur usage sur des cibles non prévues.

## 2. Production — Contrôles

Faire approuver plage et identifiants par l'équipe réseau et sécurité.

## 3. Production — Sécurité

- Compte de scan sans droits d'administrateur de domaine.
- Secrets uniquement dans le coffre du produit.

## Validation et retour arrière

- **Validation** : la plage pilote est limitée et chaque identifiant est restreint.
- **Retour arrière** : supprimer la plage pilote et les identifiants créés dans **Scanning**.

## Si le problème n'est pas résolu

- [Lansweeper — identifiants de scan](https://docs.lansweeper.com/classic/docs/create-and-map-scanning-credentials.md)
- [Lansweeper Classic — prérequis](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Guide complet](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server#3-definir-un-perimetre-pilote)