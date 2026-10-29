---
title: "Fiche Simple - VM Debian 13 Dovecot Sauvegarder Restaurer"
description: "Sauvegarder et restaurer la configuration et les boîtes Maildir gérées par Dovecot."
published: true
date: 2026-10-29T21:07:31Z
tags: ["debian13", "dovecot", "imap", "messagerie", "sauvegarder-restaurer"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_Dovecot_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13; Dovecot depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Dovecot — Sauvegarder / restaurer
- **Tags** : `debian13`, `dovecot`, `imap`, `messagerie`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration et les boîtes Maildir gérées par Dovecot.

## 1. Hors-Production (Lab / Test / POC)

1. Archiver la configuration :
   ```bash
   sudo tar -czpf /var/backups/dovecot-etc-$(date +%F).tar.gz /etc/dovecot
   ```
   👉 Explication : contient réglages et listeners ; les certificats sont sauvegardés séparément.

2. Sauvegarder une boîte avec l'outil Dovecot :
   ```bash
   sudo doveadm backup -u UTILISATEUR_TEST maildir:/var/backups/mail/UTILISATEUR_TEST
   ```
   👉 Explication : synchronise la boîte vers un Maildir de sauvegarde en conservant les métadonnées IMAP (UIDs, drapeaux). Répéter par utilisateur ou boucler sur `doveadm user '*'`.

3. Sauvegarder l'ensemble des Maildir (alternative, à froid ou avec snapshot) :
   ```bash
   sudo rsync -aH --numeric-ids /home/ /var/backups/home-mail/ --include='*/' --include='Maildir/***' --exclude='*'
   ```
   👉 Explication : copie uniquement les Maildir de chaque compte ; chiffrer et externaliser la sauvegarde (fiche Restic du pack).

4. Restaurer une boîte :
   ```bash
   sudo doveadm backup -R -u UTILISATEUR_TEST maildir:/var/backups/mail/UTILISATEUR_TEST
   ```
   👉 Explication : l'option `-R` inverse le sens de synchronisation (sauvegarde vers boîte). Tester d'abord sur un compte de lab.

5. Restaurer la configuration :
   ```bash
   sudo systemctl stop dovecot
   sudo tar -xzpf /var/backups/dovecot-etc-DATE.tar.gz -C /
   sudo doveconf -n >/dev/null && sudo systemctl start dovecot
   ```
   👉 Explication : `DATE` est à remplacer.

## 2. Production — Contrôles

Planifier, chiffrer, externaliser (3-2-1), tester la restauration régulièrement et mesurer la durée de restauration.

## 3. Production — Sécurité

- Les sauvegardes contiennent des courriers : droits 0700, chiffrement obligatoire hors serveur.
- Ne pas sauvegarder de mot de passe en clair.

## Validation et retour arrière

- **Validation** : restauration d'une boîte de test avec nombre de messages identique (`doveadm mailbox status -u UTILISATEUR_TEST messages INBOX`).
- **Retour arrière** : remettre la sauvegarde précédente ou restaurer le snapshot de VM.

## Si le problème n'est pas résolu

- [Dovecot — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-prerequis-limites)
- [Dovecot — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/dovecot/fiche-simple-vm-debian-13-dovecot-installer)
- [Restic — dépôt de sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot)
- [Dovecot 2.4 — documentation officielle](https://doc.dovecot.org/main/)
- [Dovecot — migration 2.3 vers 2.4](https://doc.dovecot.org/main/installation/upgrade/2.3-to-2.4.html)