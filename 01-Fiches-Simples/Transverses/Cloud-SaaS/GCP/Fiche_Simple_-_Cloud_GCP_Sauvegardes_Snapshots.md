# Fiche_Simple_-_Cloud_GCP_Sauvegardes_Snapshots

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — Google Cloud CLI (gcloud ; version publiée à vérifier)
- **Catégorie** : cloud public / sauvegardes et snapshots
- **Tags** : `gcp`, `sauvegardes_snapshots`, `securite`, `procedure`

---

## Problème précis à résoudre

Sauvegardes et snapshots dans Google Cloud Platform en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : Compute Engine → Snapshots → Create snapshot ; Backup and DR → Backup plans → Create backup plan.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (Google Cloud CLI (gcloud ; version publiée à vérifier)) :
   ```bash
   gcloud compute disks snapshot ID_DISQUE --zone=ZONE --snapshot-names=NOM_SNAPSHOT
gcloud compute snapshots list --project=ID_PROJET
   ```
   👉 Explication : Définir RPO/RTO, rétention, chiffrement et plan de restauration ; tester la récupération sur une ressource isolée. Les snapshots disques seuls ne garantissent pas la cohérence applicative.
3. Console et CLI : comparer la configuration affichée avec l’état attendu, puis valider sur une ressource pilote non sensible.
   👉 Explication : les interfaces évoluent ; vérifier l’aide/version officielle et les quotas/licences avant généralisation.

## 2. Production — Contrôles

Définir RPO/RTO, cohérence applicative, périmètre, rétention, région secondaire et responsable. Contrôler les jobs échoués et le coût de stockage.

## 3. Production — Sécurité

Restreindre suppression/altération, chiffrer les sauvegardes et protéger leurs clés. Appliquer séparation des tâches et rétention légale.

## Validation et retour arrière

- **Validation** : Restauration isolée testée, intégrité confirmée et temps mesuré comparé au RTO.
- **Retour arrière** : Revenir à la dernière configuration approuvée ; préserver les sauvegardes et journaux. Ne supprimer la ressource de test qu’après validation des dépendances et du propriétaire.

## Si le problème n'est pas résolu

- [Google Cloud Platform — documentation officielle](https://cloud.google.com/compute/docs/disks/snapshot)
- [Référence et bonnes pratiques](https://cloud.google.com/backup-disaster-recovery/docs/overview)
- [Fiche d’entrée Google Cloud Platform](../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md)
