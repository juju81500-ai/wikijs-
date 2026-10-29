# Fiche_Simple_-_Cloud_AWS_Nettoyage_Retour_Arriere

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / nettoyage et retour arrière

---

## Problème précis à résoudre

Nettoyage et retour arrière dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Resource Groups → Tag Editor ; EC2 → Instances/Volumes/Snapshots ; S3 → Buckets ; vérifier chaque région avant suppression.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws resourcegroupstaggingapi get-resources --region REGION --tag-filters Key=Environment,Values=lab
aws ec2 describe-instances --region REGION
   ```
   👉 Explication : Inventorier par tags, identifier propriétaire/dépendances/sauvegardes, obtenir approbation puis nettoyer explicitement les ressources de lab. Restaurer les données depuis une sauvegarde testée.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Obtenir ticket et accord du propriétaire ; inventorier dépendances, sauvegardes, journaux, clés et ressources partagées avant toute suppression.

## 3. Production — Sécurité

Ne pas supprimer les journaux, sauvegardes, clés ou ressources partagées pour réduire les coûts. Ne pas lancer de suppression automatisée sans inventaire approuvé.

## Validation et retour arrière

- **Validation** : Inventaire après action et coûts résiduels contrôlés ; ressources conservées et données nécessaires intactes.
- **Retour arrière** : Avant suppression : restaurer depuis le point de sauvegarde validé dans un périmètre isolé, comparer avec l’inventaire et faire approuver la bascule. Certains effacements de données/clés sont irréversibles.

## Si le problème n'est pas résolu

- [AWS — documentation officielle](https://docs.aws.amazon.com/resourcegroupstagging/latest/APIReference/Welcome.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)