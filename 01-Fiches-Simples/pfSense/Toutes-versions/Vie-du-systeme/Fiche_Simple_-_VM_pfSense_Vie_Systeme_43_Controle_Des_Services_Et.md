# Fiche_Simple_-_VM_pfSense_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier que seuls les services prévus fonctionnent.

## 1. Hors-Production (Lab / Test / POC)

1. Consulter Status > Services et comparer aux services attendus.
   👉 Explication : chaque service doit être démarré s'il est requis et arrêté sinon.

2. Contrôler en shell :
   ```sh
   sockstat -4 -6 -l
   service -e
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

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire pfSense CE](./Sommaire_-_Vie_du_systeme_pfSense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
