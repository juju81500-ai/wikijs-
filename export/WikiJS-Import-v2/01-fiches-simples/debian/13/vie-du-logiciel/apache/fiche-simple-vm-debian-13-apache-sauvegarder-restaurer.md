---
title: "Fiche Simple - VM Debian 13 Apache Sauvegarder Restaurer"
description: "Sauvegarder la configuration, les certificats et le contenu d'Apache et prouver la restauration."
published: true
date: 2026-10-29T20:32:41Z
tags: ["debian13", "apache", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:32:41Z
dateModified: 2026-10-29T20:32:41Z
---

# Fiche_Simple_-_VM_Debian_13_Apache_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Apache HTTP Server
- **Catégorie** : serveur Web / Apache / Sauvegarder et restaurer
- **Tags** : `debian13`, `apache`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder la configuration, les certificats et le contenu d'Apache et prouver la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver configuration, certificats et contenu :
   ```bash
   sudo install -d -m 0700 /var/backups/apache2
   sudo tar -czpf /var/backups/apache2/apache2-$(date +%F).tar.gz /etc/apache2 /etc/ssl/private /var/www
   ```
   👉 Explication : l'archive contient des clés privées : dossier en `0700` et copie externe chiffrée. Adapter les chemins si les certificats sont ailleurs.

2. Relire l'archive :
   ```bash
   sudo tar -tzf /var/backups/apache2/apache2-$(date +%F).tar.gz | head -20
   ```
   👉 Explication : contrôle de lisibilité.

3. Restaurer sur une VM pilote :
   ```bash
   sudo systemctl stop apache2
   sudo tar -xzpf /var/backups/apache2/apache2-DATE.tar.gz -C /
   sudo apache2ctl configtest && sudo systemctl start apache2
   ```
   👉 Explication : remplacer `DATE` par la date de l'archive (à remplacer).

## 2. Production — Contrôles

Planifier la sauvegarde, conserver plusieurs générations, chiffrer la copie hors site, tester une restauration à chaque changement majeur.

## 3. Production — Sécurité

- Chiffrer les copies contenant des clés privées.
- Ne pas stocker la sauvegarde sur le même disque.
- Limiter l'accès à `/var/backups/apache2`.

## Validation et retour arrière

- **Validation** : restauration testée : `configtest` OK et site accessible.
- **Retour arrière** : utiliser l'archive précédente sans écraser la dernière sauvegarde saine.

## Si le problème n'est pas résolu

- [Apache — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-valider)
- [Apache — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/apache/fiche-simple-vm-debian-13-apache-mettre-a-jour)
- [Guide complet Apache Debian 13](/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13)
- [Apache HTTP Server — documentation](https://httpd.apache.org/docs/2.4/)