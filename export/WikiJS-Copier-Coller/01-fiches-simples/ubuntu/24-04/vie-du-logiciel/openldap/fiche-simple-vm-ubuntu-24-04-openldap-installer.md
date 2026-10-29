# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Installer

- **Environnement** : VM Ubuntu 24.04 avec FQDN stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24.04 LTS Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / installer

---

## Problème précis à résoudre

Installer slapd et les utilitaires sur Ubuntu 24.04 sans écraser une base existante.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install slapd ldap-utils
   ```
   👉 Explication : Sur Ubuntu, le mot de passe administrateur est demandé par debconf : saisir une valeur générée, conservée dans le gestionnaire de secrets, jamais écrite dans la commande.

2. Si le suffixe par défaut ne convient pas, reconfigurer uniquement sur une installation vide :
   ```bash
   sudo dpkg-reconfigure slapd
   ```
   👉 Explication : Saisir le nom de domaine (suffixe), l'organisation et le mot de passe; refuser la conservation d'une base inutile. Ne jamais lancer cette commande sur un annuaire contenant des données sans sauvegarde.

3. Contrôler le service et le suffixe :
   ```bash
   sudo systemctl status slapd --no-pager
   sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b cn=config olcSuffix
   ```
   👉 Explication : slapd doit être active; olcSuffix doit correspondre au domaine saisi.

## 2. Production — Contrôles

Consigner version, suffixe et emplacement des données (/var/lib/ldap).

## 3. Production — Sécurité

- Limiter l'accès administratif à la VM; ne pas exposer le port 389 avant la configuration TLS.

## Validation et retour arrière

- **Validation** : slapd actif et suffixe conforme.
- **Retour arrière** : Conserver le snapshot; ne purger les données qu'après vérification (sudo apt remove slapd conserve les données).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-configurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-openldap)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)