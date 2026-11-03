---
title: "Vie du logiciel : Proxmox VE 8"
description: "Logiciels qui s'installent et se gèrent sur Proxmox VE 8. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier Vie-du-systeme."
published: true
date: 2026-11-03T14:22:28Z
tags: ["vie-du-logiciel", "sommaire", "proxmoxve8"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Vie du logiciel : Proxmox VE 8

- **Tags** : `vie-du-logiciel`, `sommaire`, `proxmoxve8`

Logiciels qui s'installent et se gèrent sur Proxmox VE 8. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Corosync

- [Hote Proxmox VE 8 Cluster Creer](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-creer)
- [Hote Proxmox VE 8 Cluster Maintenance](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-maintenance)
- [Hote Proxmox VE 8 Cluster Preparer](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer)
- [Hote Proxmox VE 8 Cluster Securiser](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser)
- [Hote Proxmox VE 8 Cluster Valider](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-valider)

### Proxmox OpenStack

- Fiche d'entrée : [catalogue Proxmox-OpenStack](/fr/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-proxmox-openstack) (statut : Partiel)
- [VM Proxmox VE 8 Proxmox OpenStack Choix Architecture](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-choix-architecture)
- [VM Proxmox VE 8 Proxmox OpenStack Explorer APIs](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-explorer-apis)
- [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-mise-a-jour-retour-arriere)
- [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-nettoyer-retour-arriere)
- [VM Proxmox VE 8 Proxmox OpenStack Preparer Lab](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-preparer-lab)
- [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-sauvegarder-restaurer-lab)
- [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-securiser-valider-lab)

### Zabbix

- Fiche d'entrée : [catalogue Zabbix](/fr/01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-zabbix) (statut : Couvert)
- [Proxmox VE 8 Supervision Zabbix Snmp](/fr/01-fiches-simples/proxmox/ve-8/vie-du-logiciel/zabbix/fiche-simple-proxmox-ve-8-supervision-zabbix-snmp)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.


### Sauvegarde, restauration et PRA / PCA

- [Bacula](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bacula) — Couvert
- [Bareos](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bareos) — Couvert
- [BorgBackup](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-borgbackup) — Couvert
- [Nakivo-Altaro](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24-04; Altaro/Hornetsecurity limité à la documentation publique de [[Glossary:VM]] Backup
- [Proxmox-Backup-Server](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-proxmox-backup-server) — Couvert
- [Restic](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-restic) — Couvert
- [Robocopy](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-robocopy) — Couvert
- [Veeam-Backup-Replication](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-veeam-backup-replication) — Couvert
- [rsync](/fr/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-rsync) — Couvert

### Virtualisation et conteneurisation

- [Docker-Docker-Compose](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-docker-docker-compose) — Couvert
- [Kubernetes-K3s](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-kubernetes-k3s) — Couvert
- [Microsoft-Hyper-V](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-microsoft-hyper-v) — Couvert
- [Nutanix-AHV](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-nutanix-ahv) — Matériel/éditeur propriétaire — hors périmètre pas à pas
- [Podman-Buildah](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-podman-buildah) — Couvert
- [Proxmox-VE](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-proxmox-ve) — Couvert
- [VMware-vSphere](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere) — Couvert — vSphere 8 : ESXi, vCenter Server Appliance (installation, sauvegarde/restauration VAMI, mises à jour, certificats), HA/DRS, réseau, datastore [[Glossary:NFS]], snapshots, maintenance. Hors périmètre : vSAN, NSX, Lifecycle Manager avancé.