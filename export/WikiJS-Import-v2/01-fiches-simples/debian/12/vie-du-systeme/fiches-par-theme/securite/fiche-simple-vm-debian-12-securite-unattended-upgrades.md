---
title: "VM_Debian_12_Securite_Unattended-Upgrades"
description: "Automatiser l'installation des correctifs de sécurité Debian 12 via unattended-upgrades, limiter l'automatisation aux mises à jour de sécurité et empêcher tout redémarrage automatique non planifié."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[unattended-upgrades]", "[apt]", "[patch]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Securite_Unattended-Upgrades.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Maintenance / Correctifs automatiques
- **Tags** : `[debian12]`, `[debian-family]`, `[unattended-upgrades]`, `[apt]`, `[patch]`, `[hardening]`

## 🎯 Problème précis à résoudre
Automatiser l'installation des correctifs de sécurité Debian 12 via `unattended-upgrades`, limiter l'automatisation aux mises à jour de sécurité et empêcher tout redémarrage automatique non planifié.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du mécanisme de mises à jour automatiques :
   `sudo apt-get update && sudo apt-get install -y unattended-upgrades apt-listchanges`
   👉 Explication : Installe `unattended-upgrades` et `apt-listchanges`, qui affiche les changements des paquets avant leur installation.
2. Simulation d'une exécution sans installation :
   `sudo unattended-upgrade --dry-run --debug`
   👉 Explication : Montre les paquets qui seraient mis à jour sans rien modifier sur la machine.
3. Contrôle des timers APT :
   `systemctl list-timers 'apt-daily*'`
   👉 Explication : Vérifie que les timers `apt-daily` et `apt-daily-upgrade` sont planifiés.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation des tâches périodiques APT :
   `sudoedit /etc/apt/apt.conf.d/20auto-upgrades`
   👉 Explication : Définir `APT::Periodic::Update-Package-Lists "1";` et `APT::Periodic::Unattended-Upgrade "1";` pour activer la mise à jour de la liste des paquets et l'application quotidienne.
2. Restriction aux correctifs de sécurité :
   `sudoedit /etc/apt/apt.conf.d/50unattended-upgrades`
   👉 Explication : Vérifier que seule l'origine `-security` de Debian figure dans `Allowed-Origins` (ex. `"origin=Debian,codename=${distro_codename}-security,label=Debian-Security";`).

---

## 🔒 3. Production — Façon Sécurisée (Redémarrage contrôlé & Journal d'audit)
1. Interdiction du redémarrage automatique :
   `sudoedit /etc/apt/apt.conf.d/50unattended-upgrades`
   👉 Explication : Positionner `Unattended-Upgrade::Automatic-Reboot "false";`. Les noyaux mis à jour seront effectifs au redémarrage planifié (fiche de test de redémarrage).
2. Vérification de la configuration APT effective :
   `apt-config dump | grep -i 'APT::Periodic'`
   👉 Explication : Affiche les valeurs réellement lues par APT, après fusion de tous les fichiers de `/etc/apt/apt.conf.d/`.
3. Relecture du journal des mises à jour automatiques :
   `sudo tail -n 50 /var/log/unattended-upgrades/unattended-upgrades.log`
   👉 Explication : Confirme les paquets installés automatiquement et les erreurs éventuelles, à consulter lors de l'audit mensuel.