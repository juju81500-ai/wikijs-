# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Définir la langue de l'interface.

## 1. Hors-Production (Lab / Test / POC)

1. Après installation, choisir la langue dans Système > Paramètres > Général > Langue (Français), puis Enregistrer.
   👉 Explication : l'interface web s'affiche en français; l'installateur, lui, est en anglais.

2. Contrôler la langue enregistrée dans la configuration :
   ```sh
   grep -m1 '<language>' /conf/config.xml
   ```
   👉 Explication : affiche par exemple `fr_FR`.

## 2. Production — Contrôles

Garder l'interface en français pour les exploitants, la console reste en anglais.

## 3. Production — Sécurité

La langue n'a aucun impact sur la sécurité; ne pas changer les journaux en dehors de l'UTF-8.

## Validation et retour arrière

- **Validation** : L'interface s'affiche en français.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
