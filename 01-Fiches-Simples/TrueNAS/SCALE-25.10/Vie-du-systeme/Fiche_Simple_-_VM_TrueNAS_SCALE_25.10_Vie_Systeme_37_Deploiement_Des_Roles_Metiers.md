# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Créer pool et partages selon l'usage.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le pool : GUI Stockage > Créer un pool (nom, disposition, disques).
   ```bash
   sudo zpool create -o ashift=12 POOL raidz2 sdb sdc sdd sde sdf sdg
   sudo zpool status POOL
   ```
   👉 Explication : RAIDZ2 sur six disques ; sdb à sdg sont les disques de données (en pratique, créer le pool par la GUI pour garder la gestion TrueNAS).

2. Créer un jeu de données : GUI Jeux de données > Ajouter un jeu de données.
   ```bash
   sudo zfs create POOL/DONNEES
   sudo zfs create -V 100G POOL/VOL_ISCSI
   ```
   👉 Explication : dataset de fichiers et zvol (volume bloc) pour iSCSI.

3. Créer le partage : GUI Partages > Windows (SMB) > Ajouter ; NFS ; iSCSI > Assistant.
   ```bash
   sudo midclt call sharing.smb.create '{"path": "/mnt/POOL/DONNEES", "name": "DONNEES"}'
   sudo midclt call service.start cifs
   ```
   👉 Explication : publie le dataset en SMB et démarre le service.

## 2. Production — Contrôles

Un dataset par usage, avec quotas et droits propres.

## 3. Production — Sécurité

Ne pas partager la racine du pool.

## Validation et retour arrière

- **Validation** : Le partage est accessible par un client de test.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
