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

- [Diagnostic LXC Alpine — réseau et services](../../02-Fiches-Completes/Alpine/Toutes-versions/Diagnostic/17_Diagnostic_LXC_Alpine_Reseau_Services.md)
- [Diagnostic réseau complet multi-OS](../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/15_Depannage_Reseau_Diagnostic_Complet_Multi_OS.md)
- [Diagnostic NAS, SAN, Samba, NFS, iSCSI](../../02-Fiches-Completes/Transverses/Multi-OS/Diagnostic/38_Diagnostic_NAS_SAN_Samba_NFS_iSCSI.md)
- [Diagnostic réseau OPNsense — flux, DNS, VPN](../../02-Fiches-Completes/OPNsense/Toutes-versions/Diagnostic/35_Diagnostic_Reseau_OPNsense_Flux_DNS_VPN.md)
- [Diagnostic Proxmox VE — cluster, stockage, VM](../../02-Fiches-Completes/Proxmox/Toutes-versions/Diagnostic/34_Diagnostic_Proxmox_VE_Cluster_Stockage_VM.md)

### Sauvegarde, restauration et haute disponibilité

- [Sauvegarde et restauration LXC Alpine en production](../../02-Fiches-Completes/Alpine/Toutes-versions/Autres/18_Alpine_LXC_Sauvegarde_Restauration_Production.md)
- [Sauvegarde et restauration BorgBackup Debian 12](../../02-Fiches-Completes/Debian/12/Autres/19_Sauvegarde_Restauration_BorgBackup_Debian_12.md)
- [Sauvegarde et restauration Ubuntu Server avec Restic](../../02-Fiches-Completes/Ubuntu/Toutes-versions/Autres/29_Sauvegarde_Restauration_Ubuntu_Server_Restic.md)
- [Sauvegarde et restauration des données utilisateur Windows](../../02-Fiches-Completes/Windows/Toutes-versions/Autres/27_Sauvegarde_Restauration_Donnees_Utilisateur_Windows.md)
- [Reprise de forêt AD DS Windows Server 2022](../../02-Fiches-Completes/Windows/Server-2022/Autres/26_Reprise_Foret_AD_DS_Windows_Server_2022.md)
- [Sauvegarde et restauration des stacks Docker](../../02-Fiches-Completes/Transverses/Docker/Autres/37_Sauvegarde_Restauration_Stacks_Docker.md)
- [Sauvegarde et restauration de la configuration OPNsense](../../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/36_Sauvegarde_Restauration_Configuration_OPNsense.md)
- [Proxmox Backup Server 3.x — déduplication](../../02-Fiches-Completes/Proxmox/Toutes-versions/Autres/12_Proxmox_Backup_Server_3x_PBS_Deduplication.md)
- [Haute disponibilité Keepalived VRRP et HAProxy](../../02-Fiches-Completes/Transverses/Multi-OS/Autres/08_Haute_Disponibilite_Keepalived_VRRP_HAProxy.md)
- [Pare-feu OPNsense — CARP et pfSync en haute disponibilité](../../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/10_Pare_Feu_Appliance_OPNsense_CARP_pfSync_HA.md)

### Durcissement

- [Durcissement de l'hôte Docker en production](../../02-Fiches-Completes/Transverses/Docker/Autres/32_Hardening_Hote_Docker_Production.md)
- [Durcissement de Rocky Linux 9 en production](../../02-Fiches-Completes/Rocky-Linux/9/Autres/24_Hardening_Production_Rocky_Linux_9.md)
- [Durcissement de Windows Server 2025 en production](../../02-Fiches-Completes/Windows/Server-2025/Autres/31_Hardening_Windows_Server_2025_Production.md)

### Conception

- [Conception DMZ et segmentation des flux multi-OS](../../02-Fiches-Completes/Transverses/Multi-OS/Autres/86_Conception_DMZ_Segmentation_Flux_Multi_OS.md)

## Suivi quotidien (modèle à copier)

| Date | OS / machine | Fiche utilisée | Résultat | Anomalie et référence diagnostic |
|---|---|---|---|---|
| | | | | |

## Voir aussi

- [Fiches d'aide informatique — références rapides](Fiches-Aide-Informatique.md)
- [Documentation officielle des logiciels](../02-Documentation-Officielle/Liens-Docs-Logicielles.md)
- [Hub de veille CVE](../04-Veille-CVE/Hub-CVE.md)
