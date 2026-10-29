---
title: "Fiche Simple - VM Ubuntu 24.04 Snort Installer"
description: "Installer Snort 3 et libdaq depuis les sources officielles sur VM Ubuntu Server 24.04 LTS."
published: true
date: 2026-10-29T21:00:24Z
tags: ["snort", "ubuntu24.04", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T21:00:24Z
dateModified: 2026-10-29T21:00:24Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Snort_Installer

- **Environnement** : VM Ubuntu Server 24.04 LTS dédiée à Snort
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat); version des paquets à vérifier sur l’hôte
- **Catégorie** : Snort / installation
- **Tags** : `snort`, `ubuntu24.04`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Snort 3 et libdaq depuis les sources officielles sur VM Ubuntu Server 24.04 LTS.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils de compilation et dépendances :
   ```bash
   sudo apt update
   sudo apt install -y build-essential cmake git pkg-config flex bison libpcap-dev libpcre2-dev libdumbnet-dev libhwloc-dev libluajit-5.1-dev libssl-dev zlib1g-dev libunwind-dev liblzma-dev uuid-dev
   ```
   👉 Explication : Prépare la compilation. Les noms de paquets Ubuntu peuvent varier (par exemple libpcre2-dev contre libpcre3-dev selon la release de Snort 3); le fichier README de la release fait foi.

2. Choisir et consigner les versions à compiler :
   ```bash
   git ls-remote --tags https://github.com/snort3/libdaq.git | tail -n 5
   git ls-remote --tags https://github.com/snort3/snort3.git | tail -n 5
   ```
   👉 Explication : Liste les derniers tags publiés; choisir une release stable (non une branche de développement) et la consigner : VERSION_LIBDAQ et VERSION_SNORT3 sont à remplacer.

3. Compiler et installer libdaq :
   ```bash
   mkdir -p ~/build-snort && cd ~/build-snort
   git clone --branch VERSION_LIBDAQ --depth 1 https://github.com/snort3/libdaq.git
   cd libdaq && ./bootstrap && ./configure --prefix=/opt/snort3 && make -j"$(nproc)" && sudo make install
   ```
   👉 Explication : libdaq est la couche d’acquisition des paquets; installée sous `/opt/snort3` pour ne pas écraser de paquet système.

4. Compiler et installer Snort 3 :
   ```bash
   cd ~/build-snort
   git clone --branch VERSION_SNORT3 --depth 1 https://github.com/snort3/snort3.git
   cd snort3
   export PKG_CONFIG_PATH=/opt/snort3/lib/pkgconfig:$PKG_CONFIG_PATH
   ./configure_cmake.sh --prefix=/opt/snort3
   cd build && make -j"$(nproc)" && sudo make install
   /opt/snort3/bin/snort -V
   ```
   👉 Explication : Construit puis installe Snort; le script `configure_cmake.sh` est celui fourni par le dépôt (vérifier le README de la release). `snort -V` consigne la version.

5. Option : contrôler d’abord le paquet de la distribution.
   ```bash
   apt-cache policy snort snort3 2>/dev/null
   ```
   👉 Explication : Vérifie la disponibilité de paquets; n’installer un paquet que si la branche et la maintenance sont acceptables. Ne pas mélanger deux installations dans le PATH.

## 2. Production — Contrôles

Consigner versions, tags, empreintes éventuelles et date de compilation; compiler sur une machine de build si la politique l’exige.

## 3. Production — Sécurité

- Compiler sous un compte non privilégié; seul `make install` utilise sudo.
- Vérifier l’origine du dépôt Git (organisation snort3).

## Validation et retour arrière

- **Validation** : `/opt/snort3/bin/snort -V` affiche la version compilée.
- **Retour arrière** : Supprimer l’installation : `sudo rm -rf /opt/snort3` (après sauvegarde de la configuration) et le dossier `~/build-snort`.

## Si le problème n’est pas résolu

- [Snort — documentation officielle](https://www.snort.org/documents)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort)
- [Étape suivante du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-configurer)
- [Étape précédente du guide](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/snort/fiche-simple-vm-ubuntu-24-04-snort-prerequis-limites)