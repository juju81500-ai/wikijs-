---
title: "VM_Debian_12_Diagnostic-Journalctl-Erreurs"
description: "Identifier rapidement les erreurs système d'un serveur Debian 12 : messages de niveau err et plus, unités systemd en échec, erreurs noyau et historique du démarrage précédent, pour diagnostiquer un incident sans parcourir les fichiers bruts."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[journalctl]", "[systemd]", "[dmesg]", "[diagnostic]", "[logs]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Diagnostic-Journalctl-Erreurs.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Supervision & Diagnostic / Analyse des erreurs système
- **Tags** : `[debian12]`, `[debian-family]`, `[journalctl]`, `[systemd]`, `[dmesg]`, `[diagnostic]`, `[logs]`

## 🎯 Problème précis à résoudre
Identifier rapidement les erreurs système d'un serveur Debian 12 : messages de niveau `err` et plus, unités systemd en échec, erreurs noyau et historique du démarrage précédent, pour diagnostiquer un incident sans parcourir les fichiers bruts.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Erreurs du démarrage courant :
   `sudo journalctl -p err -b`
   👉 Explication : Affiche les messages de niveau `err` ou plus grave depuis le dernier démarrage.
2. Liste des démarrages enregistrés :
   `sudo journalctl --list-boots`
   👉 Explication : Donne l'index de chaque boot (0 = actuel, -1 = précédent) pour analyser un redémarrage inattendu.
3. Erreurs du noyau :
   `sudo dmesg -l err,crit,alert,emerg`
   👉 Explication : Filtre les messages noyau critiques (disque, pilote, mémoire).

---

## ⚡ 2. Production — Façon Simplifiée
1. Avertissements et erreurs du démarrage précédent :
   `sudo journalctl -p warning..err -b -1`
   👉 Explication : Utile après un crash : la plage `warning..err` isole les messages pertinents du boot précédent.
2. Journal d'un service précis sur la dernière heure :
   `sudo journalctl -u <nom_du_service> --since "1 hour ago" -p warning`
   👉 Explication : Restreint l'analyse à l'unité concernée, par exemple `ssh` ou `nftables`.
3. Unités systemd en échec :
   `systemctl --failed`
   👉 Explication : Liste les services qui ont échoué ; pour le détail, utiliser `sudo journalctl -xeu <nom_du_service>`.

---

## 🔒 3. Production — Façon Sécurisée (Audit & Intégrité des journaux)
1. Synthèse des erreurs des 24 dernières heures :
   `sudo journalctl --since "24 hours ago" -p err --no-pager | tail -n 50`
   👉 Explication : Produit la liste des 50 dernières erreurs, à joindre au rapport d'exploitation quotidien.
2. Détection de tentatives d'authentification SSH échouées :
   `sudo journalctl -u ssh --since today | grep -i 'Failed password'`
   👉 Explication : Repère les attaques par mot de passe ; à croiser avec Fail2ban ou nftables si des IP répétées apparaissent.
3. Vérification de l'intégrité des fichiers journal :
   `sudo journalctl --verify`
   👉 Explication : Contrôle la cohérence cryptographique des fichiers journaux persistants et signale toute altération.