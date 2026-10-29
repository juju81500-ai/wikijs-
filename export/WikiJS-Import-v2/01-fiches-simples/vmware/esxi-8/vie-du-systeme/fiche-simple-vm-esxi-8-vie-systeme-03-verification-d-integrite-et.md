---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 03 Verification D Integrite Et"
description: "Prouver que l'ISO n'est pas corrompue."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

Prouver que l'ISO n'est pas corrompue.

## 1. Hors-Production (Lab / Test / POC)

1. Calculer l'empreinte SHA-256 et la comparer à celle de la page de téléchargement :
   ```sh
   sha256sum VMware-VMvisor-Installer-8.0*.iso
   ```
   👉 Explication : les deux valeurs doivent être identiques; le portail indique aussi MD5 et SHA-1 (à éviter).

2. Sous Windows (PowerShell) :
   ```sh
   Get-FileHash .\VMware-VMvisor-Installer-8.0*.iso -Algorithm SHA256
   ```
   👉 Explication : équivalent de `sha256sum`.

3. Consigner la date, le nom de l'ISO et l'empreinte dans le dossier.
   👉 Explication : traçabilité en cas d'audit.

## 2. Production — Contrôles

Conserver l'empreinte validée avec l'ISO.

## 3. Production — Sécurité

Si la valeur diffère, supprimer l'image et la retélécharger.

## Validation et retour arrière

- **Validation** : Empreinte identique à celle publiée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)