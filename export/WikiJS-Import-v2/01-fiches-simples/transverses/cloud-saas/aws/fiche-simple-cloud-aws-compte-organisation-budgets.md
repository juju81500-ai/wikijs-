---
title: "Fiche Simple - Cloud AWS Compte Organisation Budgets"
description: "Compte, organisation sécurisée et budgets dans AWS en limitant les risques de sécurité, de disponibilité et de coût."
published: true
date: 2026-10-29T21:00:44Z
tags: ["aws", "compte_organisation_budgets", "securite", "procedure"]
editor: markdown
dateCreated: 2026-10-29T21:00:44Z
dateModified: 2026-10-29T21:00:44Z
---

# Fiche_Simple_-_Cloud_AWS_Compte_Organisation_Budgets

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / compte, organisation sécurisée et budgets
- **Tags** : `aws`, `compte_organisation_budgets`, `securite`, `procedure`

---

## Problème précis à résoudre

Compte, organisation sécurisée et budgets dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : IAM Identity Center → Settings, Users/Groups, Permission sets ; IAM → Security credentials → MFA ; Billing and Cost Management → Budgets → Create budget.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws sts get-caller-identity
aws iam list-roles --max-items 20
aws budgets describe-budgets --account-id ID_COMPTE --region us-east-1
   ```
   👉 Explication : Utiliser une identité fédérée/SSO, activer MFA sur les accès privilégiés, attribuer le moindre privilège et créer une alerte de budget. Remplacer les valeurs en majuscules par celles du tenant.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Valider le tenant/compte, le périmètre d’abonnement/projet, les rôles, les accès d’urgence, les destinataires et la devise du budget. Tester l’accès nominatif et revoir les droits périodiquement.

## 3. Production — Sécurité

Ne pas utiliser l’identité root/propriétaire pour les tâches courantes. MFA résistante à l’hameçonnage pour les rôles privilégiés ; secrets dans un coffre ; séparation des tâches et deux accès d’urgence contrôlés.

## Validation et retour arrière

- **Validation** : Identité, MFA, rôle et notification budget testés ; compte/projet actif confirmé par la commande CLI de contrôle.
- **Retour arrière** : Retirer l’affectation pilote ou restaurer le jeu de permissions approuvé ; ne pas désactiver MFA pour contourner un incident. Corriger le budget sans supprimer ses historiques.

## Si le problème n'est pas résolu

- [AWS — documentation officielle](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)