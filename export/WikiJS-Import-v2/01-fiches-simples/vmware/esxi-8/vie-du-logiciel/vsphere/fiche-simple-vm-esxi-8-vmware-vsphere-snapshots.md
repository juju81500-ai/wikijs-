---
title: "Fiche Simple - VM ESXi 8 VMware vSphere Snapshots"
description: "Créer et gérer un snapshot temporaire avant un test réversible sans le confondre avec une sauvegarde."
published: true
date: 2026-10-29T20:49:11Z
tags: ["vmware-vsphere", "vsphere8", "snapshot", "vm", "restauration"]
editor: markdown
dateCreated: 2026-10-29T20:49:11Z
dateModified: 2026-10-29T20:49:11Z
---

# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_Snapshots

- **Environnement** : vCenter Server 8.x et VM jetable de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / protection des VM
- **Tags** : `vmware-vsphere`, `vsphere8`, `snapshot`, `vm`, `restauration`

---

## Problème précis à résoudre

Créer et gérer un snapshot temporaire avant un test réversible sans le confondre avec une sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler espace du datastore, sauvegarde indépendante des données à conserver et durée de conservation.
   👉 Explication : les deltas peuvent croître et remplir le datastore; un snapshot n'est pas une sauvegarde.
2. Dans vSphere Client : VM jetable > **Snapshots > Prendre un snapshot**. Donner nom/motif explicites; ne pas capturer la mémoire sans besoin précis.
   👉 Explication : conserver brièvement et tenir compte de l'impact stockage.
3. Équivalent PowerCLI documenté; remplacer le nom de VM et vérifier la cible :
   ```powershell
   $vm = Get-VM -Name 'VM_LAB_A_REMPLACER'
   New-Snapshot -VM $vm -Name 'Avant_Test' -Description 'Snapshot temporaire de laboratoire'
   Get-Snapshot -VM $vm
   ```
   👉 Explication : `VM_LAB_A_REMPLACER` est un placeholder « à remplacer »; aucun secret n'est requis.
4. Pour retirer, ouvrir **Snapshots > Gérer les snapshots**, sélectionner le snapshot attendu et supprimer. Si consolidation requise, vérifier capacité et sauvegarde avant **Consolider**.
   👉 Explication : la fusion peut durer; ne jamais supprimer les fichiers `*-delta.vmdk` à la main ni interrompre l'hôte.

## 2. Production — Contrôles

- Appliquer durée maximale, suivi d’espace, sauvegarde vérifiée et procédure de consolidation; contrôler l’impact applicatif.

## 3. Production — Sécurité

- Restreindre le droit de gestion; ne pas utiliser Revert/Delete All/consolidation sans vérifier VM, restauration et capacité.

## Validation et retour arrière

- **Validation** : snapshot retiré/consolidé et alerte absente. **Retour arrière** : Revert seulement vers le snapshot exact validé et après approbation; une sauvegarde indépendante reste le moyen de reprise.

## Si le problème n'est pas résolu

- [Broadcom PowerCLI — New-Snapshot](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/new-snapshot)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)
- [Broadcom KB — Bonnes pratiques snapshots](https://knowledge.broadcom.com/external/article/318825/best-practices-for-using-vmware-snapshot.html)