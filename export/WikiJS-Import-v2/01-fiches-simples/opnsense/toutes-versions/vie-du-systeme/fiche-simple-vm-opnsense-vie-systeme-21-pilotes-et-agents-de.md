---
title: "Fiche Simple - VM OPNsense Vie Systeme 21 Pilotes Et Agents De"
description: "Intégrer le pare-feu à l'hyperviseur."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-21"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Intégrer le pare-feu à l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le plugin invité de l'hyperviseur dans Système > Micrologiciel > Plugins (`os-qemu-guest-agent`, `os-vmware`, `os-hyperv`). En shell :
   ```sh
   pkg install -y os-qemu-guest-agent
   service qemu-guest-agent status
   ```
   👉 Explication : installe l'agent invité (Proxmox/KVM); un redémarrage active le service.

2. Activer l'agent côté hyperviseur (Proxmox : VM > Options > Agent QEMU invité).
   👉 Explication : permet l'arrêt propre et la remontée de l'adresse IP.

## 2. Production — Contrôles

Valider l'arrêt propre depuis l'hyperviseur lors de la recette.

## 3. Production — Sécurité

N'installer que le plugin correspondant à l'hyperviseur.

## Validation et retour arrière

- **Validation** : L'hyperviseur affiche l'adresse IP du pare-feu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)