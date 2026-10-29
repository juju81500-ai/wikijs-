---
title: "Fiche Simple - Jira Service Management Deploiement Controler Acces Clients"
description: "Empêcher un portail ouvert à tout Internet sans décision métier."
published: true
date: 2026-10-29T19:42:03Z
tags: ["jira-service-management", "atlassian-cloud", "itsm", "saas"]
editor: markdown
dateCreated: 2026-10-29T19:42:03Z
dateModified: 2026-10-29T19:42:03Z
---

# Fiche_Simple_-_Jira_Service_Management_Deploiement_Controler_Acces_Clients.md

- **Environnement** : Tenant Atlassian Cloud administré par l'organisation (SaaS, aucune machine locale)
- **OS / Version** : Jira Service Management Cloud (SaaS Atlassian)
- **Catégorie** : ITSM / centre de services
- **Tags** : `jira-service-management`, `atlassian-cloud`, `itsm`, `saas`

---

## Problème précis à résoudre

Empêcher un portail ouvert à tout Internet sans décision métier.

## 1. Hors-Production (Lab / Test / POC)

1. **Paramètres de l'espace > Accès client** : choisir explicitement entre clients invités uniquement et domaines approuvés.
   👉 Explication : ne pas laisser un portail public sauf décision métier documentée.

2. Vérifier l'option de partage de demandes et les organisations clientes.
   👉 Explication : évite l'exposition de tickets entre organisations.

3. Contrôler SSO/MFA dans **admin.atlassian.com > Sécurité**.
   👉 Explication : renforce l'authentification des comptes.

4. Vérifier le traitement des comptes désactivés.
   👉 Explication : un compte désactivé ne doit plus accéder aux demandes.

## 2. Production — Contrôles

Faire valider le modèle d'accès client par le responsable sécurité.

## 3. Production — Sécurité

- Pas d'accès anonyme sans décision métier documentée.
- Restreindre aux domaines approuvés.

## Validation et retour arrière

- **Validation** : un utilisateur hors périmètre ne peut ni s'inscrire ni voir de demande.
- **Retour arrière** : rétablir le paramètre d'accès précédent depuis la documentation de configuration.

## Si le problème n'est pas résolu

- [Atlassian — permissions clients](https://support.atlassian.com/jira-service-management-cloud/docs/customer-permissions-for-your-service-project-and-jira-site/)
- [Atlassian — démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Guide complet](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm#4-controler-lacces-clients)