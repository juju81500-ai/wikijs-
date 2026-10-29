---
title: "Fiche Simple - Cloud Exchange Online Definir Retention"
description: "Définir la rétention des messages et se protéger contre la suppression accidentelle."
published: true
date: 2026-10-29T20:32:32Z
tags: ["exchange-online", "microsoft-365", "cloud-saas", "administration-defensive", "messagerie", "tssr"]
editor: markdown
dateCreated: 2026-10-29T20:32:32Z
dateModified: 2026-10-29T20:32:32Z
---

# Fiche_Simple_-_Cloud_Exchange_Online_Definir_Retention

- **Environnement** : Tenant Microsoft 365 / Exchange Online (SaaS), administré depuis un poste d'administration
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `exchange-online`, `microsoft-365`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Définir la rétention des messages et se protéger contre la suppression accidentelle.

## 1. Hors-Production (Lab / Test / POC)

1. Interface : portail Microsoft Purview > Gestion du cycle de vie des données (Data Lifecycle Management) > Stratégies de rétention > Nouvelle stratégie de rétention, emplacement Exchange, durée définie par la politique de l'organisation.
   👉 Explication : la rétention est gérée par stratégie; licences requises selon le cas.

2. Vérifier la rétention des éléments supprimés d'une boîte aux lettres :
   ```powershell
   Get-Mailbox -Identity UTILISATEUR | Format-List RetainDeletedItemsFor,LitigationHoldEnabled
   ```
   👉 Explication : UTILISATEUR est à remplacer; la valeur par défaut est à vérifier dans la documentation.

3. Si la durée doit être portée à son maximum :
   ```powershell
   Set-Mailbox -Identity UTILISATEUR -RetainDeletedItemsFor 30
   ```
   👉 Explication : 30 jours est la valeur maximale documentée pour cette propriété; vérifier.

4. Pour un besoin juridique, utiliser un blocage (hold) via Purview eDiscovery plutôt qu'une modification manuelle.
   👉 Explication : le blocage est tracé et réservé aux rôles dédiés.

## 2. Production — Contrôles

Faire valider la durée par le juridique/DPO; documenter les exceptions.

## 3. Production — Sécurité

- Restreindre les rôles Purview.
- Journaliser les changements de stratégie.

## Validation et retour arrière

- **Validation** : La stratégie est « Réussie » (statut de distribution) dans Purview; la propriété est lue par `Get-Mailbox`.
- **Retour arrière** : Restaurer la valeur précédente notée avant modification; désactiver la stratégie de rétention si nécessaire.

## Si le problème n'est pas résolu

- [Stratégies de rétention Microsoft Purview](https://learn.microsoft.com/purview/retention)
- [Exchange Online — documentation officielle](https://learn.microsoft.com/exchange/exchange-online)
- [Fiche d'entrée Exchange Online](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-online)