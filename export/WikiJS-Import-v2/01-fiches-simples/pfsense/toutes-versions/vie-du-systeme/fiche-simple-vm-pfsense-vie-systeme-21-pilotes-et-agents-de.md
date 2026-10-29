---
title: "Fiche Simple - VM pfSense Vie Systeme 21 Pilotes Et Agents De"
description: "Intégrer le pare-feu à l'hyperviseur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Intégrer le pare-feu à l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet invité : System > Package Manager > Available Packages > `qemu-guest-agent` (Proxmox/KVM) ou `Open-VM-Tools` (VMware). En shell :
   ```sh
   pkg-static install -y pfSense-pkg-Qemu-Guest-Agent
   service qemu-guest-agent status
   ```
   👉 Explication : installe l'agent invité; le nom exact du paquet dépend de la version.

2. Activer l'agent côté hyperviseur (Proxmox : VM > Options > Agent QEMU invité).
   👉 Explication : permet l'arrêt propre et la remontée de l'adresse IP.

## 2. Production — Contrôles

Valider l'arrêt propre depuis l'hyperviseur lors de la recette.

## 3. Production — Sécurité

N'installer que le paquet correspondant à l'hyperviseur.

## Validation et retour arrière

- **Validation** : L'hyperviseur affiche l'adresse IP du pare-feu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)