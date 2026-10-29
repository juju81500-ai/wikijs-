---
title: "Fiche Simple - VM Ubuntu 24.04 Systeme Timezone Locale"
description: "Configurer le fuseau horaire, conserver l'horloge matérielle en UTC et générer la locale française frFR.UTF-8 sur Ubuntu Server 24.04 LTS, sans interaction avec dpkg-reconfigure."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[timezone]", "[locale]", "[timedatectl]", "[localectl]", "[utc]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Timezone_Locale

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Système / Fuseau horaire et localisation
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[timezone]`, `[locale]`, `[timedatectl]`, `[localectl]`, `[utc]`

## 🎯 Problème précis à résoudre
Configurer le fuseau horaire, conserver l'horloge matérielle en UTC et générer la locale française `fr_FR.UTF-8` sur Ubuntu Server 24.04 LTS, sans interaction avec `dpkg-reconfigure`.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Afficher l'état courant de l'horloge et de la locale :
   ```bash
   timedatectl status
   localectl status
   locale
   ```
   👉 *Explication : `timedatectl` affiche le fuseau et la synchronisation NTP ; `localectl` affiche la locale et la disposition clavier.*
2. Définir le fuseau horaire :
   ```bash
   sudo timedatectl set-timezone Europe/Paris
   timedatectl show --property=Timezone --value
   ```
   👉 *Explication : Crée le lien `/etc/localtime` vers la zone demandée. La liste complète est donnée par `timedatectl list-timezones`.*

## ⚡ 2. Production — Façon Simplifiée
1. Installer le paquet `locales` puis générer la locale française :
   ```bash
   sudo apt update
   sudo apt install -y locales
   sudo locale-gen fr_FR.UTF-8
   sudo update-locale LANG=fr_FR.UTF-8
   ```
   👉 *Explication : `locale-gen` compile la locale ; `update-locale` écrit `LANG` dans `/etc/default/locale`. Les nouvelles sessions prennent la valeur, pas les sessions déjà ouvertes.*
2. Conserver l'horloge matérielle en UTC (valeur par défaut recommandée sous Linux) :
   ```bash
   sudo timedatectl set-local-rtc 0
   timedatectl status | grep -i 'rtc in local'
   ```
   👉 *Explication : Un serveur doit garder l'horloge matérielle en UTC pour éviter les décalages lors du passage à l'heure d'été.*

## 🔒 3. Production — Façon Sécurisée
1. Vérifier que la synchronisation NTP est active avant de figer la configuration :
   ```bash
   timedatectl show --property=NTPSynchronized --value
   systemctl --no-pager status systemd-timesyncd
   ```
   👉 *Explication : Sous Ubuntu 24.04, `systemd-timesyncd` est le client NTP par défaut ; si un autre client (chrony) est installé, c'est lui qui doit être vérifié.*
2. Journaliser la modification de fuseau et de locale pour l'audit :
   ```bash
   sudo journalctl --since today | grep -i -E 'timezone|locale' | tail -n 20
   ```
   👉 *Explication : Permet de retrouver la date et le compte de la dernière modification lors d'une revue d'exploitation.*

## ✅ Validation et retour arrière
- Vérifier que `date` affiche l'heure locale attendue et que `locale` affiche `LANG=fr_FR.UTF-8`.
- Retour arrière du fuseau : `sudo timedatectl set-timezone <ancien_fuseau>` ; retour arrière de la locale : `sudo update-locale LANG=en_US.UTF-8`.