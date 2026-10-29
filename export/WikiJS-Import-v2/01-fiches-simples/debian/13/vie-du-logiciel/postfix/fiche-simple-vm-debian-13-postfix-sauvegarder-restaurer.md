---
title: "Fiche Simple - VM Debian 13 Postfix Sauvegarder Restaurer"
description: "Sauvegarder et restaurer la configuration et les données de Postfix (config, alias, file d'attente)."
published: true
date: 2026-10-29T21:07:31Z
tags: ["debian13", "postfix", "smtp", "messagerie", "sauvegarder-restaurer"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_Postfix_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Sauvegarder / restaurer
- **Tags** : `debian13`, `postfix`, `smtp`, `messagerie`, `sauvegarder-restaurer`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration et les données de Postfix (config, alias, file d'attente).

## 1. Hors-Production (Lab / Test / POC)

1. Exporter la configuration lisible :
   ```bash
   sudo postconf -n | sudo tee /root/postfix-postconf-n-$(date +%F).txt >/dev/null
   ```
   👉 Explication : trace des paramètres effectifs.

2. Archiver `/etc/postfix` :
   ```bash
   sudo tar -czpf /var/backups/postfix-etc-$(date +%F).tar.gz /etc/postfix /etc/aliases
   ```
   👉 Explication : inclut main.cf, master.cf, tables et alias. Les certificats Let's Encrypt (`/etc/letsencrypt`) se sauvegardent à part.

3. Sauvegarder la file d'attente à froid si nécessaire :
   ```bash
   sudo systemctl stop postfix
   sudo tar -czpf /var/backups/postfix-spool-$(date +%F).tar.gz /var/spool/postfix
   sudo systemctl start postfix
   ```
   👉 Explication : la file ne doit pas être copiée en cours d'écriture ; chiffrer l'archive car elle contient des courriers.

4. Restaurer la configuration :
   ```bash
   sudo systemctl stop postfix
   sudo tar -xzpf /var/backups/postfix-etc-DATE.tar.gz -C /
   sudo newaliases
   sudo postfix check
   sudo systemctl start postfix
   ```
   👉 Explication : `DATE` est à remplacer ; `newaliases` reconstruit la base d'alias.

5. Tester la restauration sur une VM de lab puis rejouer la recette :
   ```bash
   sudo postfix check && postconf -n | head
   ```
   👉 Explication : une sauvegarde non testée n'est pas une sauvegarde.

## 2. Production — Contrôles

Planifier la sauvegarde (cron ou [Restic — dépôt de sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot)), chiffrer les archives, tester la restauration périodiquement, conserver une copie hors site. Les boîtes aux lettres relèvent de Dovecot.

## 3. Production — Sécurité

- Archives en droits 0600 root, chiffrées si elles quittent le serveur.
- Ne pas sauvegarder de mots de passe en clair (les tables SASL sont gérées par Dovecot).

## Validation et retour arrière

- **Validation** : archive lisible (`tar -tzf`), restauration testée avec recette OK.
- **Retour arrière** : remettre l'archive précédente et redémarrer Postfix ; en dernier recours, restaurer le snapshot de VM.

## Si le problème n'est pas résolu

- [Postfix — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-prerequis-limites)
- [Postfix — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer)
- [Restic — dépôt de sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)