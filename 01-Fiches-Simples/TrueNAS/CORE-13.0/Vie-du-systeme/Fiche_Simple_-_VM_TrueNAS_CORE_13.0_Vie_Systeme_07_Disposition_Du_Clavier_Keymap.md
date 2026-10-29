# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Définir le clavier de la console.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Disposition du clavier de la console (fr.kbd).
   ```sh
   midclt call system.general.update '{"kbdmap": "fr"}'
   ```
   👉 Explication : applique l'AZERTY à la console.

2. Contrôler :
   ```sh
   midclt call system.general.config | grep -i kbdmap
   ```
   👉 Explication : valeur enregistrée.

## 2. Production — Contrôles

Documenter la disposition.

## 3. Production — Sécurité

Éviter les mots de passe avec caractères dépendant du clavier.

## Validation et retour arrière

- **Validation** : La saisie à la console est correcte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
