---
title: "vSphere / ESXi (VMware)"
description: "vSphere est la suite de virtualisation de VMware. Elle repose sur l’hyperviseur ESXi, administré via vCenter ou vSphere Client. Elle permet la gestion centralisée de machines virtuelles, de ressources réseau et de stockage, souvent utilisée en production dans les entreprises."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# vSphere / ESXi (VMware)

## 📌 Présentation

vSphere est la suite de virtualisation de VMware. Elle repose sur l’hyperviseur **ESXi**, administré via **vCenter** ou **vSphere Client**. Elle permet la gestion centralisée de machines virtuelles, de ressources réseau et de stockage, souvent utilisée en production dans les entreprises.

---

## 🧱 Composants clés

| Élément | Description |
|---------|-------------|
| **ESXi** | Hyperviseur bare-metal (s’installe directement sur un serveur) |
| **vCenter** | Interface de gestion centralisée (optionnelle) |
| **vSphere Client** | Interface web pour gérer un ESXi ou vCenter |
| **Datastore** | Stockage de fichiers VM (disques, ISOs…) |
| **VMNIC** | Interface réseau physique de l’hyperviseur |
| **VNIC** | Interface virtuelle d'une VM |
| **vSwitch** | Commutateur virtuel pour le trafic réseau |
| **Port Group** | Point de connexion logique pour les VMs ou services |
| **VMkernel** | Interface réseau système (gestion, iSCSI, vMotion…) |

---

## ⚙️ Types de port groups

| Type | Utilisation |
|------|-------------|
| **VM Network** | Connexion réseau des machines virtuelles |
| **VMkernel** | Services système de l’hyperviseur (vMotion, FT, management) |

---

## 🧰 Commandes utiles (en CLI via ESXi Shell)

| Commande                               | Description                               |
| -------------------------------------- | ----------------------------------------- |
| `esxcli network nic list`              | Affiche les interfaces physiques (VMNICs) |
| `esxcli network vswitch standard list` | Affiche les vSwitchs                      |
| `esxcli network ip interface list`     | Liste les interfaces VMkernel             |
| `esxcli system version get`            | Version d’ESXi installée                  |

---

## 🔧 PowerCLI (sous PowerShell)

```powershell
Connect-VIServer -Server esxi.local
Get-VM
New-VM -Name "TestVM" -ResourcePool "Pool1" -Datastore "DS1" -Template "Win10"
Start-VM -VM "TestVM"
```

---

## 🔎 Cas d’usage courant

- Déploiement et gestion de machines virtuelles
- Configuration réseau (vSwitch, VLAN, interfaces VMkernel)
- Supervision des performances via vCenter
- Snapshots, clones, sauvegardes

---

## ⚠️ Erreurs fréquentes

- Mauvais choix de type de port group : confusion entre VMkernel et VM Network
- Interfaces VMkernel mal configurées → accès distant impossible
- Problèmes de performances dus à un mauvais plan d’adressage ou manque de ressources
- Sauvegardes corrompues faute de snapshots correctement gérés

---

## ✅ Bonnes pratiques

- Séparer les réseaux de gestion, stockage, VM et vMotion via des VLAN
- Utiliser des noms explicites pour les vSwitch et port groups
- Documenter les ressources allouées à chaque VM (CPU, RAM, stockage)
- Mettre en place un monitoring (via vCenter ou outil tiers comme Veeam One)
- Planifier des sauvegardes régulières et des tests de restauration

---

## 📚 Ressources complémentaires

- [VMware Docs vSphere]https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)
- [PowerCLI Documentation](https://developer.broadcom.com/powercli)