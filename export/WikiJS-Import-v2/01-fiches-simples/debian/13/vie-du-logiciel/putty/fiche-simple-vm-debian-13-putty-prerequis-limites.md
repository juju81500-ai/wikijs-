---
title: "Fiche Simple - VM Debian 13 PuTTY Prerequis Limites"
description: "Savoir ce que fournit putty-tools sur Debian 13 et ses limites par rapport à OpenSSH."
published: true
date: 2026-10-29T21:24:09Z
tags: ["putty", "putty-tools", "plink", "puttygen", "ssh", "prerequis"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_Debian_13_PuTTY_Prerequis_Limites

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH
- **Tags** : `putty`, `putty-tools`, `plink`, `puttygen`, `ssh`, `prerequis`

---

## Problème précis à résoudre

Savoir ce que fournit `putty-tools` sur Debian 13 et ses limites par rapport à OpenSSH.

## 1. Hors-Production (Lab / Test / POC)

1. Lire la description du paquet :
   ```bash
   apt show putty-tools
   ```
   👉 Explication : le paquet fournit en ligne de commande `plink`, `pscp`, `psftp`, `psusan` et `puttygen` ; l'interface graphique PuTTY est dans le paquet distinct `putty`.
2. Vérifier l'accès aux dépôts Debian :
   ```bash
   sudo apt update
   ```
   👉 Explication : nécessite un compte avec `sudo` et un accès réseau aux dépôts.
3. Noter que `ssh` (OpenSSH) est le client natif de Debian ; PuTTY sert surtout à manipuler des clés `.ppk` ou à interopérer avec des postes Windows.
   👉 Explication : ne pas installer deux outils pour le même besoin sans raison.

## 2. Production — Contrôles

- Version : celle du dépôt Debian 13 ; vérifier la version publiée avec `apt policy putty-tools`.

## 3. Production — Sécurité

- Installer uniquement depuis les dépôts Debian officiels signés.

## Validation et retour arrière

- **Validation** : périmètre et besoin documentés. **Retour arrière** : sans objet (lecture seule).

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Debian — paquet putty-tools](https://packages.debian.org/trixie/putty-tools)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)