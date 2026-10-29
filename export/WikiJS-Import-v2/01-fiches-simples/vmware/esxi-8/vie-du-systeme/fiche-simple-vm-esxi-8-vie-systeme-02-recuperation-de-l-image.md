---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 02 Recuperation De L Image"
description: "Obtenir l'ISO officielle d'ESXi 8."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-02"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-02`

---

## Problème précis à résoudre

Obtenir l'ISO officielle d'ESXi 8.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO depuis le portail Broadcom (support.broadcom.com > Free Downloads ou My Downloads > VMware vSphere > ESXi 8.0), avec le compte associé à la licence.
   👉 Explication : le téléchargement exige un compte Broadcom; l'ISO OEM du constructeur (Dell, HPE) contient les pilotes adaptés.

2. Contrôler la taille et le nom du fichier :
   ```sh
   ls -lh VMware-VMvisor-Installer-8.0*.iso
   ```
   👉 Explication : une taille anormalement petite indique un téléchargement interrompu.

3. Ranger l'ISO dans un dépôt interne avec sa version et son numéro de build.
   👉 Explication : garantit que tous les hôtes utilisent la même image.

## 2. Production — Contrôles

Utiliser l'ISO personnalisée du constructeur du serveur.

## 3. Production — Sécurité

Télécharger uniquement depuis le portail officiel Broadcom ou le site du constructeur.

## Validation et retour arrière

- **Validation** : ISO présente, version et build notés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)