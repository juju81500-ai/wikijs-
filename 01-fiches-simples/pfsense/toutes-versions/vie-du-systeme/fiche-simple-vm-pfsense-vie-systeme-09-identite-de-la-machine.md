# Fiche_Simple_-_VM_pfSense_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Pare-feu pfSense CE ([[Glossary:VM]] ou matériel)
- **OS / Version** : pfSense CE; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Donner un nom et un domaine cohérents au pare-feu.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'assistant (Wizard, étape 1) ou System > General Setup, renseigner Hostname (ex. `fw01`) et Domain (ex. `exemple.lan`), puis Save.
   👉 Explication : le nom complet devient `fw01.exemple.lan` ([[Glossary:FQDN]]).

2. Contrôler en shell (option 8) :
   ```sh
   hostname
   grep -E '<hostname>|<domain>' /cf/conf/config.xml
   ```
   👉 Explication : affiche le nom court et le domaine stockés dans la configuration.

3. Créer l'enregistrement [[Glossary:DNS]] correspondant dans l'annuaire DNS interne.
   👉 Explication : permet d'administrer le pare-feu par son nom.

## 2. Production — Contrôles

Respecter la convention de nommage de l'entreprise et la déclarer dans la [[Glossary:CMDB]].

## 3. Production — Sécurité

Ne pas utiliser un domaine public que l'on ne possède pas.

## Validation et retour arrière

- **Validation** : `hostname` renvoie le nom attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-administration/01-gouvernance-architecture/vie-du-systeme.md)
- [Sommaire pfSense CE](./sommaire-vie-du-systeme-pfsense.md)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)
