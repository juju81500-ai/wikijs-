---
title: "Fiche Simple - VM Windows Server 2022 Vie Systeme 21 Pilotes Et Agents De"
description: "Installer les pilotes et services d'intégration."
published: true
date: 2026-11-03T14:22:28Z
tags: ["windowsserver2022", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer les pilotes et services d'intégration.

## 1. Hors-Production (Lab / Test / POC)

1. Hyper-V : les services d'intégration passent par Windows Update. Vérifier-les dans **Gestionnaire Hyper-V > Paramètres de la [[Glossary:VM]] > Services d'intégration**.
   ```powershell
   Get-VMIntegrationService -VMName NOM_VM
   ```
   👉 Explication : tous les services doivent être activés et `OK`.

2. Sur la VM, repérer les périphériques sans pilote (**Gestionnaire de périphériques**) :
   ```powershell
   Get-PnpDevice -Status Error,Unknown | Select-Object FriendlyName, Class, Status
   ```
   👉 Explication : une liste vide signifie que tous les pilotes sont chargés.

3. VMware ou Proxmox : monter l'ISO d'outils (VMware Tools ou VirtIO) et l'installer :
   ```powershell
   Get-Service | Where-Object Name -match 'VMTools|QEMU|vmicheartbeat' | Select-Object Name, Status
   ```
   👉 Explication : confirme que l'agent est démarré.

## 2. Production — Contrôles

Installer l'agent adapté à l'hyperviseur et le conserver à jour.

## 3. Production — Sécurité

Télécharger les pilotes uniquement depuis l'éditeur de l'hyperviseur ou du constructeur.

## Validation et retour arrière

- **Validation** : Aucun périphérique en erreur et agent actif.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows Server 2022 Hyper V Creer VM Pilote](/fr/01-fiches-simples/windows/server-2022/vie-du-logiciel/hyper-v/fiche-simple-vm-windows-server-2022-hyper-v-creer-vm-pilote)
- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Windows Server 2022](/fr/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)