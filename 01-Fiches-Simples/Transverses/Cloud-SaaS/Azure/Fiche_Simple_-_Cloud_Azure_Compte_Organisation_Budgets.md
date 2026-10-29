# Fiche_Simple_-_Cloud_Azure_Compte_Organisation_Budgets

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Azure CLI (az ; version publiée à vérifier)
- **Catégorie** : cloud public / compte, organisation sécurisée et budgets
- **Tags** : `azure`, `compte_organisation_budgets`, `securite`, `procedure`

---

## Problème précis à résoudre

Compte, organisation sécurisée et budgets dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Microsoft Entra admin center → Protection → Conditional Access / Authentication methods ; Azure portal → Subscriptions → Access control (IAM) ; Cost Management + Billing → Budgets.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Azure CLI (az ; version publiée à vérifier)) :
   ```bash
   az login
az account show
az consumption budget list --subscription ID_ABONNEMENT
   ```
   👉 Explication : Imposer MFA aux administrateurs via une stratégie pilotée, affecter des rôles RBAC minimaux et fixer un budget d’abonnement. Utiliser des identités managées pour l’automatisation, jamais des secrets intégrés aux scripts.
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

- [Microsoft Azure — documentation officielle](https://learn.microsoft.com/entra/identity/authentication/concept-mfa-howitworks)
- [Référence et bonnes pratiques](https://learn.microsoft.com/azure/cost-management-billing/costs/tutorial-acm-create-budgets)
- [Fiche d’entrée Microsoft Azure](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Microsoft-Azure.md)
