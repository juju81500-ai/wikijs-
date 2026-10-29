# Fiche_Simple_-_Cloud_AWS_Supervision_Alertes

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / supervision et alertes
- **Tags** : `aws`, `supervision_alertes`, `securite`, `procedure`

---

## Problème précis à résoudre

Supervision et alertes dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : CloudWatch → Metrics → All metrics ; Alarms → Create alarm ; SNS → Topics → Subscriptions.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws cloudwatch list-metrics --namespace AWS/EC2 --region REGION
aws cloudwatch describe-alarms --region REGION
   ```
   👉 Explication : Choisir une métrique utile, définir seuil/période/propriétaire et tester la notification SNS ; superviser aussi les logs et erreurs de livraison.
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

- [AWS — documentation officielle](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [Fiche d’entrée AWS](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_AWS.md)
