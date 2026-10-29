# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_12_Fuseau_Horaire

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 12 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-12`

---

## Problème précis à résoudre

Régler le fuseau.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Fuseau horaire (Europe/Paris).
   ```sh
   midclt call system.general.update '{"timezone": "Europe/Paris"}'
   ```
   👉 Explication : applique le fuseau.

2. Vérifier :
   ```sh
   date
   ls -l /etc/localtime
   ```
   👉 Explication : heure locale correcte.

## 2. Production — Contrôles

Uniformiser le fuseau sur tous les systèmes.

## 3. Production — Sécurité

Une heure fausse rend les snapshots et journaux inexploitables.

## Validation et retour arrière

- **Validation** : `date` affiche l'heure locale.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
