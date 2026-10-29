# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Connaître les outils intégrés.

## 1. Hors-Production (Lab / Test / POC)

1. Shell : GUI Shell ou SSH.
   ```sh
   zpool list
   zfs list
   camcontrol devlist
   ```
   👉 Explication : pools, datasets et disques.

2. État matériel et système :
   ```sh
   sysctl kern.version hw.model
   geom disk list | head -20
   ```
   👉 Explication : version et modèle.

3. API en ligne de commande :
   ```sh
   midclt call system.info
   ```
   👉 Explication : informations système.

## 2. Production — Contrôles

Documenter les commandes autorisées.

## 3. Production — Sécurité

Réserver les modifications à la GUI ou à `midclt`.

## Validation et retour arrière

- **Validation** : Les commandes répondent.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
