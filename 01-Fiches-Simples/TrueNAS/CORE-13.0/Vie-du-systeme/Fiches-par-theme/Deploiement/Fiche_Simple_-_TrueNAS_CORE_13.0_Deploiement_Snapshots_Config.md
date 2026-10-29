# Fiche_Simple_-_TrueNAS_CORE_13.0_Deploiement_Snapshots_Config.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en VM de laboratoire ou NAS existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / sauvegarde
- **Tags** : `truenas-core`, `truenas`, `freebsd`, `zfs`, `smb`, `nas`

---

## Problème précis à résoudre

Protéger les données par snapshots et sauvegarder la configuration hors machine.

## 1. Hors-Production (Lab / Test / POC)

1. **Storage > Snapshots > Add** : créer un snapshot du dataset de test, puis une **tâche de snapshot périodique** avec rétention définie.
   👉 Explication : protège contre les suppressions accidentelles.

2. Équivalent Shell (remplacer pool et dataset d'exemple) :
   ```sh
   zfs snapshot tank/test@avant-essai
   zfs list -t snapshot
   ```
   👉 Explication : crée et liste un snapshot manuel.

3. Pour récupérer des données, utiliser **Clone to new dataset** puis partager le clone.
   👉 Explication : le rollback d'un dataset est destructif pour les données postérieures; à éviter en production.

4. **System > General > Save Config** après chaque changement; copier le fichier hors de la machine.
   👉 Explication : l'option « Export Password Secret Seed » rend le fichier sensible : le protéger comme un secret.

5. Sauvegarder séparément `/usr/local/etc/ssh/ssh_host_*` et `/root/.ssh`.
   👉 Explication : ils ne sont pas dans la base de configuration.

## 2. Production — Contrôles

Répliquer vers un autre système : les snapshots ne remplacent pas une sauvegarde hors machine.

## 3. Production — Sécurité

- Fichier de configuration et seed de mots de passe stockés hors NAS, accès restreint.

## Validation et retour arrière

- **Validation** : Un snapshot existe, un fichier supprimé est récupéré via clone, le `.db` est stocké hors NAS.
- **Retour arrière** : Supprimer le clone ou le snapshot de test; ne pas utiliser rollback en production.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 5. Snapshots et sauvegarde de configuration](../../../../../../02-Fiches-Completes/TrueNAS/CORE-13.0/Installation-Deploiement/89_Deploiement_TrueNAS_CORE_13.0.md#5-snapshots-et-sauvegarde-de-configuration)
