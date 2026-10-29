# Matrice de couverture des logiciels de production TSSR / AIS

Cette matrice reprend la liste maximale fournie et la compare au contenu actuellement présent dans `01-Fiches-Simples` et `02-Fiches-Completes`. Elle sert de registre de travail : un produit cité dans un guide générique n'est pas considéré comme ayant une fiche dédiée.

Pour les mémos, scripts communautaires, listes d'outils et requêtes GitHub, consulter le [référentiel externe Sysadmin/TSSR](/06-documentation-ext/05-referentiel-github/github-tssr); ses liens sont des pistes à vérifier et non des procédures de production approuvées.

**État au 27 octobre 2026 :** 86 guides complets sont référencés dans la [matrice de revue](/00-administration/matrice-controle-fiches-completes-et-questions-reponses); après l'ajout du guide DMZ, le validateur a contrôlé 291 documents. Le contrôle structurel ne prouve pas le fonctionnement technique ni un essai en production.

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
| GLPI | Linux / Windows | Couvert — [guide GLPI](/02-fiches-completes/debian/12/installation-deploiement/03-helpdesk-itsm-glpi-11-12-debian-12-13) et fiches simples par étape |
| OCS Inventory | Linux / Windows | Couvert — [guide OCS Inventory](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13) et fiches simples par étape |
| Snipe-IT | Linux / Windows | Couvert — [guide Snipe-IT](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik) et fiches simples par étape |
| Jira Service Management | Cloud/SaaS | Couvert — [guide JSM](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm) et fiches simples par étape |
| OTRS / Znuny | Linux | Couvert — [guide Znuny](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12) et fiches simples par étape |
| Lansweeper | Windows | Couvert — [guide Lansweeper](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server) et fiches simples par étape |
| iTop | Linux | Couvert — [guide iTop](/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404) et fiches simples par étape |

## 2. Supervision, métrologie, logs et observabilité

| Produit | Plateforme | État / référence |
|---|---|---|
| Centreon | Linux | Couvert — [guide Centreon](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13) et fiches simples par étape |
| Zabbix | Linux | Couvert — [guide Zabbix](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12) et fiches simples par étape |
| PRTG Network Monitor | Windows | Couvert — [guide PRTG](/02-fiches-completes/windows/server-2022/installation-deploiement/47-deploiement-prtg-network-monitor-windows-server) et fiches simples par étape |
| Prometheus + Grafana | Multiplateforme | Couvert — [guide Prometheus/Grafana](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13) et fiches simples par étape |
| Datadog | Cloud/SaaS | Couvert — [guide Datadog Agent](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas) et fiches simples par étape |
| Dynatrace | Cloud/SaaS | Couvert — [guide OneAgent](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas) et fiches simples par étape |
| Cacti | Linux | Couvert — [guide Cacti](/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12) et fiches simples par étape |
| LibreNMS | Linux | Couvert — [guide LibreNMS](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04) et fiches simples par étape |
| Observium | Linux | Couvert pour l'édition Community sur Debian 13 — [guide](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13) et [fiche pilote SNMPv3](/01-fiches-simples/debian/13/vie-du-logiciel/observium/fiche-simple-vm-debian-13-observium-ajouter-hote-snmpv3) et fiches simples par étape |
| Graylog | Multiplateforme | Couvert — [guide Graylog](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04) et fiches simples par étape |
| ELK Stack | Multiplateforme | Couvert — [guide Elastic Stack](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13) et fiches simples par étape |
| Splunk Enterprise / Cloud | Multiplateforme / SaaS | Partiel — [guide Splunk Enterprise](/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12); Splunk Cloud non documenté |

## 3. Virtualisation et conteneurisation

| Produit | Plateforme | État / référence |
|---|---|---|
| VMware vSphere (ESXi / vCenter) | Appliance / bare-metal | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere>) et fiches simples par étape |
| Microsoft Hyper-V | Windows Server | Couvert — [guide Hyper-V 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/55-deploiement-hyper-v-windows-server-2022) et fiches simples par étape |
| Proxmox VE | Appliance Debian | Couvert — [guide Proxmox VE](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync) et fiches simples par étape |
| Nutanix AHV | Appliance | Manquant |
| Docker / Docker Compose | Linux / Windows | Couvert — [guide de durcissement Docker](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production), [guide de sauvegarde Compose](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker) et fiches simples par étape |
| Kubernetes / K3s | Multiplateforme | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-kubernetes-k3s>) et fiches simples par étape |
| Podman / Buildah | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-podman-buildah>) et fiches simples par étape |

## 4. Réseau et cybersécurité

| Produit / famille | Plateforme | État / référence |
|---|---|---|
| pfSense | Appliance / VM FreeBSD | Couvert pour pfSense CE 2.9.0 en laboratoire Proxmox — [guide](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab) et [fiche de validation](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-pfsense-ce-2-9-0-valider-flux-lab); appliance physique et production non couvertes et fiches simples par étape |
| OPNsense | Appliance FreeBSD | Couvert — [installation OPNsense](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production), [HA](/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha) et fiches simples par étape |
| DMZ / segmentation des zones | Multi-OS / pare-feu | Couvert pour la conception et la validation en laboratoire — [guide DMZ](/02-fiches-completes/transverses/multi-os/autres/86-conception-dmz-segmentation-flux-multi-os) et [checklist de flux](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-dmz-valider-flux-zone-lab); configurations détaillées par constructeur non couvertes et fiches simples par étape |
| FortiOS / FortiGate, PAN-OS / Palo Alto, Cisco ASA / Firepower, Stormshield | Appliances | Manquant |
| Snort / Suricata / Zeek | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata>) et fiches simples par étape |
| Wazuh | Linux / multiplateforme | Couvert — [guide Wazuh](/02-fiches-completes/debian/12/installation-deploiement/11-siem-xdr-centralise-wazuh-4x-debian-12) et fiches simples par étape |
| CrowdStrike Falcon / SentinelOne / Defender for Endpoint | SaaS / agents | Manquant |
| Bitdefender GravityZone / Kaspersky Endpoint Security | Multiplateforme | Manquant |
| Wireshark / tcpdump | Multiplateforme | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark>) et fiches simples par étape |
| Nmap / Zenmap | Multiplateforme | Défensif uniquement — pas de fiche de scan opérationnel général |
| Nessus / OpenVAS | Linux | Manquant |
| PingCastle / BloodHound | Windows / multiplateforme | Manquant |
| OpenVPN / WireGuard | Multiplateforme | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard>) et fiches simples par étape |
| FreePBX / Asterisk | Appliance / Linux supporté | Couvert pour un déploiement de laboratoire — [guide téléphonie IP](/02-fiches-completes/debian/12/installation-deploiement/13-telephonie-ip-freepbx-asterisk-20-debian-12) et fiches simples par étape; utiliser une combinaison officiellement supportée |
| Cisco AnyConnect / FortiClient / GlobalProtect | Multiplateforme | Manquant |
| Apache Guacamole | Linux | Partiel — [déploiement Guacamole 1.6.0 avec Docker Compose, PostgreSQL et reverse proxy HTTPS](/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker); MFA/SSO, haute disponibilité et connexions cibles restent à couvrir |
| FreeRADIUS | Linux | Manquant |
| Keycloak / Authelia / Authentik | Linux | Manquant |
| Cisco ISE | Appliance | Manquant |

## 5. Systèmes, annuaires et services

| Produit / famille | Plateforme | État / référence |
|---|---|---|
| Windows Server 2016 / 2019 / 2022 : AD DS, DNS, DHCP, GPO, WSUS, DFS, RDS | Windows | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-windows-server-2016-2019-2022>) et fiches simples par étape |
| Windows 10 / 11 | Windows | Couvert — [déploiement Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production) et fiches simples par étape |
| Microsoft Entra ID | Cloud | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id>) et fiches simples par étape |
| Debian / Ubuntu Server | Linux | Couvert — guides OS et services selon les versions documentées |
| RHEL / AlmaLinux / Rocky Linux | Linux | Partiel — Rocky Linux 9 documenté; RHEL/Alma et autres versions manquent |
| Samba / Samba4 | Linux | Couvert pour un lab AD DC — [guide Samba AD DC Debian 13](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13); partage SMB traité séparément dans [NAS/SAN](/02-fiches-completes/transverses/multi-os/installation-deploiement/07-stockage-reseau-nas-san-samba-nfsv4-iscsi). Migration de forêt et validation production non couvertes et fiches simples par étape |
| OpenLDAP / FreeIPA | Linux | Partiel — [OpenLDAP 2.6 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/87-deploiement-openldap-2-6-debian-13) et [FreeIPA sur Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9); guides non testés, réplication et haute disponibilité non couverts |
| BIND 9 | Linux | Couvert — [guide autoritatif Debian 13](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13) et fiche simple Debian existante et fiches simples par étape |
| Kea DHCPv4 | Linux | Couvert — [guide DHCPv4 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13) et fiche simple de contrôle et fiches simples par étape |
| ISC DHCP Server (dhcpd) | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-isc-dhcp-server>) et fiches simples par étape |

## 6. Stockage et SAN / NAS

| Produit | Plateforme | État / référence |
|---|---|---|
| TrueNAS Core | Appliance FreeBSD | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-truenas-core>) et fiches simples par étape |
| TrueNAS SCALE | Appliance Linux | Couvert — [guide SCALE 25.10](/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10) et fiches simples par étape |
| OpenMediaVault | Linux Debian | Couvert — [guide OpenMediaVault 8 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13) et fiches simples par étape |
| Ceph | Linux | Couvert pour un lab Tentacle 20.2.4 / Ubuntu 22.04 — [guide cephadm](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04). Debian 13 n'est pas listé comme plateforme testée par Ceph; revue et essais de production manquants et fiches simples par étape |
| StarWind Virtual SAN | Windows / Linux | Manquant |
| NetApp ONTAP / Dell EMC | Appliances | Manquant |

## 7. Sauvegarde, restauration et PRA / PCA

| Produit | Plateforme | État / référence |
|---|---|---|
| Veeam Backup & Replication | Windows | Couvert — [guide Veeam 13](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022) et fiches simples par étape |
| Proxmox Backup Server | Linux | Couvert — [guide PBS](/02-fiches-completes/proxmox/toutes-versions/autres/12-proxmox-backup-server-3x-pbs-deduplication) et [parcours de sauvegarde/restauration LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production) avec fiches simples par étape |
| Nakivo / Altaro (Hornetsecurity) | Multiplateforme | Manquant |
| Bacula | Linux | Couvert pour Bacula Community 15.0.3 / Debian 12 Backports — [guide](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports) et [fiche de restauration](/01-fiches-simples/debian/12/vie-du-logiciel/bacula/fiche-simple-vm-debian-12-bacula-valider-restauration) et fiches simples par étape |
| Bareos | Linux | Couvert — [guide Bareos 25](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13) et fiches simples par étape |
| BorgBackup / Restic | Linux | Couvert — [BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12) avec fiches simples par étape, [Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic) |
| rsync / Robocopy | Linux / Windows | Couvert pour les copies de fichiers sur Debian 13 et Windows Server 2022 — [rsync](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13) avec fiches simples par étape, [Robocopy](/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022); ne remplace pas une sauvegarde historisée |

## 8. Gestion des secrets et mots de passe

| Produit | Plateforme | État |
|---|---|---|
| Bitwarden | Multiplateforme / Docker / SaaS | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-bitwarden>) et fiches simples par étape |
| Vaultwarden | Multiplateforme / Docker | Couvert pour un déploiement Docker Compose avec SQLite — [guide Vaultwarden](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose); logiciel communautaire non équivalent au serveur officiel Bitwarden, non testé et fiches simples par étape |
| Passbolt | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-passbolt>) et fiches simples par étape |
| HashiCorp Vault | Linux | Couvert — [guide Vault Raft](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13) et fiches simples par étape |
| KeePass / KeePassXC | Multiplateforme | Couvert pour KeePassXC 2.8.0 sur Debian 13 — [guide d'installation, coffre KDBX et restauration](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13) et [fiche de validation du coffre](/01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-valider-coffre); KeePass (Windows) non documenté et fiches simples par étape |

## 9. Automatisation, déploiement et IaC

| Produit | Plateforme | État |
|---|---|---|
| Ansible | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-ansible>) et fiches simples par étape |
| Terraform / OpenTofu | Multiplateforme | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-terraform-opentofu>) et fiches simples par étape |
| Microsoft MECM / SCCM | Windows | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-microsoft-mecm-sccm>) et fiches simples par étape |
| WDS + MDT / FOG Project | Windows / Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt>) et fiches simples par étape |
| Git / GitLab / GitHub / Gitea | Multiplateforme | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-git>) et fiches simples par étape |
| Packer | Multiplateforme | Partiel — [pilote Packer sur Debian 13 avec plugin Docker local](/02-fiches-completes/debian/13/installation-deploiement/126-administration-packer-debian-13) et fiches simples par étape; builders VM/cloud et publication d'images restent à documenter |

## 10. Cloud public et hybride

| Produit | Plateforme | État |
|---|---|---|
| Microsoft Azure | Cloud | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-microsoft-azure>) et fiches simples par étape |
| AWS | Cloud | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-aws>) et fiches simples par étape |
| Google Cloud Platform | Cloud | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-google-cloud-platform>) et fiches simples par étape |
| Proxmox / OpenStack | Linux | Partiel — Proxmox avec [création de LXC Alpine](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox) et [diagnostic réseau/services](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services), chacun avec fiches simples par étape; OpenStack absent |

## 11. Scripting, développement et administration

| Produit | Plateforme | État |
|---|---|---|
| PowerShell | Windows / Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-powershell>) et fiches simples par étape |
| Bash / Shell | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-bash-shell>) et fiches simples par étape |
| Python | Multiplateforme | Couvert pour l'administration sur Debian 13 — [guide Python 3 avec venv/pipx](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx) et [fiche simple de validation des environnements](/01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-valider-venv-pipx); autres OS non couverts et fiches simples par étape |
| Visual Studio Code | Multiplateforme | Couvert pour Stable 1.143.1 sur Debian 13 amd64 — [guide d'installation et de sécurisation des espaces de travail/extensions](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13) et [fiche simple de validation](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-valider-installation); autres OS non couverts et fiches simples par étape |
| Postman / cURL | Multiplateforme | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman>) et fiches simples par étape |
| PuTTY / MobaXterm / mRemoteNG / Royal TS | Windows | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-mobaxterm>) et fiches simples par étape |
| Sysinternals | Windows | Partiel — [diagnostic défensif avec Sysinternals sur Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/123-administration-microsoft-sysinternals-windows-11); les usages modifiant l'état système ne sont pas couverts |

## 12. Messagerie et collaboratif

| Produit | Plateforme | État |
|---|---|---|
| Exchange Server / Exchange Online | Windows / Cloud | Manquant |
| Google Workspace | Cloud | Manquant |
| Postfix / Dovecot | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-dovecot>) et fiches simples par étape |
| Zimbra / BleuKango / BlueMind | Linux | Manquant |
| Nextcloud / ownCloud | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-nextcloud>) et fiches simples par étape |

## 13. Poste de travail et VDI

| Produit | Plateforme | État |
|---|---|---|
| Microsoft RDS | Windows | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-microsoft-rds>) et fiches simples par étape |
| Citrix Virtual Apps and Desktops | Windows / Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops>) et fiches simples par étape |
| VMware Horizon | Appliance / Windows | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-vmware-horizon>) et fiches simples par étape |
| Apache Guacamole | Linux | Partiel — [déploiement Guacamole 1.6.0 avec Docker Compose](/02-fiches-completes/transverses/docker/installation-deploiement/121-deploiement-apache-guacamole-1-6-docker); MFA/SSO, haute disponibilité et connexions cibles restent à couvrir |

## 14. Services Web et bases de données

| Produit | Plateforme | État |
|---|---|---|
| Apache / Nginx / IIS | Linux / Windows | Partiel — [Apache HTTP Server sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/124-deploiement-apache-http-server-debian-13) et fiches simples par étape, [guide LEMP Nginx Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb) et fiches simples par étape, [IIS pilote sur Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022); architectures de production et applications spécifiques restent à couvrir |
| HAProxy / Traefik / Caddy | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-traefik>) et fiches simples par étape |
| MySQL / MariaDB / PostgreSQL / SQL Server | Linux / Windows | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-mariadb>) et fiches simples par étape |
| MongoDB / Redis / InfluxDB | Linux | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-influxdb>) et fiches simples par étape |

## 15. Topologie, IPAM et outils métiers

| Produit | Plateforme | État |
|---|---|---|
| NetBox | Linux | Couvert pour NetBox 4.7.4 sur Debian 13 — [guide](/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13), fiches simples par étape et [fiche pilote IPAM](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam) |
| phpIPAM | Linux | Couvert pour phpIPAM 1.8.3 sur Debian 13 — [guide](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13) et [fiche pilote IPAM](/01-fiches-simples/debian/13/vie-du-logiciel/phpipam/fiche-simple-vm-debian-13-phpipam-valider-ipam) et fiches simples par étape |
| QGIS | Multiplateforme | Couvert pour QGIS 3.44.15 LTR sur Debian 13 — [guide](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13) et [fiche projet](/01-fiches-simples/debian/13/vie-du-logiciel/qgis/fiche-simple-vm-debian-13-qgis-valider-projet) et fiches simples par étape |
| draw.io Desktop | Multiplateforme | Couvert pour draw.io Desktop 32.6.1 hors ligne sur Debian 13 — [guide](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13) et [fiche de contrôle](/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-valider-diagramme) et fiches simples par étape |
| Microsoft Visio | Windows / Microsoft 365 | Couvert — [fiche logiciel](</01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio>) et fiches simples par étape |
| GNS3 | Multiplateforme | Couvert pour GNS3 2.2.61 stable sur Debian 13, lab local isolé — [guide](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13) et [fiche de contrôle](/01-fiches-simples/debian/13/vie-du-logiciel/gns3/fiche-simple-vm-debian-13-gns3-valider-lab-isole) et fiches simples par étape |
| Cisco Packet Tracer | Windows / macOS / Ubuntu | Couvert pour Packet Tracer 9.0.1 sur Ubuntu 24.04 — [guide](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04) et [fiche de validation](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/packet-tracer/fiche-simple-vm-ubuntu-24-04-packet-tracer-valider-simulation); compte Cisco/NetAcad requis, Debian non pris en charge et fiches simples par étape |
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