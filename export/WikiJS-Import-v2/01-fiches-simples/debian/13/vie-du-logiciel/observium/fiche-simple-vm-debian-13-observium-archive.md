---
title: "Fiche Simple - VM Debian 13 Observium Archive"
description: "Télécharger l'archive officielle, la contrôler et l'extraire dans /opt/observium."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "observium", "archive", "checksum"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Observium_Archive.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / installation
- **Tags** : `debian13`, `observium`, `archive`, `checksum`

---

## Problème précis à résoudre

Télécharger l'archive officielle, la contrôler et l'extraire dans /opt/observium.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un dossier de travail et télécharger l'archive via HTTPS :
   ```bash
   sudo install -d -o root -g root -m 0755 /opt/observium-stage
   cd /opt/observium-stage
   sudo curl --fail --location --proto '=https' --tlsv1.2 -o observium-community-latest.tar.gz https://www.observium.org/observium-community-latest.tar.gz
   ```
   👉 Explication : la ressource `community-latest` est mobile; on consigne donc date et version.

2. Calculer l'empreinte et examiner le contenu avant extraction :
   ```bash
   sha256sum observium-community-latest.tar.gz
   tar -tzf observium-community-latest.tar.gz | head
   ```
   👉 Explication : l'empreinte locale sert à la reproductibilité (ce n'est pas une signature de l'éditeur); la liste doit montrer un dossier `observium/`.

3. Vérifier que /opt/observium n'existe pas, puis extraire :
   ```bash
   test ! -e /opt/observium && sudo tar -xzf observium-community-latest.tar.gz -C /opt
   sudo chown -R root:root /opt/observium
   ```
   👉 Explication : si le dossier existe déjà, arrêter et suivre la procédure de mise à niveau au lieu d'écraser.

## 2. Production — Contrôles

Conserver la version et l'empreinte dans le dossier de changement.

## 3. Production — Sécurité

- Ne pas lancer de script téléchargé directement.
- Télécharger en HTTPS avec TLS 1.2 minimum.

## Validation et retour arrière

- **Validation** : `ls /opt/observium` montre `config.php.default`, `discovery.php` et `poller.php`.
- **Retour arrière** : `sudo rm -r /opt/observium` uniquement si installation neuve sans données, après sauvegarde.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 3](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13#3-recuperer-larchive-community)