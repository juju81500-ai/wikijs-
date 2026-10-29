---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 05 Configuration Materielle Firmware"
description: "Préparer le BIOS/UEFI et le matériel."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-05"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-05`

---

## Problème précis à résoudre

Préparer le BIOS/UEFI et le matériel.

## 1. Hors-Production (Lab / Test / POC)

1. Au démarrage, entrer dans le Setup (F2 ou F11) et activer : Virtualisation (Intel VT-x / AMD-V), VT-d/IOMMU, mode UEFI, Secure Boot et TPM 2.0 selon la politique.
   👉 Explication : VT-x/AMD-V est indispensable; TPM et Secure Boot renforcent l'attestation de l'hôte.

2. Configurer le RAID matériel (iDRAC : **Configuration > Configuration du stockage**) pour le datastore local, ou passer en mode HBA pour vSAN.
   👉 Explication : ESXi ne gère pas de RAID logiciel : le contrôleur doit présenter un volume redondant.

3. Après installation, vérifier le matériel vu par l'hôte :
   ```sh
   esxcli hardware platform get
   esxcli hardware cpu global get
   esxcli hardware trustedboot get
   ```
   👉 Explication : affiche constructeur, modèle, CPU, TPM; l'hôte doit voir la virtualisation matérielle.

4. Mettre à jour BIOS, iDRAC, contrôleur RAID et cartes réseau avant la mise en production.
   👉 Explication : corrige des défauts connus; respecter la matrice de compatibilité.

## 2. Production — Contrôles

Documenter la version du firmware et les réglages BIOS retenus.

## 3. Production — Sécurité

Changer les mots de passe par défaut de l'iDRAC et du BIOS.

## Validation et retour arrière

- **Validation** : L'hôte démarre en UEFI et la virtualisation est active.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)