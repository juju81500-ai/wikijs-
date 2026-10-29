# 📄 Fiche_Simple_-_TrueNAS_SCALE_25.10_Sauvegarde_Snapshots_Repl.md

- **Environnement** : TrueNAS SCALE 25.10 (Goldeye), NAS source et second NAS ou pool de réplication
- **OS / Version** : TrueNAS SCALE 25.10 Goldeye (base Debian, système de fichiers ZFS)
- **Catégorie** : Sauvegarde / Snapshots et réplication
- **Tags** : `truenas`, `scale2510`, `zfs`, `snapshot`, `replication`, `backup`

---

## 🎯 Problème précis à résoudre
Planifier des snapshots ZFS automatiques, puis répliquer ces snapshots vers un second emplacement, pour qu'une copie des données survive à la perte ou à la compromission du NAS source.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer un dataset de test :
   `zfs create <pool>/<dataset_test>`
   👉 Explication : Isole les essais sur un dataset dédié, sans toucher aux partages existants.
2. Créer un snapshot manuel :
   `zfs snapshot <pool>/<dataset_test>@test-manuel-1`
   👉 Explication : Fige l'état du dataset à un instant donné.
3. Planifier des snapshots automatiques :
   `Data Protection > Periodic Snapshot Tasks > Add` : Dataset = `<pool>/<dataset_test>`, Recursive = coché, Schedule = `quotidien 02:00`, Lifetime = `14 days`, Naming Schema = `auto-%Y-%m-%d_%H-%M` (libellés à vérifier sur la version déployée)
   👉 Explication : Conserve 14 jours de points de retour sans intervention.
4. Répliquer le snapshot vers un second pool ou un second NAS de lab :
   `zfs send <pool>/<dataset_test>@test-manuel-1 | ssh <utilisateur>@<hote_cible> zfs receive -u <pool_cible>/<dataset_test>`
   👉 Explication : Envoie le contenu du snapshot ; l'option -u évite de monter automatiquement le dataset reçu.
5. Vérifier la présence du snapshot sur la cible :
   `ssh <utilisateur>@<hote_cible> zfs list -t snapshot -r <pool_cible>/<dataset_test>`
   👉 Explication : Confirme que la réplication a réussi.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer une tâche de réplication automatique :
   `Data Protection > Replication Tasks > Add` : Source = `<pool>/<dataset>`, Destination = `<hote_cible>` (connexion SSH enregistrée), Schedule = `quotidien`, Retention = `identique à la source` (libellés à vérifier sur la version déployée)
   👉 Explication : Les snapshots sont envoyés vers le second emplacement selon le planning, sans commande manuelle.
2. Vérifier l'état de la dernière réplication :
   `Data Protection > Replication Tasks` : état et date de la dernière exécution
   👉 Explication : Une réplication en échec laisse la cible en retard sans alerte visible si elle n'est pas surveillée.
3. Contrôler la liste des snapshots source :
   `zfs list -t snapshot -o name,creation -s creation <pool>/<dataset> | tail -n 20`
   👉 Explication : Confirme que les snapshots automatiques sont créés chaque jour.

---

## 🔒 3. Production — Façon Sécurisée
1. Protéger les snapshots critiques contre une suppression accidentelle :
   `zfs hold <tag_protection> <pool>/<dataset>@<nom_snapshot>`
   👉 Explication : Un snapshot tenu ne peut pas être détruit tant que le tag n'est pas retiré (`zfs release <tag_protection> <pool>/<dataset>@<nom_snapshot>`).
2. Répliquer en incrémental pour limiter le trafic :
   `zfs send -i <pool>/<dataset>@<ancien_snapshot> <pool>/<dataset>@<nouveau_snapshot> | ssh <utilisateur>@<hote_cible> zfs receive -u <pool_cible>/<dataset>`
   👉 Explication : N'envoie que les différences entre deux snapshots ; l'ancien snapshot doit déjà exister sur la cible.
3. Authentifier la réplication par clé dédiée :
   `Credentials > Backup Credentials > SSH Connections` : clé dédiée à la réplication (libellé à vérifier sur la version déployée)
   👉 Explication : Le compte de réplication n'a que le droit de recevoir des snapshots.
4. Vérifier la copie hors NAS :
   `ssh <utilisateur>@<hote_cible> zfs list -t snapshot -r <pool_cible>/<dataset>` et comparaison avec la source
   👉 Explication : Une copie n'existe que si la cible la contient réellement.
