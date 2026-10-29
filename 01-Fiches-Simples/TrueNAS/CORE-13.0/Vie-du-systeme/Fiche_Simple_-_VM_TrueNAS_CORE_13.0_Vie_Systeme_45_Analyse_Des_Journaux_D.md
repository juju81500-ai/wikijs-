# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-45`

---

## Problème précis à résoudre

Chercher les erreurs matérielles et ZFS.

## 1. Hors-Production (Lab / Test / POC)

1. Alertes : cloche de l'interface ou :
   ```sh
   midclt call alert.list | head -40
   ```
   👉 Explication : alertes en cours.

2. Erreurs disque et noyau :
   ```sh
   dmesg | grep -i -E 'error|fail|cam status' | tail
   zpool status -v
   ```
   👉 Explication : erreurs de lecture, d'écriture, de somme de contrôle.

3. SMART : GUI Stockage > Disks > S.M.A.R.T. Tests.
   ```sh
   smartctl -H /dev/da0
   smartctl -A /dev/da0 | grep -i -E 'reallocated|pending|crc'
   ```
   👉 Explication : santé du disque.

## 2. Production — Contrôles

Traiter chaque erreur.

## 3. Production — Sécurité

Compteur croissant : remplacer le disque.

## Validation et retour arrière

- **Validation** : Aucune erreur inexpliquée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
