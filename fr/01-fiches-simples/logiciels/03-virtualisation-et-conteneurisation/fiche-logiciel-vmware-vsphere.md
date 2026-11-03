---
title: "VMware vSphere"
description: "Couvert — [guide ESXi 8.0](../../../02-fiches-completes/vmware/esxi-8/installation-deploiement/56-deploiement-vmware-esxi-8-0.md) et série vSphere 8 : installation du VCSA, sauvegarde/restauration VAMI, mises à jour, certificats, HA, [[Glossary:DRS]], datastore NFS, vSwitch standard, réseau vMotion,"
published: true
date: 2026-11-03T14:22:28Z
tags: ["logiciel", "03-virtualisation-et-conteneurisation", "couvert"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# 📄 VMware vSphere

- **Catégorie** : Virtualisation et conteneurisation
- **Plateforme** : Appliance / bare-metal
- **Produit (matrice)** : VMware vSphere (ESXi / vCenter)
- **Statut dans le pack** : Couvert — vSphere 8 : ESXi, vCenter Server Appliance (installation, sauvegarde/restauration VAMI, mises à jour, certificats), HA/DRS, réseau, datastore [[Glossary:NFS]], snapshots, maintenance. Hors périmètre : vSAN, NSX, Lifecycle Manager avancé.
- **Tags** : `logiciel`, `03-virtualisation-et-conteneurisation`, `couvert`

## 📚 Couverture dans le pack

Couvert — [guide ESXi 8.0](/fr/02-fiches-completes/vmware/esxi-8/installation-deploiement/56-deploiement-vmware-esxi-8-0) et série vSphere 8 : installation du VCSA, sauvegarde/restauration VAMI, mises à jour, certificats, HA, [[Glossary:DRS]], datastore NFS, vSwitch standard, réseau vMotion, snapshots et maintenance d'hôte. Non couverts : vSAN, NSX, Lifecycle Manager avancé, vSphere avec Tanzu.🧭 Utilisation

Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Fiches simples du guide : [valider le matériel et le droit d'usage](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-valider-materiel-droits), [installer ESXi](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-installer-hote), [configurer les services essentiels](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-configurer-services-essentiels), [ajouter vCenter et un premier invité](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-ajouter-vcenter-premier-invite), [vérification et maintenance](/fr/01-fiches-simples/vmware/esxi-8/vie-du-systeme/fiches-par-theme/installation/fiche-simple-hote-vmware-esxi-8-esxi-verifier-maintenir), [créer un datastore NFS](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-datastore-nfs), [créer un vSwitch standard](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vswitch-standard), [préparer vMotion](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vmotion-vmkernel), [gérer les snapshots](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-snapshots), [mettre un hôte en maintenance](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-maintenance-hote)., [Certificats](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-certificats), [DRS](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-drs), [HA](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-ha), [VCSA Installer](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-installer), [VCSA Mises A Jour](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-mises-a-jour), [VCSA Sauvegarde Restauration VAMI](/fr/01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-sauvegarde-restauration-vami)