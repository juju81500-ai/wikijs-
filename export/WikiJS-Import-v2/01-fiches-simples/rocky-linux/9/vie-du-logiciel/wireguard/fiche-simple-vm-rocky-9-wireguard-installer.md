---
title: "Fiche Simple - VM Rocky 9 WireGuard Installer"
description: "Installer WireGuard natif sans activer d'interface non configurée."
published: true
date: 2026-10-29T21:01:00Z
tags: ["wireguard", "rocky9", "vie-du-logiciel", "installer"]
editor: markdown
dateCreated: 2026-10-29T21:01:00Z
dateModified: 2026-10-29T21:01:00Z
---

# Fiche_Simple_-_VM_Rocky_9_WireGuard_Installer

- **Environnement** : VM Rocky Linux 9 dédiée à un serveur WireGuard natif
- **OS / Version** : Rocky Linux 9; wireguard-tools issu d'EPEL, module noyau à vérifier sur l'hôte
- **Catégorie** : WireGuard natif / installer
- **Tags** : `wireguard`, `rocky9`, `vie-du-logiciel`, `installer`

---

## Problème précis à résoudre

Installer WireGuard natif sans activer d'interface non configurée.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils :
   ```bash
   sudo dnf install epel-release
   dnf info wireguard-tools
   sudo dnf install wireguard-tools
   sudo modprobe wireguard
   lsmod | grep wireguard
   wg --version
   ```
   👉 Explication : wireguard-tools provient d'EPEL (dépôt communautaire à faire approuver). Le module doit se charger avec le noyau fourni : si modprobe échoue, ne pas installer de module tiers sans validation et consulter la documentation Rocky/RHEL de la version.

2. Contrôler les unités fournies :
   ```bash
   systemctl list-unit-files | grep -i wg-quick
   ```
   👉 Explication : Le modèle wg-quick@.service (NOM_INTERFACE = nom de wg0.conf) pilote chaque interface; vérifier le nom sur l'hôte.

## 2. Production — Contrôles

Consigner versions et origine des paquets.

## 3. Production — Sécurité

- Ne pas activer d'interface ni ouvrir de port avant validation de la configuration.

## Validation et retour arrière

- **Validation** : wg --version répond.
- **Retour arrière** : Désinstaller : sudo dnf remove wireguard-tools (aucune configuration créée).

## Si le problème n'est pas résolu

- [Étape suivante du guide](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/wireguard/fiche-simple-vm-rocky-9-wireguard-configurer)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard)
- [WireGuard — installation officielle](https://www.wireguard.com/install/)
- [WireGuard — démarrage rapide](https://www.wireguard.com/quickstart/)