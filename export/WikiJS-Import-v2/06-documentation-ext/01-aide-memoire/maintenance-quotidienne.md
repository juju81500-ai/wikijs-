---
title: "Maintenance quotidienne — aide-mémoire"
description: "Routine courte à réaliser chaque jour sur les machines du pack. Elle renvoie vers les fiches internes du pack : les fiches simples (01-Fiches-Simples/) et les fiches complètes (02-Fiches-Completes/) sont séparées."
published: true
date: 2026-10-29T10:46:11Z
tags: ["maintenance", "aide-memoire", "quotidien", "exploitation"]
editor: markdown
dateCreated: 2026-10-29T10:46:11Z
dateModified: 2026-10-29T10:46:11Z
---

# Maintenance quotidienne — aide-mémoire

Routine courte à réaliser chaque jour sur les machines du pack. Elle renvoie vers les fiches internes du pack : les fiches simples (`01-Fiches-Simples/`) et les fiches complètes (`02-Fiches-Completes/`) sont séparées.

- **Tags** : `maintenance`, `aide-memoire`, `quotidien`, `exploitation`
- **Périmètre** : fiches internes du pack uniquement. Les procédures restent à valider sur le système et la version réellement déployés.

## Routine quotidienne (environ 10 minutes)

1. Vérifier les mises à jour de sécurité de chaque OS (voir la section par OS).
2. Contrôler l'espace disque et l'état des services critiques.
3. Vérifier que les sauvegardes de la veille sont terminées. Un test de restauration a lieu chaque semaine.
4. Relire les alertes de supervision et les journaux d'erreurs récents.
5. Compléter la fiche d'installation du jour : version, date, résultat, anomalies rencontrées.
6. En cas d'anomalie, ouvrir la fiche de diagnostic correspondante et noter la référence dans le suivi.

## Fiches simples par OS

| Famille | Version | Nombre de fiches simples | Dossier |
|---|---|---|---|
| Alpine | 3.19 | 8 | `01-Fiches-Simples/Alpine/3.19/` |
| Alpine | Toutes-versions | 4 | `01-Fiches-Simples/Alpine/Toutes-versions/` |
| Debian | 12 | 25 | `01-Fiches-Simples/Debian/12/` |
| Debian | 13 | 50 | `01-Fiches-Simples/Debian/13/` |
| Rocky-Linux | 9 | 12 | `01-Fiches-Simples/Rocky-Linux/9/` |
| Transverses | Cloud-SaaS | 3 | `01-Fiches-Simples/Transverses/Cloud-SaaS/` |
| Transverses | Docker | 16 | `01-Fiches-Simples/Transverses/Docker/` |
| TrueNAS | SCALE-25.10 | 1 | `01-Fiches-Simples/TrueNAS/SCALE-25.10/` |
| Ubuntu | 24.04 | 14 | `01-Fiches-Simples/Ubuntu/24.04/` |
| Ubuntu | 26.04 | 2 | `01-Fiches-Simples/Ubuntu/26.04/` |
| Ubuntu | Toutes-versions | 1 | `01-Fiches-Simples/Ubuntu/Toutes-versions/` |
| VMware | ESXi-8 | 1 | `01-Fiches-Simples/VMware/ESXi-8/` |
| Windows | Client-10 | 1 | `01-Fiches-Simples/Windows/Client-10/` |
| Windows | Client-11 | 12 | `01-Fiches-Simples/Windows/Client-11/` |
| Windows | Server-2022 | 30 | `01-Fiches-Simples/Windows/Server-2022/` |
| Windows | Server-2025 | 2 | `01-Fiches-Simples/Windows/Server-2025/` |
| Windows | Toutes-versions | 2 | `01-Fiches-Simples/Windows/Toutes-versions/` |
| pfSense | Toutes-versions | 2 | `01-Fiches-Simples/pfSense/Toutes-versions/` |

## Fiches complètes par OS

| Famille | Version | Installation-Deploiement | Diagnostic | Autres | Dossier |
|---|---|---|---|---|---|
| Alpine | Toutes-versions | 1 | 1 | 1 | `02-Fiches-Completes/Alpine/Toutes-versions/` |
| Debian | 12 | 8 | 0 | 1 | `02-Fiches-Completes/Debian/12/` |
| Debian | 13 | 25 | 0 | 0 | `02-Fiches-Completes/Debian/13/` |
| OPNsense | Toutes-versions | 1 | 1 | 2 | `02-Fiches-Completes/OPNsense/Toutes-versions/` |
| Proxmox | Toutes-versions | 0 | 1 | 1 | `02-Fiches-Completes/Proxmox/Toutes-versions/` |
| Proxmox | VE-8 | 1 | 0 | 0 | `02-Fiches-Completes/Proxmox/VE-8/` |
| Rocky-Linux | 9 | 2 | 0 | 1 | `02-Fiches-Completes/Rocky-Linux/9/` |
| Transverses | Cloud-SaaS | 3 | 0 | 0 | `02-Fiches-Completes/Transverses/Cloud-SaaS/` |
| Transverses | Docker | 5 | 0 | 2 | `02-Fiches-Completes/Transverses/Docker/` |
| Transverses | Multi-OS | 2 | 2 | 2 | `02-Fiches-Completes/Transverses/Multi-OS/` |
| TrueNAS | SCALE-25.10 | 1 | 0 | 0 | `02-Fiches-Completes/TrueNAS/SCALE-25.10/` |
| Ubuntu | 22.04 | 1 | 0 | 0 | `02-Fiches-Completes/Ubuntu/22.04/` |
| Ubuntu | 24.04 | 4 | 0 | 0 | `02-Fiches-Completes/Ubuntu/24.04/` |
| Ubuntu | 26.04 | 2 | 0 | 0 | `02-Fiches-Completes/Ubuntu/26.04/` |
| Ubuntu | Toutes-versions | 0 | 0 | 1 | `02-Fiches-Completes/Ubuntu/Toutes-versions/` |
| VMware | ESXi-8 | 1 | 0 | 0 | `02-Fiches-Completes/VMware/ESXi-8/` |
| Windows | Client-11 | 3 | 0 | 0 | `02-Fiches-Completes/Windows/Client-11/` |
| Windows | Server-2022 | 5 | 0 | 1 | `02-Fiches-Completes/Windows/Server-2022/` |
| Windows | Server-2025 | 1 | 0 | 1 | `02-Fiches-Completes/Windows/Server-2025/` |
| Windows | Toutes-versions | 0 | 0 | 1 | `02-Fiches-Completes/Windows/Toutes-versions/` |
| pfSense | Toutes-versions | 1 | 0 | 0 | `02-Fiches-Completes/pfSense/Toutes-versions/` |

## Fiches complètes de diagnostic et d'exploitation

### Diagnostic

- [Diagnostic LXC Alpine — réseau et services](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services)
- [Diagnostic réseau complet multi-OS](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os)
- [Diagnostic NAS, SAN, Samba, NFS, iSCSI](/02-fiches-completes/transverses/multi-os/diagnostic/38-diagnostic-nas-san-samba-nfs-iscsi)
- [Diagnostic réseau OPNsense — flux, DNS, VPN](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn)
- [Diagnostic Proxmox VE — cluster, stockage, VM](/02-fiches-completes/proxmox/toutes-versions/diagnostic/34-diagnostic-proxmox-ve-cluster-stockage-vm)

### Sauvegarde, restauration et haute disponibilité

- [Sauvegarde et restauration LXC Alpine en production](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production)
- [Sauvegarde et restauration BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)
- [Sauvegarde et restauration Ubuntu Server avec Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic)
- [Sauvegarde et restauration des données utilisateur Windows](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows)
- [Reprise de forêt AD DS Windows Server 2022](/02-fiches-completes/windows/server-2022/autres/26-reprise-foret-ad-ds-windows-server-2022)
- [Sauvegarde et restauration des stacks Docker](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker)
- [Sauvegarde et restauration de la configuration OPNsense](/02-fiches-completes/opnsense/toutes-versions/autres/36-sauvegarde-restauration-configuration-opnsense)
- [Proxmox Backup Server 3.x — déduplication](/02-fiches-completes/proxmox/toutes-versions/autres/12-proxmox-backup-server-3x-pbs-deduplication)
- [Haute disponibilité Keepalived VRRP et HAProxy](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy)
- [Pare-feu OPNsense — CARP et pfSync en haute disponibilité](/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha)

### Durcissement

- [Durcissement de l'hôte Docker en production](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production)
- [Durcissement de Rocky Linux 9 en production](/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9)
- [Durcissement de Windows Server 2025 en production](/02-fiches-completes/windows/server-2025/autres/31-hardening-windows-server-2025-production)

### Conception

- [Conception DMZ et segmentation des flux multi-OS](/02-fiches-completes/transverses/multi-os/autres/86-conception-dmz-segmentation-flux-multi-os)

## Suivi quotidien (modèle à copier)

| Date | OS / machine | Fiche utilisée | Résultat | Anomalie et référence diagnostic |
|---|---|---|---|---|
| | | | | |

## Voir aussi

- [Fiches d'aide informatique — références rapides](/06-documentation-ext/01-aide-memoire/fiches-aide-informatique)
- [Documentation officielle des logiciels](/06-documentation-ext/02-documentation-officielle/liens-docs-logicielles)
- [Hub de veille CVE](/06-documentation-ext/04-veille-cve/hub-cve)