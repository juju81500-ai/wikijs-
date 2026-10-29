# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Configurer

- **Environnement** : VM Ubuntu 24.04 avec FQDN stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24.04 LTS Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / configurer
- **Tags** : `openldap`, `ubuntu24-04`, `vie-du-logiciel`, `configurer`

---

## Problème précis à résoudre

Configurer TLS sur Ubuntu en tenant compte d'AppArmor et des droits de la clé.

## 1. Hors-Production (Lab / Test / POC)

1. Placer la chaîne et la clé du certificat (CN/SAN = FQDN) :
   ```bash
   sudo install -d -m 0755 /etc/ldap/tls
   sudo install -m 0644 CA_CERTIFICAT.crt LDAP_CERTIFICAT.crt /etc/ldap/tls/
   sudo install -m 0600 -o openldap -g openldap LDAP_CLE.key /etc/ldap/tls/
   ```
   👉 Explication : CA_CERTIFICAT.crt, LDAP_CERTIFICAT.crt et LDAP_CLE.key sont les fichiers fournis par la PKI (à remplacer); la clé reste en 0600 pour l'utilisateur openldap.

2. Appliquer la modification TLS cn=config :
   👉 Explication : Reprendre les étapes d'écriture du LDIF de [la fiche Debian Configurer TLS](../../../../Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Configurer_TLS.md) (modification olcTLSCACertificateFile, olcTLSCertificateFile, olcTLSCertificateKeyFile), après sauvegarde de cn=config.

3. Si slapd refuse de lire les fichiers, chercher un refus AppArmor :
   ```bash
   sudo journalctl -k | grep -i 'apparmor.*slapd'
   sudoedit /etc/apparmor.d/local/usr.sbin.slapd
   ```
   👉 Explication : Ajouter dans le fichier local une règle de lecture pour le dossier utilisé, de la forme /etc/ldap/tls/** r, puis recharger : sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.slapd. Vérifier le nom exact du profil sur l'hôte avant d'agir.

4. Redémarrer et tester STARTTLS :
   ```bash
   sudo systemctl restart slapd
   LDAPTLS_CACERT=/etc/ldap/tls/CA_CERTIFICAT.crt ldapsearch -x -ZZ -H ldap://FQDN -b '' -s base
   ```
   👉 Explication : FQDN est le nom du serveur (à remplacer); -ZZ impose STARTTLS et échoue si TLS n'est pas valide.

## 2. Production — Contrôles

Faire relire la chaîne et la date d'expiration; la création de l'arborescence (OU) suit [la fiche Debian Creer OU](../../../../Debian/13/Vie-du-logiciel/OpenLDAP/Fiche_Simple_-_VM_Debian_13_OpenLDAP_Creer_OU.md).

## 3. Production — Sécurité

- Clé TLS lisible uniquement par openldap; ne pas assouplir AppArmor au-delà du dossier nécessaire.

## Validation et retour arrière

- **Validation** : Un client avec la CA approuvée établit STARTTLS sans erreur.
- **Retour arrière** : Restaurer cn=config depuis la sauvegarde LDIF (voir la fiche Sauvegarder / Restaurer) puis redémarrer slapd.

## Si le problème n'est pas résolu

- [Étape suivante du guide](./Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Securiser.md)
- [Fiche d'entrée du logiciel](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_OpenLDAP.md)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)
