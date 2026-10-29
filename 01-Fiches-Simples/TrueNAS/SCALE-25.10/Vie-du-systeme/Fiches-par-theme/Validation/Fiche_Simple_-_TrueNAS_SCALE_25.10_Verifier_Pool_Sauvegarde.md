# 📄 Fiche_Simple_-_TrueNAS_SCALE_25.10_Verifier_Pool_Sauvegarde.md

- **Environnement** : TrueNAS SCALE 25.10, NAS de lab ou de production
- **OS / Version** : TrueNAS SCALE 25.10 Goldeye
- **Catégorie** : Stockage / exploitation
- **Tags** : `truenas`, `scale2510`, `zfs`, `pool`, `snapshot`, `restore`

---

## 🎯 Problème précis à résoudre

Contrôler la santé d'un pool et prouver qu'un fichier de test peut être restauré.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Contrôler le pool : **Storage > Pools** (état `Online`), **Storage > Disks**, alertes (cloche en haut), dernier scrub dans **Data Protection > Scrub Tasks**; en shell :
   ```bash
   sudo zpool status
   sudo zpool list
   ```
   👉 Explication : aucune erreur, scrub récent, espace libre suffisant.

2. Créer un snapshot d'un dataset pilote : **Datasets > dataset > Create Snapshot**, puis supprimer un fichier de test non sensible :
   ```bash
   sudo zfs list -t snapshot -r POOL/DATASET_PILOTE
   rm /mnt/POOL/DATASET_PILOTE/fichier-test.txt
   ```
   👉 Explication : remplacer pool et dataset.

3. Restaurer vers un répertoire temporaire :
   ```bash
   mkdir -p /tmp/restore-test
   cp -a /mnt/POOL/DATASET_PILOTE/.zfs/snapshot/NOM_SNAPSHOT/fichier-test.txt /tmp/restore-test/
   ```
   👉 Explication : ou **Snapshots > Clone to New Dataset**; comparer contenu et permissions (`ls -l`, `sha256sum`).

4. Exporter la configuration : **System > General > Manage Configuration > Download File** (cocher **Export Password Secret Seed** si besoin).
   👉 Explication : ranger la copie hors du NAS, chiffrée.


## ⚡ 2. Production — Façon Simplifiée

1. Vérifier périodiquement : **Data Protection > Periodic Snapshot Tasks / Replication Tasks / Cloud Sync Tasks** (dernier statut), espace de la cible, clés de chiffrement (**Datasets > Encryption Options > Export Key**) :
   ```bash
   sudo zfs list -t snapshot | tail -5
   ```
   👉 Explication : un snapshot local ne protège pas contre la perte ou la compromission du NAS.


## 🔒 3. Production — Façon Sécurisée

- Garder identifiants et clés de chiffrement séparés du NAS et limiter les administrateurs.
- Ne pas supprimer, importer ou recréer un pool pour corriger une alerte sans procédure de reprise et validation des disques.
- Tester une restauration sur un dataset séparé avant d'écraser des données existantes.

## ✅ Validation et retour arrière

- **Validation** : pool sain, tâche terminée, fichier restauré lisible et ACL attendue.
- **Retour arrière** : conserver le snapshot source et supprimer seulement le clone/répertoire de test après contrôle.

## 🔗 Si le problème n'est pas résolu

- [TrueNAS — Sauvegarde et restauration](https://www.truenas.com/docs/scale/25.10/gettingstarted/configure/setupbackupscale/)
- [TrueNAS — Configuration système](https://www.truenas.com/docs/scale/25.10/scaletutorials/systemsettings/advanced/managesysconfig/)