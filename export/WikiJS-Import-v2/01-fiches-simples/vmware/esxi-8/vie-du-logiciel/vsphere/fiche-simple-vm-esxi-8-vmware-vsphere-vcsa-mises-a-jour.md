---
title: "Fiche Simple - VM ESXi 8 VMware vSphere VCSA Mises A Jour"
description: "Mettre à jour le VCSA par la VAMI avec un retour arrière préparé."
published: true
date: 2026-10-29T21:24:09Z
tags: ["vmware-vsphere", "vsphere8", "vcenter", "vcsa", "vami", "mise-a-jour"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_ESXi_8_VMware_vSphere_VCSA_Mises_A_Jour

- **Environnement** : vCenter Server Appliance 8.x et hôtes ESXi 8.x de laboratoire
- **OS / Version** : VMware vSphere 8.x
- **Catégorie** : virtualisation / vCenter
- **Tags** : `vmware-vsphere`, `vsphere8`, `vcenter`, `vcsa`, `vami`, `mise-a-jour`

---

## Problème précis à résoudre

Mettre à jour le VCSA par la VAMI avec un retour arrière préparé.

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute mise à jour : lancer une sauvegarde VAMI et prendre un snapshot de la VM VCSA (éteint ou à chaud, selon la documentation Broadcom).
   👉 Explication : le snapshot est un retour arrière court, pas une sauvegarde.
2. Consulter les notes de version et la matrice d'interopérabilité (ESXi, sauvegarde, produits tiers).
   👉 Explication : un VCSA mis à jour avant ses hôtes ou produits liés peut devenir incompatible.
3. Dans la VAMI : **Mettre à jour > Rechercher des mises à jour** (dépôt en ligne ou ISO attaché), puis **Mettre en place** et **Installer**.
   👉 Explication : la mise à jour redémarre les services ; attendre la fin avant de reconnecter les clients.
4. Mettre ensuite à jour les hôtes ESXi : voir la fiche Maintenance_Hote.
   👉 Explication : les hôtes se mettent à jour après le vCenter.

## 2. Production — Contrôles

- Mise à jour en fenêtre de maintenance, hôtes en état stable, DRS/HA contrôlés (voir fiches HA et DRS).

## 3. Production — Sécurité

- Télécharger les mises à jour depuis le portail officiel et vérifier les sommes de contrôle ; supprimer le snapshot après validation.

## Validation et retour arrière

- **Validation** : la version affichée dans la VAMI correspond à la cible et les services démarrent. **Retour arrière** : revenir au snapshot VCSA ou restaurer la sauvegarde VAMI.

## Si le problème n'est pas résolu

- [Fiche d'entrée VMware vSphere](/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere)
- [Fiche voisine — Maintenance hôte](/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-maintenance-hote)
- [Fiche voisine — Snapshots vSphere](/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-snapshots)
- [Broadcom — Documentation vSphere 8](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0.html)