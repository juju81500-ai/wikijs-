---
title: "Fiche Simple - VM Debian 13 Bareos Installer Paquets"
description: "Installer les composants Bareos depuis un dépôt vérifié sans exécuter aveuglément un script téléchargé."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "bareos", "apt", "postgresql", "installation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Bareos_Installer_Paquets.md

- **Environnement** : Debian 13 Trixie; dépôt officiel Bareos 25 Community
- **OS / Version** : Debian 13; Bareos 25 et PostgreSQL
- **Catégorie** : sauvegarde réseau / installation
- **Tags** : `debian13`, `bareos`, `apt`, `postgresql`, `installation`

---

## Problème précis à résoudre

Installer les composants Bareos depuis un dépôt vérifié sans exécuter aveuglément un script téléchargé.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis :
   ```bash
   sudo apt update
   sudo apt install -y ca-certificates curl gnupg
   ```
   👉 Explication : outils pour récupérer le dépôt de façon sûre.

2. Télécharger le script de dépôt dans un fichier, le lire avant exécution :
   ```bash
   cd /tmp
   curl -fsSLO URL_OFFICIELLE_DU_SCRIPT_DEPOT_BAREOS
   less add_bareos_repositories.sh
   ```
   👉 Explication : remplacer l'URL par celle de la documentation officielle (Bareos 25, compatible Trixie); jamais de `curl | sh`.

3. Exécuter le script après relecture, puis installer PostgreSQL et Bareos :
   ```bash
   sudo bash ./add_bareos_repositories.sh
   sudo apt update
   apt-cache policy bareos
   sudo apt install postgresql bareos
   ```
   👉 Explication : le méta-paquet `bareos` installe le serveur complet; vérifier version et origine avec `apt-cache policy`.

4. Vérifier :
   ```bash
   dpkg -l | grep -i bareos
   ```
   👉 Explication : tous les composants doivent avoir la même version majeure.

## 2. Production — Contrôles

Consigner le dépôt, versions, architecture des composants, fenêtre de mise à jour et procédure de mise à niveau compatible.

## 3. Production — Sécurité

- Ne pas exécuter en root un script réseau non inspecté.
- Ne pas désactiver APT Secure ni utiliser une clé d'origine incertaine.
- Ne pas installer les paquets si la version candidate ou le dépôt n'est pas celui attendu.
- Ne pas purger les paquets PostgreSQL ou Bareos en présence de données sans sauvegarde vérifiée.

## Validation et retour arrière

- **Validation** : origine APT, versions, composants et catalogue choisis explicitement.
- **Retour arrière** : conserver les versions et dépôts précédents; stopper si l'installateur propose de remplacer des données existantes.

## Si le problème n'est pas résolu

- [Bareos 25 — installation serveur](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareos.html)
- [Debian — paquet PostgreSQL](https://packages.debian.org/trixie/postgresql)
- [Guide complet Bareos Debian 13](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13#2-installer-les-paquets-debian-13)