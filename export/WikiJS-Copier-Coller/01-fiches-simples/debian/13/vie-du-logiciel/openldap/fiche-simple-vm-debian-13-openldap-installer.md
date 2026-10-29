# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Installer.md

- **Environnement** : VM Debian 13 Trixie dédiée, dépôts APT approuvés
- **OS / Version** : Debian 13; slapd 2.6
- **Catégorie** : annuaire / identité / installation

---

## Problème précis à résoudre

Installer slapd et les utilitaires LDAP Debian sans remplacer une base existante ni exposer un secret.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install slapd ldap-utils
   ```
   👉 Explication : `slapd` est le serveur, `ldap-utils` fournit `ldapsearch`, `ldapadd`, `ldapwhoami`.

2. À l'invite debconf, saisir un mot de passe administrateur généré aléatoirement, conservé dans le gestionnaire de secrets.
   👉 Explication : ne jamais l'écrire dans l'historique shell, un ticket ou le wiki.

3. Vérifier le service et l'écoute :
   ```bash
   sudo systemctl status slapd --no-pager
   sudo ss -ltnp | grep -E ':(389)\b'
   ```
   👉 Explication : `slapd` doit être `active (running)`.

4. Contrôler le suffixe créé :
   ```bash
   sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b "olcDatabase={1}mdb,cn=config" olcSuffix
   ```
   👉 Explication : Debian dérive le suffixe du domaine; ne pas relancer `dpkg-reconfigure slapd` sur un annuaire contenant des données sans sauvegarde.

## 2. Production — Contrôles

Consigner la version, le suffixe, le `olcRootDN`, l'emplacement des données et la procédure de rotation des secrets.

## 3. Production — Sécurité

- Ne pas taper le mot de passe admin dans une commande ou un script.
- Ne jamais accepter une option qui supprime/remplace l'ancienne base sans sauvegarde et approbation.
- Installer uniquement depuis des dépôts approuvés; ne pas désactiver la vérification APT.
- Limiter l'accès administratif à la VM.

## Validation et retour arrière

- **Validation** : paquet et source vérifiés, slapd actif, suffixe et identité admin consignés.
- **Retour arrière** : conserver le snapshot; ne pas purger les données LDAP après une installation incorrecte sans vérifier leur propriétaire.

## Si le problème n'est pas résolu

- [Debian — paquet slapd Trixie](https://packages.debian.org/trixie/slapd)
- [Debian — OpenLDAPSetup](https://wiki.debian.org/LDAP/OpenLDAPSetup)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#2-installer)