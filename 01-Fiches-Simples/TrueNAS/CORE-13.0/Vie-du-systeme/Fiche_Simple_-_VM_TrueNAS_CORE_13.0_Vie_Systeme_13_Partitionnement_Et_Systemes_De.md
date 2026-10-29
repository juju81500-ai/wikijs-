# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_13_Partitionnement_Et_Systemes_De

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 13 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-13`

---

## Problème précis à résoudre

Choisir les disques de démarrage ; ZFS gère le reste.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : Install/Upgrade, cocher un ou deux disques de démarrage.
   👉 Explication : l'installateur crée seul le pool `freenas-boot`.

2. Après installation :
   ```sh
   zpool status freenas-boot
   gpart show
   ```
   👉 Explication : pool ONLINE. GUI : Système > Mises à jour de démarrage > État.

3. Ne pas modifier les partitions du système.
   👉 Explication : le système est restauré à chaque démarrage.

## 2. Production — Contrôles

Deux disques de démarrage en miroir.

## 3. Production — Sécurité

Ne pas stocker de données sur `freenas-boot`.

## Validation et retour arrière

- **Validation** : `freenas-boot` ONLINE.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
