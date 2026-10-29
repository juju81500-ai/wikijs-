# Fiche_Simple_-_Cloud_GCP_Journalisation_Audit

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / journalisation et audit
- **Tags** : `gcp`, `journalisation_audit`, `securite`, `procedure`

---

## Problème précis à résoudre

Journalisation et audit dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Logging → Logs Explorer ; IAM & Admin → Audit Logs ; Logging → Log Router → Create sink.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud logging sinks list --project=ID_PROJET
gcloud logging read 'logName:"cloudaudit.googleapis.com%2Factivity"' --project=ID_PROJET --limit=20
   ```
   👉 Explication : Vérifier les journaux d’audit Admin Activity et activer les catégories Data Access nécessaires ; router vers une destination protégée avec rétention contrôlée.
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

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/logging/docs/audit)
- [Référence et bonnes pratiques](https://cloud.google.com/logging/docs/routing/overview)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
