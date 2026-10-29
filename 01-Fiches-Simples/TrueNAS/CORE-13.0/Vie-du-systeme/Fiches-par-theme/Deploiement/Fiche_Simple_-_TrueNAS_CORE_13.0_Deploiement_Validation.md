# Fiche_Simple_-_TrueNAS_CORE_13.0_Deploiement_Validation.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en VM de laboratoire ou NAS existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / validation
- **Tags** : `truenas-core`, `truenas`, `freebsd`, `zfs`, `smb`, `nas`

---

## Problème précis à résoudre

Contrôler que pool, partage, snapshots, configuration et alertes sont opérationnels.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état du pool dans **Storage > Pools** et dans le Shell :
   ```sh
   zpool status
   ```
   👉 Explication : aucune erreur ne doit apparaître.

2. Tester l'accès SMB avec le compte de service puis avec un utilisateur non autorisé.
   👉 Explication : le second doit être refusé.

3. Vérifier l'existence du snapshot et la récupération d'un fichier via un clone.
   👉 Explication : prouve que la restauration fonctionne.

4. **System > General > Save Config**, stocker le `.db` hors du NAS.
   👉 Explication : la configuration est récupérable.

5. Configurer l'e-mail d'alerte et envoyer un test.
   👉 Explication : garantit que les alertes arrivent.

## 2. Production — Contrôles

Consigner les résultats de la recette.

## 3. Production — Sécurité

- Contenu du fichier de configuration non exposé.

## Validation et retour arrière

- **Validation** : Tous les contrôles ci-dessus passent.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 6. Validation](../../../../../../02-Fiches-Completes/TrueNAS/CORE-13.0/Installation-Deploiement/89_Deploiement_TrueNAS_CORE_13.0.md#6-validation)
