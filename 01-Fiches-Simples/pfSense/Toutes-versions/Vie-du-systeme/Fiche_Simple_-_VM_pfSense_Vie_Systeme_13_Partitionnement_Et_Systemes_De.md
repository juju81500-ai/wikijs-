# Fiche_Simple_-_VM_pfSense_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir le système de fichiers de l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur, écran « Partitioning » : choisir `Auto (ZFS)` (recommandé) ou `Auto (UFS)` pour du matériel très limité.
   👉 Explication : ZFS permet les environnements de démarrage (System > Boot Environments) pour annuler une mise à jour.

2. Choisir la disposition `stripe` (un disque) ou `mirror` (deux disques) et confirmer l'effacement du disque.
   👉 Explication : le miroir protège contre la panne d'un disque.

3. Contrôler après installation :
   ```sh
   zpool status
   df -h
   gpart show
   ```
   👉 Explication : montre le pool, l'espace libre et la table de partitions.

## 2. Production — Contrôles

Surveiller l'espace disque (Status > Dashboard) pour que les journaux ne remplissent pas le disque.

## 3. Production — Sécurité

Ne pas installer sur un disque contenant des données à conserver.

## Validation et retour arrière

- **Validation** : `zpool status` indique `ONLINE` sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
