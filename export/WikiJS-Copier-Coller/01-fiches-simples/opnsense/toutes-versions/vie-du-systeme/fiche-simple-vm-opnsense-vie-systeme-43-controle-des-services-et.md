# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier que seuls les services prévus fonctionnent.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter Lobby > Tableau de bord > Services (ou Système > Diagnostics > Services) et comparer aux services attendus.
   👉 Explication : chaque service doit être démarré s'il est requis et arrêté sinon.

2. Contrôler en shell :
   ```sh
   sockstat -4 -6 -l
   configctl service list 2>/dev/null | head -30
   pfctl -si | head -8
   ```
   👉 Explication : liste les ports en écoute, les services et l'état de pf.

## 2. Production — Contrôles

Conserver cette liste comme référence de recette.

## 3. Production — Sécurité

Tout port inattendu à l'écoute est un incident à analyser.

## Validation et retour arrière

- **Validation** : Les ports ouverts correspondent à la liste attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)