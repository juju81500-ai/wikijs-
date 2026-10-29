---
title: "Fiche Simple - VM Debian 13 Centreon Script"
description: "Récupérer le script d'installation officiel Centreon et le lire avant de l'exécuter."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "centreon", "supervision", "script", "verification"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Centreon_Script.md

- **Environnement** : VM Debian 13 dédiée, serveur Centreon Central avec MariaDB locale
- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Catégorie** : supervision / installation
- **Tags** : `debian13`, `centreon`, `supervision`, `script`, `verification`

---

## Problème précis à résoudre

Récupérer le script d'installation officiel Centreon et le lire avant de l'exécuter.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo install -d -m 0700 /root/centreon-install
   cd /root/centreon-install
   ```
   👉 Explication : crée un dossier réservé à root pour le script.

2. Exécuter :
   ```bash
   sudo curl -fL https://download.centreon.com/26.10/unattended.sh -o unattended.sh
   ```
   👉 Explication : télécharge le script dans un fichier (jamais directement dans bash).

3. Exécuter :
   ```bash
   sudo less unattended.sh
   ```
   👉 Explication : lit le script : vérifier le domaine `download.centreon.com`, la version 26.10 et l'absence d'URL inattendue.

4. Exécuter :
   ```bash
   sudo bash unattended.sh -h
   ```
   👉 Explication : affiche les options proposées par cette version sans rien installer.

## 2. Production — Contrôles

Comparer le script aux documents officiels; s'il diffère ou contient des URL inattendues, arrêter et contacter le support Centreon.

## 3. Production — Sécurité

- Ne jamais exécuter un script distant par un tube vers `bash`.
- Télécharger uniquement en HTTPS depuis le domaine officiel.
- Conserver le script lu, dans un dossier à droits 0700.

## Validation et retour arrière

- **Validation** : le script est présent, lu, et l'aide s'affiche.
- **Retour arrière** : supprimer `/root/centreon-install` (rien n'est encore installé).

## Si le problème n'est pas résolu

- [Centreon — installation unattended](https://docs.centreon.com/docs/installation/installation-of-a-central-server/unattended-install-central/)
- [Guide complet Déployer Centreon 26.10 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13#2-telecharger-et-controler-le-script-officiel)