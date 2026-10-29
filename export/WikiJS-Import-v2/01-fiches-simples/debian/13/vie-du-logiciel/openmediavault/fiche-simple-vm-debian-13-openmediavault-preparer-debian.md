---
title: "Fiche Simple - VM Debian 13 OpenMediaVault Preparer Debian"
description: "Préparer une Debian 13 minimale, à jour, avec réseau fixe et DNS fonctionnel."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "openmediavault", "reseau", "dns"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_OpenMediaVault_Preparer_Debian.md

- **Environnement** : OpenMediaVault 8 sur Debian 13 minimal
- **OS / Version** : Debian 13; OpenMediaVault 8.0 Synchrony
- **Catégorie** : stockage / préparation système
- **Tags** : `debian13`, `openmediavault`, `debian13`, `reseau`, `dns`

---

## Problème précis à résoudre

Préparer une Debian 13 minimale, à jour, avec réseau fixe et DNS fonctionnel.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler nom d'hôte, adresse et route :
   ```bash
   sudo hostnamectl
   sudo ip -br address
   sudo ip route
   ```
   👉 Explication : Relève la configuration réseau avant qu'OMV ne la reprenne.

2. Valider la résolution DNS du dépôt OMV :
   ```bash
   sudo getent hosts packages.openmediavault.org
   ```
   👉 Explication : Sans DNS, l'installation échouera.

3. Mettre à jour puis redémarrer :
   ```bash
   sudo apt update
   sudo apt full-upgrade
   sudo reboot
   ```
   👉 Explication : Après redémarrage, confirmer que l'administration locale fonctionne et que le système démarre sur le disque prévu.

## 2. Production — Contrôles

Installer Debian sans environnement graphique ni serveur Web; relever les numéros de série des disques.

## 3. Production — Sécurité

- Ne pas initialiser ni effacer le disque système dans OMV.

## Validation et retour arrière

- **Validation** : système à jour, nom d'hôte, IP et DNS corrects.
- **Retour arrière** : restaurer l'instantané ou la sauvegarde de la VM avant mise à jour.

## Si le problème n'est pas résolu

- [OpenMediaVault — installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html)
- [OpenMediaVault — prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html)
- [Guide complet OpenMediaVault Debian 13](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13#2-preparer-debian-13)