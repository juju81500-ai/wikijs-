---
title: "Fiche Simple - VM Windows Server 2025 Hardening Reduire Acces Administration"
description: "Limiter les moyens d'administration à ce qui est requis."
published: true
date: 2026-10-29T20:22:42Z
tags: ["windows-server-2025", "hardening", "smb", "ldap", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Reduire_Acces_Administration.md

- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : sécurité / administration
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `securite`

---

## Problème précis à résoudre

Limiter les moyens d'administration à ce qui est requis.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler SSH, pare-feu et Defender :
   ```powershell
   Get-Service sshd -ErrorAction SilentlyContinue
   Get-NetFirewallProfile | Select-Object Name, Enabled
   Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
   ```
   👉 Explication : Vérifie le service SSH, l'état du pare-feu par profil et celui de Defender (lecture seule).

2. Vérifier que `sshd` n'écoute ou n'accepte que les connexions requises et filtrer au réseau d'administration si SSH est utilisé.
   👉 Explication : réduit la surface d'attaque.

3. Conserver WinRM/RDP seulement selon le modèle retenu, avec NLA, pare-feu à portée limitée et comptes dédiés.
   👉 Explication : limite les accès distants.

4. Utiliser Windows LAPS et des comptes nominatifs; retirer les rôles locaux non requis.
   👉 Explication : évite les mots de passe administrateur partagés.

5. Examiner **Sécurité Windows > Sécurité de l'appareil** : isolation du noyau (VBS), démarrage sécurisé; Credential Guard selon la compatibilité du rôle.
   👉 Explication : protections matérielles à valider rôle par rôle.

## 2. Production — Contrôles

Documenter le modèle d'administration retenu.

## 3. Production — Sécurité

- Pas de compte partagé; portée du pare-feu limitée.

## Validation et retour arrière

- **Validation** : seuls les accès d'administration prévus fonctionnent.
- **Retour arrière** : rétablir la règle ou le service modifié depuis la stratégie précédente.

## Si le problème n'est pas résolu

- [Microsoft Learn — OpenSSH pour Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview)
- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Guide complet — étape 4](/02-fiches-completes/windows/server-2025/autres/31-hardening-windows-server-2025-production#4-reduire-les-acces-dadministration)