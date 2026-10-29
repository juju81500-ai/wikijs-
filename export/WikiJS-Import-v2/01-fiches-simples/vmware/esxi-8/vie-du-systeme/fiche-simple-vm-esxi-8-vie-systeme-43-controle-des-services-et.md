---
title: "Fiche Simple - VM ESXi 8 Vie Systeme 43 Controle Des Services Et"
description: "Vérifier que seuls les services attendus tournent."
published: true
date: 2026-10-29T20:22:10Z
tags: ["esxi8", "vie-du-systeme", "cycle-de-vie", "etape-43"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier que seuls les services attendus tournent.

## 1. Hors-Production (Lab / Test / POC)

1. Host Client : **Gérer > Services**. En ligne de commande :
   ```sh
   esxcli network ip connection list | grep LISTEN
   esxcli system services list 2>/dev/null | head
   ```
   👉 Explication : comparer à la liste attendue (hostd, vpxa, ntpd, DCUI).

2. Contrôler le pare-feu :
   ```sh
   esxcli network firewall get
   esxcli network firewall ruleset list | grep true
   ```
   👉 Explication : affiche les ensembles de règles activés.

3. Contrôler l'état de santé de l'hôte :
   ```sh
   vim-cmd hostsvc/hostsummary | grep -i -E 'overallStatus|uptime'
   ```
   👉 Explication : `overallStatus = green` attendu.

## 2. Production — Contrôles

Comparer à la baseline de l'étape 25.

## 3. Production — Sécurité

Corriger tout écart avant production.

## Validation et retour arrière

- **Validation** : Aucun service inattendu; statut `green`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)