# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Prerequis_Limites

- **Environnement** : VM Ubuntu 24.04 avec FQDN stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24.04 LTS Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / prérequis et limites
- **Tags** : `openldap`, `ubuntu24-04`, `vie-du-logiciel`, `prerequis-limites`

---

## Problème précis à résoudre

Valider les prérequis Ubuntu 24.04 avant d'installer slapd, sans répéter le cadrage Debian.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'OS, le FQDN et l'heure :
   ```bash
   cat /etc/os-release
   hostnamectl
   timedatectl
   ```
   👉 Explication : Le FQDN doit être stable et résolu par les clients; le suffixe LDAP en dépendra.

2. Vérifier la version candidate de slapd :
   ```bash
   apt-cache policy slapd
   ```
   👉 Explication : Noter la version (série 2.6 attendue); consigner l'origine du paquet.

3. Vérifier AppArmor, spécificité d'Ubuntu :
   ```bash
   sudo aa-status | grep -i slapd
   ```
   👉 Explication : Un profil slapd peut être appliqué : les fichiers TLS et sauvegardes hors des chemins habituels peuvent être refusés (voir la fiche Configurer).

## 2. Production — Contrôles

Pour le cadrage fonctionnel (suffixe, DIT, périmètre), reprendre [la fiche Debian Cadrer](../../../../Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Cadrer.md). Limites : pas de réplication ni de HA traitées ici. Rocky Linux 9 n'est pas couvert : OpenLDAP serveur n'y est pas fourni dans les dépôts de base (à vérifier avant tout choix).

## 3. Production — Sécurité

- Aucun mot de passe écrit dans la documentation; le gestionnaire de secrets garde les valeurs.

## Validation et retour arrière

- **Validation** : FQDN, version de slapd et statut AppArmor consignés.
- **Retour arrière** : Aucun changement : rien à restaurer.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Installer.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_OpenLDAP.md)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)
