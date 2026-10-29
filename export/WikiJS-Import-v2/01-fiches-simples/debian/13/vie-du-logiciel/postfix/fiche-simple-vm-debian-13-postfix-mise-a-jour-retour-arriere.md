---
title: "Fiche Simple - VM Debian 13 Postfix Mise A Jour Retour Arriere"
description: "Mettre à jour Postfix par les dépôts Debian 13 avec un retour arrière maîtrisé."
published: true
date: 2026-10-29T21:07:31Z
tags: ["debian13", "postfix", "smtp", "messagerie", "mise-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Debian_13_Postfix_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13; Postfix depuis les dépôts de la distribution
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Postfix — Mise à jour et retour arrière
- **Tags** : `debian13`, `postfix`, `smtp`, `messagerie`, `mise-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour Postfix par les dépôts Debian 13 avec un retour arrière maîtrisé.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder avant toute mise à jour (voir la fiche Sauvegarder / restaurer) et prendre un snapshot de VM.
   👉 Explication : le retour arrière fiable repose sur le snapshot et l'archive de configuration.

2. Lister les mises à jour disponibles :
   ```bash
   sudo apt update
   apt list --upgradable 2>/dev/null | grep -i postfix
   ```
   👉 Explication : consulter les notes de version Debian/Postfix avant de continuer.

3. Mettre à jour uniquement Postfix :
   ```bash
   sudo apt install --only-upgrade postfix
   sudo postfix check
   sudo systemctl restart postfix
   ```
   👉 Explication : `apt` conserve vos fichiers de configuration ; répondre « conserver la version actuelle » à toute question dpkg sur `main.cf`.

4. Rejouer la recette (fiche Valider) :
   ```bash
   postconf mail_version
   sudo postqueue -p
   ```
   👉 Explication : confirme la version et l'absence de file bloquée.

5. Retour arrière d'un paquet (si l'ancienne version est encore disponible) :
   ```bash
   apt-cache policy postfix
   sudo apt install postfix=VERSION_PRECEDENTE
   ```
   👉 Explication : `VERSION_PRECEDENTE` est à remplacer par une version listée par `apt-cache policy` ; sinon restaurer le snapshot.

## 2. Production — Contrôles

Fenêtre de maintenance annoncée, file vide avant opération, vérification des notes de version, test après mise à jour, surveillance des journaux pendant 24 h.

## 3. Production — Sécurité

- N'appliquer que les paquets des dépôts Debian signés.
- Activer `unattended-upgrades` pour les correctifs de sécurité après validation en lab.

## Validation et retour arrière

- **Validation** : version attendue, recette OK, file d'attente saine.
- **Retour arrière** : restaurer le snapshot, ou réinstaller la version précédente puis rétablir `/etc/postfix` depuis l'archive.

## Si le problème n'est pas résolu

- [Postfix — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-prerequis-limites)
- [Postfix — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/postfix/fiche-simple-vm-debian-13-postfix-installer)
- [Postfix — documentation officielle](https://www.postfix.org/documentation.html)
- [Debian — Postfix](https://wiki.debian.org/Postfix)