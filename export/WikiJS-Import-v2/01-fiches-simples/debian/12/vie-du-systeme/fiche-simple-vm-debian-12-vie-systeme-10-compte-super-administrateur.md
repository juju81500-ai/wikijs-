---
title: "Fiche Simple - VM Debian 12 Vie Systeme 10 Compte Super Administrateur"
description: "Décider du sort du compte root."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-10"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Décider du sort du compte root.

## 1. Hors-Production (Lab / Test / POC)

1. Verrouiller la connexion directe de root par mot de passe (sudo suffit) :
   ```bash
   sudo passwd -l root
   sudo passwd -S root
   ```
   👉 Explication : `L` indique un compte verrouillé; garder un accès console de secours testé.

2. Ne jamais saisir de mot de passe en argument; en cas de définition, laisser `passwd` le demander :
   ```bash
   sudo passwd root
   ```
   👉 Explication : la commande demande le mot de passe sans l'afficher.

## 2. Production — Contrôles

Stocker tout mot de passe root de secours dans le coffre d'entreprise.

## 3. Production — Sécurité

Interdire root en SSH (étape 27).

## Validation et retour arrière

- **Validation** : `passwd -S root` affiche `L`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)