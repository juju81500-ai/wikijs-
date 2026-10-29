# Fiche_Simple_-_Cloud_GCP_Supervision_Alertes

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / supervision et alertes
- **Tags** : `gcp`, `supervision_alertes`, `securite`, `procedure`

---

## Problème précis à résoudre

Supervision et alertes dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Monitoring → Metrics Explorer ; Alerting → Policies → Create policy ; Notification channels.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud monitoring policies list --project=ID_PROJET
gcloud monitoring channels list --project=ID_PROJET
   ```
   👉 Explication : Créer une alerte fondée sur une métrique/SLO, définir fenêtre, sévérité et canal testé ; suivre également l’absence de données et erreurs de notification.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Définir propriétaire, sévérité, seuils fondés sur SLO, escalade, canal d’astreinte et comportement en absence de métriques.

## 3. Production — Sécurité

Limiter les droits sur les canaux de notification et de gestion ; ne pas transmettre de secret ou donnée personnelle dans une alerte.

## Validation et retour arrière

- **Validation** : L’alarme de test se déclenche et la notification est reçue par les opérateurs prévus.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/monitoring/docs)
- [Référence et bonnes pratiques](https://cloud.google.com/monitoring/alerts)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
