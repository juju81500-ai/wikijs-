# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir la langue de l'interface et du système.

## 1. Hors-Production (Lab / Test / POC)

1. L'installateur TrueNAS est en anglais ; régler la langue de l'interface web dans : Système > Général > Localisation > Langue (Français).
   ```bash
   sudo midclt call system.general.config | python3 -m json.tool | grep -i language
   ```
   👉 Explication : l'interface web s'affiche dans la langue choisie ; le système reste en anglais.

2. Définir la langue en ligne de commande :
   ```bash
   sudo midclt call system.general.update '{"language": "fr"}'
   ```
   👉 Explication : équivalent de la modification dans la GUI.

## 2. Production — Contrôles

Garder les journaux et la console en anglais pour faciliter la recherche d'erreurs.

## 3. Production — Sécurité

Ne pas modifier les fichiers système à la main : tout passe par la GUI ou `midclt`.

## Validation et retour arrière

- **Validation** : Interface en français après rechargement.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)