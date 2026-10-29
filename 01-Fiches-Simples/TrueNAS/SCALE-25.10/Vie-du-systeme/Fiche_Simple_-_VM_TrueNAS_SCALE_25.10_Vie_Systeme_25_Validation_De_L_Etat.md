# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Capturer l'état de référence du NAS neuf.

## 1. Hors-Production (Lab / Test / POC)

1. Exporter la configuration : GUI Système > Général > Gérer la configuration > Télécharger le fichier.
   ```bash
   sudo midclt call system.info | python3 -m json.tool
   sudo zpool status
   ```
   👉 Explication : informations système et pools.

2. Créer un instantané de l'environnement d'amorçage : GUI Système > Environnements d'amorçage > Ajouter.
   ```bash
   sudo midclt call bootenv.create '{"name": "baseline"}'
   ```
   👉 Explication : point de retour du système.

## 2. Production — Contrôles

Conserver la baseline avec le dossier du NAS.

## 3. Production — Sécurité

Chiffrer le fichier de configuration exporté (case « Exporter les secrets » uniquement si nécessaire).

## Validation et retour arrière

- **Validation** : Baseline archivée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
