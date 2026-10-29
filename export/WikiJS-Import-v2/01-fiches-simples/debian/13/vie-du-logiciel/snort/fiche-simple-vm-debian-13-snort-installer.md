---
title: "Fiche Simple - VM Debian 13 Snort Installer"
description: "Installer Snort depuis un dépôt approuvé et identifier la branche livrée."
published: true
date: 2026-10-29T20:35:43Z
tags: ["snort", "debian13", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_Snort_Installer

- **Environnement** : VM Debian 13 dédiée à Snort IDS passif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : Snort IDS passif / installer
- **Tags** : `snort`, `debian13`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer Snort depuis un dépôt approuvé et identifier la branche livrée.

## 1. Hors-Production (Lab / Test / POC)

1. Inspecter la version candidate :
   ```bash
   sudo apt update
   apt-cache policy snort
   ```
   👉 Explication : Confirmer origine, branche, maintenance et dépendances avant installation.

2. Installer puis relever la version :
   ```bash
   sudo apt install snort
   snort -V
   ```
   👉 Explication : Le paquet peut demander des paramètres de réseau; confirmer qu’ils correspondent au plan approuvé.

3. Lister les configurations livrées :
   ```bash
   dpkg-query -L snort | grep -E "snort.*(conf|lua)"
   ```
   👉 Explication : La configuration peut être snort.conf ou snort.lua selon la branche; confirmer le chemin réel.

## 2. Production — Contrôles

Consigner version, origine du paquet, fichier de configuration et unité systemd si elle existe.

## 3. Production — Sécurité

- Ne pas installer de règles depuis une source non vérifiée; ne pas exposer un service avant recette.

## Validation et retour arrière

- **Validation** : Version et chemin de configuration identifiés; installation réussie.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [Snort IDS passif — documentation officielle](https://www.snort.org/documents)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/snort/fiche-simple-vm-debian-13-snort-configurer)