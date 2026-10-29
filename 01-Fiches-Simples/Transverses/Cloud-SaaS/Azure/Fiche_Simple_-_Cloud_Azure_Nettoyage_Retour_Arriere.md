# Fiche_Simple_-_Cloud_Azure_Nettoyage_Retour_Arriere

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Azure CLI (az ; version publiée à vérifier)
- **Catégorie** : cloud public / nettoyage et retour arrière
- **Tags** : `azure`, `nettoyage_retour_arriere`, `securite`, `procedure`

---

## Problème précis à résoudre

Nettoyage et retour arrière dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Resource groups → sélectionner groupe → Resources/Deployments ; vérifier Disks, Snapshots, Storage et Network avant suppression.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Azure CLI (az ; version publiée à vérifier)) :
   ```bash
   az resource list --resource-group GROUPE --output table
az backup item list --resource-group GROUPE --vault-name NOM_VAULT --backup-management-type AzureIaasVM --workload-type VM
   ```
   👉 Explication : Inventorier ressources, propriétaires, dépendances, coûts et sauvegardes ; obtenir approbation avant suppression. Restaurer les données depuis un point vérifié, jamais depuis une hypothèse.
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

- [Microsoft Azure — documentation officielle](https://learn.microsoft.com/azure/azure-resource-manager/management/manage-resource-groups-portal)
- [Référence et bonnes pratiques](https://learn.microsoft.com/azure/backup/backup-azure-arm-restore-vms)
- [Fiche d’entrée Microsoft Azure](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Microsoft-Azure.md)
