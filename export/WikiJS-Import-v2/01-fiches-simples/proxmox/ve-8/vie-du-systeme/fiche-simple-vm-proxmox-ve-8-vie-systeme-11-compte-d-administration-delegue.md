---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 11 Compte D Administration Delegue"
description: "Créer un compte nominatif avec droits limités."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-11"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Créer un compte nominatif avec droits limités.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Datacenter > Permissions > Users > Add** (domaine **Proxmox VE authentication server**), puis **Permissions > Add > User Permission** (chemin `/`, rôle `Administrator` ou plus restreint). En ligne de commande (remplacer `ADMIN1`) :
   ```bash
   pveum user add ADMIN1@pve --comment "Admin nominatif"
   pveum passwd ADMIN1@pve
   pveum acl modify / --users ADMIN1@pve --roles Administrator
   ```
   👉 Explication : crée l'utilisateur, définit son mot de passe et lui donne un rôle sur la racine.

2. Lister les utilisateurs et droits :
   ```bash
   pveum user list
   pveum acl list
   ```
   👉 Explication : vérifie que le compte et son rôle existent.

3. Pour des droits limités (GUI : **Datacenter > Permissions > Roles**), utiliser un rôle comme `PVEVMAdmin` ou `PVEAuditor` sur un chemin précis (`/vms/ID`).
   👉 Explication : principe du moindre privilège.

## 2. Production — Contrôles

Un compte par administrateur; pas de compte partagé.

## 3. Production — Sécurité

Activer le 2FA pour chaque compte (TOTP).

## Validation et retour arrière

- **Validation** : Connexion du compte nominatif réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)