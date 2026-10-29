# Fiche_Simple_-_Cloud_AWS_Journalisation_Audit

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / journalisation et audit

---

## Problème précis à résoudre

Journalisation et audit dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : CloudTrail → Trails → Create trail ; activer multi-région/organisation et choisir une destination protégée ; AWS Config → Settings.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws cloudtrail describe-trails --include-shadow-trails
aws cloudtrail get-trail-status --name NOM_TRAIL
   ```
   👉 Explication : Centraliser les événements de gestion et, selon besoin, les événements de données ; contrôler livraison, rétention, intégrité, couverture des comptes/régions.
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

- [AWS — documentation officielle](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)