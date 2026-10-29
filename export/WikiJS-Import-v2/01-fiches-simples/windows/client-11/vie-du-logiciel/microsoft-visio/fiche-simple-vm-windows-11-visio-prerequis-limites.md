---
title: "Fiche Simple - VM Windows 11 Visio Prerequis Limites"
description: "Cadrer édition, licence et limites avant de déployer Microsoft Visio sur Windows 11."
published: true
date: 2026-10-29T20:57:15Z
tags: ["visio", "windows11", "microsoft-365", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T20:57:15Z
dateModified: 2026-10-29T20:57:15Z
---

# Fiche_Simple_-_VM_Windows_11_Visio_Prerequis_Limites

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `prerequis`

---

## Problème précis à résoudre

Cadrer édition, licence et limites avant de déployer Microsoft Visio sur Windows 11.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir l'offre : Visio Plan 2 (application de bureau, abonnement), Visio Plan 1 (web uniquement), ou Visio perpétuel (Standard/Professional VERSION_VISIO à remplacer). Vérifier le catalogue actuel de Microsoft.
   👉 Explication : seules les offres desktop installent VISIO.EXE ; les offres évoluent, ne pas supposer.

2. Vérifier la licence du compte : GUI **Centre d'administration Microsoft 365 > Utilisateurs > Utilisateurs actifs > UTILISATEUR > Licences et applications**.
   👉 Explication : UTILISATEUR est à remplacer ; la licence Visio doit être cochée pour l'utilisateur.

3. Contrôler le poste. PowerShell :
```powershell
Get-ComputerInfo -Property OsName,OsVersion,OsArchitecture
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Office\ClickToRun\Configuration' -ErrorAction SilentlyContinue | Select-Object VersionToReport,Platform,CDNBaseUrl
```
   👉 Explication : Visio doit utiliser la même architecture (32/64 bits) que les autres applications Office installées ; la clé n'existe que si Office Click-to-Run est déjà présent.

4. Prévoir le mode de déploiement : Office Deployment Tool (ODT) ou Intune, et la source (CDN Microsoft ou partage SOURCE_ODT).
   👉 Explication : SOURCE_ODT est un partage réseau à remplacer, utile hors ligne.

5. Si l'on souhaite une alternative sans licence, voir la fiche draw.io indiquée en bas de page.
   👉 Explication : draw.io couvre les schémas simples, mais n'édite pas tous les formats Visio.

## 2. Production — Contrôles

- Édition, architecture et canal de mise à jour validés.
- Test sur poste pilote.

## 3. Production — Sécurité

- Compte nominatif ; aucune clé de produit stockée dans la fiche.

## Validation et retour arrière

- **Validation** : Licence assignée et poste conforme.
- **Retour arrière** : Rien n'est installé.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio)
- [Alternative draw.io : fiche d'entrée](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-draw-io-desktop)
- [Alternative draw.io : installation (Debian 13)](/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer)