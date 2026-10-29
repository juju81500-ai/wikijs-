# Fiche_Simple_-_TrueNAS_SCALE_25.10_Deploiement_Sauvegarder_Recuperer.md

- **Environnement** : NAS autonome pilote (matériel x86-64 ou VM de laboratoire)
- **OS / Version** : TrueNAS SCALE 25.10 Community Edition
- **Catégorie** : stockage NAS / sauvegarde
- **Tags** : `truenas`, `scale2510`, `zfs`, `nas`, `smb`, `sauvegarde`

---

## Problème précis à résoudre

Exporter la configuration et prévoir une copie indépendante.

## 1. Hors-Production (Lab / Test / POC)

1. **System > General > Manage Configuration > Download File** : exporter la configuration (avec **Export Password Secret Seed** si nécessaire).
   👉 Explication : le fichier doit être protégé physiquement comme un secret.

2. Conserver les clés des jeux de données chiffrés et un debug initial.
   👉 Explication : indispensables à la restauration.

3. Configurer snapshots et réplication vers un autre TrueNAS, ou Cloud Sync/TrueCloud, selon coûts et confidentialité.
   👉 Explication : les snapshots seuls ne remplacent pas une copie indépendante.

4. Lister les snapshots depuis le Shell :
   ```bash
   zfs list -t snapshot
   ```
   👉 Explication : vérifie que les snapshots attendus existent.

5. Tester une restauration de fichier et une réimportation de configuration sur un appareil de laboratoire séparé.
   👉 Explication : une sauvegarde non testée n'est pas fiable.

## 2. Production — Contrôles

Définir RPO/RTO et rétention.

## 3. Production — Sécurité

- Fichier de configuration et clés stockés hors NAS, accès restreint.

## Validation et retour arrière

- **Validation** : Un restore de fichier et de configuration réussit en laboratoire.
- **Retour arrière** : Réimporter la configuration exportée sur l'appareil de laboratoire.

## Si le problème n'est pas résolu

- [TrueNAS SCALE 25.10 — installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/)
- [TrueNAS SCALE 25.10 — guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/)
- [Guide complet — 5. Sauvegarder et récupérer](../../../../../../02-Fiches-Completes/TrueNAS/SCALE-25.10/Installation-Deploiement/60_Deploiement_TrueNAS_SCALE_25.10.md#5-sauvegarder-et-recuperer)
