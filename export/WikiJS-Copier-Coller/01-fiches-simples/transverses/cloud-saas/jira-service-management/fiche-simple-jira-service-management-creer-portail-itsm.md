# 📄 Fiche_Simple_-_Jira_Service_Management_Creer_Portail_ITSM.md

- **Environnement** : Jira Service Management Cloud
- **OS / Version** : N/A — service SaaS
- **Catégorie** : Service / ITSM

---

## 🎯 Problème précis à résoudre

Créer un portail de service ITSM opérationnel sans ouvrir l'accès client par défaut à tout Internet.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Créer un espace de test : **Spaces > Create space > Service space > IT service management** (nom, clé).
   👉 Explication : sur un site de test, pas sur le tenant de production.

2. Ajouter un agent et un client de test : **Space settings > Access > Add people** (rôle **Agent**) et **Customers > Add customers**.
   👉 Explication : comptes de test uniquement.

3. Créer le request type : **Space settings > Request types > Create request type** (nom « Incident », groupe, champs). Créer la file : **Queues > Create queue** (filtre : demandes ouvertes).
   👉 Explication : la file affiche les demandes à traiter.

4. Tester : ouvrir le portail client (**Space settings > Portal > View portal**), soumettre une demande, répondre en tant qu'agent, vérifier la notification.
   👉 Explication : supprimer ensuite les données de test selon la politique du tenant.

## ⚡ 2. Production — Façon Simplifiée

1. Créer le service space sous le tenant approuvé et ajouter les agents via le groupe d'identité.
2. Dans **Space settings > Access > Customer permissions**, définir si le portail est réservé aux personnes invitées ou ouvert à des domaines approuvés.
3. Créer request types pour les catégories réellement supportées et limiter les champs requis aux informations nécessaires.
4. Configurer une file pour les demandes ouvertes et vérifier les notifications par e-mail.

## 🔒 3. Production — Façon Sécurisée

- Garder l'accès clients sur **Restricted** ou domaines explicitement approuvés, sauf décision métier documentée.
- Désactiver le partage entre clients s'il n'est pas nécessaire; vérifier l'effet du partage par organisation.
- Activer SSO/MFA pour les agents et gérer leur arrivée/départ par groupe.
- Ne pas demander mots de passe, clés API ou données sensibles dans les champs de demande.
- Tester séparément les rôles d'agent, client et administrateur avant ouverture du portail.

## ✅ Validation et retour arrière

- **Précontrôles** : site, licence, groupes, propriétaire, accès client et canaux autorisés.
- **Validation** : client de test crée une demande; agent la voit dans la bonne file et répond; aucun compte non autorisé n'accède au portail.
- **Retour arrière** : restreindre le canal client ou désactiver l'espace sans supprimer les tickets.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[JiraSM_Cloud_Portail_Acces_Client]]
- [Atlassian — Démarrage admin JSM](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/)
- [Atlassian — Permissions clients](https://support.atlassian.com/jira-service-management-cloud/docs/customer-permissions-for-your-service-project-and-jira-site/)