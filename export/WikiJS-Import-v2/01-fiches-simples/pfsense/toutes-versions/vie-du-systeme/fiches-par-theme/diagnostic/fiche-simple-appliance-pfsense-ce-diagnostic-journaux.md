---
title: "Fiche Simple - Appliance pfSense CE Diagnostic Journaux"
description: "Identifier les erreurs système et les blocages de pare-feu sur pfSense CE, à partir de l'interface web et du shell, puis centraliser les journaux pour conservation."
published: true
date: 2026-10-29T20:22:42Z
tags: ["pfsense", "ce", "freebsd", "logs", "syslog", "diagnostic"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_Appliance_pfSense_CE_Diagnostic_Journaux.md

- **Environnement** : pfSense CE sur VM Proxmox VE ou appliance dédiée
- **OS / Version** : pfSense CE 2.x (base FreeBSD) - Toutes-versions
- **Catégorie** : Diagnostic / Journaux système
- **Tags** : `pfsense`, `ce`, `freebsd`, `logs`, `syslog`, `diagnostic`

---

## 🎯 Problème précis à résoudre
Identifier les erreurs système et les blocages de pare-feu sur pfSense CE, à partir de l'interface web et du shell, puis centraliser les journaux pour conservation.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ouvrir le journal système dans l'interface :
   `Status > System Logs > System` : filtrer sur les niveaux `error`, `critical`, `alert`
   👉 Explication : Affiche les erreurs des services (DHCP, DNS, VPN, sshd, webConfigurator).
2. Contrôler les blocages du pare-feu :
   `Status > System Logs > Firewall` : filtrer par interface et par action `block`
   👉 Explication : Permet de vérifier qu'un flux bloqué l'est par une règle attendue.
3. Lire les dernières lignes du journal système depuis le shell (option 8) :
   `clog /var/log/system.log | tail -n 100`
   👉 Explication : `clog` lit le fichier de journal avec sa signature interne ; `tail` limite l'affichage aux événements récents.
4. Rechercher les erreurs noyau :
   `dmesg | grep -iE 'error|fail|panic' | tail -n 50`
   👉 Explication : Détecte les erreurs matérielles ou pilotes (interfaces vtnet, disques) absentes des journaux applicatifs.
5. Valider un flux suspect avec une capture ciblée :
   `Diagnostics > Packet Capture` : Interface = `<interface_lan>`, Count = `100`, Filter = `port 53`
   👉 Explication : Confirme si les requêtes DNS arrivent à pfSense et y reçoivent une réponse.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activer l'envoi des journaux vers un serveur syslog :
   `Status > System Logs > Settings > Remote Logging Options` : Enable Remote Logging, Remote log servers = `<adresse_ip_syslog>:514`
   👉 Explication : Conserve les journaux hors de l'appliance, même si elle tombe en panne.
2. Vérifier l'arrivée des messages sur le serveur syslog :
   `tcpdump -ni any udp port 514 -c 5` (sur `<adresse_ip_syslog>`)
   👉 Explication : Confirme que pfSense envoie réellement ses événements.
3. Contrôler l'espace disque consacré aux journaux :
   `df -h /var /cf`
   👉 Explication : Un système de fichiers plein arrête l'écriture des journaux et peut bloquer la configuration.

---

## 🔒 3. Production — Façon Sécurisée
1. Vérifier les services d'administration en écoute :
   `sockstat -4 -6 -l`
   👉 Explication : Repère tout service ouvert non prévu dans le plan d'adressage.
2. Contrôler l'état du service SSH :
   `service sshd status`
   👉 Explication : Confirme que sshd fonctionne avec la configuration validée.
3. Conserver les journaux d'administration plus longtemps que les journaux de trafic :
   `Status > System Logs > Settings` : Log file size et Keep log for (à vérifier sur la version déployée), puis copie vers le serveur syslog distant
   👉 Explication : Les événements d'authentification servent aux enquêtes et doivent être disponibles plus longtemps.