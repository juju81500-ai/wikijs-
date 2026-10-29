---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 11 Compte D Administration Delegue"
description: "Disposer d'un compte nominatif avec sudo."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-11"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Disposer d'un compte nominatif avec sudo.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'utilisateur et l'ajouter au groupe `sudo` (remplacer `admin01`) :
   ```bash
   sudo adduser admin01
   sudo usermod -aG sudo admin01
   id admin01
   ```
   👉 Explication : `adduser` demande le mot de passe à l'écran; `id` confirme l'appartenance au groupe.

2. Tester depuis ce compte :
   ```bash
   sudo -l -U admin01
   ```
   👉 Explication : liste les droits sudo accordés.

## 2. Production — Contrôles

Un compte par administrateur, pas de compte partagé.

## 3. Production — Sécurité

Limiter les droits via `/etc/sudoers.d/` (étape 28).

## Validation et retour arrière

- **Validation** : `sudo -l` fonctionne pour le compte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)