---
title: "Fiche Simple - VM Debian 12 Vie Systeme 28 Gestion Fine Des Privileges"
description: "Limiter les droits sudo."
published: true
date: 2026-11-03T09:36:13Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-28"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : [[Glossary:VM]] Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Limiter les droits sudo.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une règle (remplacer groupe et commande) :
   ```bash
   sudo visudo -f /etc/sudoers.d/exploitation
   ```
   👉 Explication : exemple : `%exploitation ALL=(root) /usr/bin/systemctl restart nginx`.

2. Contrôler :
   ```bash
   sudo visudo -c
   sudo -l -U admin01
   ```
   👉 Explication : valide la syntaxe et liste les droits.

## 2. Production — Contrôles

Principe du moindre privilège, revue trimestrielle.

## 3. Production — Sécurité

Toujours éditer avec `visudo`.

## Validation et retour arrière

- **Validation** : `visudo -c` : `parsed OK`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Debian 12](/fr/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)