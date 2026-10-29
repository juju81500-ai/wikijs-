---
title: "Déployer OpenLDAP (slapd 2.6) sur Debian 13"
description: "Fiche simple : [cadrer le pilote OpenLDAP](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/OpenLDAP/FicheSimple-VMDebian13OpenLDAPCadrer.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["openldap", "slapd", "ldap", "debian13", "cn-config", "slapcat", "ldaps"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer OpenLDAP (slapd 2.6) sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; paquet `slapd` 2.6.10+dfsg-1 (version du dépôt Debian vérifiée le 29 octobre 2026)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : annuaire LDAP autonome (un serveur), configuration OLC `cn=config`, TLS, sauvegarde `slapcat`
- **Catégorie** : annuaire / identité
- **Tags** : `openldap`, `slapd`, `ldap`, `debian13`, `cn-config`, `slapcat`, `ldaps`

## 1. Périmètre et choix

Fiche simple : [cadrer le pilote OpenLDAP](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-cadrer).

Ce guide installe l'annuaire OpenLDAP fourni par Debian 13. Il ne remplace ni Active Directory, ni Samba AD DC (voir le [guide Samba AD DC](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13)), ni FreeIPA (Kerberos, CA et DNS intégrés, voir le [guide FreeIPA Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9)). Choisir OpenLDAP quand une application demande uniquement un annuaire LDAP/LDAPS. Réplication (syncrepl), overlays (memberOf, ppolicy), SSSD client et migration depuis un autre annuaire ne sont pas couverts.

Prérequis : VM Debian 13 dédiée, nom d'hôte FQDN stable, DNS résolvant ce nom, heure synchronisée, snapshot de la VM avant les étapes de configuration. Ce guide n'a pas été testé sur une machine Debian 13.

## 2. Installer

Fiche simple : [installer slapd et les utilitaires LDAP](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-installer).

```bash
sudo apt update
sudo apt install slapd ldap-utils
```

debconf demande le mot de passe administrateur de l'annuaire. Utiliser un secret généré aléatoirement, conservé dans le gestionnaire de secrets approuvé, jamais dans l'historique shell. Debian crée une base MDB dont le suffixe est dérivé du domaine du système. Ne pas relancer `dpkg-reconfigure slapd` sur un annuaire contenant des données sans sauvegarde préalable : la reconfiguration peut remplacer la base (lire chaque question et accepter uniquement de conserver l'ancienne base).

## 3. Vérifier la configuration OLC

Fiche simple : [vérifier la configuration OLC](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-verifier-olc).

La configuration se lit et se modifie dans `cn=config` via le socket local `ldapi:///` avec l'authentification `EXTERNAL` (root local) :

```bash
sudo systemctl status slapd --no-pager
sudo ldapwhoami -Y EXTERNAL -H ldapi:/// -Q
sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b cn=config -s one dn
sudo ldapsearch -LLLQ -Y EXTERNAL -H ldapi:/// -b "olcDatabase={1}mdb,cn=config" olcSuffix olcRootDN olcAccess
```

Noter le suffixe (`olcSuffix`) et le `olcRootDN` : ils remplacent les valeurs `dc=example,dc=org` utilisées ci-dessous. Ne jamais éditer les fichiers sous `/etc/ldap/slapd.d` à la main; utiliser `ldapmodify`/`ldapadd`.

## 4. Créer une structure minimale

Fiche simple : [créer les unités organisationnelles](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-creer-ou).

Créer `/root/ou-base.ldif` (adapter le suffixe) :

```ldif
dn: ou=People,dc=example,dc=org
objectClass: organizationalUnit
ou: People

dn: ou=Groups,dc=example,dc=org
objectClass: organizationalUnit
ou: Groups
```

```bash
ldapadd -x -D "cn=admin,dc=example,dc=org" -W -f /root/ou-base.ldif
ldapsearch -x -LLL -D "cn=admin,dc=example,dc=org" -W -b "dc=example,dc=org" -s one dn
```

Si l'annuaire est local, `-x -D ... -W` demande le mot de passe en interactif; ne pas le passer avec `-w`. Les comptes applicatifs ne doivent pas utiliser `cn=admin` : créer des comptes de lecture dédiés et limiter les `olcAccess` (voir la documentation « Access Control »). Ne pas ouvrir le port 389 vers Internet.

## 5. Activer TLS

Fiche simple : [configurer TLS](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-configurer-tls).

Obtenir un certificat dont le CN/SAN correspond au FQDN utilisé par les clients (CA interne ou ACME). Copier la chaîne et la clé sous `/etc/ldap/tls/`, propriétaire de la clé `openldap:openldap`, mode `0600`. Puis, avec `/root/tls.ldif` :

```ldif
dn: cn=config
changetype: modify
replace: olcTLSCACertificateFile
olcTLSCACertificateFile: /etc/ldap/tls/ca.crt
-
replace: olcTLSCertificateFile
olcTLSCertificateFile: /etc/ldap/tls/ldap.crt
-
replace: olcTLSCertificateKeyFile
olcTLSCertificateKeyFile: /etc/ldap/tls/ldap.key
```

```bash
sudo ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f /root/tls.ldif
```

Pour LDAPS sur 636, ajouter `ldaps:///` dans `SLAPD_SERVICES` du fichier `/etc/default/slapd`, puis redémarrer `slapd`. Valider ensuite STARTTLS et LDAPS avant d'imposer le chiffrement (`olcSecurity`, décrit dans l'Administrator's Guide). Une valeur TLS erronée empêche le démarrage : garder la session ouverte et conserver le LDIF inverse.

## 6. Sauvegarder

Fiche simple : [sauvegarder OpenLDAP](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-sauvegarder).

Exporter la configuration et les données avec `slapcat` (lecture seule) vers un répertoire protégé, puis copier hors hôte, chiffré :

```bash
sudo install -d -m 0700 /var/backups/ldap
sudo slapcat -n 0 -l /var/backups/ldap/config-$(date +%F).ldif
sudo slapcat -n 1 -l /var/backups/ldap/data-$(date +%F).ldif
sudo ls -l /var/backups/ldap
```

Les LDIF contiennent des condensats de mots de passe : les protéger comme des secrets. Sauvegarder aussi les certificats/clés TLS séparément.

## 7. Restaurer (test sur une VM isolée)

Fiche simple : [tester la restauration sur une VM isolée](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-restaurer-test).

`slapadd` écrit directement dans la base et exige `slapd` arrêté ; il ajoute à une base vide. Ne jamais l'exécuter sur la production pour « tester ». Sur une VM de test avec le même suffixe et une base vide :

```bash
sudo systemctl stop slapd
sudo -u openldap slapadd -n 1 -l /chemin/data-AAAA-MM-JJ.ldif
sudo systemctl start slapd
```

Exécuter `slapadd` sous l'utilisateur `openldap` évite de créer des fichiers appartenant à root. La restauration de `-n 0` (config) est une opération de reconstruction complète : se référer à la page de manuel et la répéter d'abord sur la VM de test.

## 8. Validation

Fiche simple : [valider LDAP, TLS et les flux](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-valider).

- `slapd` actif, `ldapwhoami -Y EXTERNAL -H ldapi:/// -Q` répond `dn:gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth`.
- Les entrées `ou=People` et `ou=Groups` sont lisibles avec `ldapsearch`.
- Un test STARTTLS/LDAPS depuis un client valide la chaîne : `LDAPTLS_CACERT=/chemin/ca.crt ldapsearch -x -H ldaps://FQDN -b "dc=example,dc=org" -s base`.
- Les LDIF de sauvegarde existent, ne sont pas vides, et un import test sur VM isolée retrouve le même nombre d'entrées.
- Port 389/636 limité aux clients autorisés (pare-feu).

## 9. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-retour-arriere).

Avant toute modification de `cn=config`, exporter `slapcat -n 0`. En cas d'échec TLS ou ACL : `ldapmodify -Y EXTERNAL` pour remettre les anciennes valeurs, ou restaurer le snapshot de la VM. En dernier recours, arrêter `slapd` et restaurer les LDIF sur une base vide (étape 7), après avoir conservé les répertoires `/var/lib/ldap` et `/etc/ldap/slapd.d` actuels en les renommant (ne pas les supprimer).

## Sources

- [Debian — paquet slapd (trixie)](https://packages.debian.org/trixie/slapd)
- [Debian Wiki — LDAP/OpenLDAPSetup](https://wiki.debian.org/LDAP/OpenLDAPSetup)
- [OpenLDAP — Administrator's Guide 2.6](https://www.openldap.org/doc/admin26/)
- [OpenLDAP — configuration slapd-config (OLC)](https://www.openldap.org/doc/admin26/slapdconf2.html)
- [OpenLDAP — TLS](https://www.openldap.org/doc/admin26/tls.html)
- [OpenLDAP — maintenance et sauvegardes](https://www.openldap.org/doc/admin26/maintenance.html)
- [Debian — page de manuel slapcat](https://manpages.debian.org/trixie/slapd/slapcat.8.en.html)
- [Debian — page de manuel slapadd](https://manpages.debian.org/trixie/slapd/slapadd.8.en.html)

L'installation, TLS, la sauvegarde et la restauration n'ont pas été testés sur Debian 13. Conserver les statuts **À revoir** et **À tester** jusqu'à validation sur une VM pilote.