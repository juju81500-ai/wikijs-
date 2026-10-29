---
title: "Fiche Simple - VM Proxmox VE 8 Vie Systeme 36 Integration A L Annuaire"
description: "Authentifier les administrateurs via l'annuaire (LDAP/AD)."
published: true
date: 2026-10-29T20:22:10Z
tags: ["proxmoxve8", "vie-du-systeme", "cycle-de-vie", "etape-36"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Authentifier les administrateurs via l'annuaire (LDAP/AD).

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Datacenter > Permissions > Realms > Add > Active Directory** (serveur, domaine, port 636 avec SSL). En ligne de commande :
   ```bash
   pveum realm add AD --type ad --domain DOMAINE --server1 IP_AD --secure 1
   pveum realm sync AD
   ```
   👉 Explication : `DOMAINE` = domaine AD; `IP_AD` = contrôleur; la synchro importe utilisateurs et groupes.

2. Donner un rôle à un groupe de l'annuaire (remplacer `GROUPE`) :
   ```bash
   pveum acl modify / --groups GROUPE-AD --roles PVEAdmin
   ```
   👉 Explication : les droits suivent l'appartenance au groupe.

3. Placer l'hôte dans le VLAN d'administration et l'inscrire dans l'IPAM.
   👉 Explication : accès réservé aux postes d'administration.

## 2. Production — Contrôles

Utiliser LDAPS (port 636), pas LDAP en clair.

## 3. Production — Sécurité

Garder le compte `root@pam` comme secours uniquement.

## Validation et retour arrière

- **Validation** : Connexion avec un compte de l'annuaire réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)