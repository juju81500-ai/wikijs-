---
title: "Fiche Simple - Cloud AWS Sauvegardes Snapshots"
description: "Sauvegardes et snapshots dans AWS en limitant les risques de sécurité, de disponibilité et de coût."
published: true
date: 2026-10-29T21:00:44Z
tags: ["aws", "sauvegardes_snapshots", "securite", "procedure"]
editor: markdown
dateCreated: 2026-10-29T21:00:44Z
dateModified: 2026-10-29T21:00:44Z
---

# Fiche_Simple_-_Cloud_AWS_Sauvegardes_Snapshots

- **Environnement** : tenant/compte de laboratoire contrôlé ; accès d’administration autorisé
- **OS / Version** : Cloud/SaaS — AWS CLI v2
- **Catégorie** : cloud public / sauvegardes et snapshots
- **Tags** : `aws`, `sauvegardes_snapshots`, `securite`, `procedure`

---

## Problème précis à résoudre

Sauvegardes et snapshots dans AWS en limitant les risques de sécurité, de disponibilité et de coût.

Les valeurs écrites en MAJUSCULES sont des placeholders à remplacer par les valeurs validées de l’environnement. Ne coller aucun secret réel dans les commandes, les fiches ou l’historique shell.

## 1. Hors-Production (Lab / Test / POC)

1. Console : AWS Backup → Backup vaults → Create backup vault ; Backup plans → Create backup plan ; Protected resources → Restore.
   👉 Explication : vérifier le compte/projet/abonnement et la région sélectionnés avant toute modification.
2. CLI officielle (AWS CLI v2) :
   ```bash
   aws backup list-backup-vaults --region REGION
aws ec2 create-snapshot --volume-id ID_VOLUME --description "Snapshot de test"
   ```
   👉 Explication : Définir fréquence, RPO/RTO, rétention, chiffrement et ressource de test ; restaurer dans un périmètre isolé. Un snapshot seul ne remplace pas un test de restauration.
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

- [AWS — documentation officielle](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)
- [Référence et bonnes pratiques](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshots.html)
- [Fiche d’entrée AWS](/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws)