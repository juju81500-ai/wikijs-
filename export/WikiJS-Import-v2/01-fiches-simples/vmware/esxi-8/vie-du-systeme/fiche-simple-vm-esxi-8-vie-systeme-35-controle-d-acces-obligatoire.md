---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 35 Controle D Acces Obligatoire"
description: "Choisir le contrôle d'accès adapté à ESXi."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-35"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Choisir le contrôle d'accès adapté à ESXi.

## 1. Hors-Production (Lab / Test / POC)

1. ESXi n'utilise pas SELinux. La protection repose sur le noyau VMkernel, `execInstalledOnly`, Secure Boot et le mode verrouillage. Vérifier :
   ```sh
   esxcli system settings kernel list -o execInstalledOnly
   esxcli hardware trustedboot get
   esxcli system settings encryption get
   ```
   👉 Explication : indique si les binaires sont limités, si TPM est utilisé et si la configuration est chiffrée.

2. Activer l'application du chiffrement de configuration lié au TPM (ESXi 7.0 U2 et supérieur) :
   ```sh
   esxcli system settings encryption set --mode=TPM
   esxcli system security keypersistence get
   ```
   👉 Explication : lie la configuration de l'hôte au TPM.

3. Utiliser le rôle `ReadOnly` et le mode verrouillage pour limiter les accès.
   👉 Explication : le contrôle d'accès repose sur les rôles.

## 2. Production — Contrôles

Documenter l'absence de SELinux et les protections retenues.

## 3. Production — Sécurité

Ne pas désactiver `execInstalledOnly`.

## Validation et retour arrière

- **Validation** : `execInstalledOnly` à `TRUE` et mode de chiffrement TPM actif.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)