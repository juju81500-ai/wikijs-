# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-45`

---

## Problème précis à résoudre

Chercher les erreurs matérielles et ZFS.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les alertes : cloche de l'interface ou :
   ```bash
   sudo midclt call alert.list | python3 -m json.tool | head -40
   ```
   👉 Explication : alertes en cours.

2. Chercher les erreurs disque et noyau :
   ```bash
   sudo dmesg -T | grep -i -E 'error|fail|ata|nvme' | tail
   sudo zpool status -v
   ```
   👉 Explication : erreurs de lecture, d'écriture ou de somme de contrôle.

3. Contrôler SMART : GUI Stockage > Disques > Tests S.M.A.R.T.
   ```bash
   sudo smartctl -H /dev/sdX
   sudo smartctl -A /dev/sdX | grep -i -E 'reallocated|pending|crc'
   ```
   👉 Explication : santé du disque ; secteurs réalloués ou en attente à surveiller.

## 2. Production — Contrôles

Traiter chaque erreur et clore l'alerte.

## 3. Production — Sécurité

Un compteur d'erreurs croissant impose le remplacement du disque.

## Validation et retour arrière

- **Validation** : Aucune erreur non expliquée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : TrueNAS SCALE 25.10 Supervision Alertes Pool](<../Vie-du-logiciel/Supervision/Fiche_Simple_-_TrueNAS_SCALE_25.10_Supervision_Alertes_Pool.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
