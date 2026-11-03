---
title: "Matrice de couverture des logiciels de production TSSR / AIS"
description: "Cette matrice reprend la liste maximale fournie et la compare au contenu actuellement présent dans 01-fiches-simples et 02-fiches-completes. Elle sert de registre de travail : un produit cité dans un guide générique n'est pas considéré comme ayant une fiche dédiée."
published: true
date: 2026-11-03T09:36:13Z
tags: []
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Matrice de couverture des logiciels de production TSSR / AIS

Cette matrice reprend la liste maximale fournie et la compare au contenu actuellement présent dans `01-fiches-simples` et `02-fiches-completes`. Elle sert de registre de travail : un produit cité dans un guide générique n'est pas considéré comme ayant une fiche dédiée.

Pour les mémos, scripts communautaires, listes d'outils et requêtes GitHub, consulter le [référentiel externe Sysadmin/TSSR](/fr/06-documentation-ext/05-referentiel-github/github-tssr); ses liens sont des pistes à vérifier et non des procédures de production approuvées.

**Mise à jour au 31 octobre 2026 :** les nouvelles fiches dédiées comblent les lacunes documentaires recensées ci-dessous. Leur présence dans cette matrice ne signifie pas qu'elles ont été testées sur la plateforme cible ; chaque procédure doit être vérifiée pour la version et la licence effectivement utilisées.

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
| GLPI | Linux / Windows | Couvert — [guide GLPI](/fr/02-fiches-completes/debian/12/installation-deploiement/03-helpdesk-itsm-glpi-11-12-debian-12-13) et fiches simples par étape |
| OCS Inventory | Linux / Windows | Couvert — [guide OCS Inventory](/fr/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13) et fiches simples par étape |
| Snipe-IT | Linux / Windows | Couvert — [guide Snipe-IT](/fr/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik) et fiches simples par étape |
| Jira Service Management | Cloud/SaaS | Couvert — [guide JSM](/fr/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm) et fiches simples par étape |
| OTRS / Znuny | Linux | Couvert — [guide Znuny](/fr/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12) et fiches simples par étape |
| Lansweeper | Windows | Couvert — [guide Lansweeper](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server) et fiches simples par étape |
| iTop | Linux | Couvert — [guide iTop](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404) et fiches simples par étape |

## 2. Supervision, métrologie, logs et observabilité

| Produit | Plateforme | État / référence |
|---|---|---|
| Centreon | Linux | Couvert — [guide Centreon](/fr/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13) et fiches simples par étape |
| Zabbix | Linux | Couvert — [guide Zabbix](/fr/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12) et fiches simples par étape |
| PRTG Network Monitor | Windows | Couvert — [guide PRTG](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/47-deploiement-prtg-network-monitor-windows-server) et fiches simples par étape |
| Prometheus + Grafana | Multiplateforme | Couvert — [guide Prometheus/Grafana](/fr/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13) et fiches simples par étape |
| Datadog | Cloud/SaaS | Couvert — [guide Datadog Agent](/fr/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas) et fiches simples par étape |
| Dynatrace | Cloud/SaaS | Couvert — [guide OneAgent](/fr/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas) et fiches simples par étape |
| Cacti | Linux | Couvert — [guide Cacti](/fr/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12) et fiches simples par étape |
| LibreNMS | Linux | Couvert — [guide LibreNMS](/fr/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04) et fiches simples par étape |
| Observium | Linux | Couvert pour l'édition Community sur Debian 13 — [guide](/fr/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13) et [fiche pilote SNMPv3](/fr/01-fiches-simples/debian/13/vie-du-logiciel/observium/fiche-simple-vm-debian-13-observium-ajouter-hote-snmpv3) et fiches simples par étape |
| Graylog | Multiplateforme | Couvert — [guide Graylog](/fr/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04) et fiches simples par étape |
| ELK Stack | Multiplateforme | Couvert — [guide Elastic Stack](/fr/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13) et fiches simples par étape |
| Splunk Enterprise / Cloud | Multiplateforme / SaaS | Couvert pour Enterprise sur Debian 12 — [guide existant](/fr/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12) ; [onboarding Splunk Cloud](/fr/02-fiches-completes/transverses/cloud-saas/installation-deploiement/splunk-cloud-platform-onboarding-forwarders-hec-saas) — non testé sur plateforme cible |

## 3. Virtualisation et conteneurisation

| Produit | Plateforme | État / référence |
|---|---|---|
| VMware vSphere (ESXi / vCenter) | Appliance / bare-metal | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere) et fiches simples par étape |
| Microsoft Hyper-V | Windows Server | Couvert — [guide Hyper-V 2022](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/55-deploiement-hyper-v-windows-server-2022) et fiches simples par étape |
| Proxmox VE | Appliance Debian | Couvert — [guide Proxmox VE](/fr/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync) et fiches simples par étape |
| Nutanix AHV | Appliance | Fiche de cadrage du cluster et de la première VM — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/deploiement-nutanix-ahv-cluster-et-premiere-vm), non testé |
| Docker / Docker Compose | Linux / Windows | Couvert — [guide de durcissement Docker](/fr/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production), [guide de sauvegarde Compose](/fr/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker) et fiches simples par étape |
| Kubernetes / K3s | Multiplateforme | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-kubernetes-k3s) et fiches simples par étape |
| Podman / Buildah | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-podman-buildah) et fiches simples par étape |

## 4. Réseau et cybersécurité

| Produit / famille | Plateforme | État / référence |
|---|---|---|
| pfSense | Appliance / VM FreeBSD | Couvert pour pfSense CE 2.9.0 en laboratoire Proxmox — [guide](/fr/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab) et [fiche de validation](/fr/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-pfsense-ce-2-9-0-valider-flux-lab); appliance physique et production non couvertes et fiches simples par étape |
| OPNsense | Appliance FreeBSD | Couvert — [installation OPNsense](/fr/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production), [HA](/fr/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha) et fiches simples par étape |
| DMZ / segmentation des zones | Multi-OS / pare-feu | Couvert pour la conception et la validation en laboratoire — [guide DMZ](/fr/02-fiches-completes/transverses/multi-os/autres/86-conception-dmz-segmentation-flux-multi-os) et [checklist de flux](/fr/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-dmz-valider-flux-zone-lab); configurations détaillées par constructeur non couvertes et fiches simples par étape |
| FortiOS / FortiGate, PAN-OS / Palo Alto, Cisco ASA / Firepower, Stormshield | Appliances | Fiche comparative de configuration défensive multi-appliance — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/appliances-pare-feu-forti-pan-cisco-stormshield), non testé par constructeur |
| Snort / Suricata / Zeek | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata) et fiches simples par étape |
| Wazuh | Linux / multiplateforme | Couvert — [guide Wazuh](/fr/02-fiches-completes/debian/12/installation-deploiement/11-siem-xdr-centralise-wazuh-4x-debian-12) et fiches simples par étape |
| CrowdStrike Falcon / SentinelOne / Defender for Endpoint | SaaS / agents | Fiche de déploiement pilote et gestion des agents — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/edr-crowdstrike-sentinelone-defender), non testé |
| Bitdefender GravityZone / Kaspersky Endpoint Security | Multiplateforme | Fiche comparative de déploiement et gestion défensive — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/antivirus-bitdefender-gravityzone-kaspersky), non testé |
| Wireshark / tcpdump | Multiplateforme | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark) et fiches simples par étape |
| Nmap / Zenmap | Multiplateforme | Défensif uniquement — pas de fiche de scan opérationnel général |
| Nessus / OpenVAS | Linux | Fiche de scan limité aux cibles autorisées — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/scan-vulnerabilites-nessus-openvas), non testé |
| PingCastle / BloodHound | Windows / multiplateforme | Fiche d'audit AD défensif et autorisé — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/audit-ad-pingcastle-bloodhound), non testé |
| OpenVPN / WireGuard | Multiplateforme | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard) et fiches simples par étape |
| FreePBX / Asterisk | Appliance / Linux supporté | Couvert pour un déploiement de laboratoire — [guide téléphonie IP](/fr/02-fiches-completes/debian/12/installation-deploiement/13-telephonie-ip-freepbx-asterisk-20-debian-12) et fiches simples par étape; utiliser une combinaison officiellement supportée |
| Cisco AnyConnect / FortiClient / GlobalProtect | Multiplateforme | Fiche de déploiement et contrôle des clients VPN — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/clients-vpn-anyconnect-forticlient-globalprotect), non testé par éditeur |
| Apache Guacamole | Linux | Déploiement de base par [guide Docker](/fr/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker) et complément MFA/SSO/HA/cibles — [guide d'architecture](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/apache-guacamole-architecture-complete-mfa-sso-ha-cibles), non testé |
| FreeRADIUS | Linux | Fiche de cadrage et configuration d'authentification réseau — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/authentification-freeradius), non testé |
| Keycloak / Authelia / Authentik | Linux | Fiche comparative de déploiement SSO — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/sso-keycloak-authelia-authentik), non testé par produit |
| Cisco ISE | Appliance | Fiche de cadrage du contrôle d'accès réseau — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/controle-acces-cisco-ise), non testé |

## 5. Systèmes, annuaires et services

| Produit / famille | Plateforme | État / référence |
|---|---|---|
| Windows Server 2016 / 2019 / 2022 : AD DS, DNS, DHCP, GPO, WSUS, DFS, RDS | Windows | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-windows-server-2016-2019-2022) et fiches simples par étape |
| Windows 10 / 11 | Windows | Couvert — [déploiement Windows 11](/fr/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production) et fiches simples par étape |
| Microsoft Entra ID | Cloud | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id) et fiches simples par étape |
| Debian / Ubuntu Server | Linux | Couvert — guides OS et services selon les versions documentées |
| RHEL / AlmaLinux / Rocky Linux | Linux | Rocky Linux 9 documenté ; [fiche comparative des prérequis RHEL/Alma/Rocky](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/complement-rhel-almalinux-par-rapport-a-rocky-linux-9). Les déploiements RHEL/Alma restent à valider sur versions supportées |
| Samba / Samba4 | Linux | Couvert pour un lab AD DC — [guide Samba AD DC Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13); partage SMB traité séparément dans [NAS/SAN](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/07-stockage-reseau-nas-san-samba-nfsv4-iscsi). Migration de forêt et validation production non couvertes et fiches simples par étape |
| OpenLDAP / FreeIPA | Linux | Guides d'installation existants : [OpenLDAP Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13) et [FreeIPA Rocky Linux 9](/fr/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9) ; réplication/HA décrites dans le [guide comparatif](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/replication-et-haute-disponibilite-openldap-et-freeipa-comparatif), non testé |
| BIND 9 | Linux | Couvert — [guide autoritatif Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13) et fiche simple Debian existante et fiches simples par étape |
| Kea DHCPv4 | Linux | Couvert — [guide DHCPv4 Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13) et fiche simple de contrôle et fiches simples par étape |
| ISC DHCP Server (dhcpd) | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-isc-dhcp-server) et fiches simples par étape |

## 6. Stockage et SAN / NAS

| Produit | Plateforme | État / référence |
|---|---|---|
| TrueNAS Core | Appliance FreeBSD | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-truenas-core) et fiches simples par étape |
| TrueNAS SCALE | Appliance Linux | Couvert — [guide SCALE 25.10](/fr/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10) et fiches simples par étape |
| OpenMediaVault | Linux Debian | Couvert — [guide OpenMediaVault 8 sur Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13) et fiches simples par étape |
| Ceph | Linux | Couvert pour un lab Tentacle 20.2.4 / Ubuntu 22-04 — [guide cephadm](/fr/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04). Debian 13 n'est pas listé comme plateforme testée par Ceph; revue et essais de production manquants et fiches simples par étape |
| StarWind Virtual SAN | Windows / Linux | Fiche de cadrage d'un cluster à deux nœuds — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/deploiement-starwind-virtual-san-stockage-hyperconverge-2-noeuds), non testé |
| NetApp ONTAP / Dell EMC | Appliances | Fiche de comparaison des solutions et interfaces d'administration — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/stockage-netapp-ontap-et-dell-emc-solutions-et-interfaces), non testé par équipement |

## 7. Sauvegarde, restauration et PRA / PCA

| Produit | Plateforme | État / référence |
|---|---|---|
| Veeam Backup & Replication | Windows | Couvert — [guide Veeam 13](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022) et fiches simples par étape |
| Proxmox Backup Server | Linux | Couvert — [guide PBS](/fr/02-fiches-completes/proxmox/toutes-versions/autres/12-proxmox-backup-server-3x-pbs-deduplication) et [parcours de sauvegarde/restauration LXC Alpine](/fr/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production) avec fiches simples par étape |
| Nakivo / Altaro (Hornetsecurity) | Multiplateforme | Fiche comparative des produits, prérequis et licences — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/sauvegarde-nakivo-et-altaro-hornetsecurity-produits-et-licences), non testé |
| Bacula | Linux | Couvert pour Bacula Community 15.0.3 / Debian 12 Backports — [guide](/fr/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports) et [fiche de restauration](/fr/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-restauration) et fiches simples par étape |
| Bareos | Linux | Couvert — [guide Bareos 25](/fr/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13) et fiches simples par étape |
| BorgBackup / Restic | Linux | Couvert — [BorgBackup Debian 12](/fr/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12) avec fiches simples par étape, [Restic](/fr/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic) |
| rsync / Robocopy | Linux / Windows | Couvert pour les copies de fichiers sur Debian 13 et Windows Server 2022 — [rsync](/fr/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13) avec fiches simples par étape, [Robocopy](/fr/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022); ne remplace pas une sauvegarde historisée |

## 8. Gestion des secrets et mots de passe

| Produit | Plateforme | État |
|---|---|---|
| Bitwarden | Multiplateforme / Docker / SaaS | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-bitwarden) et fiches simples par étape |
| Vaultwarden | Multiplateforme / Docker | Couvert pour un déploiement Docker Compose avec SQLite — [guide Vaultwarden](/fr/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose); logiciel communautaire non équivalent au serveur officiel Bitwarden, non testé et fiches simples par étape |
| Passbolt | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-passbolt) et fiches simples par étape |
| HashiCorp Vault | Linux | Couvert — [guide Vault Raft](/fr/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13) et fiches simples par étape |
| KeePass / KeePassXC | Multiplateforme | Couvert pour KeePassXC 2.8.0 sur Debian 13 — [guide d'installation, coffre KDBX et restauration](/fr/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13) et [fiche de validation du coffre](/fr/01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-valider-coffre); KeePass (Windows) non documenté et fiches simples par étape |

## 9. Automatisation, déploiement et IaC

| Produit | Plateforme | État |
|---|---|---|
| Ansible | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-ansible) et fiches simples par étape |
| Terraform / OpenTofu | Multiplateforme | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-terraform-opentofu) et fiches simples par étape |
| Microsoft MECM / SCCM | Windows | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm) et fiches simples par étape |
| WDS + MDT / FOG Project | Windows / Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt) et fiches simples par étape |
| Git / GitLab / GitHub / Gitea | Multiplateforme | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-git) et fiches simples par étape |
| Packer | Multiplateforme | [Pilote Debian 13 avec plugin Docker local](/fr/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13) et [complément builders VM/cloud et publication d'images](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/packer-builders-vm-et-cloud-et-publication-dimages), non testés sur les cibles correspondantes |

## 10. Cloud public et hybride

| Produit | Plateforme | État |
|---|---|---|
| Microsoft Azure | Cloud | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-microsoft-azure) et fiches simples par étape |
| AWS | Cloud | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws) et fiches simples par étape |
| Google Cloud Platform | Cloud | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-google-cloud-platform) et fiches simples par étape |
| Proxmox / OpenStack | Linux | Proxmox avec [cluster VE](/fr/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync), [création de LXC Alpine](/fr/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox) et [diagnostic LXC](/fr/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services) ; [guide OpenStack de laboratoire](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/deploiement-openstack-plateforme-de-laboratoire-et-controles), non testé |

## 11. Scripting, développement et administration

| Produit | Plateforme | État |
|---|---|---|
| PowerShell | Windows / Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-powershell) et fiches simples par étape |
| Bash / Shell | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-bash-shell) et fiches simples par étape |
| Python | Multiplateforme | Couvert pour l'administration sur Debian 13 — [guide Python 3 avec venv/pipx](/fr/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx) et [fiche simple de validation des environnements](/fr/01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-valider-venv-pipx); autres OS non couverts et fiches simples par étape |
| Visual Studio Code | Multiplateforme | Couvert pour Stable 1.143.1 sur Debian 13 amd64 — [guide d'installation et de sécurisation des espaces de travail/extensions](/fr/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13) et [fiche simple de validation](/fr/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-valider-installation); autres OS non couverts et fiches simples par étape |
| Postman / cURL | Multiplateforme | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman) et fiches simples par étape |
| PuTTY / MobaXterm / mRemoteNG / Royal TS | Windows | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-mobaxterm) et fiches simples par étape |
| Sysinternals | Windows | [Guide existant de diagnostic défensif Windows 11](/fr/02-fiches-completes/windows/client-11/installation-deploiement/123-administration-microsoft-sysinternals-windows-11) et [complément Sysmon/Autoruns contrôlé](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/sysinternals-usages-defensifs-controles-sysmon-autoruns-windows), non testé sur les variantes ciblées |

## 12. Messagerie et collaboratif

| Produit | Plateforme | État |
|---|---|---|
| Exchange Server / Exchange Online | Windows / Cloud | Deux parcours distincts (sur site, SaaS et hybride) dans le [guide Exchange](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/exchange-server-et-exchange-online-deux-chemins-deploiement), non testé |
| Google Workspace | Cloud | Fiche d'administration initiale, identité et messagerie — [guide](/fr/02-fiches-completes/transverses/cloud-saas/installation-deploiement/google-workspace-administration-initiale-sso-messagerie), non testé |
| Postfix / Dovecot | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-dovecot) et fiches simples par étape |
| Zimbra / BleuKango / BlueMind | Linux | Fiche de comparaison et de sélection de version — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/zimbra-bluemind-bleukango-produits-versions-choix-deploiement). BleuKango reste à identifier ; non testé |
| Nextcloud / ownCloud | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-nextcloud) et fiches simples par étape |

## 13. Poste de travail et VDI

| Produit | Plateforme | État |
|---|---|---|
| Microsoft RDS | Windows | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-microsoft-rds) et fiches simples par étape |
| Citrix Virtual Apps and Desktops | Windows / Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops) et fiches simples par étape |
| VMware Horizon | Appliance / Windows | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-vmware-horizon) et fiches simples par étape |
| Apache Guacamole | Linux | Déploiement de base par [guide Docker](/fr/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker) et complément MFA/SSO/HA/cibles — [guide d'architecture](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/apache-guacamole-architecture-complete-mfa-sso-ha-cibles), non testé |

## 14. Services Web et bases de données

| Produit | Plateforme | État |
|---|---|---|
| Apache / Nginx / IIS | Linux / Windows | Guides existants : [Apache Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13), [LEMP Nginx Debian 13](/fr/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb) et [IIS Windows Server 2022](/fr/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022), complétés par l'[architecture de production comparative](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/architectures-production-apache-nginx-iis-comparatif-linux-windows), non testée |
| HAProxy / Traefik / Caddy | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-traefik) et fiches simples par étape |
| MySQL / MariaDB / PostgreSQL / SQL Server | Linux / Windows | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-mariadb) et fiches simples par étape |
| MongoDB / Redis / InfluxDB | Linux | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-influxdb) et fiches simples par étape |

## 15. Topologie, IPAM et outils métiers

| Produit | Plateforme | État |
|---|---|---|
| NetBox | Linux | Couvert pour NetBox 4.7.4 sur Debian 13 — [guide](/fr/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13), fiches simples par étape et [fiche pilote IPAM](/fr/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam) |
| phpIPAM | Linux | Couvert pour phpIPAM 1.8.3 sur Debian 13 — [guide](/fr/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13) et [fiche pilote IPAM](/fr/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-valider-ipam) et fiches simples par étape |
| QGIS | Multiplateforme | Couvert pour QGIS 3.44.15 LTR sur Debian 13 — [guide](/fr/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13) et [fiche projet](/fr/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-projet) et fiches simples par étape |
| draw-io Desktop | Multiplateforme | Couvert pour draw-io Desktop 32.6.1 hors ligne sur Debian 13 — [guide](/fr/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13) et [fiche de contrôle](/fr/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-valider-diagramme) et fiches simples par étape |
| Microsoft Visio | Windows / Microsoft 365 | Couvert — [fiche logiciel](/fr/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio) et fiches simples par étape |
| GNS3 | Multiplateforme | Couvert pour GNS3 2.2.61 stable sur Debian 13, lab local isolé — [guide](/fr/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13) et [fiche de contrôle](/fr/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-valider-lab-isole) et fiches simples par étape |
| Cisco Packet Tracer | Windows / macOS / Ubuntu | Couvert pour Packet Tracer 9.0.1 sur Ubuntu 24-04 — [guide](/fr/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04) et [fiche de validation](/fr/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-valider-simulation); compte Cisco/NetAcad requis, Debian non pris en charge et fiches simples par étape |
| EVE-NG | Appliance / VM | Guide de déploiement de laboratoire et de cadrage des éditions/licences — [guide](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/deploiement-eve-ng-community-freemium-pro-licences-et-statut) ; confirmer statut/EOL Community et droits sur les images avant usage, non testé |

## 16. Kali Linux / Parrot OS et outillage offensif

Les outils et actions orientés intrusion, exploitation, déauthentification Wi-Fi, brute-force/cracking, vol d'identifiants ou exécution d'exploits ne recevront pas de fiches opératoires. Une couverture future peut porter sur la préparation défensive d'un lab isolé, l'inventaire et le durcissement, l'analyse passive autorisée, la détection et le traitement des résultats. Toute activité doit relever d'un périmètre explicitement autorisé.

| Produit / groupe d'outils | État |
|---|---|
| Kali Linux / Parrot Security OS | Guide de préparation d'un laboratoire défensif isolé — [fiche](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/kali-linux-parrot-os-laboratoire-defensif-isole), non testée |
| Aircrack-ng / Wifite | Défensif uniquement — pas de procédures de capture d'identifiants, déauthentification ou cassage |
| Kismet | Guide de détection radio passive dans un périmètre autorisé — [fiche](/fr/02-fiches-completes/transverses/multi-os/installation-deploiement/kismet-detection-sans-fil-passive-autorisee-laboratoire), non testé |
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