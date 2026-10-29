---
title: "Fiche Simple - VM Windows Server 2022 Reprise Foret AD DS Lab"
description: "Répéter et valider le plan de récupération d'une forêt AD DS en laboratoire, sans connecter les DC restaurés au réseau de production."
published: true
date: 2026-10-29T19:26:46Z
tags: ["windows-server-2022", "ad-ds", "forest-recovery", "dsrm", "sauvegarde", "lab"]
editor: markdown
dateCreated: 2026-10-29T19:26:46Z
dateModified: 2026-10-29T19:26:46Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Lab.md

- **Environnement** : Forêt AD DS Windows Server 2022, sauvegardes testées et lab isolé
- **OS / Version** : Windows Server 2022
- **Catégorie** : Continuité / reprise après sinistre
- **Tags** : `windows-server-2022`, `ad-ds`, `forest-recovery`, `dsrm`, `sauvegarde`, `lab`

---

## 🎯 Problème précis à résoudre

Répéter et valider le plan de récupération d'une forêt AD DS en laboratoire, sans connecter les DC restaurés au réseau de production.

## ⚠️ Périmètre critique

La récupération de forêt est un dernier recours pour une panne forêt entière. Elle ne s'applique pas à la perte d'un seul DC lorsque la réplication fonctionne. Suivre le plan propre à l'organisation et la documentation Microsoft; coordonner avec l'équipe identité et le support Microsoft avant une reprise réelle.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Préparer un réseau virtuel isolé : **Hyper-V Manager > Virtual Switch Manager > Create > Private**, relier les VM de lab à ce switch :
   ```powershell
   New-VMSwitch -Name "LAB-ISOLE" -SwitchType Private
   Get-VM | Get-VMNetworkAdapter | Select-Object VMName, SwitchName
   ```
   👉 Explication : aucun routage ni pont vers la production; utiliser des copies de sauvegardes approuvées.

2. Confirmer la sauvegarde System State et les prérequis :
   ```powershell
   wbadmin get versions
   Get-ADDomain | Select-Object Forest, InfrastructureMaster, PDCEmulator, RIDMaster
   netdom query fsmo
   ```
   👉 Explication : horodatage, média, mot de passe DSRM, DNS, rôles FSMO et dépendances consignés.

3. Restaurer un DC inscriptible du domaine racine (démarrage en mode DSRM) :
   ```powershell
   bcdedit /set safeboot dsrepair
   Restart-Computer
   wbadmin start systemstaterecovery -version:AAAA-MM-JJ-HH:MM -backupTarget:E: -quiet
   ```
   👉 Explication : suivre le guide Microsoft de récupération de forêt; remplacer version et cible; pour SYSVOL, appliquer la restauration faisant autorité selon la procédure.

4. Compléter dans le lab seulement : réinitialiser les comptes privilégiés (dont `krbtgt`), nettoyer les métadonnées, relever le pool RID, contrôler la réplication :
   ```powershell
   repadmin /replsummary
   repadmin /showrepl
   ```
   👉 Explication : suivre l'ordre du plan de reprise.

5. Ajouter progressivement DC et domaines enfants, puis contrôler :
   ```powershell
   dcdiag /v /c /e
   Get-WinEvent -LogName "Directory Service" -MaxEvents 30
   ```
   👉 Explication : aucune décision de production avant la fin de ces contrôles.


## ⚡ 2. Production — Façon Simplifiée

1. Ne pas improviser : ouvrir le plan de reprise forêt approuvé :
   ```powershell
   netdom query fsmo
   repadmin /replsummary
   ```
   👉 Explication : assigner un responsable unique, noter les points de décision, ne reconnecter les DC qu'après validation de l'équipe identité.


## 🔒 3. Production — Façon Sécurisée

- Restaurer les DC sur réseau isolé; ne pas démarrer plusieurs DC restaurés simultanément sur le réseau de production.
- Ne pas effectuer une restauration autoritaire globale de SYSVOL; Microsoft demande une procédure précise et un seul premier DC faisant autorité selon le scénario.
- En cas de compromission suspectée, intégrer rotation des comptes privilégiés, `krbtgt`, gMSA et secrets de confiance dans le plan après validation des rôles et dépendances.
- Toute commande de prise de rôle FSMO, suppression de métadonnées ou modification SYSVOL doit être approuvée pour cette forêt/version et exécutée par l'équipe habilitée.

## ✅ Validation et retour arrière

- **Validation lab** : services AD DS/DNS, SYSVOL/NETLOGON, DNS SRV, état des rôles, réplication et ouverture de session testés.
- **Retour arrière lab** : détruire le réseau isolé et les copies VM de test; conserver la preuve de test sans réutiliser ces DC en production.
- **Critère production** : documenter le plan, résultats du dernier exercice, RTO/RPO, sauvegardes confirmées et approbations avant bascule.

## 🔗 Si le problème n'est pas résolu

- [Microsoft — Guide de récupération de forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-guide)
- [Microsoft — Prérequis de récupération](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-prerequisites)
- [Microsoft — Récupération initiale](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-perform-initial-recovery)
- [Microsoft — Récupération d'état système](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wbadmin-start-systemstaterecovery)