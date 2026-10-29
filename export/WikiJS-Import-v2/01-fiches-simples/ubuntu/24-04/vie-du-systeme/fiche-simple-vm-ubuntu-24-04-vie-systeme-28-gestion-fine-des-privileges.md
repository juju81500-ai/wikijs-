---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 28 Gestion Fine Des Privileges"
description: "Limiter les droits sudo."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-28"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-28`

---

## Problème précis à résoudre

Limiter les droits sudo.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'implémentation de `sudo` installée (la version d'Ubuntu peut fournir `sudo-rs` à la place du `sudo` historique) :
   ```bash
   sudo --version | head -1
   which -a sudo visudo
   ```
   👉 Explication : identifie la variante; les règles de `/etc/sudoers.d/` restent éditées avec `visudo`.

2. Créer une règle (remplacer groupe et commande) :
   ```bash
   sudo visudo -f /etc/sudoers.d/exploitation
   ```
   👉 Explication : exemple : `%exploitation ALL=(root) /usr/bin/systemctl restart nginx`.

3. Contrôler :
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

- **Validation** : `visudo -c` : `parsed OK` (ou équivalent sans erreur).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)