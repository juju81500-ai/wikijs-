---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 28 Gestion Fine Des Privileges"
description: "Limiter les droits administratifs."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-28"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Limiter les droits administratifs.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une règle dédiée avec `visudo` (adapter `GRPOPS`) :
   ```bash
   echo '%GRPOPS ALL=(root) /usr/bin/systemctl restart nginx' | sudo tee /etc/sudoers.d/grpops
   sudo chmod 440 /etc/sudoers.d/grpops
   sudo visudo -cf /etc/sudoers.d/grpops
   ```
   👉 Explication : autorise une seule commande; `visudo -cf` valide la syntaxe.

2. Lister les droits d'un utilisateur :
   ```bash
   sudo -l -U ADMIN1
   ```
   👉 Explication : montre ce qu'il peut exécuter.

3. Consulter les traces sudo :
   ```bash
   sudo journalctl _COMM=sudo --since today
   ```
   👉 Explication : chaque usage est journalisé.

## 2. Production — Contrôles

Appliquer le moindre privilège et revoir les droits périodiquement.

## 3. Production — Sécurité

Éviter `NOPASSWD: ALL`.

## Validation et retour arrière

- **Validation** : Seules les commandes prévues sont autorisées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)