# Fiche_Simple_-_VM_Ubuntu_Ceph_Ajouter_OSD.md

- **Environnement** : Cluster Ceph de laboratoire à trois nœuds (ceph01, ceph02, ceph03) géré par cephadm
- **OS / Version** : Ubuntu Server 22.04 LTS; Ceph Tentacle 20.2.4
- **Catégorie** : stockage / cluster Ceph
- **Tags** : `ubuntu2204`, `ceph`, `tentacle`, `cephadm`

---

## Problème précis à résoudre

Créer un OSD par nœud sur un disque de données explicitement choisi, sans effacer un mauvais disque.

## 1. Hors-Production (Lab / Test / POC)

1. Sur chaque hôte, vérifier identité, numéro de série et absence de données :
   ```bash
   lsblk -o NAME,SIZE,MODEL,SERIAL,FSTYPE,MOUNTPOINTS
   ```
   👉 Explication : un disque éligible doit être vide, non monté, sans partition, système de fichiers ni LVM.

2. Lister les périphériques vus par Ceph :
   ```bash
   sudo ceph orch device ls --wide
   ```
   👉 Explication : confirme quels disques Ceph juge disponibles.

3. Ne pas utiliser `--all-available-devices`.
   👉 Explication : cette spécification est persistante et consommerait automatiquement tout futur disque libre.

4. Créer `/root/osd-lab.yaml` avec une spécification par hôte (remplacer ID_DISQUE_CEPH01/02/03 par les chemins `/dev/disk/by-id/` réels de chaque nœud) :
   ```yaml
   service_type: osd
   service_id: lab-ceph01
   placement:
     hosts: [ceph01]
   spec:
     data_devices:
       paths:
         - /dev/disk/by-id/ID_DISQUE_CEPH01
   ---
   service_type: osd
   service_id: lab-ceph02
   placement:
     hosts: [ceph02]
   spec:
     data_devices:
       paths:
         - /dev/disk/by-id/ID_DISQUE_CEPH02
   ---
   service_type: osd
   service_id: lab-ceph03
   placement:
     hosts: [ceph03]
   spec:
     data_devices:
       paths:
         - /dev/disk/by-id/ID_DISQUE_CEPH03
   ```
   👉 Explication : un `service_id` unique et un seul hôte par spécification; un chemin n'est valable que sur l'hôte où le disque a été identifié.

5. Prévisualiser :
   ```bash
   sudo ceph orch apply -i /root/osd-lab.yaml --dry-run
   ```
   👉 Explication : comparer chaque disque prévu à l'inventaire; ne continuer que si l'aperçu correspond exactement.

6. Appliquer, puis contrôler :
   ```bash
   sudo ceph orch apply -i /root/osd-lab.yaml
   sudo ceph orch ps --daemon-type osd
   sudo ceph osd tree
   ```
   👉 Explication : la création d'OSD efface les métadonnées et le contenu du disque ciblé; attendre la fin de la récupération avant tout autre changement.

## 2. Production — Contrôles

Faire valider physiquement chaque disque (série, by-id) par un second administrateur; jamais sur un disque système, monté, partagé avec une VM ou contenant des données.

## 3. Production — Sécurité

- L'application efface le disque ciblé: aucun retour possible sur ses données.
- Ne pas utiliser de spécification globale persistante.

## Validation et retour arrière

- **Validation** : 3 OSD `up` et `in` dans `sudo ceph osd tree`.
- **Retour arrière** : avant application: abandonner. Après: retirer un OSD avec `sudo ceph orch osd rm ID_OSD` (ID réel de `ceph osd tree`), suivre `ceph orch osd rm status`; ne pas utiliser `--force` ni `--zap` en dépannage courant.

## Si le problème n'est pas résolu

- [Ceph — service OSD](https://docs.ceph.com/en/tentacle/cephadm/services/osd/)
- [Ceph Tentacle — cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/)
- [Guide complet](../../../../../02-Fiches-Completes/Ubuntu/22.04/Installation-Deploiement/67_Deploiement_Ceph_Tentacle_20_2_4_Ubuntu_22_04.md#5-ajouter-des-osd-sans-consommer-le-mauvais-disque)
