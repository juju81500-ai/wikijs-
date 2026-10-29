---
title: "Fiche Simple - Cloud Google Workspace Valider Recette"
description: "Recetter l'ensemble de la configuration défensive de Google Workspace."
published: true
date: 2026-10-29T20:32:32Z
tags: ["google-workspace", "gmail", "cloud-saas", "administration-defensive", "messagerie", "tssr"]
editor: markdown
dateCreated: 2026-10-29T20:32:32Z
dateModified: 2026-10-29T20:32:32Z
---

# Fiche_Simple_-_Cloud_Google_Workspace_Valider_Recette

- **Environnement** : Tenant Google Workspace (SaaS), administré via la console d'administration admin.google.com
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `google-workspace`, `gmail`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Recetter l'ensemble de la configuration défensive de Google Workspace.

## 1. Hors-Production (Lab / Test / POC)

1. Console d'administration > Compte > Domaines : domaine validé.
   👉 Explication : cohérence avec l'inventaire.

2. Contrôler la 2SV :
   ```bash
   gam print users fields isenrolledin2sv,isenforcedin2sv
   ```
   👉 Explication : taux d'enrôlement cohérent (GAM optionnel).

3. Envoyer un message de test vers une boîte externe et lire les en-têtes (SPF, DKIM, DMARC).
   👉 Explication : confirme les contrôles de bout en bout.

4. Vérifier dans Vault que la règle de rétention est active.
   👉 Explication : preuve de recette.

## 2. Production — Contrôles

Archiver captures et résultats.

## 3. Production — Sécurité

- Ne pas inclure de données personnelles.

## Validation et retour arrière

- **Validation** : Tous les contrôles sont conformes.
- **Retour arrière** : Annuler le dernier changement selon la fiche concernée.

## Si le problème n'est pas résolu

- [Centre d'aide Google Workspace Admin](https://support.google.com/a/)
- [Fiche d'entrée Google Workspace](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-google-workspace)