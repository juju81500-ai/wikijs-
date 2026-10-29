---
title: "Fiche Simple - Windows Server 2022 MECM Prerequis"
description: "Vérifier que l'architecture (AD DS, SQL Server, ADK/WinPE, rôles Windows) est prête et supportée avant toute installation de MECM/SCCM. Cette fiche n'installe pas le produit."
published: true
date: 2026-10-29T20:39:58Z
tags: ["windows-server-2022", "mecm", "sccm", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_Windows_Server_2022_MECM_Prerequis

- **Environnement** : Windows Server 2022 (futur serveur de site MECM/SCCM) dans un domaine AD DS
- **OS / Version** : Windows Server 2022; version de Configuration Manager current branch : vérifier la version publiée et la matrice de support Microsoft
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `windows-server-2022`, `mecm`, `sccm`, `prerequis`

---

## Problème précis à résoudre

Vérifier que l'architecture (AD DS, SQL Server, ADK/WinPE, rôles Windows) est prête et supportée avant toute installation de MECM/SCCM. Cette fiche n'installe pas le produit.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les variables (MAJUSCULES, à remplacer) :
   ```powershell
   $Domaine = "DOMAINE.LOCAL"      # à remplacer : nom DNS du domaine
   $DnDomaine = "DC=DOMAINE,DC=LOCAL"   # à remplacer : DN du domaine
   ```
   👉 Explication : ces valeurs servent aux contrôles suivants; rien n'est modifié.

2. Contrôler l'OS et le domaine. GUI : `Gestionnaire de serveur > Serveur local`.
   ```powershell
   Get-ComputerInfo | Select-Object OsName, OsVersion, CsDomain, CsPartOfDomain
   ```
   👉 Explication : le serveur doit être membre du domaine et sous Windows Server 2022; confirmer que cet OS figure dans la matrice « Supported operating systems for site system servers » de la version choisie.

3. Contrôler le schéma AD et le conteneur System Management (module ActiveDirectory requis).
   ```powershell
   $Schema = (Get-ADRootDSE).schemaNamingContext
   Get-ADObject $Schema -Properties objectVersion | Select-Object objectVersion
   Get-ADObject -Filter 'Name -eq "System Management"' -SearchBase "CN=System,$DnDomaine"
   ```
   👉 Explication : la dernière commande ne renvoie rien si le conteneur n'existe pas encore (créé lors de la publication du site). L'extension du schéma est facultative dans les versions récentes : vérifier la version publiée.

4. Contrôler SQL Server (la version supportée dépend de la version MECM : vérifier la page « Support for SQL Server versions »).
   ```powershell
   Get-Service MSSQLSERVER, SQLSERVERAGENT -ErrorAction SilentlyContinue
   sqlcmd -S . -E -Q "SELECT SERVERPROPERTY('ProductVersion') AS Version, SERVERPROPERTY('Collation') AS Collation"
   ```
   👉 Explication : la collation requise par Microsoft (`SQL_Latin1_General_CP1_CI_AS`, à vérifier) doit correspondre. Si le service n'existe pas, SQL n'est pas installé : s'arrêter ici.

5. Contrôler ADK et WinPE. GUI : `Paramètres > Applications > Applications installées`.
   ```powershell
   Get-Package -Name "Windows Assessment and Deployment Kit*" -ErrorAction SilentlyContinue
   ```
   👉 Explication : l'ADK et son extension WinPE doivent figurer dans la liste; la version exigée dépend de la version MECM : vérifier la version publiée.

6. Contrôler les fonctionnalités Windows (selon les rôles de site retenus).
   ```powershell
   Get-WindowsFeature BITS, RDC, Web-Server, NET-Framework-45-Core | Select-Object Name, InstallState
   ```
   👉 Explication : la liste exacte dépend des rôles (point de distribution, point de gestion…) : vérifier la page « Site and site system prerequisites ».

## 2. Production — Contrôles

Faire valider par l'architecte : topologie (site autonome ou hiérarchie), dimensionnement, espace disque, code de site, planning. Ne pas installer tant qu'un contrôle est en échec.

## 3. Production — Sécurité

- Prévoir des comptes de service dédiés, sans droits d'administrateur de domaine; aucun mot de passe dans les fiches ni les scripts.
- Si un prérequis n'est pas supporté par la matrice, ne pas contourner : changer la version cible.

## Validation et retour arrière

- **Validation** : chaque contrôle est consigné; aucune ligne de la matrice n'est « non supportée ».
- **Retour arrière** : aucune modification effectuée : rien à annuler.

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm)
- [Microsoft Learn — Prérequis de site](https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/configs/site-and-site-system-prerequisites)
- [Microsoft Learn — Versions de SQL Server prises en charge](https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/configs/support-for-sql-server-versions)
- [Microsoft Learn — Systèmes d'exploitation pris en charge](https://learn.microsoft.com/en-us/intune/configmgr/core/plan-design/configs/supported-operating-systems-for-site-system-servers)