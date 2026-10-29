---
title: "Fiche Simple - VM Ubuntu 24.04 OpenLDAP Securiser"
description: "Limiter l'exposition d'OpenLDAP sur Ubuntu : pare-feu, accès anonyme et chiffrement."
published: true
date: 2026-10-29T21:01:38Z
tags: ["openldap", "ubuntu24-04", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:01:38Z
dateModified: 2026-10-29T21:01:38Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Securiser

- **Environnement** : VM Ubuntu 24.04 avec FQDN stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24.04 LTS Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / sécuriser
- **Tags** : `openldap`, `ubuntu24-04`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Limiter l'exposition d'OpenLDAP sur Ubuntu : pare-feu, accès anonyme et chiffrement.

## 1. Hors-Production (Lab / Test / POC)

1. Autoriser LDAP/LDAPS seulement depuis les réseaux clients :
   ```bash
   sudo ufw allow from ADMIN_NETWORK to any port 22 proto tcp
   sudo ufw allow from CLIENT_NETWORK to any port 389,636 proto tcp
   sudo ufw enable
   sudo ufw status verbose
   ```
   👉 Explication : ADMIN_NETWORK et CLIENT_NETWORK sont des CIDR approuvés (à remplacer); autoriser SSH avant l'activation d'ufw.

2. Vérifier l'accès anonyme :
   ```bash
   ldapsearch -x -H ldap://FQDN -b DOMAINE_BASE -s base
   ```
   👉 Explication : DOMAINE_BASE est le suffixe, par exemple dc=exemple,dc=org (à remplacer). Une lecture anonyme du contenu doit être refusée ou limitée selon la politique.

3. Contrôler les droits des fichiers :
   ```bash
   sudo ls -l /etc/ldap/tls /var/lib/ldap
   ```
   👉 Explication : Clé TLS en 0600; données lisibles par openldap seulement.

## 2. Production — Contrôles

Imposer TLS pour les liaisons authentifiées; journaliser via journalctl -u slapd.

## 3. Production — Sécurité

- Ne pas exposer 389/636 hors des réseaux approuvés.

## Validation et retour arrière

- **Validation** : Seuls les réseaux autorisés atteignent 389/636; accès anonyme conforme.
- **Retour arrière** : sudo ufw delete allow from CLIENT_NETWORK to any port 389,636 proto tcp (CLIENT_NETWORK à remplacer par la valeur utilisée).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-valider)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-openldap)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)