# Fiche_Simple_-_Jira_Service_Management_Deploiement_Structurer_Demandes_Files.md

- **Environnement** : Tenant Atlassian Cloud administré par l'organisation (SaaS, aucune machine locale)
- **OS / Version** : Jira Service Management Cloud (SaaS Atlassian)
- **Catégorie** : ITSM / centre de services

---

## Problème précis à résoudre

Créer request types, files, workflows et SLA alignés sur le processus réel.

## 1. Hors-Production (Lab / Test / POC)

1. **Paramètres de l'espace > Types de demande > Créer** : incident, accès, équipement, logiciel, demande standard.
   👉 Explication : les noms correspondent au vocabulaire des utilisateurs.

2. Associer champs obligatoires, catégories et formulaires à chaque type.
   👉 Explication : éviter de demander des secrets dans les descriptions ou pièces jointes.

3. **Files > Créer une file** selon priorité, statut, équipe et SLA.
   👉 Explication : les agents travaillent depuis ces files.

4. **Paramètres de l'espace > Workflows** : configurer les transitions approuvées avec assignation et escalade.
   👉 Explication : limite les transitions à celles réellement validées.

5. **Paramètres de l'espace > SLA** : définir calendriers, priorités et objectifs, puis tester avec des exemples et le bon fuseau.
   👉 Explication : vérifie que les conditions de démarrage et d'arrêt sont correctes.

## 2. Production — Contrôles

Faire valider les types de demande, workflows et SLA par le propriétaire du service avant l'ouverture.

## 3. Production — Sécurité

- Interdire les mots de passe et secrets dans les champs de demande.

## Validation et retour arrière

- **Validation** : une demande de test par type suit son workflow, apparaît dans la bonne file et déclenche le bon SLA.
- **Retour arrière** : restaurer le workflow ou le SLA précédent depuis la configuration documentée et désactiver le type de demande fautif.

## Si le problème n'est pas résolu

- [Atlassian — request types](https://support.atlassian.com/jira-service-management-cloud/docs/create-service-desk-request-types/)
- [Atlassian — démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Guide complet](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm#3-structurer-demandes-et-files)