# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau pour des journaux et snapshots cohérents.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Localisation > Fuseau horaire (Europe/Paris).
   ```bash
   sudo midclt call system.general.update '{"timezone": "Europe/Paris"}'
   ```
   👉 Explication : applique le fuseau au système et aux tâches planifiées.

2. Vérifier :
   ```bash
   timedatectl
   ```
   👉 Explication : affiche le fuseau et l'état de l'horloge.

## 2. Production — Contrôles

Uniformiser le fuseau sur tous les NAS et la supervision.

## 3. Production — Sécurité

Une heure fausse rend les snapshots et journaux inexploitables.

## Validation et retour arrière

- **Validation** : `timedatectl` montre Europe/Paris.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
