---
title: "Fiche Simple - VM Debian 12 Vie Systeme 36 Integration A L Annuaire"
description: "Joindre le domaine ou le VPN."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-36"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Joindre le domaine ou le VPN.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les outils de jonction AD :
   ```bash
   sudo apt install realmd sssd sssd-tools adcli krb5-user packagekit
   ```
   👉 Explication : paquets nécessaires à `realm`.

2. Découvrir puis joindre (remplacer domaine et compte) :
   ```bash
   realm discover EXEMPLE.LAN
   sudo realm join -U admin-ad EXEMPLE.LAN
   ```
   👉 Explication : `realm` demande le mot de passe à l'écran.

## 2. Production — Contrôles

Compte de jonction dédié à droits limités.

## 3. Production — Sécurité

Vérifier l'heure (Kerberos tolère 5 minutes d'écart).

## Validation et retour arrière

- **Validation** : `id utilisateur@exemple.lan` répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)