---
title: "Fiche Simple - VM Ubuntu 24.04 Zeek Installer"
description: "Installer Zeek 8.0 LTS sur VM Ubuntu Server 24.04 LTS."
published: true
date: 2026-10-29T20:59:32Z
tags: ["zeek", "ubuntu24.04", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:59:32Z
dateModified: 2026-10-29T20:59:32Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Zeek_Installer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Zeek
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Zeek / installation
- **Tags** : `zeek`, `ubuntu24.04`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Zeek 8.0 LTS sur VM Ubuntu Server 24.04 LTS.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et le répertoire de clés :
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl gnupg libcap2-bin
   sudo install -d -m 0755 /etc/apt/keyrings
   ```
   👉 Explication : Prépare l’import de la clé dans un keyring dédié.

2. Déclarer le dépôt OBS signé pour Ubuntu 24.04 :
   ```bash
   curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_24.04/Release.key | sudo gpg --dearmor --yes -o /etc/apt/keyrings/zeek-obs.gpg
   echo 'deb [signed-by=/etc/apt/keyrings/zeek-obs.gpg] https://download.opensuse.org/repositories/security:/zeek/xUbuntu_24.04/ /' | sudo tee /etc/apt/sources.list.d/zeek-obs.list
   ```
   👉 Explication : `signed-by` limite la confiance de la clé à ce dépôt. Vérifier l’empreinte de la clé auprès de la documentation officielle avant production.

3. Vérifier puis installer la ligne LTS :
   ```bash
   sudo apt update
   apt-cache policy zeek-8.0
   sudo apt install zeek-8.0
   /opt/zeek/bin/zeek --version
   /opt/zeek/bin/zeek -N Zeek::AF_Packet
   ```
   👉 Explication : Le candidat doit venir de `security:zeek`; la dernière commande doit lister AF_PACKET. Vérifier la ligne LTS publiée (8.0 au moment de l’écriture).

## 2. Production — Contrôles

Figer la ligne LTS (ne pas utiliser la ligne roulante en production) et consigner la source.

## 3. Production — Sécurité

- Vérifier l’origine du paquet ou de l’image avant installation.
- Pas de secret dans les dépôts ou les variables.

## Validation et retour arrière

- **Validation** : La commande `zeek --version` affiche la version 8.0.x attendue.
- **Retour arrière** : Désinstaller : `sudo apt remove zeek-8.0` puis supprimer `/etc/apt/sources.list.d/zeek-obs.list` et `/etc/apt/keyrings/zeek-obs.gpg`.

## Si le problème n’est pas résolu

- [Zeek — documentation officielle](https://docs.zeek.org/en/master/install.html)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-configurer)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/zeek/fiche-simple-vm-ubuntu-24-04-zeek-prerequis-limites)