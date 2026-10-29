---
title: "Fiche Simple - VM Debian 13 WireGuard Installer"
description: "Installer les outils WireGuard disponibles pour Debian 13."
published: true
date: 2026-10-29T20:35:43Z
tags: ["wireguard", "debian13", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T20:35:43Z
dateModified: 2026-10-29T20:35:43Z
---

# Fiche_Simple_-_VM_Debian_13_WireGuard_Installer

- **Environnement** : VM Debian 13 dédiée à WireGuard natif
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : WireGuard natif / installer
- **Tags** : `wireguard`, `debian13`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer les outils WireGuard disponibles pour Debian 13.

## 1. Hors-Production (Lab / Test / POC)

1. Actualiser les index et inspecter les candidats :
   ```bash
   sudo apt update
   apt-cache policy wireguard wireguard-tools
   ```
   👉 Explication : Confirmer paquets et origine avant installation.

2. Installer les paquets et vérifier l’outil :
   ```bash
   sudo apt install wireguard wireguard-tools
   wg --version
   ```
   👉 Explication : Le module noyau peut être fourni différemment selon le noyau Debian; confirmer sur l’hôte.

3. Vérifier les commandes et unités disponibles :
   ```bash
   command -v wg wg-quick
   systemctl list-unit-files | grep wg-quick
   ```
   👉 Explication : Ne pas activer l’interface avant d’avoir préparé sa configuration.

## 2. Production — Contrôles

Consigner version, noyau, origine des paquets et méthode de chargement du module.

## 3. Production — Sécurité

- Ne pas ajouter de dépôt tiers ou module hors noyau sans revue de maintenance.

## Validation et retour arrière

- **Validation** : wg et wg-quick sont disponibles et le modèle d’unité est identifié.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [WireGuard natif — documentation officielle](https://www.wireguard.com/quickstart/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/wireguard/fiche-simple-vm-debian-13-wireguard-configurer)