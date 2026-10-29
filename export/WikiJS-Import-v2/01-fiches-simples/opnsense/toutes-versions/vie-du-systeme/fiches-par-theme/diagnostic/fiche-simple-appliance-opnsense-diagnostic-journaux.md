---
title: "Fiche Simple - Appliance OPNsense Diagnostic Journaux"
description: "Identifier les erreurs système et les blocages de pare-feu d'OPNsense depuis l'interface web et le shell, et contrôler les services et ports actifs."
published: true
date: 2026-10-29T20:22:42Z
tags: ["opnsense", "freebsd", "logs", "diagnostic", "firewall"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_Appliance_OPNsense_Diagnostic_Journaux.md

- **Environnement** : OPNsense sur VM Proxmox VE ou appliance dédiée
- **OS / Version** : OPNsense (base FreeBSD) - Toutes-versions (chemins de menu à vérifier sur la version déployée)
- **Catégorie** : Diagnostic / Journaux système
- **Tags** : `opnsense`, `freebsd`, `logs`, `diagnostic`, `firewall`

---

## 🎯 Problème précis à résoudre
Identifier les erreurs système et les blocages de pare-feu d'OPNsense depuis l'interface web et le shell, et contrôler les services et ports actifs.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Consulter les journaux généraux :
   `Diagnostics > Log Files > General` (à vérifier sur la version déployée) : filtrer sur `error` ou `critical`
   👉 Explication : Affiche les erreurs des services (DHCP, DNS, VPN, sshd, interface web).
2. Suivre les blocages du pare-feu en direct :
   `Firewall > Log Files > Live View` : filtrer par interface et par action `block`
   👉 Explication : Permet de vérifier qu'un flux est bloqué par la règle attendue pendant le test.
3. Lire les erreurs noyau depuis le shell (option 8) :
   `dmesg | grep -iE 'error|fail|panic' | tail -n 50`
   👉 Explication : Détecte les erreurs de pilotes et de disques absentes des journaux applicatifs.
4. Lister les fichiers de journaux disponibles :
   `ls -l /var/log/`
   👉 Explication : Repère les journaux de service à consulter (le nom exact dépend de la version).
5. Tester un flux précis avec une capture :
   `Interfaces > Diagnostics > Packet capture` (à vérifier sur la version déployée) : Interface = `<interface_lan>`, filtre = `port 53`
   👉 Explication : Confirme si les requêtes DNS arrivent à OPNsense et y reçoivent une réponse.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier le service DNS et son état d'écoute :
   `Services > Unbound DNS > General` : Enable = coché, puis `sockstat -4 -6 -l | grep ':53 '`
   👉 Explication : Confirme que le résolveur répond sur les interfaces prévues.
2. Vérifier les services activés au démarrage :
   `service -e`
   👉 Explication : Liste les services FreeBSD actifs après redémarrage, à comparer avec le plan de services.
3. Contrôler l'espace disque utilisé par les journaux :
   `df -h /var`
   👉 Explication : Un système de fichiers plein arrête l'écriture des journaux.

---

## 🔒 3. Production — Façon Sécurisée
1. Envoyer les journaux vers un serveur distant (voir la fiche Supervision_Syslog) :
   `System > Settings > Logging / targets`
   👉 Explication : Les journaux restent disponibles même si l'appliance est compromise ou tombe en panne.
2. Vérifier les ports d'écoute non prévus :
   `sockstat -4 -6 -l`
   👉 Explication : Repère tout service ouvert hors du plan d'adressage validé.
3. Contrôler les processus de sécurité :
   `service sshd status` et `pfctl -si | head -n 10`
   👉 Explication : Confirme que sshd tourne et que le filtrage Packet Filter est actif.