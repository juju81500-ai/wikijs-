# Fiche_Simple_-_Cloud_Azure_Journalisation_Audit

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Azure CLI (az ; version publiée à vérifier)
- **Catégorie** : cloud public / journalisation et audit
- **Tags** : `azure`, `journalisation_audit`, `securite`, `procedure`

---

## Problème précis à résoudre

Journalisation et audit dans Microsoft Azure en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Monitor → Activity log ; Monitor → Diagnostic settings → Add diagnostic setting ; envoyer vers Log Analytics/Storage approuvé.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Azure CLI (az ; version publiée à vérifier)) :
   ```bash
   az monitor activity-log list --subscription ID_ABONNEMENT --max-events 20
az monitor diagnostic-settings list --resource ID_RESSOURCE
   ```
   👉 Explication : L’Activity Log trace les opérations du plan de contrôle ; créer les paramètres de diagnostic pour les journaux de ressources requis et définir destination/rétention.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Confirmer couverture de toutes les régions/projets/abonnements, événements, destination centralisée, intégrité, rétention et alertes en cas d’arrêt/échec.

## 3. Production — Sécurité

Restreindre accès/suppression, bloquer l’accès public, chiffrer les journaux et préserver l’intégrité. Contrôler les données sensibles qui pourraient apparaître dans les événements.

## Validation et retour arrière

- **Validation** : Un événement de test est retrouvé dans la source et la destination centrale ; les alertes de livraison sont contrôlées.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Microsoft Azure — documentation officielle](https://learn.microsoft.com/azure/azure-monitor/essentials/activity-log)
- [Référence et bonnes pratiques](https://learn.microsoft.com/azure/azure-monitor/platform/diagnostic-settings)
- [Fiche d’entrée Microsoft Azure](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Microsoft-Azure.md)
