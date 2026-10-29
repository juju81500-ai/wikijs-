---
title: "Fiche Simple - Jira Service Management Deploiement Recette Ouverture"
description: "Tester chaque parcours avant d'ouvrir le portail."
published: true
date: 2026-10-29T19:42:03Z
tags: ["jira-service-management", "atlassian-cloud", "itsm", "saas"]
editor: markdown
dateCreated: 2026-10-29T19:42:03Z
dateModified: 2026-10-29T19:42:03Z
---

# Fiche_Simple_-_Jira_Service_Management_Deploiement_Recette_Ouverture.md

- **Environnement** : Tenant Atlassian Cloud administré par l'organisation (SaaS, aucune machine locale)
- **OS / Version** : Jira Service Management Cloud (SaaS Atlassian)
- **Catégorie** : ITSM / centre de services
- **Tags** : `jira-service-management`, `atlassian-cloud`, `itsm`, `saas`

---

## Problème précis à résoudre

Tester chaque parcours avant d'ouvrir le portail.

## 1. Hors-Production (Lab / Test / POC)

1. Tester un parcours par catégorie avec un client, un agent et un administrateur.
   👉 Explication : valide les trois rôles.

2. Vérifier visibilité des demandes, pièces jointes, notifications, permissions et partage inter-organisation.
   👉 Explication : détecte les fuites d'information.

3. Contrôler files, rapports et SLA pendant les horaires de test.
   👉 Explication : vérifie le calcul réel des délais.

4. Consulter le journal d'audit : **admin.atlassian.com > Sécurité > Journal d'audit** (selon le plan).
   👉 Explication : confirme que les actions sensibles sont tracées; vérifier aussi SSO/MFA et arrivée/départ des agents.

5. Publier le portail seulement après approbation du propriétaire du service.
   👉 Explication : évite une ouverture non validée.

## 2. Production — Contrôles

Conserver le compte rendu de recette signé par le propriétaire du service.

## 3. Production — Sécurité

- Utiliser des données de test, pas de données personnelles réelles.

## Validation et retour arrière

- **Validation** : tous les parcours de recette sont réussis et approuvés.
- **Retour arrière** : repasser le portail en inaccessible ou retirer le canal tant que les anomalies ne sont pas corrigées.

## Si le problème n'est pas résolu

- [Atlassian — Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/)
- [Atlassian — démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Guide complet](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm#6-recette-avant-ouverture)