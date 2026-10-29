# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Dimensionner le NAS (capacité utile, RAM, niveau de redondance) avant d'acheter ou de créer la machine.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources d'une machine ou d'un NAS existant :
   ```bash
   nproc
   free -h
   lsblk -o NAME,MODEL,SIZE,ROTA,TYPE
   sudo zpool list
   ```
   👉 Explication : CPU, RAM, disques (ROTA=1 : disque tournant, 0 : SSD) et occupation des pools actuels.

2. Calculer la capacité utile selon la topologie :
   ```bash
   # MIRROR : 50 % ; RAIDZ1 : (N-1)/N ; RAIDZ2 : (N-2)/N ; RAIDZ3 : (N-3)/N
   # Exemple : 6 disques de 8 To en RAIDZ2 = (6-2) x 8 = 32 To bruts, environ 28 To utilisables (marge de 80 % conseillée)
   ```
   👉 Explication : ZFS ne doit pas dépasser environ 80 % d'occupation du pool.

3. Dimensionner la RAM : 8 Go minimum, puis environ 1 Go par To de stockage, de préférence ECC. Noter le besoin dans le dossier.
   👉 Explication : la RAM alimente le cache ARC de ZFS ; l'ECC évite la corruption silencieuse en mémoire.

4. Choisir les disques (CMR, pas SMR pour ZFS) et prévoir un disque de démarrage SSD distinct (16 Go minimum, 2 SSD en miroir en production).
   👉 Explication : le pool de données n'est jamais le disque système.

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge de croissance, valider la topologie et la tolérance aux pannes avec le propriétaire du service.

## 3. Production — Sécurité

Une redondance ZFS n'est pas une sauvegarde : prévoir une seconde copie sur un autre NAS ou dans le cloud.

## Validation et retour arrière

- **Validation** : Tableau de sizing (capacité, RAM, disques, topologie) signé et conservé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)