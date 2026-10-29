---
title: "Fiche Simple - Windows Server 2022 Exchange Server Mise A Jour CU"
description: "Appliquer un Cumulative Update (ou une mise à jour de sécurité) sans perte de service et savoir comment revenir en arrière."
published: true
date: 2026-10-29T20:32:39Z
tags: ["windows-server-2022", "exchange-server", "messagerie", "mise-a-jour", "cumulative-update", "cu"]
editor: markdown
dateCreated: 2026-10-29T20:32:39Z
dateModified: 2026-10-29T20:32:39Z
---

# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Mise_A_Jour_CU

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / maintenance
- **Tags** : `windows-server-2022`, `exchange-server`, `messagerie`, `mise-a-jour`, `cumulative-update`, `cu`

---

## Problème précis à résoudre

Appliquer un Cumulative Update (ou une mise à jour de sécurité) sans perte de service et savoir comment revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les notes de version du CU, vérifier la matrice de support, télécharger l'ISO depuis la source Microsoft et contrôler son hachage.
   👉 Explication : un CU est un paquet complet, appliqué directement sur la version précédente.

2. Sauvegarder (voir fiche DAG et sauvegarde) et lancer le contrôle d'état avant intervention, par exemple avec l'outil officiel HealthChecker (CSS-Exchange) ; contrôler `Get-MailboxDatabaseCopyStatus`.
   👉 Explication : garantir un état sain avant la mise à jour.

3. Mettre le serveur en maintenance (DAG) depuis Exchange Management Shell :
   ```powershell
   cd $env:ExchangeInstallPath\Scripts
   .\StartDagServerMaintenance.ps1 -serverName EXCH01
   Set-ServerComponentState EXCH01 -Component ServerWideOffline -State Inactive -Requester Maintenance
   ```
   👉 Explication : vide les files et déplace les bases actives ; sans DAG, informer les utilisateurs de l'interruption.

4. Monter l'ISO du CU et lancer la mise à jour : assistant `Setup.exe` > Mise à niveau, ou :
   ```powershell
   D:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /Mode:Upgrade
   ```
   👉 Explication : tourner sous un compte administrateur local, en PowerShell élevé et non en session RDP déconnectable.

5. Sortir le serveur de maintenance :
   ```powershell
   Set-ServerComponentState EXCH01 -Component ServerWideOffline -State Active -Requester Maintenance
   .\StopDagServerMaintenance.ps1 -serverName EXCH01
   Restart-Computer
   ```
   👉 Explication : les composants redeviennent actifs ; refaire les contrôles après redémarrage.

## 2. Production — Contrôles

Mettre à jour un serveur à la fois, hors heures ouvrées, ordre selon la documentation (extensions AD si exigées), redémarrer, puis appliquer les mises à jour de sécurité (SU) en mode élevé.

## 3. Production — Sécurité

- Télécharger uniquement depuis Microsoft et vérifier la signature.
- Conserver les mises à jour de sécurité à jour : un CU récent est requis pour installer une SU.
- Auditer les accès durant la maintenance.

## Validation et retour arrière

- **Validation** : `Get-ExchangeServer | fl Name,AdminDisplayVersion` indique le nouveau build, `Test-ServiceHealth` et `Test-ReplicationHealth` sont sains.
- **Retour arrière** : la désinstallation d'un CU n'est pas supportée : restaurer la VM/sauvegarde ou réinstaller le serveur avec `Setup.exe /Mode:RecoverServer` après avoir réinstallé le système, puis ré-ajouter les copies DAG ; tester ce scénario en lab.

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-server)