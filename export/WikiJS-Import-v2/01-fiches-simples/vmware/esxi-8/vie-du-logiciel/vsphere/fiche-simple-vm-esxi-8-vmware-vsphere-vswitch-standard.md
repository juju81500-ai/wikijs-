---
title: "Fiche Simple - VM ESXi 8 VMware vSphere vSwitch Standard"
description: "Créer un vSwitch standard de laboratoire sans déconnecter la gestion ni détourner un uplink utilisé."
published: true
date: 2026-10-29T20:49:11Z
tags: ["vmware-vsphere", "vsphere8", "vswitch", "reseau", "standard-switch"]
editor: markdown
dateCreated: 2026-10-29T20:49:11Z
dateModified: 2026-10-29T20:49:11Z
---

# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_vSwitch_Standard

- **Environnement** : Hôte ESXi 8.x isolé de laboratoire; NIC physique libre si liaison externe
- **OS / Version** : VMware ESXi 8.x / vCenter Server 8.x
- **Catégorie** : virtualisation / réseau
- **Tags** : `vmware-vsphere`, `vsphere8`, `vswitch`, `reseau`, `standard-switch`

---

## Problème précis à résoudre

Créer un vSwitch standard de laboratoire sans déconnecter la gestion ni détourner un uplink utilisé.

## 1. Hors-Production (Lab / Test / POC)

1. Dans vSphere Client : **Hôte ESXi > Configurer > Réseau > Commutateurs virtuels > Ajouter une mise en réseau**. Choisir **Réseau de machine virtuelle > Nouveau commutateur standard**; sélectionner une NIC seulement si elle est libre et nécessaire.
   👉 Explication : sans uplink, un switch convient à un segment interne isolé. Ne jamais déplacer la NIC de gestion sans accès console.
2. Créer `vSwitch_LAB` et port group `PG_LAB` (noms à remplacer). N'appliquer un VLAN que si sa valeur correspond au réseau validé.
   👉 Explication : VLAN/MTU incorrects peuvent interrompre des services.
3. Équivalent PowerCLI documenté pour une NIC libre (remplacer les valeurs) :
   ```powershell
   $vmhost = Get-VMHost -Name 'ESXI_LAB_FQDN'
   New-VirtualSwitch -VMHost $vmhost -Name 'vSwitch_LAB' -Nic 'VMNIC_LIBRE_A_REMPLACER'
   ```
   👉 Explication : omettre `-Nic` pour un segment interne; vérifier que la NIC n'est affectée à aucun autre switch.
4. Contrôler **Hôte > Configurer > Réseau > Commutateurs virtuels** et `esxcli network vswitch standard list` (lecture seule).
   👉 Explication : comparer uplinks et groupes de ports au schéma prévu.

## 2. Production — Contrôles

- Vérifier redondance, VLAN, MTU, teaming/failover, accès console et fenêtre approuvée avant changement.

## 3. Production — Sécurité

- Séparer gestion, stockage, vMotion et trafic invité; ne pas relier une VM non maîtrisée au réseau de gestion.

## Validation et retour arrière

- **Validation** : VM jetable sur le port group communique uniquement avec les hôtes prévus. **Retour arrière** : éteindre la VM, retirer ses cartes puis supprimer seulement les objets sans dépendance.

## Si le problème n'est pas résolu

- [Broadcom PowerCLI — New-VirtualSwitch](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/new-virtualswitch)
- [Broadcom ESXCLI — commandes réseau](https://developer.broadcom.com/xapis/esxcli-command-reference/latest/namespace/esxcli_network.html)
- [Broadcom — Documentation vSphere](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)