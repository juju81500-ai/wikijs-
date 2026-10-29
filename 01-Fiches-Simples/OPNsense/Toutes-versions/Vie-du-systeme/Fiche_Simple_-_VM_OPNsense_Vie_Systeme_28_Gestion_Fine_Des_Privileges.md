# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Limiter les droits des administrateurs délégués.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Accès > Groupes > Privilèges et attribuer des pages précises (ex. `GUI : Pare-feu : Règles`, `Diagnostics`) au lieu de `Tous`.
   👉 Explication : chaque groupe n'accède qu'aux pages utiles.

2. Si le shell est nécessaire, contrôler les droits sudo du compte :
   ```sh
   sudo -l -U ADMIN01 2>/dev/null
   grep -A5 '<group>' /conf/config.xml | head -20
   ```
   👉 Explication : affiche les droits sudo (plugin `os-sudo` ou option du compte) et les groupes définis.

## 2. Production — Contrôles

Revue des groupes et privilèges à chaque changement d'équipe.

## 3. Production — Sécurité

Aucun compte ne doit avoir `Tous` hors administrateur principal.

## Validation et retour arrière

- **Validation** : Un compte limité ne voit pas les pages non autorisées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire OPNsense](./Sommaire_-_Vie_du_systeme_OPNsense.md)
- [Documentation officielle](https://docs.opnsense.org/)
