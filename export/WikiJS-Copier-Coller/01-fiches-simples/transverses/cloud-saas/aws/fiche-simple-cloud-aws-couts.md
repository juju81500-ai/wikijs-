# Fiche_Simple_-_Cloud_AWS_Couts

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / maîtrise des coûts

---

## Problème précis à résoudre

Maîtrise des coûts dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Billing and Cost Management → Cost Explorer ; Cost allocation tags ; Budgets ; Cost Anomaly Detection.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws budgets describe-budgets --account-id ID_COMPTE --region us-east-1
aws ce get-cost-and-usage --time-period Start=DATE_DEBUT,End=DATE_FIN --granularity MONTHLY --metrics UnblendedCost
   ```
   👉 Explication : Ventiler les coûts par compte/service/région/tags ; activer les tags avant déploiement et configurer budgets et détection d’anomalies. Une alerte budget ne bloque pas automatiquement les ressources.
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

- [AWS — documentation officielle](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)