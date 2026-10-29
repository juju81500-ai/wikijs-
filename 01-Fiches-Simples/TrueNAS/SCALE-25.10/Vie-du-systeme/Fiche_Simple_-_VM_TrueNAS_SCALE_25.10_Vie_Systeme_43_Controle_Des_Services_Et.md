# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier les services et ports ouverts.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Services (état et démarrage automatique).
   ```bash
   sudo midclt call service.query | python3 -m json.tool | grep -E '"service"|"state"'
   ```
   👉 Explication : état de chaque service.

2. Lister les ports :
   ```bash
   sudo ss -tulpn
   ```
   👉 Explication : comparer à la liste attendue.

## 2. Production — Contrôles

Comparer avec le runbook.

## 3. Production — Sécurité

Tout port non prévu est une anomalie.

## Validation et retour arrière

- **Validation** : Aucun service ni port imprévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
