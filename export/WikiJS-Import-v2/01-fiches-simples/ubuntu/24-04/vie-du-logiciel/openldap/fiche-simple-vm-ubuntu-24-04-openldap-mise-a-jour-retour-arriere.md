---
title: "Fiche Simple - VM Ubuntu 24.04 OpenLDAP Mise A Jour Retour Arriere"
description: "Mettre à jour slapd avec retour arrière."
published: true
date: 2026-10-29T21:01:38Z
tags: ["openldap", "ubuntu24-04", "vie-du-logiciel", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T21:01:38Z
dateModified: 2026-10-29T21:01:38Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_OpenLDAP_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Ubuntu 24.04 avec FQDN stable, serveur OpenLDAP (slapd)
- **OS / Version** : Ubuntu 24.04 LTS Noble; slapd 2.6 des dépôts, version à vérifier
- **Catégorie** : annuaire OpenLDAP / mise à jour / retour arrière
- **Tags** : `openldap`, `ubuntu24-04`, `vie-du-logiciel`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour slapd avec retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder (voir la fiche précédente) puis noter la version :
   ```bash
   slapd -VV 2>&1 | head -n 3
   apt-cache policy slapd
   ```
   👉 Explication : La version de référence sert au retour arrière.

2. Mettre à jour uniquement les paquets OpenLDAP :
   ```bash
   sudo apt update
   sudo apt install --only-upgrade slapd ldap-utils
   ```
   👉 Explication : Conserver les fichiers de configuration locaux si dpkg pose la question.

3. Rejouer la recette puis, en cas d'échec, revenir en arrière :
   ```bash
   sudo systemctl status slapd --no-pager
   sudo apt install slapd=VERSION_PRECEDENTE
   ```
   👉 Explication : VERSION_PRECEDENTE est la version notée (à remplacer) et doit rester disponible dans un dépôt approuvé; sinon restaurer le snapshot puis les LDIF. Voir aussi [la fiche Debian Retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-retour-arriere).

## 2. Production — Contrôles

Prendre un snapshot de la VM et prévenir les consommateurs de l'annuaire.

## 3. Production — Sécurité

- Dépôts approuvés uniquement.

## Validation et retour arrière

- **Validation** : slapd actif, version attendue, recette réussie.
- **Retour arrière** : Snapshot de la VM, ou version précédente de slapd puis restauration des LDIF.

## Si le problème n'est pas résolu

- [Première étape du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-prerequis-limites)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-openldap)
- [Ubuntu Server — OpenLDAP (documentation officielle)](https://documentation.ubuntu.com/server/how-to/openldap/install-openldap/)
- [OpenLDAP — guide administrateur 2.6](https://www.openldap.org/doc/admin26/)