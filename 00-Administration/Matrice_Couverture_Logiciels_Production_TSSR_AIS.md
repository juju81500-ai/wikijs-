# Matrice de couverture des logiciels de production TSSR / AIS

Cette matrice reprend la liste maximale fournie et la compare au contenu actuellement présent dans `01-Fiches-Simples` et `02-Fiches-Completes`. Elle sert de registre de travail : un produit cité dans un guide générique n'est pas considéré comme ayant une fiche dédiée.

Pour les mémos, scripts communautaires, listes d'outils et requêtes GitHub, consulter le [référentiel externe Sysadmin/TSSR](../06-Documentation-ext/05-Referentiel-GitHub/Github-TSSR.md); ses liens sont des pistes à vérifier et non des procédures de production approuvées.

**État au 27 octobre 2026 :** 86 guides complets sont référencés dans la [matrice de revue](Matrice_Controle_Fiches_Completes_et_Questions_Reponses.md); après l'ajout du guide DMZ, le validateur a contrôlé 291 documents. Le contrôle structurel ne prouve pas le fonctionnement technique ni un essai en production.

## Légende

| État | Sens |
|---|---|
| `Couvert` | Guide complet dédié et/ou fiche simple spécifique présents; voir la référence. |
| `Partiel` | Cité comme composant ou traité dans une procédure générique, sans fiche dédiée couvrant le produit. |
| `Manquant` | Pas de fiche spécifique identifiée dans le pack. |
| `Défensif uniquement` | Pas de fiche opérationnelle offensive; seuls l'administration défensive, la détection et les labs isolés sont envisageables. |

## 1. Gestion de parc, ticketing et inventaire

| Produit | Plateforme | État / référence |
|---|---|---|
| GLPI | Linux / Windows | Couvert — [guide GLPI](../02-Fiches-Completes/Debian/12/Installation-Deploiement/03_Helpdesk_ITSM_GLPI_11_12_Debian_12_13.md) et fiches simples par étape |
| OCS Inventory | Linux / Windows | Couvert — [guide OCS Inventory](../02-Fiches-Completes/Debian/13/Installation-Deploiement/41_Deploiement_OCS_Inventory_3_Debian_13.md) et fiches simples par étape |
| Snipe-IT | Linux / Windows | Couvert — [guide Snipe-IT](../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/39_Deploiement_Snipe_IT_8_Docker_MariaDB_Traefik.md) et fiches simples par étape |
| Jira Service Management | Cloud/SaaS | Couvert — [guide JSM](../02-Fiches-Completes/Transverses/Cloud-SaaS/Installation-Deploiement/43_Deploiement_Jira_Service_Management_Cloud_ITSM.md) et fiches simples par étape |
| OTRS / Znuny | Linux | Couvert — [guide Znuny](../02-Fiches-Completes/Debian/12/Installation-Deploiement/42_Deploiement_Znuny_7_3_8_Debian_12.md) et fiches simples par étape |
| Lansweeper | Windows | Couvert — [guide Lansweeper](../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/44_Deploiement_Lansweeper_Classic_Windows_Server.md) et fiches simples par étape |
| iTop | Linux | Couvert — [guide iTop](../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/40_Deploiement_iTop_3.3_Debian12_Ubuntu2404.md) et fiches simples par étape |

## 2. Supervision, métrologie, logs et observabilité

| Produit | Plateforme | État / référence |
|---|---|---|
| Centreon | Linux | Couvert — [guide Centreon](../02-Fiches-Completes/Debian/13/Installation-Deploiement/48_Deploiement_Centreon_26.10_Debian_13.md) et fiches simples par étape |
| Zabbix | Linux | Couvert — [guide Zabbix](../02-Fiches-Completes/Debian/12/Installation-Deploiement/04_Supervision_Centralisee_Zabbix_70_LTS_Debian_12.md) et fiches simples par étape |
| PRTG Network Monitor | Windows | Couvert — [guide PRTG](../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/47_Deploiement_PRTG_Network_Monitor_Windows_Server.md) et fiches simples par étape |
| Prometheus + Grafana | Multiplateforme | Couvert — [guide Prometheus/Grafana](../02-Fiches-Completes/Debian/13/Installation-Deploiement/45_Deploiement_Prometheus_Grafana_Debian_13.md) et fiches simples par étape |
| Datadog | Cloud/SaaS | Couvert — [guide Datadog Agent](../02-Fiches-Completes/Transverses/Cloud-SaaS/Installation-Deploiement/52_Deploiement_Datadog_Agent_Linux_SaaS.md) et fiches simples par étape |
| Dynatrace | Cloud/SaaS | Couvert — [guide OneAgent](../02-Fiches-Completes/Transverses/Cloud-SaaS/Installation-Deploiement/53_Deploiement_Dynatrace_OneAgent_Linux_SaaS.md) et fiches simples par étape |
| Cacti | Linux | Couvert — [guide Cacti](../02-Fiches-Completes/Debian/12/Installation-Deploiement/51_Deploiement_Cacti_1.2.31_Debian_12.md) et fiches simples par étape |
| LibreNMS | Linux | Couvert — [guide LibreNMS](../02-Fiches-Completes/Ubuntu/26.04/Installation-Deploiement/46_Deploiement_LibreNMS_26.10.2_Ubuntu_26.04.md) et fiches simples par étape |
| Observium | Linux | Couvert pour l'édition Community sur Debian 13 — [guide](../02-Fiches-Completes/Debian/13/Installation-Deploiement/69_Deploiement_Observium_Community_Debian_13.md) et [fiche pilote SNMPv3](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Observium/Fiche_Simple_-_VM_Debian_13_Observium_Ajouter_Hote_SNMPv3.md) et fiches simples par étape |
| Graylog | Multiplateforme | Couvert — [guide Graylog](../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/49_Deploiement_Graylog_7.2_Ubuntu_24.04.md) et fiches simples par étape |
| ELK Stack | Multiplateforme | Couvert — [guide Elastic Stack](../02-Fiches-Completes/Debian/13/Installation-Deploiement/50_Deploiement_Elastic_Stack_9.5_Debian_13.md) et fiches simples par étape |
| Splunk Enterprise / Cloud | Multiplateforme / SaaS | Partiel — [guide Splunk Enterprise](../02-Fiches-Completes/Debian/12/Installation-Deploiement/54_Deploiement_Splunk_Enterprise_10.2_Debian_12.md); Splunk Cloud non documenté |

## 3. Virtualisation et conteneurisation

| Produit | Plateforme | État / référence |
|---|---|---|
| VMware vSphere (ESXi / vCenter) | Appliance / bare-metal | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_VMware-vSphere.md>) et fiches simples par étape |
| Microsoft Hyper-V | Windows Server | Couvert — [guide Hyper-V 2022](../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/55_Deploiement_Hyper_V_Windows_Server_2022.md) et fiches simples par étape |
| Proxmox VE | Appliance Debian | Couvert — [guide Proxmox VE](../02-Fiches-Completes/Proxmox/VE-8/Installation-Deploiement/09_Hyperviseur_Proxmox_VE_8x_Cluster_Corosync.md) et fiches simples par étape |
| Nutanix AHV | Appliance | Manquant |
| Docker / Docker Compose | Linux / Windows | Couvert — [guide de durcissement Docker](../02-Fiches-Completes/Transverses/Docker/Autres/32_Hardening_Hote_Docker_Production.md), [guide de sauvegarde Compose](../02-Fiches-Completes/Transverses/Docker/Autres/37_Sauvegarde_Restauration_Stacks_Docker.md) et fiches simples par étape |
| Kubernetes / K3s | Multiplateforme | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Kubernetes-K3s.md>) et fiches simples par étape |
| Podman / Buildah | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Podman-Buildah.md>) et fiches simples par étape |

## 4. Réseau et cybersécurité

| Produit / famille | Plateforme | État / référence |
|---|---|---|
| pfSense | Appliance / VM FreeBSD | Couvert pour pfSense CE 2.9.0 en laboratoire Proxmox — [guide](../02-Fiches-Completes/pfSense/Toutes-versions/Installation-Deploiement/70_Deploiement_pfSense_CE_2.9.0_Proxmox_Lab.md) et [fiche de validation](../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Administration-systeme/Fiche_Simple_-_pfSense_CE_2.9.0_Valider_Flux_Lab.md); appliance physique et production non couvertes et fiches simples par étape |
| OPNsense | Appliance FreeBSD | Couvert — [installation OPNsense](../02-Fiches-Completes/OPNsense/Toutes-versions/Installation-Deploiement/33_Installation_Appliance_OPNsense_Production.md), [HA](../02-Fiches-Completes/OPNsense/Toutes-versions/Autres/10_Pare_Feu_Appliance_OPNsense_CARP_pfSync_HA.md) et fiches simples par étape |
| DMZ / segmentation des zones | Multi-OS / pare-feu | Couvert pour la conception et la validation en laboratoire — [guide DMZ](../02-Fiches-Completes/Transverses/Multi-OS/Autres/86_Conception_DMZ_Segmentation_Flux_Multi_OS.md) et [checklist de flux](../01-Fiches-Simples/pfSense/Toutes-versions/Vie-du-systeme/Fiches-par-theme/Administration-systeme/Fiche_Simple_-_DMZ_Valider_Flux_Zone_Lab.md); configurations détaillées par constructeur non couvertes et fiches simples par étape |
| FortiOS / FortiGate, PAN-OS / Palo Alto, Cisco ASA / Firepower, Stormshield | Appliances | Manquant |
| Snort / Suricata / Zeek | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Suricata.md>) et fiches simples par étape |
| Wazuh | Linux / multiplateforme | Couvert — [guide Wazuh](../02-Fiches-Completes/Debian/12/Installation-Deploiement/11_SIEM_XDR_Centralise_Wazuh_4x_Debian_12.md) et fiches simples par étape |
| CrowdStrike Falcon / SentinelOne / Defender for Endpoint | SaaS / agents | Manquant |
| Bitdefender GravityZone / Kaspersky Endpoint Security | Multiplateforme | Manquant |
| Wireshark / tcpdump | Multiplateforme | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_Wireshark.md>) et fiches simples par étape |
| Nmap / Zenmap | Multiplateforme | Défensif uniquement — pas de fiche de scan opérationnel général |
| Nessus / OpenVAS | Linux | Manquant |
| PingCastle / BloodHound | Windows / multiplateforme | Manquant |
| OpenVPN / WireGuard | Multiplateforme | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/04-Reseau-et-cybersecurite/Fiche_Logiciel_-_WireGuard.md>) et fiches simples par étape |
| FreePBX / Asterisk | Appliance / Linux supporté | Couvert pour un déploiement de laboratoire — [guide téléphonie IP](../02-Fiches-Completes/Debian/12/Installation-Deploiement/13_Telephonie_IP_FreePBX_Asterisk_20_Debian_12.md) et fiches simples par étape; utiliser une combinaison officiellement supportée |
| Cisco AnyConnect / FortiClient / GlobalProtect | Multiplateforme | Manquant |
| Apache Guacamole | Linux | Partiel — [déploiement Guacamole 1.6.0 avec Docker Compose, PostgreSQL et reverse proxy HTTPS](../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md); MFA/SSO, haute disponibilité et connexions cibles restent à couvrir |
| FreeRADIUS | Linux | Manquant |
| Keycloak / Authelia / Authentik | Linux | Manquant |
| Cisco ISE | Appliance | Manquant |

## 5. Systèmes, annuaires et services

| Produit / famille | Plateforme | État / référence |
|---|---|---|
| Windows Server 2016 / 2019 / 2022 : AD DS, DNS, DHCP, GPO, WSUS, DFS, RDS | Windows | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Windows-Server-2016-2019-2022.md>) et fiches simples par étape |
| Windows 10 / 11 | Windows | Couvert — [déploiement Windows 11](../02-Fiches-Completes/Windows/Client-11/Installation-Deploiement/25_Deploiement_Postes_Windows_11_Production.md) et fiches simples par étape |
| Microsoft Entra ID | Cloud | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Microsoft-Entra-ID.md>) et fiches simples par étape |
| Debian / Ubuntu Server | Linux | Couvert — guides OS et services selon les versions documentées |
| RHEL / AlmaLinux / Rocky Linux | Linux | Partiel — Rocky Linux 9 documenté; RHEL/Alma et autres versions manquent |
| Samba / Samba4 | Linux | Couvert pour un lab AD DC — [guide Samba AD DC Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/65_Deploiement_Samba_AD_DC_Debian_13.md); partage SMB traité séparément dans [NAS/SAN](../02-Fiches-Completes/Transverses/Multi-OS/Installation-Deploiement/07_Stockage_Reseau_NAS_SAN_Samba_NFSv4_iSCSI.md). Migration de forêt et validation production non couvertes et fiches simples par étape |
| OpenLDAP / FreeIPA | Linux | Partiel — [OpenLDAP 2.6 sur Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/87_Deploiement_OpenLDAP_2.6_Debian_13.md) et [FreeIPA sur Rocky Linux 9](../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/88_Deploiement_FreeIPA_Rocky_Linux_9.md); guides non testés, réplication et haute disponibilité non couverts |
| BIND 9 | Linux | Couvert — [guide autoritatif Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/63_Deploiement_BIND9_Autoritatif_Debian_13.md) et fiche simple Debian existante et fiches simples par étape |
| Kea DHCPv4 | Linux | Couvert — [guide DHCPv4 Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/64_Deploiement_Kea_DHCPv4_Debian_13.md) et fiche simple de contrôle et fiches simples par étape |
| ISC DHCP Server (dhcpd) | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_ISC-DHCP-Server.md>) et fiches simples par étape |

## 6. Stockage et SAN / NAS

| Produit | Plateforme | État / référence |
|---|---|---|
| TrueNAS Core | Appliance FreeBSD | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/06-Stockage-et-SAN-NAS/Fiche_Logiciel_-_TrueNAS-Core.md>) et fiches simples par étape |
| TrueNAS SCALE | Appliance Linux | Couvert — [guide SCALE 25.10](../02-Fiches-Completes/TrueNAS/SCALE-25.10/Installation-Deploiement/60_Deploiement_TrueNAS_SCALE_25.10.md) et fiches simples par étape |
| OpenMediaVault | Linux Debian | Couvert — [guide OpenMediaVault 8 sur Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/66_Deploiement_OpenMediaVault_8_Debian_13.md) et fiches simples par étape |
| Ceph | Linux | Couvert pour un lab Tentacle 20.2.4 / Ubuntu 22.04 — [guide cephadm](../02-Fiches-Completes/Ubuntu/22.04/Installation-Deploiement/67_Deploiement_Ceph_Tentacle_20_2_4_Ubuntu_22_04.md). Debian 13 n'est pas listé comme plateforme testée par Ceph; revue et essais de production manquants et fiches simples par étape |
| StarWind Virtual SAN | Windows / Linux | Manquant |
| NetApp ONTAP / Dell EMC | Appliances | Manquant |

## 7. Sauvegarde, restauration et PRA / PCA

| Produit | Plateforme | État / référence |
|---|---|---|
| Veeam Backup & Replication | Windows | Couvert — [guide Veeam 13](../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/58_Deploiement_Veeam_Backup_Replication_13_Windows_Server_2022.md) et fiches simples par étape |
| Proxmox Backup Server | Linux | Couvert — [guide PBS](../02-Fiches-Completes/Proxmox/Toutes-versions/Autres/12_Proxmox_Backup_Server_3x_PBS_Deduplication.md) et [parcours de sauvegarde/restauration LXC Alpine](../02-Fiches-Completes/Alpine/Toutes-versions/Autres/18_Alpine_LXC_Sauvegarde_Restauration_Production.md) avec fiches simples par étape |
| Nakivo / Altaro (Hornetsecurity) | Multiplateforme | Manquant |
| Bacula | Linux | Couvert pour Bacula Community 15.0.3 / Debian 12 Backports — [guide](../02-Fiches-Completes/Debian/12/Installation-Deploiement/68_Deploiement_Bacula_15_Debian_12_Backports.md) et [fiche de restauration](../01-Fiches-Simples/Debian/12/Vie-du-logiciel/Bacula/Fiche_Simple_-_VM_Debian_12_Bacula_Valider_Restauration.md) et fiches simples par étape |
| Bareos | Linux | Couvert — [guide Bareos 25](../02-Fiches-Completes/Debian/13/Installation-Deploiement/59_Deploiement_Bareos_25_Debian_13.md) et fiches simples par étape |
| BorgBackup / Restic | Linux | Couvert — [BorgBackup Debian 12](../02-Fiches-Completes/Debian/12/Autres/19_Sauvegarde_Restauration_BorgBackup_Debian_12.md) avec fiches simples par étape, [Restic](../02-Fiches-Completes/Ubuntu/Toutes-versions/Autres/29_Sauvegarde_Restauration_Ubuntu_Server_Restic.md) |
| rsync / Robocopy | Linux / Windows | Couvert pour les copies de fichiers sur Debian 13 et Windows Server 2022 — [rsync](../02-Fiches-Completes/Debian/13/Autres/92_Sauvegarde_Fichiers_rsync_Debian_13.md) avec fiches simples par étape, [Robocopy](../02-Fiches-Completes/Windows/Server-2022/Autres/93_Copie_Sauvegarde_Fichiers_Robocopy_Windows_Server_2022.md); ne remplace pas une sauvegarde historisée |

## 8. Gestion des secrets et mots de passe

| Produit | Plateforme | État |
|---|---|---|
| Bitwarden | Multiplateforme / Docker / SaaS | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/08-Gestion-des-secrets-et-mots-de-passe/Fiche_Logiciel_-_Bitwarden.md>) et fiches simples par étape |
| Vaultwarden | Multiplateforme / Docker | Couvert pour un déploiement Docker Compose avec SQLite — [guide Vaultwarden](../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/94_Deploiement_Vaultwarden_Docker_Compose.md); logiciel communautaire non équivalent au serveur officiel Bitwarden, non testé et fiches simples par étape |
| Passbolt | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/08-Gestion-des-secrets-et-mots-de-passe/Fiche_Logiciel_-_Passbolt.md>) et fiches simples par étape |
| HashiCorp Vault | Linux | Couvert — [guide Vault Raft](../02-Fiches-Completes/Debian/13/Installation-Deploiement/61_Deploiement_Hashicorp_Vault_Raft_Debian_13.md) et fiches simples par étape |
| KeePass / KeePassXC | Multiplateforme | Couvert pour KeePassXC 2.8.0 sur Debian 13 — [guide d'installation, coffre KDBX et restauration](../02-Fiches-Completes/Debian/13/Installation-Deploiement/79_Deploiement_KeePassXC_2.8.0_Debian_13.md) et [fiche de validation du coffre](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/KeePassXC/Fiche_Simple_-_VM_Debian_13_KeePassXC_Valider_Coffre.md); KeePass (Windows) non documenté et fiches simples par étape |

## 9. Automatisation, déploiement et IaC

| Produit | Plateforme | État |
|---|---|---|
| Ansible | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_Ansible.md>) et fiches simples par étape |
| Terraform / OpenTofu | Multiplateforme | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_Terraform-OpenTofu.md>) et fiches simples par étape |
| Microsoft MECM / SCCM | Windows | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_Microsoft-MECM-SCCM.md>) et fiches simples par étape |
| WDS + MDT / FOG Project | Windows / Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_WDS-MDT.md>) et fiches simples par étape |
| Git / GitLab / GitHub / Gitea | Multiplateforme | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_Git.md>) et fiches simples par étape |
| Packer | Multiplateforme | Partiel — [pilote Packer sur Debian 13 avec plugin Docker local](../02-Fiches-Completes/Debian/13/Installation-Deploiement/126_Administration_Packer_Debian_13.md) et fiches simples par étape; builders VM/cloud et publication d'images restent à documenter |

## 10. Cloud public et hybride

| Produit | Plateforme | État |
|---|---|---|
| Microsoft Azure | Cloud | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Microsoft-Azure.md>) et fiches simples par étape |
| AWS | Cloud | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_AWS.md>) et fiches simples par étape |
| Google Cloud Platform | Cloud | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Google-Cloud-Platform.md>) et fiches simples par étape |
| Proxmox / OpenStack | Linux | Partiel — Proxmox avec [création de LXC Alpine](../02-Fiches-Completes/Alpine/Toutes-versions/Installation-Deploiement/16_Installation_LXC_Alpine_Proxmox.md) et [diagnostic réseau/services](../02-Fiches-Completes/Alpine/Toutes-versions/Diagnostic/17_Diagnostic_LXC_Alpine_Reseau_Services.md), chacun avec fiches simples par étape; OpenStack absent |

## 11. Scripting, développement et administration

| Produit | Plateforme | État |
|---|---|---|
| PowerShell | Windows / Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_PowerShell.md>) et fiches simples par étape |
| Bash / Shell | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_Bash-Shell.md>) et fiches simples par étape |
| Python | Multiplateforme | Couvert pour l'administration sur Debian 13 — [guide Python 3 avec venv/pipx](../02-Fiches-Completes/Debian/13/Installation-Deploiement/81_Administration_Python_3_Debian_13_Venv_Pipx.md) et [fiche simple de validation des environnements](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Python/Fiche_Simple_-_VM_Debian_13_Python_Valider_Venv_Pipx.md); autres OS non couverts et fiches simples par étape |
| Visual Studio Code | Multiplateforme | Couvert pour Stable 1.143.1 sur Debian 13 amd64 — [guide d'installation et de sécurisation des espaces de travail/extensions](../02-Fiches-Completes/Debian/13/Installation-Deploiement/80_Deploiement_Visual_Studio_Code_1.143.1_Debian_13.md) et [fiche simple de validation](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/VS-Code/Fiche_Simple_-_VM_Debian_13_VSCode_Valider_Installation.md); autres OS non couverts et fiches simples par étape |
| Postman / cURL | Multiplateforme | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_Postman.md>) et fiches simples par étape |
| PuTTY / MobaXterm / mRemoteNG / Royal TS | Windows | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_MobaXterm.md>) et fiches simples par étape |
| Sysinternals | Windows | Partiel — [diagnostic défensif avec Sysinternals sur Windows 11](../02-Fiches-Completes/Windows/Client-11/Installation-Deploiement/123_Administration_Microsoft_Sysinternals_Windows_11.md); les usages modifiant l'état système ne sont pas couverts |

## 12. Messagerie et collaboratif

| Produit | Plateforme | État |
|---|---|---|
| Exchange Server / Exchange Online | Windows / Cloud | Manquant |
| Google Workspace | Cloud | Manquant |
| Postfix / Dovecot | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Dovecot.md>) et fiches simples par étape |
| Zimbra / BleuKango / BlueMind | Linux | Manquant |
| Nextcloud / ownCloud | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Nextcloud.md>) et fiches simples par étape |

## 13. Poste de travail et VDI

| Produit | Plateforme | État |
|---|---|---|
| Microsoft RDS | Windows | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_Microsoft-RDS.md>) et fiches simples par étape |
| Citrix Virtual Apps and Desktops | Windows / Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_Citrix-Virtual-Apps-and-Desktops.md>) et fiches simples par étape |
| VMware Horizon | Appliance / Windows | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_VMware-Horizon.md>) et fiches simples par étape |
| Apache Guacamole | Linux | Partiel — [déploiement Guacamole 1.6.0 avec Docker Compose](../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md); MFA/SSO, haute disponibilité et connexions cibles restent à couvrir |

## 14. Services Web et bases de données

| Produit | Plateforme | État |
|---|---|---|
| Apache / Nginx / IIS | Linux / Windows | Partiel — [Apache HTTP Server sur Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/124_Deploiement_Apache_HTTP_Server_Debian_13.md) et fiches simples par étape, [guide LEMP Nginx Debian 13](../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md) et fiches simples par étape, [IIS pilote sur Windows Server 2022](../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/122_Installation_IIS_Windows_Server_2022.md); architectures de production et applications spécifiques restent à couvrir |
| HAProxy / Traefik / Caddy | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/14-Services-Web-et-bases-de-donnees/Fiche_Logiciel_-_Traefik.md>) et fiches simples par étape |
| MySQL / MariaDB / PostgreSQL / SQL Server | Linux / Windows | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/14-Services-Web-et-bases-de-donnees/Fiche_Logiciel_-_MariaDB.md>) et fiches simples par étape |
| MongoDB / Redis / InfluxDB | Linux | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/14-Services-Web-et-bases-de-donnees/Fiche_Logiciel_-_InfluxDB.md>) et fiches simples par étape |

## 15. Topologie, IPAM et outils métiers

| Produit | Plateforme | État |
|---|---|---|
| NetBox | Linux | Couvert pour NetBox 4.7.4 sur Debian 13 — [guide](../02-Fiches-Completes/Debian/13/Installation-Deploiement/73_Deploiement_NetBox_4.7.4_Debian_13.md), fiches simples par étape et [fiche pilote IPAM](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/NetBox/Fiche_Simple_-_VM_Debian_13_NetBox_Valider_IPAM.md) |
| phpIPAM | Linux | Couvert pour phpIPAM 1.8.3 sur Debian 13 — [guide](../02-Fiches-Completes/Debian/13/Installation-Deploiement/74_Deploiement_phpIPAM_1.8.3_Debian_13.md) et [fiche pilote IPAM](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/phpIPAM/Fiche_Simple_-_VM_Debian_13_phpIPAM_Valider_IPAM.md) et fiches simples par étape |
| QGIS | Multiplateforme | Couvert pour QGIS 3.44.15 LTR sur Debian 13 — [guide](../02-Fiches-Completes/Debian/13/Installation-Deploiement/75_Deploiement_QGIS_3.44_LTR_Debian_13.md) et [fiche projet](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/QGIS/Fiche_Simple_-_VM_Debian_13_QGIS_Valider_Projet.md) et fiches simples par étape |
| draw.io Desktop | Multiplateforme | Couvert pour draw.io Desktop 32.6.1 hors ligne sur Debian 13 — [guide](../02-Fiches-Completes/Debian/13/Installation-Deploiement/76_Deploiement_draw_io_Desktop_32.6.1_Debian_13.md) et [fiche de contrôle](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/draw.io/Fiche_Simple_-_VM_Debian_13_draw_io_Valider_Diagramme.md) et fiches simples par étape |
| Microsoft Visio | Windows / Microsoft 365 | Couvert — [fiche logiciel](<../01-Fiches-Simples/Logiciels/15-Topologie-IPAM-et-outils-metiers/Fiche_Logiciel_-_Microsoft-Visio.md>) et fiches simples par étape |
| GNS3 | Multiplateforme | Couvert pour GNS3 2.2.61 stable sur Debian 13, lab local isolé — [guide](../02-Fiches-Completes/Debian/13/Installation-Deploiement/77_Deploiement_GNS3_2.2.61_Debian_13.md) et [fiche de contrôle](../01-Fiches-Simples/Debian/13/Vie-du-logiciel/GNS3/Fiche_Simple_-_VM_Debian_13_GNS3_Valider_Lab_Isole.md) et fiches simples par étape |
| Cisco Packet Tracer | Windows / macOS / Ubuntu | Couvert pour Packet Tracer 9.0.1 sur Ubuntu 24.04 — [guide](../02-Fiches-Completes/Ubuntu/24.04/Installation-Deploiement/78_Deploiement_Cisco_Packet_Tracer_9.0.1_Ubuntu_24.04.md) et [fiche de validation](../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Packet-Tracer/Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Valider_Simulation.md); compte Cisco/NetAcad requis, Debian non pris en charge et fiches simples par étape |
| EVE-NG | Appliance / VM | Manquant — Community 6.2.0-4 marquée EOL juin 2026; édition actuelle Freemium/Pro soumise à des limites et conditions de licence, images éditeur à autoriser |

## 16. Kali Linux / Parrot OS et outillage offensif

Les outils et actions orientés intrusion, exploitation, déauthentification Wi-Fi, brute-force/cracking, vol d'identifiants ou exécution d'exploits ne recevront pas de fiches opératoires. Une couverture future peut porter sur la préparation défensive d'un lab isolé, l'inventaire et le durcissement, l'analyse passive autorisée, la détection et le traitement des résultats. Toute activité doit relever d'un périmètre explicitement autorisé.

| Produit / groupe d'outils | État |
|---|---|
| Kali Linux / Parrot Security OS | Manquant — guide d'installation défensive/lab à créer |
| Aircrack-ng / Wifite | Défensif uniquement — pas de procédures de capture d'identifiants, déauthentification ou cassage |
| Kismet | Manquant — une fiche de détection passive et autorisée peut être étudiée |
| Nmap / Zenmap, Maltego, Recon-ng | Défensif uniquement — inventaire passif/autorisé seulement; pas de reconnaissance autonome de tiers |
| SearchSploit / Nikto | Défensif uniquement — pas de reproduction ou exploitation de vulnérabilités |
| Burp Suite / SQLmap / Gobuster / Dirb | Défensif uniquement — pas de procédure d'exploitation ou de brute-force web |
| Metasploit / BeEF / Responder | Défensif uniquement — détection, prévention et labs sans instructions d'intrusion |
| John the Ripper / Hashcat / Hydra | Défensif uniquement — pas de cracking ou brute-force opératoire |

## Ordre de traitement proposé pour la suite

1. Sauvegarde d'entreprise : Veeam, puis Bacula/Bareos.
2. Stockage virtualisé et NAS : TrueNAS, Ceph et ONTAP selon l'environnement disponible.
3. Identité/secrets : Vaultwarden/Bitwarden et HashiCorp Vault.
4. Réseau/sécurité défensive : pfSense, IDS/IPS, scanners de vulnérabilités et outils de logs/endpoint, avec sources et autorisation explicites.
5. Automatisation et cloud : Ansible complet, Terraform/OpenTofu, MECM/WDS, puis fournisseurs cloud.

Les sujets commerciaux (Veeam, Fortinet, Cisco, Citrix, etc.) nécessitent de préciser la version/licence et l'environnement effectivement visés avant de produire un runbook détaillé.