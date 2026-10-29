# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Choisir la langue de l'interface.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Général > Langue (Français).
   ```sh
   midclt call system.general.update '{"language": "fr"}'
   ```
   👉 Explication : l'interface web passe en français ; la console reste en anglais.

2. Vérifier :
   ```sh
   midclt call system.general.config | grep -i language
   ```
   👉 Explication : valeur enregistrée.

## 2. Production — Contrôles

Garder les journaux en anglais.

## 3. Production — Sécurité

Ne pas modifier les fichiers système à la main (perdus au redémarrage).

## Validation et retour arrière

- **Validation** : Interface en français.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
