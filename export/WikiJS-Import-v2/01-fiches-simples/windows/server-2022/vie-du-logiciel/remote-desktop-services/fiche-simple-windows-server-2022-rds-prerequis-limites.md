---
title: "Fiche Simple - Windows Server 2022 RDS Prerequis Limites"
description: "Définir le périmètre et une architecture RDS supportable avant d'installer un hôte de session ou d'ouvrir l'accès distant."
published: true
date: 2026-10-29T20:39:58Z
tags: ["windows-server-2022", "rds", "prerequis", "architecture"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_Windows_Server_2022_RDS_Prerequis_Limites

- **Environnement** : VM ou serveur Windows dédié aux services Bureau à distance
- **OS / Version** : Windows Server 2022 Desktop Experience
- **Catégorie** : Vie du logiciel / Services Bureau à distance
- **Tags** : `windows-server-2022`, `rds`, `prerequis`, `architecture`

---

## Problème précis à résoudre

Définir le périmètre et une architecture RDS supportable avant d'installer un hôte de session ou d'ouvrir l'accès distant.

## 1. Hors-Production (Lab / Test / POC)

1. Relever édition, version et nom du serveur :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   hostname
   ```
   👉 Explication : Confirme l'identité de la machine cible; vérifier les prérequis officiels avant la production.
2. Inventorier les rôles déjà installés :
   ```powershell
   Get-WindowsFeature RDS*, Remote-Desktop-Services*
   ```
   👉 Explication : Repère les services RDS présents et évite d'ajouter un rôle à un serveur dont le périmètre n'a pas été validé.
3. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités**, examiner les règles et rôles RDS sans valider l'installation.
   👉 Explication : L'assistant distingue l'installation d'un rôle seul d'un déploiement RDS complet; les choix dépendent du scénario.

## 2. Production — Contrôles

- Documenter nombre de sessions, capacité, disponibilité, DNS, certificats, réseau d'administration et dépendance Active Directory.
- Vérifier licence Windows Server, CAL RDS, mode de licence et capacité du serveur de licences avant l'ouverture.
- Les déploiements multi-serveurs et rôles Broker/Gateway/Web Access exigent une architecture cohérente; ne pas les ajouter par défaut sur un contrôleur de domaine.

## 3. Production — Sécurité

- Ne pas publier directement TCP/UDP 3389 sur Internet; privilégier VPN ou RD Gateway approuvée.
- Prévoir accès console hors bande et pilote avant tout changement de rôle ou de pare-feu.
- Limiter les groupes autorisés aux utilisateurs ayant un besoin métier documenté.

## Validation et retour arrière

- **Validation** : édition, rôle envisagé, licences et flux sont documentés et approuvés.
- **Retour arrière** : aucune modification appliquée; suspendre le déploiement si un prérequis manque.

## Si le problème n'est pas résolu

- [Microsoft Learn — Vue d'ensemble RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/overview)
- [Microsoft Learn — Licences RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license)
- [Installer et configurer RDS](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-installer-configurer)