---
title: "Fiche Simple - Windows Server 2025 Exchange Server Prerequis Limites"
description: "Confirmer que Windows Server 2025 et l’environnement Active Directory sont compatibles avec Exchange Server Subscription Edition avant de préparer un serveur."
published: true
date: 2026-10-29T21:10:29Z
tags: ["windows-server-2025", "exchange-server-se", "messagerie", "prerequis-limites"]
editor: markdown
dateCreated: 2026-10-29T21:10:29Z
dateModified: 2026-10-29T21:10:29Z
---

# Fiche_Simple_-_Windows_Server_2025_Exchange_Server_Prerequis_Limites

- **Environnement** : Windows Server 2025 Standard ou Datacenter; Exchange Server Subscription Edition
- **OS / Version** : Windows Server 2025; Exchange SE — valider le build et les prérequis publiés avant intervention
- **Catégorie** : messagerie / prérequis
- **Tags** : `windows-server-2025`, `exchange-server-se`, `messagerie`, `prerequis-limites`

---

## Problème précis à résoudre

Confirmer que Windows Server 2025 et l’environnement Active Directory sont compatibles avec Exchange Server Subscription Edition avant de préparer un serveur.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier l’édition et la version de Windows Server dans **Paramètres > Système > Informations système** ou avec PowerShell :
   ```powershell
   Get-ComputerInfo -Property OsName,OsVersion,WindowsProductName
   ```
   👉 Explication : Exchange SE est publié comme pris en charge sur Windows Server 2025 Standard ou Datacenter; Desktop Experience et Server Core sont listés, Server Core recommandé.

2. Consulter la matrice Microsoft pour confirmer la combinaison Exchange SE / Windows Server 2025 et le CU/SU visé.
   👉 Explication : la matrice éditeur prévaut; une compatibilité non listée ne doit pas être supposée.

3. Vérifier l’environnement Active Directory et les prérequis Exchange SE avant toute préparation de schéma.
   👉 Explication : Microsoft précise qu’un contrôleur Windows Server 2025 portant le rôle Schema Master doit avoir la mise à jour cumulative de novembre 2025 (KB5068861) ou ultérieure avant l’opération PrepareAD.

4. Concevoir stockage, réseau, DNS et sauvegarde selon la documentation de déploiement Microsoft.
   👉 Explication : les valeurs de dimensionnement et composants requis changent selon le CU/SU; ne pas recopier une liste d’un ancien guide sans vérification.

5. Vérifier qu’aucune mise à niveau sur place de l’OS d’un serveur Exchange existant n’est prévue.
   👉 Explication : Microsoft ne prend pas en charge la mise à niveau majeure de Windows Server avec Exchange installé; cette fiche couvre un nouveau déploiement.

## 2. Production — Contrôles

Planifier une fenêtre de changement, sauvegarder les configurations concernées, vérifier l’état AD/DNS et Exchange, puis appliquer les étapes d’abord en environnement pilote.

## 3. Production — Sécurité

- Utiliser des comptes nominatifs et les rôles minimaux requis; retirer les privilèges temporaires après l’opération.
- Restreindre EAC et Exchange Management Shell au réseau d’administration.
- Ne pas consigner de mot de passe, clé privée, jeton ou donnée de boîte aux lettres dans cette fiche.

## Validation et retour arrière

**Validation** : Windows Server 2025, édition, niveau de correctifs AD, rôle Schema Master, version Exchange SE et prérequis sont consignés et concordent avec les pages Microsoft consultées.
- **Retour arrière** : aucune modification n’est faite à cette étape.

## Si le problème n’est pas résolu

- [Matrice de support Exchange](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/supportability-matrix)
- [Prérequis Exchange SE](https://learn.microsoft.com/en-us/exchange/plan-and-deploy/prerequisites)
- [Fiche d’entrée Exchange Server](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-server)