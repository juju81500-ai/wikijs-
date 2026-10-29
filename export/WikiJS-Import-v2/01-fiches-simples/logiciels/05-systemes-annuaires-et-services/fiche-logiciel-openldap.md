---
title: "OpenLDAP"
description: "Couvert — OpenLDAP 2.6 (slapd) sur Debian 13 et Ubuntu 24.04. Rocky Linux 9 non couvert : le serveur OpenLDAP n’y est pas fourni dans les dépôts de base (à vérifier). Guide non testé; réplication et haute disponibilité non couvertes."
published: true
date: 2026-10-29T21:02:52Z
tags: ["logiciel", "05-Systemes-annuaires-et-services", "couvert"]
editor: markdown
dateCreated: 2026-10-29T21:02:52Z
dateModified: 2026-10-29T21:02:52Z
---

# 📄 OpenLDAP

- **Catégorie** : Systèmes, annuaires et services
- **Plateforme** : Linux
- **Produit (matrice)** : OpenLDAP
- **Statut dans le pack** : Couvert
- **Tags** : `logiciel`, `05-Systemes-annuaires-et-services`, `couvert`

## 📚 Couverture dans le pack

Couvert — OpenLDAP 2.6 (slapd) sur Debian 13 et Ubuntu 24.04. Rocky Linux 9 non couvert : le serveur OpenLDAP n’y est pas fourni dans les dépôts de base (à vérifier). Guide non testé; réplication et haute disponibilité non couvertes.

Fiches simples du guide : [cadrer le pilote OpenLDAP](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-cadrer), [installer slapd et les utilitaires LDAP](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-installer), [vérifier la configuration OLC](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-verifier-olc), [créer les unités organisationnelles](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-creer-ou), [configurer TLS](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-configurer-tls), [sauvegarder OpenLDAP](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-sauvegarder), [tester la restauration sur une VM isolée](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-restaurer-test), [valider LDAP, TLS et les flux](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-valider), [préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-retour-arriere)., [Ubuntu 24.04 — prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-prerequis-limites), [Ubuntu 24.04 — installation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-installer), [Ubuntu 24.04 — configuration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-configurer), [Ubuntu 24.04 — sécurisation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-securiser), [Ubuntu 24.04 — validation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-valider), [Ubuntu 24.04 — sauvegarde/restauration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-sauvegarder-restaurer), [Ubuntu 24.04 — mise à jour/retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/openldap/fiche-simple-vm-ubuntu-24-04-openldap-mise-a-jour-retour-arriere)

## 🧭 Utilisation

Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Fiche de repère : [OpenLDAP](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-simple-openldap). Fiches simples des étapes : [cadrage](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-cadrer), [installation](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-installer), [configuration OLC](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-verifier-olc), [structure OU](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-creer-ou), [TLS](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-configurer-tls), [sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-sauvegarder), [restauration de test](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-restaurer-test), [validation](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-valider) et [retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/openldap/fiche-simple-vm-debian-13-openldap-retour-arriere).