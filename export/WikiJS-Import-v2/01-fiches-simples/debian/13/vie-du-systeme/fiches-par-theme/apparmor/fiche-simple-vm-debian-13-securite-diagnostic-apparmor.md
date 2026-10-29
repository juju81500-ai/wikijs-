---
title: "Fiche Simple - VM Debian 13 Securite Diagnostic AppArmor"
description: "Vérifier l'état d'AppArmor et diagnostiquer un refus d'accès applicatif sans désactiver le contrôle d'accès obligatoire."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[debian]", "[apparmor]", "[securite]", "[audit]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Securite_Diagnostic_AppArmor.md

- **Environnement** : VM ou serveur Debian 13
- **OS / Version** : Debian 13 (Trixie)
- **Catégorie** : Sécurité / Contrôle d'accès
- **Tags** : `[debian13]`, `[debian]`, `[apparmor]`, `[securite]`, `[audit]`, `[hardening]`

## 🎯 Problème précis à résoudre
Vérifier l'état d'AppArmor et diagnostiquer un refus d'accès applicatif sans désactiver le contrôle d'accès obligatoire.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la présence du paquet, le service et les profils chargés :
   ```bash
   sudo apt update
   sudo apt install apparmor apparmor-utils
   sudo systemctl enable --now apparmor
   sudo aa-status
   ```
2. Rechercher les refus récents :
   ```bash
   sudo journalctl -k --since today --no-pager | grep -i 'apparmor.*denied'
   ```
   👉 *Explication : un refus doit être rapproché de l'application, du chemin et de l'opération réellement attendue.*

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer le profil associé au programme et son mode :
   ```bash
   sudo aa-status
   sudo aa-complain /etc/apparmor.d/<profil-identifie>
   ```
   Utiliser `aa-complain` seulement pendant une investigation approuvée et limitée dans le temps; le profil passe alors en mode plainte.
2. Examiner les événements et les accès nécessaires :
   ```bash
   sudo journalctl -k --since '30 minutes ago' --no-pager | grep -i 'apparmor.*denied'
   sudo aa-logprof
   ```
3. Réviser chaque changement proposé avant de l'enregistrer, puis remettre le profil en application stricte :
   ```bash
   sudo aa-enforce /etc/apparmor.d/<profil-identifie>
   sudo aa-status
   ```
   👉 *Explication : `aa-logprof` peut modifier un profil; ne pas accepter automatiquement des accès larges ou inattendus.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas désactiver AppArmor globalement et ne pas laisser un profil en mode plainte en production.
2. Sauvegarder le profil avant modification et n'autoriser que les chemins et opérations confirmés par le besoin de l'application.
3. Si aucun profil ne correspond au service, élaborer et tester un profil dédié dans un environnement de préproduction.

## ✅ Validation et retour arrière
- Vérifier `aa-status`, reproduire l'action applicative et confirmer l'absence de refus inattendu.
- Restaurer le profil sauvegardé si le comportement change, recharger AppArmor et valider à nouveau le service.
- Examiner les événements noyau après le retour au mode `enforce`.