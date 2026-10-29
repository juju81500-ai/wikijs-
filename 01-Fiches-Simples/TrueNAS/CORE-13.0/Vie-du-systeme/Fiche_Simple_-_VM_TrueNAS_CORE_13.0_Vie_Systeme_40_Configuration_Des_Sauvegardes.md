# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder données et configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Snapshots : GUI Tâches > Instantanés périodiques > Ajouter.
   ```sh
   zfs snapshot POOL/DATASET@MANUEL
   zfs list -t snapshot -r POOL/DATASET
   ```
   👉 Explication : crée et liste les snapshots.

2. Réplication : GUI Tâches > Replication Tasks > Ajouter.
   ```sh
   midclt call replication.query | head -30
   ```
   👉 Explication : envoi des snapshots vers un autre NAS.

3. Configuration : GUI Système > Général > Enregistrer la configuration.
   ```sh
   midclt call config.save
   ```
   👉 Explication : exporte la base de configuration (stocker chiffrée hors du NAS).

## 2. Production — Contrôles

Règle 3-2-1.

## 3. Production — Sécurité

Chiffrer les sauvegardes et protéger les clés.

## Validation et retour arrière

- **Validation** : Une copie récente existe ailleurs.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
