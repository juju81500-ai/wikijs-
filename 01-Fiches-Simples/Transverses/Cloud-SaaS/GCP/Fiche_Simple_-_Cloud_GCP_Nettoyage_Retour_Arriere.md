# Fiche_Simple_-_Cloud_GCP_Nettoyage_Retour_Arriere

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / nettoyage et retour arrière
- **Tags** : `gcp`, `nettoyage_retour_arriere`, `securite`, `procedure`

---

## Problème précis à résoudre

Nettoyage et retour arrière dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Compute Engine → VM instances/Disks/Snapshots ; VPC network ; Cloud Storage ; vérifier le projet sélectionné.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud compute instances list --project=ID_PROJET
gcloud storage buckets list --project=ID_PROJET
   ```
   👉 Explication : Inventorier ressources et dépendances par projet/labels ; faire valider propriétaire et sauvegardes avant suppression. Tester la restauration dans un projet ou réseau isolé.
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

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/resource-manager/docs/creating-managing-projects)
- [Référence et bonnes pratiques](https://cloud.google.com/compute/docs/disks/restore-snapshot)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
