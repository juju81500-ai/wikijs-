---
title: "fiche-simple-vm-debian-13-caddy-installer"
description: "Installer Caddy depuis le dépôt [[Glossary:APT]] officiel et confirmer la version et l'origine du paquet."
published: true
date: 2026-11-03T14:22:28Z
tags: ["debian13", "caddy", "apt", "installation", "signature"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# fiche-simple-vm-debian-13-caddy-installer.md

- **Environnement** : [[Glossary:VM]] Debian 13 Trixie, dépôt officiel Caddy stable
- **OS / Version** : Debian 13; Caddy stable
- **Catégorie** : serveur Web / installation
- **Tags** : `debian13`, `caddy`, `apt`, `installation`, `signature`

---

## Problème précis à résoudre

Installer Caddy depuis le dépôt [[Glossary:APT]] officiel et confirmer la version et l'origine du paquet.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis :
   ```bash
   sudo apt update
   sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl gnupg
   sudo install -d -m 0755 /usr/share/keyrings
   ```
   👉 Explication : outils nécessaires pour valider le dépôt signé.

2. Ajouter le dépôt officiel Caddy :
   ```bash
   curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
   curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
   sudo chmod o+r /usr/share/keyrings/caddy-stable-archive-keyring.gpg /etc/apt/sources.list.d/caddy-stable.list
   ```
   👉 Explication : clé et liste de dépôt publiées par l'éditeur.

3. Installer :
   ```bash
   sudo apt update
   apt-cache policy caddy
   sudo apt install caddy
   ```
   👉 Explication : relever la version et l'origine avant installation.

4. Vérifier :
   ```bash
   caddy version
   systemctl status caddy --no-pager
   ```
   👉 Explication : consigner la version; ne pas importer de binaire d'origine inconnue.

## 2. Production — Contrôles

Consigner la version, l'origine du paquet, le propriétaire du service et la cadence de mise à jour; tester toute montée de version sur une VM pilote.

## 3. Production — Sécurité

- Ne pas désactiver la vérification APT ni installer depuis un miroir non approuvé.
- Ne pas remplacer un trousseau existant sans examiner ses usages.
- Conserver le service sous son compte système et ses permissions par défaut.
- Ne pas publier de domaine ni ouvrir le pare-feu avant validation des proxys et certificats.

## Validation et retour arrière

- **Validation** : paquet, version et service vérifiés; aucun port public ne doit être ouvert par cette seule étape.
- **Retour arrière** : si la provenance est incorrecte, arrêter et appliquer la procédure de changement APT, sans supprimer des clés partagées.

## Si le problème n'est pas résolu

- [Caddy — installation](https://caddyserver.com/docs/install)
- [Caddy — Debian/Ubuntu](https://caddyserver.com/docs/install#debian-ubuntu-raspbian)
- [Guide complet Caddy Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/91-deploiement-caddy-debian-13#2-installer-depuis-le-depot-officiel)