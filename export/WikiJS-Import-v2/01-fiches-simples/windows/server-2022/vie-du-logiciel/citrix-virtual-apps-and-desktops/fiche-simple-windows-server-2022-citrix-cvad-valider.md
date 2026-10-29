---
title: "Fiche Simple - Windows Server 2022 Citrix CVAD Valider"
description: "Recetter le site CVAD : enregistrement, licences, lancement de session."
published: true
date: 2026-10-29T20:56:04Z
tags: ["citrix", "cvad", "windows-server", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:56:04Z
dateModified: 2026-10-29T20:56:04Z
---

# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Valider

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix
- **Tags** : `citrix`, `cvad`, `windows-server`, `validation`

---

## Problème précis à résoudre

Recetter le site CVAD : enregistrement, licences, lancement de session.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état du site. PowerShell :
```powershell
Add-PSSnapin Citrix*
Get-BrokerController | Select-Object DNSName,State
Get-BrokerMachine | Select-Object MachineName,RegistrationState,PowerState
Get-BrokerCatalog | Select-Object Name,UnassignedCount
```
   👉 Explication : State doit être Active, RegistrationState Registered.

2. Contrôler les licences : GUI **Studio > Licensing** (ou console d'administration des licences Citrix) pour les licences en usage et disponibles.
   👉 Explication : les alertes d'expiration apparaissent ici.

3. Se connecter à https://STORE_FQDN avec un utilisateur de test et lancer un bureau ou une application.
   👉 Explication : valide la chaîne complète StoreFront, Controller, VDA.

4. Consulter **Studio > Monitor** (Director si installé) pour vérifier la session.
   👉 Explication : confirme la collecte de supervision.

## 2. Production — Contrôles

- Relever les temps d'ouverture de session.
- Consigner le résultat dans la fiche de recette.

## 3. Production — Sécurité

- Utiliser un compte de test sans privilèges.
- Supprimer ce compte après recette.

## Validation et retour arrière

- **Validation** : Machines Registered, licences consommées, session ouverte.
- **Retour arrière** : Si la recette échoue, corriger puis relancer ; sinon revenir au snapshot pré-installation.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops)