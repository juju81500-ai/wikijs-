# Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Pool_Datasets.md

- **Environnement** : NAS autonome pilote (matériel x86-64 ou VM de laboratoire)
- **OS / Version** : TrueNAS SCALE 25.10 Community Edition
- **Catégorie** : stockage NAS / ZFS

---

## Problème précis à résoudre

Créer un pool miroir pilote et des datasets par usage.

## 1. Hors-Production (Lab / Test / POC)

1. **Storage > Create Pool** : choisir les disques attendus et un layout miroir simple pour un pilote.
   👉 Explication : le layout est difficile à modifier après création.

2. Créer des datasets enfants : **Datasets > Add Dataset**, un par usage ou équipe.
   👉 Explication : on ne partage jamais le dataset racine.

3. Examiner preset, sensibilité à la casse, ACL et chiffrement avant d'y mettre des données.
   👉 Explication : ces choix sont durables.

4. Vérifier depuis le Shell (remplacer `tank` par le nom du pool) :
   ```bash
   zpool status tank
   zfs list -r tank
   ```
   👉 Explication : pool `ONLINE` et datasets présents.

## 2. Production — Contrôles

En production, faire valider vdevs, redondance, spare et plan de remplacement par le responsable stockage.

## 3. Production — Sécurité

- Datasets chiffrés : protéger les clés.

## Validation et retour arrière

- **Validation** : Pool `ONLINE` et datasets créés.
- **Retour arrière** : Avant mise en service seulement : supprimer le dataset de test; la destruction du pool efface les données.

## Si le problème n'est pas résolu

- [TrueNAS SCALE 25.10 — installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/)
- [TrueNAS SCALE 25.10 — guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/)
- [Guide complet — 3. Créer le pool et les datasets](/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10#3-creer-le-pool-et-les-datasets)