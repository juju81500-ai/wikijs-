# Fiche_Simple_-_VM_pfSense_Vie_Systeme_06_Langue_Et_Localisation_Locales

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 06 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-06`

---

## Problème précis à résoudre

Définir la langue de l'interface.

## 1. Hors-Production (Lab / Test / POC)

1. Dans System > General Setup > localization > Language, choisir `Français` (disponible sur les versions récentes), puis Save.
   👉 Explication : l'interface web passe en français partiellement; l'installateur reste en anglais.

2. Contrôler la valeur enregistrée :
   ```sh
   grep -m1 '<language>' /cf/conf/config.xml
   ```
   👉 Explication : affiche par exemple `fr_FR`.

## 2. Production — Contrôles

Conserver l'anglais si les procédures de l'équipe y font référence.

## 3. Production — Sécurité

La langue n'a aucun impact sur la sécurité.

## Validation et retour arrière

- **Validation** : L'interface s'affiche dans la langue choisie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
