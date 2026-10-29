# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Capturer l'état de référence.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Enregistrer la configuration.
   ```sh
   midclt call system.info | head -20
   zpool status
   ```
   👉 Explication : état système et pools.

2. Créer un environnement d'amorçage : Système > Mises à jour de démarrage > Ajouter.
   ```sh
   beadm create baseline
   ```
   👉 Explication : point de retour du système.

## 2. Production — Contrôles

Conserver la baseline avec le dossier.

## 3. Production — Sécurité

Chiffrer le fichier de configuration exporté.

## Validation et retour arrière

- **Validation** : Baseline archivée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)