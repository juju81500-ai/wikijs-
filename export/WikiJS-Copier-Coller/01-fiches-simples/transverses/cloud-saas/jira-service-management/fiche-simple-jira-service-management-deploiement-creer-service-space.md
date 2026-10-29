# Fiche_Simple_-_Jira_Service_Management_Deploiement_Creer_Service_Space.md

- **Environnement** : Tenant Atlassian Cloud administré par l'organisation (SaaS, aucune machine locale)
- **OS / Version** : Jira Service Management Cloud (SaaS Atlassian)
- **Catégorie** : ITSM / centre de services

---

## Problème précis à résoudre

Créer l'espace de service ITSM et y rattacher les bons agents.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le site Atlassian Cloud selon la procédure de l'organisation, ou sélectionner le site existant.
   👉 Explication : le site contient l'espace de service.

2. Dans Jira Service Management : **Espaces > Créer un espace > Gestion des services informatiques (ITSM)**.
   👉 Explication : utilise le modèle ITSM prévu.

3. Renseigner nom, clé, description, responsable et fuseau horaire.
   👉 Explication : la clé ne se change pas facilement; choisir un fuseau cohérent avec les SLA.

4. Définir le groupe d'agents autorisé : **Paramètres de l'espace > Accès**.
   👉 Explication : seuls les agents désignés accèdent à l'espace.

5. Ajouter les agents via les groupes d'identité et les licences attribuées.
   👉 Explication : évite l'ajout nominatif manuel hors processus.

## 2. Production — Contrôles

Documenter propriétaire, clé de l'espace, groupes et licences utilisées.

## 3. Production — Sécurité

- Appliquer le moindre privilège aux agents et administrateurs d'espace.

## Validation et retour arrière

- **Validation** : l'espace existe, le responsable est défini et seuls les agents prévus y accèdent.
- **Retour arrière** : archiver ou supprimer l'espace de test (**Paramètres de l'espace > Supprimer**) tant qu'il ne contient pas de tickets réels.

## Si le problème n'est pas résolu

- [Atlassian — bases d'un projet ITSM](https://support.atlassian.com/jira-service-management-cloud/docs/itsm-project-basics/)
- [Atlassian — démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Guide complet](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm#2-creer-le-service-space)