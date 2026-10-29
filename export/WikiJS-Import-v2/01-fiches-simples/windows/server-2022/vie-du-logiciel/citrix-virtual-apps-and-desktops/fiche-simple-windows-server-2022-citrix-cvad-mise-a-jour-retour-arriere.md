---
title: "Fiche Simple - Windows Server 2022 Citrix CVAD Mise A Jour Retour Arriere"
description: "Mettre à jour CVAD et prévoir le retour arrière."
published: true
date: 2026-10-29T20:56:04Z
tags: ["citrix", "cvad", "windows-server", "mise-a-jour"]
editor: markdown
dateCreated: 2026-10-29T20:56:04Z
dateModified: 2026-10-29T20:56:04Z
---

# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Mise_A_Jour_Retour_Arriere

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix
- **Tags** : `citrix`, `cvad`, `windows-server`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour CVAD et prévoir le retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version et la procédure officielle d'upgrade de VERSION_CVAD (ordre des composants, compatibilité VDA/Controller).
   👉 Explication : l'ordre habituel part des Controllers vers StoreFront puis les VDA, à confirmer.

2. Faire une sauvegarde SQL complète des bases et un snapshot des VM Controller et StoreFront (voir fiche sauvegarde).
   👉 Explication : c'est le point de retour.

3. Passer en mode maintenance les catalogues : GUI **Studio > Machine Catalogs** ou PowerShell :
```powershell
Set-BrokerMachine -MachineName 'DOMAINE\VDA01' -InMaintenanceMode $true
```
   👉 Explication : DOMAINE\VDA01 est à remplacer.

4. Lancer l'ISO de la nouvelle version sur chaque Controller ; puis dans Studio exécuter la mise à niveau de la base si proposée (**Upgrade databases**).
   👉 Explication : la base de site est migrée par l'assistant ; l'opération est irréversible sans restauration.

5. Mettre à jour StoreFront puis les images VDA, retirer le mode maintenance et recetter.
   👉 Explication : voir la fiche de validation.

## 2. Production — Contrôles

- Fenêtre de maintenance annoncée.
- Versions avant/après notées.

## 3. Production — Sécurité

- Télécharger les médias uniquement depuis le portail Citrix.
- Vérifier l'empreinte.

## Validation et retour arrière

- **Validation** : Version attendue, machines Registered, recette OK.
- **Retour arrière** : Restaurer les bases SQL sauvegardées et les snapshots des serveurs ; réinstaller l'ancien VDA si nécessaire.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops)