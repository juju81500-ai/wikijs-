---
title: "Présentation de la virtualisation"
description: "Partage de ressources matérielles (serveurs, stockage, etc.) entre plusieurs services ou utilisateurs pour optimiser leur usage."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Présentation de la virtualisation

## 📚 Définitions clés

### Mutualisation

Partage de ressources matérielles (serveurs, stockage, etc.) entre plusieurs services ou utilisateurs pour optimiser leur usage.

### Consolidation

Réduction du nombre de serveurs physiques en regroupant plusieurs services sur un même hôte via des machines virtuelles.

### Rationalisation

Réorganisation de l'infrastructure pour améliorer l'efficacité, réduire les coûts et faciliter l’administration.

---

## 📅 La virtualisation en 8 dates clés

- **1960-70** : IBM teste la virtualisation sur ses mainframes
- **Milieu 1990s** : apparition d’émulateurs (Amiga, Atari, etc.)
- **Début 2000s** : VMware popularise la virtualisation x86
- **2006** : instructions de virtualisation supportées par les CPU
- **2007** : Citrix rachète XenSource
- **2007** : KVM intégré au noyau Linux
- **2009** : plus de serveurs virtuels que physiques
- **vSphere, VDI** : généralisation dans le cloud et les postes de travail

---

## 🧰 Usages principaux

- Serveurs d’infrastructure locaux ou distants (cloud)
- Environnements de test et compatibilité logicielle
- Scénarios de PRA (Plan de Reprise d’Activité)

## ✅ Avantages

- Optimisation de l’usage matériel (moins de serveurs physiques)
- Réduction des coûts d’infrastructure et d’énergie
- Meilleure gestion et granularité des systèmes

## ⚠️ Inconvénients

- Dépendance vis-à-vis d’une solution ou d’un éditeur
- Investissement initial élevé (matériel, licences)
- Complexité d’administration (sauvegarde, déploiement, supervision)

---

## 🏢 Les acteurs du marché

### Solutions propriétaires

- VMware vSphere / Workstation / ESXi
- Microsoft Hyper-V
- Citrix XenServer (basé sur Xen)

### Solutions libres

- KVM (Linux)
- QEMU
- VirtualBox (Oracle)

---

## 🧩 Domaines de virtualisation

- Virtualisation de serveurs (ex. Hyper-V, ESXi)
- Virtualisation de postes de travail (VDI)
- Virtualisation d’applications (App-V, ThinApp)
- Virtualisation réseau (NSX, SDN)
- Virtualisation de stockage (vSAN, Ceph)
- Virtualisation des services (containers, microservices)

---

## 🖥️ Outils et composants

### Outils de virtualisation poste de travail

- VMware Workstation / Player
- VirtualBox
- Windows Virtual PC, Hyper-V Client

### Outils de virtualisation serveur

- VMware vSphere/ESXi
- Microsoft Hyper-V (Windows Server)
- KVM, XenServer (Citrix)

### Composants techniques

- Fichiers de configuration : VMX, VDI, VHD, VBOX...
- BIOS / CPU compatibles virtualisation
- Réseaux virtuels : NAT, bridge, interne, LAN dédié
- Support ISO, USB, FLP...

---

## 🧠 Hyperviseurs : types et distinctions

### Hyperviseur de type 1 (natif)

- Exécuté **directement sur le matériel**
- Exemples : VMware ESXi, Microsoft Hyper-V (core), XenServer, KVM
- Plus rapide, plus sécurisé

### Hyperviseur de type 2 (hébergé)

- Exécuté **au-dessus d’un OS hôte**
- Exemples : VirtualBox, VMware Player/Workstation
- Plus souple, mais plus lent et moins optimisé

---

## 🔍 Virtualisation vs Paravirtualisation

### Virtualisation classique

- L’OS invité ne « sait pas » qu’il est virtualisé
- Hyperviseur simule l’ensemble du matériel (traduction binaire)

### Paravirtualisation

- L’OS invité est **modifié** pour faire appel directement à l’hyperviseur
- Exécution plus rapide, appels système remplacés par des hypercalls
- Utilisé par Xen et certains modules de pilotes dans KVM

---

## ✅ À retenir pour les révisions

- La virtualisation permet d’**optimiser l’infrastructure IT** en réduisant les coûts et en augmentant la flexibilité.
- Les **hyperviseurs type 1** sont plus performants que les hyperviseurs de type 2.
- La **paravirtualisation** améliore la performance mais nécessite des OS adaptés.
- Il existe une large gamme de **solutions propriétaires et libres** selon les besoins (serveur, test, production…)

---

## 📌 Bonnes pratiques professionnelles

- Vérifier le **support matériel** (BIOS, CPU VT-x/AMD-V) avant toute installation
- Choisir l’hyperviseur adapté selon l’usage (test vs production)
- Centraliser la gestion via une **console de supervision** (vCenter, SCVMM...)
- Ne pas surprovisionner les VMs sur un hôte pour éviter l’effet « noyer la RAM »
- Intégrer les VMs dans une stratégie de **sauvegarde, supervision et PRA**

---

## 🔗 Commandes / outils à connaître

- `Get-VM`, `Start-VM`, `Stop-VM` (PowerShell / Hyper-V)
- `virt-manager`, `virsh`, `qemu-img` (KVM / QEMU)
- Interfaces de gestion : vSphere Client, Hyper-V Manager, VirtualBox UI