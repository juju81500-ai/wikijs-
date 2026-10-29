---
title: "Fiche Simple - VM Rocky 9 Systeme Test Redemarrage"
description: "Vérifier qu'un serveur Rocky Linux 9 redémarre proprement et que les montages, le réseau, l'heure, SELinux, le pare-feu et les services métiers reviennent sans intervention manuelle."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[rocky9]", "[rhel9]", "[reboot]", "[persistance]", "[systemd]", "[validation]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Rocky_9_Systeme_Test_Redemarrage.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 avec systemd
- **Catégorie** : Système & Services / Validation de persistance
- **Tags** : `[rocky9]`, `[rhel9]`, `[reboot]`, `[persistance]`, `[systemd]`, `[validation]`

## 🎯 Problème précis à résoudre
Vérifier qu'un serveur Rocky Linux 9 redémarre proprement et que les montages, le réseau, l'heure, SELinux, le pare-feu et les services métiers reviennent sans intervention manuelle.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Noter l'état avant redémarrage :
   ```bash
   systemctl --failed --no-pager
   systemctl list-unit-files --state=enabled --no-pager
   ```
   👉 Explication : Les unités en échec sont à corriger avant le test. La liste des services activés sert de référence pour la comparaison après redémarrage.

2. Redémarrer la machine :
   ```bash
   sudo systemctl reboot
   ```
   👉 Explication : Demande un redémarrage propre à systemd. Prévenir les utilisateurs et garder un accès console disponible en cas de blocage.

3. Contrôler l'état après redémarrage :
   ```bash
   uptime
   systemctl --failed --no-pager
   sudo findmnt --verify --verbose
   ```
   👉 Explication : `uptime` confirme la date du dernier démarrage. Aucun échec ne doit apparaître et les montages doivent être valides.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier le réseau et l'heure :
   ```bash
   ip -br address
   nmcli -t -f NAME,DEVICE connection show --active
   timedatectl status
   ```
   👉 Explication : Chaque interface attendue doit avoir son adresse IP et son profil NetworkManager actif. `timedatectl` confirme l'horloge synchronisée.

2. Vérifier SELinux, le pare-feu et les services métiers :
   ```bash
   getenforce
   sudo firewall-cmd --state
   systemctl is-active <nom_du_service>
   ```
   👉 Explication : SELinux doit rester en `Enforcing`, firewalld doit répondre `running`, et chaque service métier doit retourner `active`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Analyser le temps de démarrage et les goulots d'étranglement :
   ```bash
   systemd-analyze
   systemd-analyze blame --no-pager | head -n 15
   ```
   👉 Explication : `systemd-analyze` donne la durée totale du démarrage. `blame` classe les unités par durée, ce qui permet de repérer un service qui retarde le démarrage ou un montage réseau trop lent.

2. Relire les erreurs de la session de démarrage :
   ```bash
   sudo journalctl -b -p err --no-pager
   ```
   👉 Explication : Une erreur peut ne pas bloquer le démarrage mais révéler une mauvaise configuration persistante.

3. Planifier le redémarrage de test sur un serveur distant :
   ```bash
   sudo shutdown -r +5 "Test de redémarrage planifié"
   sudo shutdown -c
   ```
   👉 Explication : Le délai de cinq minutes laisse le temps de prévenir les utilisateurs. `shutdown -c` annule le redémarrage programmé.

---

## ✅ Contrôle
```bash
systemctl is-system-running
```
👉 Explication : Le résultat attendu est `running`. Les valeurs `degraded` signalent une unité en échec à analyser.