# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_32_Automatisation_Des_Correctifs_De

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 32 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-32`

---

## Problème précis à résoudre

Suivre les mises à jour sans les subir.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Mises à jour : surveiller les alertes de mise à jour.
   ```sh
   midclt call update.check_available
   ```
   👉 Explication : interroge le serveur de mises à jour.

2. Planifier : annoncer, sauvegarder la configuration, mettre à jour, valider.
   👉 Explication : pas de mise à jour automatique non supervisée.

## 2. Production — Contrôles

Tester d'abord sur un NAS de test.

## 3. Production — Sécurité

Lire les notes de version ; CORE ne reçoit plus que des correctifs limités (voir fiche de statut).

## Validation et retour arrière

- **Validation** : Procédure de patching documentée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
