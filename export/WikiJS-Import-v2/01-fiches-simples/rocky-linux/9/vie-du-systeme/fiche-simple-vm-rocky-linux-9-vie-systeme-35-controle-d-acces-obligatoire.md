---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 35 Controle D Acces Obligatoire"
description: "Garder SELinux en mode enforcing."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-35"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Garder SELinux en mode enforcing.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le mode :
   ```bash
   getenforce
   sestatus
   ```
   👉 Explication : doit afficher `Enforcing`.

2. Forcer enforcing de façon persistante :
   ```bash
   sudo setenforce 1
   sudo sed -i 's/^SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config
   ```
   👉 Explication : `setenforce` agit immédiatement, le fichier garde le réglage après redémarrage.

3. Corriger un contexte et autoriser un port (adapter `/srv/app`, `8080`) :
   ```bash
   sudo semanage fcontext -a -t httpd_sys_content_t '/srv/app(/.*)?'
   sudo restorecon -Rv /srv/app
   sudo semanage port -a -t http_port_t -p tcp 8080
   ```
   👉 Explication : applique le contexte voulu; `/srv/app` et `8080` sont des exemples.

## 2. Production — Contrôles

Analyser les refus avec `ausearch -m avc -ts recent` avant toute dérogation.

## 3. Production — Sécurité

Ne jamais désactiver SELinux pour résoudre un problème.

## Validation et retour arrière

- **Validation** : `getenforce` renvoie `Enforcing` sans refus inattendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)