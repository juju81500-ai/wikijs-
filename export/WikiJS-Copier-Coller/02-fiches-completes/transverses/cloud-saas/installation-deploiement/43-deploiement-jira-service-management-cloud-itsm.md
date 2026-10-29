# Mettre en service Jira Service Management Cloud pour l'ITSM

- **OS / Version** : Jira Service Management Cloud; service SaaS Atlassian
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Tenant Atlassian Cloud administré par l'organisation
- **Machine ciblée** : N/A — application hébergée par Atlassian
- **Catégorie** : ITSM / centre de services

## 1. Préparer le tenant et la gouvernance

Fiche simple : [préparer le tenant et la gouvernance](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-preparer-tenant-gouvernance).

Jira Service Management Cloud ne s'installe pas sur un serveur local. Valider le tenant, région/résidence des données disponible selon le plan, licences, domaines autorisés, équipe propriétaire, politique de conservation et exigences de conformité. Nommer des administrateurs de site et d'espace; ne pas créer un compte partagé.

Définir les canaux, plages d'assistance, urgences, catégories, délais de service, escalades, intégrations, données personnelles et parcours d'approbation avant d'activer le portail.

## 2. Créer le service space

Fiche simple : [créer le service space](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-creer-service-space).

1. Créer le site Atlassian Cloud selon la procédure de l'organisation, ou sélectionner un site existant.
2. Créer un service space à partir du modèle IT Service Management.
3. Renseigner nom, clé, description, responsable et fuseau horaire; définir le groupe d'agents autorisé.
4. Ajouter les agents nécessaires via les groupes de gestion d'identités et les licences attribuées.

## 3. Structurer demandes et files

Fiche simple : [structurer demandes et files](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-structurer-demandes-files).

- Créer des request types correspondant au vocabulaire des utilisateurs : incident, accès, équipement, logiciel et demande standard.
- Associer les champs requis, catégories et formulaires au processus réel; éviter de collecter des secrets dans les descriptions ou pièces jointes.
- Créer les files de travail des agents selon priorité, statut, équipe et SLA.
- Configurer les workflows pour les transitions réellement approuvées, avec règles d'assignation et d'escalade.
- Configurer les calendriers, priorités et objectifs SLA; tester les conditions et le fuseau horaire avec des exemples.

## 4. Contrôler l'accès clients

Fiche simple : [contrôler l'accès clients](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-controler-acces-clients).

Dans les paramètres d'accès du site et de l'espace, choisir explicitement entre accès restreint aux clients invités et domaines approuvés. Ne pas laisser un portail ouvert à tout Internet sauf décision métier documentée. Vérifier également l'option de partage de demandes, les organisations clientes, SSO/MFA et le traitement des comptes désactivés.

## 5. Configurer les canaux et intégrations

Fiche simple : [configurer les canaux et intégrations](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-configurer-canaux-integrations).

Activer le portail, l'adresse e-mail d'assistance et les canaux retenus. Tester création, accusé de réception, réponse, pièces jointes et déduplication d'e-mails. Ajouter la base de connaissances seulement si elle est gérée et accessible par le bon public.

Pour les intégrations, utiliser des comptes techniques dédiés, scopes minimaux, secrets stockés dans le coffre et rotation planifiée. Les changements de connecteur doivent être validés en espace de test avant production.

## 6. Recette avant ouverture

Fiche simple : [recette avant ouverture](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-recette-ouverture).

- Tester un parcours par catégorie avec un client, un agent et un administrateur.
- Vérifier visibilité des demandes, pièces jointes, notifications, permissions et partage inter-organisation.
- Contrôler files, rapports et SLA pendant les horaires de test.
- Vérifier audit log, SSO/MFA et processus d'arrivée/départ des agents.
- Publier le portail uniquement après approbation du propriétaire du service.

## 7. Exploitation et réversibilité

Fiche simple : [exploitation et réversibilité](/01-fiches-simples/transverses/cloud-saas/jira-service-management/fiche-simple-jira-service-management-deploiement-exploitation-reversibilite).

Documenter propriétaires, licences, groupes, request types, SLA, intégrations, région et export de configuration/données selon les capacités du plan. En cas d'erreur, désactiver le canal ou le connecteur concerné, conserver les tickets existants et rétablir les permissions précédentes.

## Sources

- [Atlassian — Démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Atlassian — Bases d'un projet ITSM](https://support.atlassian.com/jira-service-management-cloud/docs/itsm-project-basics/)
- [Atlassian — Request types](https://support.atlassian.com/jira-service-management-cloud/docs/create-service-desk-request-types/)
- [Atlassian — Permissions clients](https://support.atlassian.com/jira-service-management-cloud/docs/customer-permissions-for-your-service-project-and-jira-site/)