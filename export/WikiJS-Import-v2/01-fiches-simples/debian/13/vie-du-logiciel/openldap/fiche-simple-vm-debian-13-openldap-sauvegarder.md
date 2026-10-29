---
title: "Fiche Simple - VM Debian 13 OpenLDAP Sauvegarder"
description: "Exporter configuration et données LDAP en LDIF et protéger les fichiers hors hôte."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "openldap", "slapcat", "backup", "ldif"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OpenLDAP_Sauvegarder.md

- **Environnement** : OpenLDAP Debian 13 avec accès privilégié local et dépôt de sauvegarde chiffré
- **OS / Version** : Debian 13; slapd 2.6
- **Catégorie** : annuaire / sauvegarde
- **Tags** : `debian13`, `openldap`, `slapcat`, `backup`, `ldif`

---

## Problème précis à résoudre

Exporter configuration et données LDAP en LDIF et protéger les fichiers hors hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le dossier protégé :
   ```bash
   sudo install -d -m 0700 /var/backups/ldap
   ```
   👉 Explication : les LDIF contiennent des condensats de mots de passe; accès `root` seulement.

2. Exporter configuration et données :
   ```bash
   sudo slapcat -n 0 -l /var/backups/ldap/config-$(date +%F).ldif
   sudo slapcat -n 1 -l /var/backups/ldap/data-$(date +%F).ldif
   ```
   👉 Explication : `slapcat` lit la base sans la modifier; `-n 0` = configuration, `-n 1` = données.

3. Contrôler les fichiers :
   ```bash
   sudo ls -l /var/backups/ldap
   sudo grep -c '^dn:' /var/backups/ldap/data-$(date +%F).ldif
   ```
   👉 Explication : les fichiers ne doivent pas être vides; noter le nombre d'entrées pour la comparaison à la restauration.

4. Sauvegarder séparément les certificats et clés TLS, puis copier le tout chiffré hors hôte :
   ```bash
   sudo tar -czf /var/backups/ldap/tls-$(date +%F).tar.gz /etc/ldap/tls
   ```
   👉 Explication : la clé est un secret; chiffrer l'archive avant transfert.

## 2. Production — Contrôles

Définir fréquence, RPO/RTO, rétention, chiffrement, transfert hors site, destinataires et test périodique de restauration.

## 3. Production — Sécurité

- Les LDIF peuvent contenir des condensats de mots de passe et des données personnelles; les traiter comme des secrets.
- Ne pas laisser les fichiers de sauvegarde dans un répertoire partagé ou accessible aux utilisateurs.
- Ne pas considérer la réussite de `slapcat` comme preuve de restaurabilité.
- Conserver les clés TLS séparément et contrôler leurs accès.

## Validation et retour arrière

- **Validation** : exports de configuration et données présents, chiffrés hors machine, contrôle d'accès vérifié.
- **Retour arrière** : si transfert ou chiffrement échoue, conserver l'original sous accès restreint et ouvrir un incident; ne pas le supprimer avant copie vérifiée.

## Si le problème n'est pas résolu

- [OpenLDAP — maintenance et sauvegarde](https://www.openldap.org/doc/admin26/maintenance.html)
- [Debian — slapcat](https://manpages.debian.org/trixie/slapd/slapcat.8.en.html)
- [Guide complet OpenLDAP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13#6-sauvegarder)