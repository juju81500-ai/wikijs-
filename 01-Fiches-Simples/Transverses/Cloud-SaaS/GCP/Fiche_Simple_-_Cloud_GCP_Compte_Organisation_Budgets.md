# Fiche_Simple_-_Cloud_GCP_Compte_Organisation_Budgets

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / compte, organisation sécurisée et budgets
- **Tags** : `gcp`, `compte_organisation_budgets`, `securite`, `procedure`

---

## Problème précis à résoudre

Compte, organisation sécurisée et budgets dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Google Cloud console → IAM & Admin → IAM ; Google Account → Security → 2-Step Verification ; Billing → Budgets & alerts → Create budget.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud auth list
gcloud config get-value project
gcloud billing budgets list --billing-account=BILLING_ACCOUNT_ID
   ```
   👉 Explication : Confirmer organisation/projet actifs, imposer la validation en deux étapes aux administrateurs, attribuer les rôles minimaux et configurer les alertes de budget. Les valeurs en majuscules sont à remplacer.
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

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/iam/docs/overview)
- [Référence et bonnes pratiques](https://cloud.google.com/billing/docs/how-to/budgets)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
