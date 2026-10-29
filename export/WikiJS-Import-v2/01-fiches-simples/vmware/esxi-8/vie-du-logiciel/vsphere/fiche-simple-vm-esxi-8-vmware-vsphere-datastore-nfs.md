---
title: "Fiche Simple - VM ESXi 8 VMware vSphere Datastore NFS"
description: "Ajouter un datastore NFS de laboratoire sans toucher aux banques VMFS de production ni aux données existantes."
published: true
date: 2026-10-29T20:49:36Z
tags: ["vmware-vsphere", "vsphere8", "datastore", "nfs", "stockage"]
editor: markdown
dateCreated: 2026-10-29T20:49:36Z
dateModified: 2026-10-29T20:49:36Z
---

# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_Datastore_NFS

- **Environnement** : vCenter Server et ESXi 8.x de laboratoire; serveur NFS de test
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / stockage
- **Tags** : `vmware-vsphere`, `vsphere8`, `datastore`, `nfs`, `stockage`

---

## Problème précis à résoudre

Ajouter un datastore NFS de laboratoire sans toucher aux banques VMFS de production ni aux données existantes.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier serveur NFS, export, résolution, accès réseau et autorisations. Procédure limitée à NFS 3.
   👉 Explication : ne jamais monter un export dont le contenu ou les droits sont inconnus.
2. Dans vSphere Client : **Hôte ESXi > Configurer > Stockage > Banques de données > Nouvelle banque de données**. Choisir **NFS > NFS 3**, puis renseigner `NFS_LAB`, `SERVEUR_NFS_LAB` et `/EXPORT_LAB` (valeurs à remplacer).
   👉 Explication : confirmer protocole et chemin auprès de l'administrateur stockage avant de terminer.
3. Équivalent PowerCLI, connecté au vCenter du lab (remplacer les valeurs en majuscules) :
   ```powershell
   $vmhost = Get-VMHost -Name 'ESXI_LAB_FQDN'
   New-Datastore -Nfs -VMHost $vmhost -Name 'NFS_LAB' -Path '/EXPORT_LAB' -NfsHost 'SERVEUR_NFS_LAB'
   ```
   👉 Explication : `New-Datastore -Nfs` crée le montage. Les placeholders sont « à remplacer »; aucun secret dans le script.
4. Vérifier dans l'inventaire puis en lecture seule : `esxcli storage filesystem list`.
   👉 Explication : contrôler nom et point de montage sans modifier le serveur NFS.

## 2. Production — Contrôles

- Tester compatibilité, permissions, réseau, capacité et sauvegarde avec le fournisseur; approuver fenêtre et retour arrière.

## 3. Production — Sécurité

- Limiter l’export au réseau/hôtes requis; ne pas en faire l’unique sauvegarde et ne pas supprimer/reformater l’export pour diagnostiquer.

## Validation et retour arrière

- **Validation** : datastore monté et données de test vérifiées. **Retour arrière** : après arrêt/retrait des VM, démonter dans vSphere; supprimer l’export uniquement avec l’accord de son propriétaire.

## Si le problème n'est pas résolu

- [Broadcom PowerCLI — New-Datastore](https://developer.broadcom.com/powercli/latest/vmware.vimautomation.core/commands/new-datastore)
- [Broadcom ESXCLI — commandes stockage](https://developer.broadcom.com/xapis/esxcli-command-reference/latest/namespace/esxcli_storage.html)
- [Broadcom — Documentation vSphere](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere.html)