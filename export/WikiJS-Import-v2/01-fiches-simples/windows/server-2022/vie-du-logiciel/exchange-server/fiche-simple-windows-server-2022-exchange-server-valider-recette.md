---
title: "Fiche Simple - Windows Server 2022 Exchange Server Valider Recette"
description: "Valider le bon fonctionnement d'Exchange avant ouverture aux utilisateurs."
published: true
date: 2026-10-29T20:32:39Z
tags: ["windows-server-2022", "exchange-server", "messagerie", "recette", "validation", "test"]
editor: markdown
dateCreated: 2026-10-29T20:32:39Z
dateModified: 2026-10-29T20:32:39Z
---

# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Valider_Recette

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / recette
- **Tags** : `windows-server-2022`, `exchange-server`, `messagerie`, `recette`, `validation`, `test`

---

## Problème précis à résoudre

Valider le bon fonctionnement d'Exchange avant ouverture aux utilisateurs.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une boîte de test : EAC > Destinataires > Boîtes aux lettres > + ; ou :
   ```powershell
   $pwd1 = Read-Host "Mot de passe" -AsSecureString
   New-Mailbox -Name "Test Recette" -UserPrincipalName test.recette@example.net -Password $pwd1
   ```
   👉 Explication : le mot de passe est saisi, jamais écrit dans la fiche.

2. Contrôler les services et la santé :
   ```powershell
   Test-ServiceHealth -Server EXCH01
   Get-HealthReport -Server EXCH01 | Where-Object AlertValue -ne Healthy
   ```
   👉 Explication : détecte services arrêtés et sondes en échec.

3. Tester les flux client et la messagerie :
   ```powershell
   Test-MapiConnectivity -Server EXCH01
   Test-OutlookWebServices -Identity test.recette@example.net
   Test-Mailflow EXCH01
   ```
   👉 Explication : valide MAPI, Autodiscover/EWS et flux de messages ; compléter par l'outil Microsoft Remote Connectivity Analyzer pour l'externe.

4. Envoyer un message interne puis externe depuis OWA (`https://mail.example.net/owa`) et vérifier la réception.
   👉 Explication : valide l'ensemble du chemin utilisateur.

## 2. Production — Contrôles

Conserver les résultats de test, vérifier l'événementiel et les files, et signer la recette avec le référent messagerie.

## 3. Production — Sécurité

- Supprimer les boîtes et comptes de test après recette.
- Contrôler qu'aucun relais ouvert n'existe (test depuis une IP non autorisée).

## Validation et retour arrière

- **Validation** : tous les tests retournent `Success`, aucun élément critique du rapport de santé.
- **Retour arrière** : supprimer la boîte de test (`Remove-Mailbox`) ; en cas d'échec, ne pas ouvrir le service et corriger les points bloquants.

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-server)