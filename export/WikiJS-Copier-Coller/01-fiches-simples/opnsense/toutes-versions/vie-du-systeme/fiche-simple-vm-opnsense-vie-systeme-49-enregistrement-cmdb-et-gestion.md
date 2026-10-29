# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Déclarer le pare-feu dans l'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Créer la fiche CMDB : nom, FQDN, adresses WAN/LAN, version, interfaces, rôle, propriétaire, criticité, lien vers la sauvegarde.
   👉 Explication : rend le pare-feu identifiable pour les équipes.

2. Exporter les informations techniques :
   ```sh
   opnsense-version -v
   hostname
   ifconfig | grep -E '^[a-z]|inet '
   sha256 /conf/config.xml
   ```
   👉 Explication : version, nom, adresses et empreinte de la configuration à saisir dans la CMDB.

3. Valider la liste des comptes dans Système > Accès > Utilisateurs.
   👉 Explication : chaque compte doit être rattaché à une personne ou un outil.

## 2. Production — Contrôles

Mettre à jour la CMDB à chaque changement majeur.

## 3. Production — Sécurité

Revue périodique des comptes et clés API.

## Validation et retour arrière

- **Validation** : Fiche CMDB complète et comptes validés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)