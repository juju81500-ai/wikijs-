---
title: "Fiche Simple - VM Debian 13 OpenLDAP Configurer TLS"
description: "Configurer TLS pour protéger les échanges LDAP, sans exposer ou rendre illisible la clé privée."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "openldap", "tls", "ldaps", "starttls", "certificat"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Configurer_TLS.md

- **Environnement** : VM Debian 13 avec FQDN stable et certificat provisionné par l'organisation
- **OS / Version** : Debian 13; OpenLDAP 2.6
- **Catégorie** : annuaire / chiffrement TLS
- **Tags** : `debian13`, `openldap`, `tls`, `ldaps`, `starttls`, `certificat`

---

## Problème précis à résoudre

Configurer TLS pour protéger les échanges LDAP, sans exposer ou rendre illisible la clé privée.

## 1. Hors-Production (Lab / Test / POC)

1. Copier la chaîne et la clé du certificat (CN/SAN = FQDN des clients) :
   ```bash
   sudo install -d -m 0755 /etc/ldap/tls
   sudo install -m 0644 ca.crt ldap.crt /etc/ldap/tls/
   sudo install -m 0600 -o openldap -g openldap ldap.key /etc/ldap/tls/
   ls -l /etc/ldap/tls
   ```
   👉 Explication : la clé doit appartenir à `openldap` avec le mode `0600`.

2. Sauvegarder la configuration avant modification :
   ```bash
   sudo slapcat -n 0 -l /var/backups/ldap/config-avant-tls-$(date +%F).ldif
   ```
   👉 Explication : permet le retour arrière; créer le dossier `/var/backups/ldap` avec `install -d -m 0700` au besoin.

3. Créer `/root/tls.ldif` :
   ```bash
   sudo tee /root/tls.ldif >/dev/null <<'EOF'
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
   EOF
   sudo ldapmodify -Q -Y EXTERNAL -H ldapi:/// -f /root/tls.ldif
   ```
   👉 Explication : une valeur erronée peut empêcher le démarrage; garder la session ouverte et conserver le LDIF inverse.

4. Pour LDAPS, modifier `/etc/default/slapd` :
   ```bash
   sudo sed -i 's|^SLAPD_SERVICES=.*|SLAPD_SERVICES="ldap:/// ldapi:/// ldaps:///"|' /etc/default/slapd
   sudo systemctl restart slapd
   sudo ss -ltnp | grep -E ':(389|636)\b'
   ```
   👉 Explication : `636` doit écouter; imposer ensuite le chiffrement (`olcSecurity`) seulement après validation STARTTLS/LDAPS.

## 2. Production — Contrôles

Documenter émission, renouvellement, chaîne CA, FQDN, clients, listener, ports, dépendances et procédure de changement de TLS.

## 3. Production — Sécurité

- Ne pas copier la clé privée dans le wiki ou un dépôt; garder les permissions strictes.
- Ne pas ouvrir TCP/389 ou TCP/636 avant validation et filtrage client.
- Ne pas imposer TLS avant que tous les clients requis aient été testés.
- Garder un LDIF inverse et une session d'administration locale pendant le changement.

## Validation et retour arrière

- **Validation** : validation du certificat côté client, TLS établi, listener seulement sur interfaces prévues.
- **Retour arrière** : restaurer les anciennes valeurs via `ldapmodify`/LDIF inverse; si slapd ne démarre plus, utiliser l'accès console et le snapshot approuvé.

## Si le problème n'est pas résolu

- [OpenLDAP — TLS](https://www.openldap.org/doc/admin26/tls.html)
- [OpenLDAP — configuration OLC](https://www.openldap.org/doc/admin26/slapdconf2.html)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#5-activer-tls)