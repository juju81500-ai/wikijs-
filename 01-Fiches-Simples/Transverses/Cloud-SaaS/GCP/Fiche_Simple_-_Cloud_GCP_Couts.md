# Fiche_Simple_-_Cloud_GCP_Couts

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / maîtrise des coûts
- **Tags** : `gcp`, `couts`, `securite`, `procedure`

---

## Problème précis à résoudre

Maîtrise des coûts dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Billing → Reports ; Cost table ; Budgets & alerts ; Billing export.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud billing budgets list --billing-account=BILLING_ACCOUNT_ID
gcloud billing projects describe ID_PROJET
   ```
   👉 Explication : Ventiler par projet/service/labels, activer exports et budgets, vérifier les destinataires. Un budget émet des alertes mais n’arrête pas automatiquement les services.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Réconcilier coûts prévus/réels, frais de transfert, stockage, licences et ressources partagées. Attribuer une responsabilité et analyser les dérives avant d’agir.

## 3. Production — Sécurité

Restreindre les données de facturation et ne pas automatiser arrêt/suppression à partir d’une seule alerte de coût sans approbation du service.

## Validation et retour arrière

- **Validation** : Ventilation par tags/dimensions, seuil budget, destinataires et responsabilité financière vérifiés.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/billing/docs/how-to/reports)
- [Référence et bonnes pratiques](https://cloud.google.com/billing/docs/how-to/budgets)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
