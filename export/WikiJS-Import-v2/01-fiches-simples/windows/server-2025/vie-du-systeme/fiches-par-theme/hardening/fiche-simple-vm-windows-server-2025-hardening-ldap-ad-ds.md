---
title: "Fiche Simple - VM Windows Server 2025 Hardening LDAP AD DS"
description: "Contrôler la compatibilité LDAP et AD DS avant toute migration."
published: true
date: 2026-10-29T20:22:42Z
tags: ["windows-server-2025", "hardening", "smb", "ldap", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Hardening_LDAP_AD_DS.md

- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : sécurité / annuaire
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `securite`

---

## Problème précis à résoudre

Contrôler la compatibilité LDAP et AD DS avant toute migration.

## 1. Hors-Production (Lab / Test / POC)

1. Pour une nouvelle forêt, vérifier la compatibilité des applications avec la signature LDAP appliquée par défaut aux clients SASL.
   👉 Explication : une application incompatible ne pourra plus se lier à l'annuaire.

2. Auditer d'abord les événements et clients concernés, migrer les applications vers des connexions sécurisées, puis contrôler authentification et réplication.
   👉 Explication : démarche progressive et réversible.

3. Vérifier la réplication :
   ```powershell
   repadmin /replsummary
   ```
   👉 Explication : Contrôle de la réplication après changements (lecture seule).

4. Ne pas activer la taille de page ESE 32K ni le niveau fonctionnel 2025 sans plan de compatibilité et validation de tous les contrôleurs de domaine.
   👉 Explication : ces options peuvent être difficiles à annuler.

## 2. Production — Contrôles

Valider chaque contrôleur de domaine avant activation d'une nouvelle option.

## 3. Production — Sécurité

- Connexions LDAP sécurisées exigées.

## Validation et retour arrière

- **Validation** : applications compatibles, authentification et réplication saines.
- **Retour arrière** : ne pas activer les options AD DS; restaurer les stratégies précédentes si modifiées.

## Si le problème n'est pas résolu

- [Microsoft Learn — Signature LDAP pour AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing)
- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Guide complet — étape 3](/02-fiches-completes/windows/server-2025/autres/31-hardening-windows-server-2025-production#3-verifier-ldap-et-ad-ds)