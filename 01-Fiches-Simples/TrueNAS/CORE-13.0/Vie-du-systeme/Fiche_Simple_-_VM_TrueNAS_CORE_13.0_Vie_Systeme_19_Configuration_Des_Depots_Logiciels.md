# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-19`

---

## Problème précis à résoudre

Choisir le canal de mise à jour.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Mises à jour > Train (STABLE).
   ```sh
   midclt call update.get_trains | head -30
   ```
   👉 Explication : liste les trains et le train courant.

2. Ne pas utiliser `pkg` sur le système : la commande n'est pas supportée.
   👉 Explication : le système se met à jour comme un ensemble.

## 2. Production — Contrôles

Train STABLE uniquement.

## 3. Production — Sécurité

Pas de train de test sur des données réelles.

## Validation et retour arrière

- **Validation** : Train STABLE sélectionné.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
