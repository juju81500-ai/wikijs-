# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier services et ports.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Services.
   ```sh
   service -e
   midclt call service.query | grep -E '"service"|"state"'
   ```
   👉 Explication : services actifs.

2. Lister les ports :
   ```sh
   sockstat -4 -6 -l
   ```
   👉 Explication : comparer à la liste attendue.

## 2. Production — Contrôles

Comparer au runbook.

## 3. Production — Sécurité

Tout port imprévu est une anomalie.

## Validation et retour arrière

- **Validation** : Aucun service imprévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
