---
title: "Fiche Simple - Jira Service Management Deploiement Preparer Tenant Gouvernance"
description: "Valider tenant, licences et règles de gouvernance avant d'activer le portail."
published: true
date: 2026-10-29T19:42:03Z
tags: ["jira-service-management", "atlassian-cloud", "itsm", "saas"]
editor: markdown
dateCreated: 2026-10-29T19:42:03Z
dateModified: 2026-10-29T19:42:03Z
---

# Fiche_Simple_-_Jira_Service_Management_Deploiement_Preparer_Tenant_Gouvernance.md

- **Environnement** : Tenant Atlassian Cloud administré par l'organisation (SaaS, aucune machine locale)
- **OS / Version** : Jira Service Management Cloud (SaaS Atlassian)
- **Catégorie** : ITSM / centre de services
- **Tags** : `jira-service-management`, `atlassian-cloud`, `itsm`, `saas`

---

## Problème précis à résoudre

Valider tenant, licences et règles de gouvernance avant d'activer le portail.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **admin.atlassian.com > Produits** pour confirmer le site, les licences et le plan.
   👉 Explication : Jira Service Management Cloud ne s'installe pas localement; tout se règle dans le tenant.

2. Vérifier la région et la résidence des données disponibles selon le plan : **Paramètres > Résidence des données** (libellé variable selon le plan).
   👉 Explication : à valider avec la conformité avant de créer des données.

3. Vérifier **Domaines** et la politique d'identité (SSO/MFA).
   👉 Explication : seuls les domaines de l'organisation doivent être autorisés.

4. Nommer des administrateurs de site et d'espace nominatifs : **Utilisateurs > Gérer les utilisateurs**.
   👉 Explication : ne jamais créer un compte partagé.

5. Rédiger par écrit canaux, plages d'assistance, urgences, catégories, délais, escalades, intégrations, données personnelles et parcours d'approbation.
   👉 Explication : ces décisions doivent exister avant d'activer le portail.

## 2. Production — Contrôles

Faire valider par le propriétaire du service : conservation des données, conformité, licences, équipe propriétaire.

## 3. Production — Sécurité

- Aucun compte administrateur partagé.
- Données personnelles: définir conservation et accès avant ouverture.

## Validation et retour arrière

- **Validation** : tenant, région, licences, domaines et administrateurs nommés sont documentés.
- **Retour arrière** : aucune donnée créée par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Atlassian — bases d'un projet ITSM](https://support.atlassian.com/jira-service-management-cloud/docs/itsm-project-basics/)
- [Atlassian — démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Guide complet](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm#1-preparer-le-tenant-et-la-gouvernance)