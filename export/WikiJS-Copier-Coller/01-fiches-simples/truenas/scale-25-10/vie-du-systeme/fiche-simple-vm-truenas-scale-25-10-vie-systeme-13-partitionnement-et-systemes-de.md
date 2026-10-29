# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir les disques de démarrage lors de l'installation : le reste est géré par ZFS.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : Install/Upgrade, cocher un (ou deux pour un miroir) disque de démarrage SSD.
   👉 Explication : l'installateur crée seul le pool `boot-pool` ; ne pas choisir de disque de données.

2. Après installation, vérifier le pool de démarrage :
   ```bash
   sudo zpool status boot-pool
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```
   👉 Explication : ONLINE, sans erreur. GUI : Système > Environnements d'amorçage.

3. Ne pas créer de partitions à la main sur le système.
   👉 Explication : TrueNAS gère le système en lecture seule ; toute modification passe par la GUI.

## 2. Production — Contrôles

Utiliser deux SSD en miroir pour le pool de démarrage.

## 3. Production — Sécurité

Ne jamais stocker de données sur le pool de démarrage.

## Validation et retour arrière

- **Validation** : `boot-pool` ONLINE.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)