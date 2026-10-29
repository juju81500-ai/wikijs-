---
title: "Fiche Simple - Windows Server 2022 Differences 2016 2019 Fin Support Perimetre"
description: "Identifier la version et l'édition en place, puis situer 2016 et 2019 dans leur cycle de support avant toute décision de maintien ou de migration."
published: true
date: 2026-10-29T21:23:12Z
tags: ["windows-server", "windows-server-2016", "windows-server-2019", "windows-server-2022", "fin-de-support", "cycle-de-vie"]
editor: markdown
dateCreated: 2026-10-29T21:23:12Z
dateModified: 2026-10-29T21:23:12Z
---

# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Fin_Support_Perimetre

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions
- **Tags** : `windows-server`, `windows-server-2016`, `windows-server-2019`, `windows-server-2022`, `fin-de-support`, `cycle-de-vie`

---

## Problème précis à résoudre

Identifier la version et l'édition en place, puis situer 2016 et 2019 dans leur cycle de support avant toute décision de maintien ou de migration.

## 1. Hors-Production (Lab / Test / POC)

1. Relever la version, l'édition et le numéro de build :
   ```powershell
   Get-ComputerInfo -Property WindowsProductName,WindowsVersion,OsBuildNumber
   (Get-CimInstance Win32_OperatingSystem).Caption
   ```
   👉 Explication : le build identifie la version réelle ; `WindowsProductName` indique 2016, 2019 ou 2022.
2. Consulter la page de cycle de vie Microsoft de la version concernée (Microsoft Lifecycle) et noter les dates de fin de support standard et étendu.
   👉 Explication : ne pas se fier à une date recopiée : la date officielle publiée par Microsoft fait foi ; à ce jour Windows Server 2016 et 2019 sont en support étendu (correctifs de sécurité seulement, pas de nouvelles fonctions), à vérifier à la date de la décision.
3. Lister les rôles installés pour mesurer l'effort de migration :
   ```powershell
   Get-WindowsFeature | Where-Object Installed
   ```
   👉 Explication : un serveur à rôles nombreux (AD DS, DNS, DHCP, WSUS, RDS) demande un plan de migration dédié.

## 2. Production — Contrôles

- Inscrire la date de fin de support dans l'inventaire et planifier la migration au moins 12 mois avant.
- Après la fin du support étendu, des mises à jour de sécurité ne sont disponibles que via un programme payant éventuel (ESU) : vérifier la disponibilité sur la page officielle.

## 3. Production — Sécurité

- Un serveur hors support exposé au réseau est un risque : isoler (VLAN, pare-feu) et réduire les rôles si la migration est reportée.

## Validation et retour arrière

- **Validation** : version, build et dates de support consignés dans l'inventaire. **Retour arrière** : sans objet (lecture seule).

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-windows-server-2016-2019-2022)
- [Microsoft Lifecycle — Windows Server 2016](https://learn.microsoft.com/fr-fr/lifecycle/products/windows-server-2016)
- [Microsoft Lifecycle — Windows Server 2019](https://learn.microsoft.com/fr-fr/lifecycle/products/windows-server-2019)
- [Microsoft Learn — Windows Server](https://learn.microsoft.com/fr-fr/windows-server/)