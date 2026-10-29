---
title: "Fiche Simple - VM Ubuntu 24.04 Diagnostic Journalctl Erreurs"
description: "Identifier rapidement les services en échec et les erreurs noyau ou système d'un serveur Ubuntu Server 24.04 LTS, sur le démarrage courant comme sur le démarrage précédent, avec systemctl et journalctl."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[journalctl]", "[dmesg]", "[systemd]", "[troubleshooting]", "[logs]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Diagnostic_Journalctl_Erreurs

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - systemd 255 (journalctl, systemctl)
- **Catégorie** : Diagnostic / Analyse des erreurs système
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[journalctl]`, `[dmesg]`, `[systemd]`, `[troubleshooting]`, `[logs]`

## 🎯 Problème précis à résoudre
Identifier rapidement les services en échec et les erreurs noyau ou système d'un serveur Ubuntu Server 24.04 LTS, sur le démarrage courant comme sur le démarrage précédent, avec `systemctl` et `journalctl`.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les unités en échec :
   ```bash
   systemctl --failed --no-pager
   ```
   👉 *Explication : Affiche les services dont le démarrage a échoué ou qui se sont arrêtés anormalement.*
2. Lister les erreurs du démarrage courant :
   ```bash
   sudo journalctl -p err -b --no-pager
   ```
   👉 *Explication : `-p err` filtre les messages de niveau erreur et plus grave ; `-b` limite la recherche au démarrage en cours.*

## ⚡ 2. Production — Façon Simplifiée
1. Examiner le journal d'une unité précise :
   ```bash
   sudo journalctl -u <nom_du_service> -n 100 --no-pager
   systemctl status <nom_du_service> --no-pager
   ```
   👉 *Explication : `-n 100` affiche les cent dernières lignes ; `status` ajoute l'état, le code de sortie et la cause de l'échec.*
2. Examiner les erreurs noyau et matérielles avec `dmesg` :
   ```bash
   sudo dmesg -l err,crit,alert,emerg
   ```
   👉 *Explication : Sous Ubuntu 24.04, `kernel.dmesg_restrict` est souvent à `1` ; l'usage de `sudo` est donc nécessaire pour lire le tampon noyau.*

## 🔒 3. Production — Façon Sécurisée
1. Comparer avec le démarrage précédent pour distinguer une régression d'un problème ancien :
   ```bash
   sudo journalctl --list-boots
   sudo journalctl -b -1 -p err --no-pager
   ```
   👉 *Explication : `--list-boots` liste les identifiants de démarrage conservés ; l'index `-1` correspond au démarrage précédent. Les journaux ne sont disponibles que si le stockage est persistant.*
2. Consigner une période précise pour un rapport d'incident :
   ```bash
   sudo journalctl -p warning --since "2 hours ago" --until "now" --no-pager > /tmp/diagnostic_erreurs.txt
   ```
   👉 *Explication : Exporte les avertissements et erreurs dans un fichier temporaire à transmettre à l'équipe ; supprimer ensuite ce fichier de `/tmp` s'il contient des données sensibles.*

## ✅ Validation et retour arrière
- Après correction, `systemctl --failed --no-pager` doit afficher `0 loaded units listed` ou ne plus contenir le service concerné.
- Confirmer par `sudo journalctl -u <nom_du_service> --since "10 minutes ago" --no-pager` qu'aucune nouvelle erreur n'apparaît.
- Cette fiche est en lecture seule : aucun retour arrière n'est nécessaire, sauf la suppression du fichier exporté avec `rm /tmp/diagnostic_erreurs.txt`.