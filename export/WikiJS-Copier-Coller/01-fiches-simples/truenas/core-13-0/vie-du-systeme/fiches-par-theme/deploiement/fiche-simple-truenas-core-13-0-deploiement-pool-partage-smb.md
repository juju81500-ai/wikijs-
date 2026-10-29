# Fiche_Simple_-_TrueNAS_CORE_13.0_Deploiement_Pool_Partage_SMB.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en VM de laboratoire ou NAS existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / ZFS et SMB

---

## Problème précis à résoudre

Créer un pool redondant, un dataset et un partage SMB avec compte de service.

## 1. Hors-Production (Lab / Test / POC)

1. **Storage > Pools > Add** : créer un pool miroir ou RAIDZ avec uniquement les disques prévus.
   👉 Explication : la création détruit le contenu des disques sélectionnés.

2. Créer un dataset par usage : **Storage > Pools > ⋮ > Add Dataset**.
   👉 Explication : on ne partage jamais la racine du pool.

3. **Accounts > Users > Add** : créer un utilisateur de service et un groupe.
   👉 Explication : `root` n'est pas utilisé pour les partages.

4. **Sharing > Windows Shares (SMB) > Add** : choisir le chemin du dataset, activer le service SMB, tester depuis un client de test.
   👉 Explication : ACL et intégration Active Directory se traitent dans une procédure distincte.

5. Contrôler dans le Shell le pool et les datasets (remplacer `tank` par le nom de votre pool) :
   ```sh
   zpool status tank
   zfs list -r tank
   ```
   👉 Explication : affiche l'état `ONLINE` et les datasets créés.

## 2. Production — Contrôles

Faire valider layout, redondance et plan de remplacement par le responsable stockage.

## 3. Production — Sécurité

- Un utilisateur non autorisé doit être refusé sur le partage.
- Ne pas utiliser `root` pour accéder aux partages.

## Validation et retour arrière

- **Validation** : Pool `ONLINE`, partage accessible avec le compte de service.
- **Retour arrière** : Supprimer le partage de test; la destruction d'un pool est irréversible sans sauvegarde externe.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 4. Créer un pool et un partage SMB](/02-fiches-completes/truenas/core-13-0/installation-deploiement/89-deploiement-truenas-core-13-0#4-creer-un-pool-et-un-partage-smb)