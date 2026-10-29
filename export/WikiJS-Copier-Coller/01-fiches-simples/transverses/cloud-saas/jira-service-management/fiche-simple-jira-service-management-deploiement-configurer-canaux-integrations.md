# Fiche_Simple_-_Jira_Service_Management_Deploiement_Configurer_Canaux_Integrations.md

- **Environnement** : Tenant Atlassian Cloud administré par l'organisation (SaaS, aucune machine locale)
- **OS / Version** : Jira Service Management Cloud (SaaS Atlassian)
- **Catégorie** : ITSM / centre de services

---

## Problème précis à résoudre

Activer portail, e-mail et intégrations avec des droits minimaux.

## 1. Hors-Production (Lab / Test / POC)

1. **Paramètres de l'espace > Canaux > Portail** : activer le portail.
   👉 Explication : point d'entrée principal des clients.

2. **Canaux > E-mail** : configurer l'adresse d'assistance, puis tester création, accusé de réception, réponse, pièces jointes et déduplication.
   👉 Explication : valide le cycle complet par e-mail.

3. Ajouter la base de connaissances seulement si elle est gérée et accessible par le bon public.
   👉 Explication : évite de publier des contenus internes.

4. Pour chaque intégration, créer un compte technique dédié avec des scopes minimaux; stocker le secret dans le coffre et planifier sa rotation.
   👉 Explication : limite l'impact d'une fuite.

5. Valider les changements de connecteur dans un espace de test avant production.
   👉 Explication : évite les perturbations du service.

## 2. Production — Contrôles

Tenir le registre des intégrations, comptes techniques, scopes et dates de rotation.

## 3. Production — Sécurité

- Aucun secret saisi en clair dans un ticket ou une fiche.
- Comptes techniques nominatifs au rôle, jamais personnels.

## Validation et retour arrière

- **Validation** : création de ticket par portail et e-mail fonctionnelle, intégrations testées.
- **Retour arrière** : désactiver le canal ou le connecteur concerné et conserver les tickets existants.

## Si le problème n'est pas résolu

- [Atlassian — Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/)
- [Atlassian — démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Guide complet](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm#5-configurer-les-canaux-et-integrations)