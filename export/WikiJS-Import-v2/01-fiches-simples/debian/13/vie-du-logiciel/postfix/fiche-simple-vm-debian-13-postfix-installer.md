---
title: "Fiche Simple - VM Debian 13 Postfix Installer"
description: "Installer Postfix (paquet Debian 13) en mode non interactif avec les outils de test."
published: true
date: 2026-10-29T21:07:31Z
tags: ["debian13", "postfix", "smtp", "messagerie", "installer"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_Postfix_Installer

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Installer
- **Tags** : `debian13`, `postfix`, `smtp`, `messagerie`, `installer`

---

## Problème précis à résoudre

Installer Postfix (paquet Debian 13) en mode non interactif avec les outils de test.

## 1. Hors-Production (Lab / Test / POC)

1. Pré-répondre aux questions debconf (type « Internet Site ») :
   ```bash
   echo "postfix postfix/main_mailer_type select Internet Site" | sudo debconf-set-selections
   echo "postfix postfix/mailname string MAIL.EXAMPLE.NET" | sudo debconf-set-selections
   ```
   👉 Explication : évite le dialogue interactif ; `MAIL.EXAMPLE.NET` est à remplacer par le FQDN réel.

2. Installer les paquets :
   ```bash
   sudo apt update
   sudo DEBIAN_FRONTEND=noninteractive apt install -y postfix bsd-mailx swaks
   ```
   👉 Explication : `bsd-mailx` fournit la commande `mail`, `swaks` est un client SMTP de test.

3. Activer et démarrer le service :
   ```bash
   sudo systemctl enable --now postfix
   systemctl is-active postfix
   ```
   👉 Explication : `postfix.service` est un service d'ensemble ; l'état doit être `active`.

4. Relever la version installée :
   ```bash
   postconf mail_version
   ```
   👉 Explication : à consigner dans la documentation d'exploitation.

## 2. Production — Contrôles

Vérifier que le paquet vient du dépôt Debian officiel (`apt-cache policy postfix`), que `exim4` n'est pas actif et que le service démarre au boot.

## 3. Production — Sécurité

- Installer uniquement depuis les dépôts Debian signés.
- Ne pas exposer le port 25 avant la configuration (fiche Configurer et Sécuriser).

## Validation et retour arrière

- **Validation** : `systemctl is-active postfix` renvoie `active` et `postconf mail_version` répond.
- **Retour arrière** : `sudo apt purge postfix bsd-mailx swaks` puis `sudo apt autoremove`, ou restauration du snapshot de VM.

## Si le problème n'est pas résolu

- [Postfix — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-prerequis-limites)
- [Postfix — Configurer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-configurer)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)