---
title: "Fiche Simple - VM ESXi 8 VMware vSphere vMotion VMkernel"
description: "Préparer le VMkernel vMotion et vérifier les prérequis d’une migration de test, sans déclencher de migration en production."
published: true
date: 2026-10-29T20:49:11Z
tags: ["vmware-vsphere", "vsphere8", "vmotion", "vmkernel", "reseau"]
editor: markdown
dateCreated: 2026-10-29T20:49:11Z
dateModified: 2026-10-29T20:49:11Z
---

# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_vMotion_VMkernel

- **Environnement** : vCenter Server 8.x et deux hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / réseau / mobilité
- **Tags** : `vmware-vsphere`, `vsphere8`, `vmotion`, `vmkernel`, `reseau`

---

## Problème précis à résoudre

Préparer le VMkernel vMotion et vérifier les prérequis d’une migration de test, sans déclencher de migration en production.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer deux hôtes gérés par le même vCenter, compatibilité CPU, réseau VMkernel joignable et stockage compatible/partagé si les disques ne sont pas migrés.
   👉 Explication : réseau vMotion seul ne rend pas les disques partagés; capacités/licences dépendent de l'édition et du type de migration.
2. Dans vSphere Client : **Hôte ESXi > Configurer > Réseau > Adaptateurs VMkernel > Ajouter une mise en réseau**. Créer un VMkernel sur le port group prévu, activer **vMotion**, puis attribuer l'IP/masque réservés; répéter sur le second hôte.
   👉 Explication : éviter doublons IP et activation sur le réseau de gestion non conçu pour cet usage.
3. Contrôles en lecture seule :
   ```shell
   esxcli network ip interface list
   esxcli network vswitch standard list
   ```
   👉 Explication : contrôler VMkernel, port group et uplinks sans changement.
4. Inspection facultative PowerCLI (nom à remplacer) :
   ```powershell
   $vmhost = Get-VMHost -Name 'ESXI_LAB_FQDN'
   Get-VMHostNetworkAdapter -VMHost $vmhost -VMKernel | Format-List *
   ```
   👉 Explication : le cmdlet documenté retourne les interfaces VMkernel; garder les modifications réseau dans l’assistant GUI.
5. Sélectionner une VM jetable > **Actions > Migrer > Modifier la ressource de calcul**, choisir l'hôte de test et relire le résumé avant lancement.
   👉 Explication : annuler si compatibilité ou prérequis échouent.

## 2. Production — Contrôles

- Contrôler CPU/EVC, licences, versions, datastore, MTU/routage, charge et fenêtre approuvée; effectuer d’abord une migration de test.

## 3. Production — Sécurité

- Isoler vMotion sur réseau protégé; autoriser seulement les hôtes nécessaires et ne pas exposer les interfaces d’administration.

## Validation et retour arrière

- **Validation** : migration jetable terminée, destination et stockage vérifiés. **Retour arrière** : migrer la VM de test vers l’hôte initial après contrôle; ne retirer un VMkernel qu’après vérification d’absence de flux.

## Si le problème n'est pas résolu

- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)
- [Broadcom ESXCLI — commandes réseau](https://developer.broadcom.com/xapis/esxcli-command-reference/latest/namespace/esxcli_network.html)
- [Broadcom PowerCLI — Get-VMHostNetworkAdapter](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/get-vmhostnetworkadapter)