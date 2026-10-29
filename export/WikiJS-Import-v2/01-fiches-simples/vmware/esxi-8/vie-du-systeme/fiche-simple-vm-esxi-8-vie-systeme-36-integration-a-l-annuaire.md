---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 36 Integration A L Annuaire"
description: "Authentifier les administrateurs via Active Directory."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-36"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_36_Integration_A_L_Annuaire

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 36 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-36`

---

## Problème précis à résoudre

Authentifier les administrateurs via Active Directory.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Sécurité > Authentification > Joindre le domaine** (nom de domaine, compte). En ligne de commande :
   ```sh
   /usr/lib/vmware/likewise/bin/domainjoin-cli join DOMAINE ADMIN_AD
   esxcli system settings advanced set -o /Config/HostAgent/plugins/hostsvc/esxAdminsGroup -s GROUPE_AD_ESX
   esxcli system permission set -i GROUPE_AD_ESX -r Admin
   ```
   👉 Explication : `DOMAINE` = domaine AD; `ADMIN_AD` = compte autorisé à joindre (mot de passe demandé); `GROUPE_AD_ESX` = groupe AD dédié aux administrateurs ESXi, différent du nom par défaut `ESX Admins`.

2. Sous vCenter, rejoindre la source d'identité (vSphere Client : **Administration > Single Sign-On > Configuration > Fournisseurs d'identité**).
   👉 Explication : centralise l'authentification de tous les hôtes.

3. Placer l'hôte dans le VLAN d'administration et l'inscrire dans l'IPAM.
   👉 Explication : accès réservé aux postes d'administration.

## 2. Production — Contrôles

Utiliser LDAPS/Kerberos; jamais LDAP en clair.

## 3. Production — Sécurité

Changer le nom du groupe AD d'administration par défaut (`ESX Admins`) pour éviter un abus connu.

## Validation et retour arrière

- **Validation** : Connexion avec un compte de l'annuaire réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)