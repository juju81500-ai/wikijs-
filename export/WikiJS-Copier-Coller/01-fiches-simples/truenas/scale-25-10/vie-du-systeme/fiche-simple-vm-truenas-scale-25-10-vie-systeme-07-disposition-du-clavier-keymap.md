# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Définir le clavier de la console locale.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Localisation > Disposition du clavier (Français - fr).
   ```bash
   sudo midclt call system.general.update '{"kbdmap": "fr"}'
   ```
   👉 Explication : applique la disposition AZERTY à la console.

2. Contrôler le réglage :
   ```bash
   sudo midclt call system.general.config | grep -i kbdmap
   ```
   👉 Explication : affiche la valeur enregistrée.

## 2. Production — Contrôles

Documenter la disposition utilisée pour la console et le BMC.

## 3. Production — Sécurité

Éviter les mots de passe contenant des caractères sensibles à la disposition.

## Validation et retour arrière

- **Validation** : Les caractères saisis à la console correspondent au clavier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)