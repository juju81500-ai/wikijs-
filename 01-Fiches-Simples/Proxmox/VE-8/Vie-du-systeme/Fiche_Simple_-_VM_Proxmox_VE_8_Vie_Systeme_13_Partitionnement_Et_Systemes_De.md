# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir le système de fichiers de l'hôte et du stockage des VM.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : **Options** du disque cible : ext4 (simple, LVM-thin), ZFS (RAID1/10/Z1... pour redondance, snapshots), ou XFS/Btrfs. Choisir le disque de démarrage (idéalement 2 disques en miroir).
   👉 Explication : ZFS RAID1 sur 2 disques protège le système contre la panne d'un disque.

2. Après installation, contrôler la disposition :
   ```bash
   lsblk -f
   df -hT
   vgs
   lvs
   zpool status
   ```
   👉 Explication : montre LVM (`pve/data` = LVM-thin) ou le pool ZFS `rpool`.

3. Réserver un volume séparé pour les sauvegardes locales, hors des disques des VM.
   👉 Explication : évite qu'une sauvegarde remplisse le stockage des VM.

## 2. Production — Contrôles

Documenter le choix (ZFS miroir pour le système, NVMe pour les VM, etc.).

## 3. Production — Sécurité

Laisser de la marge libre (80 % maximum d'occupation pour ZFS et LVM-thin).

## Validation et retour arrière

- **Validation** : `zpool status` indique `ONLINE` ou `lvs` montre `data` sans alerte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
