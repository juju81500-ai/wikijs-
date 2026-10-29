# Matrice de contrôle des fiches complètes et Questions/Réponses

**Périmètre :** les 86 fiches complètes actuellement présentes dans `02-Fiches-Completes` et les 11 fiches de `04-Questions-Reponses` (5 fiches QA et 6 fiches de réparation).

**État au 27 octobre 2026 :** le dernier contrôle global avant la fiche DMZ avait vérifié 289 documents; après son ajout, 291 documents passent le contrôle des titres, tags et placeholders. Le validateur ne vérifie pas les commandes, les versions, la sécurité effective ni le comportement en production.

## Méthode de revue

1. **Figer le périmètre** : relever le système, la version logicielle, le rôle et les prérequis effectivement visés. Une documentation `latest` ne remplace pas celle de la version cible.
2. **Comparer aux sources primaires** : vérifier les prérequis, valeurs par défaut, syntaxe, options obsolètes et limites connues.
3. **Revue technique** : contrôler le chemin nominal, les erreurs, les droits minimaux, secrets, exposition réseau, persistance, sauvegarde/restauration, vérifications et retour arrière.
4. **Validation statique** : employer le validateur adapté au format et à la version. Consigner la commande et le résultat; un contrôle syntaxique ne prouve pas le fonctionnement.
5. **Essai isolé** : reproduire sur une VM ou un laboratoire représentatif, sans données réelles, avec sauvegarde et retour arrière.
6. **Tracer la preuve** : renseigner la date, version, environnement, opérateur, résultats, anomalies et prochaine revue.

## États

| État | Signification |
|---|---|
| `OK structure` | Titre, Tags et placeholders contrôlés par `verify_wiki.py`. |
| `À revoir` | Revue technique de la fiche non enregistrée dans cette matrice. |
| `À tester` | Aucun résultat d'essai représentatif n'est consigné. |
| `Validée` | À utiliser après revue technique et test représentatif documentés, avec date et version. |
| `N/A` | Contrôle non applicable, avec justification. |

## Fiches complètes

| Fiche | Sujet / périmètre indiqué | Sources primaires à confronter | Structure | Revue technique | Essai cible |
|---|---|---|---|---|---|
| [01 Active Directory DS, DNS, DHCP](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022) | Windows Server 2022, AD DS, DNS et DHCP | [R1] [R2] [R3] [R48] | OK structure | À revoir | À tester |
| [02 Pile LEMP](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb) | Debian 13, Nginx, PHP 8.4, MariaDB 11.8 | [R4] [R5] [R6] [R7] | OK structure | À revoir | À tester |
| [03 GLPI](/02-fiches-completes/debian/12/installation-deploiement/03-helpdesk-itsm-glpi-11-12-debian-12-13) | GLPI 11.12, Debian 12/13 | [R8] [R9] | OK structure | À revoir | À tester |
| [04 Zabbix](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12) | Zabbix 7.0 LTS, Debian 12 | [R10] [R11] | OK structure | À revoir | À tester |
| [05 Nextcloud](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis) | Nextcloud 29, Docker, MariaDB, Redis | [R12] [R13] [R14] | OK structure | À revoir | À tester |
| [06 Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker) | Traefik 3.1, Let's Encrypt, Docker | [R15] [R14] | OK structure | À revoir | À tester |
| [07 Stockage NAS/SAN](/02-fiches-completes/transverses/multi-os/installation-deploiement/07-stockage-reseau-nas-san-samba-nfsv4-iscsi) | Samba, NFSv4, iSCSI | [R16] [R17] [R18] | OK structure | À revoir | À tester |
| [08 Haute disponibilité](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy) | Keepalived/VRRP, HAProxy | [R19] [R20] | OK structure | À revoir | À tester |
| [09 Proxmox VE](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync) | Proxmox VE 8.x, cluster Corosync | [R21] [R22] | OK structure | À revoir | À tester |
| [10 OPNsense](/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha) | OPNsense, CARP/pfSync, haute disponibilité | [R23] [R24] | OK structure | À revoir | À tester |
| [11 Wazuh](/02-fiches-completes/debian/12/installation-deploiement/11-siem-xdr-centralise-wazuh-4x-debian-12) | Wazuh 4.x, Debian 12 | [R25] [R26] | OK structure | À revoir | À tester |
| [12 Proxmox Backup Server](/02-fiches-completes/proxmox/toutes-versions/autres/12-proxmox-backup-server-3x-pbs-deduplication) | Proxmox Backup Server 3.x | [R27] [R28] | OK structure | À revoir | À tester |
| [13 FreePBX/Asterisk](/02-fiches-completes/debian/12/installation-deploiement/13-telephonie-ip-freepbx-asterisk-20-debian-12) | FreePBX, Asterisk 20, Debian 12 | [R29] [R30] | OK structure | À revoir | À tester |
| [14 K3s](/02-fiches-completes/debian/13/installation-deploiement/14-orchestration-cluster-k3s-kubernetes-debian-13) | K3s/Kubernetes, Debian 13 | [R31] [R32] | OK structure | À revoir | À tester |
| [15 Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | Diagnostic et réparation réseau multi-OS | — | OK structure | À revoir | À tester |
| [16 Installation LXC Alpine](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox) | LXC Alpine sur Proxmox | — | OK structure | À revoir | À tester |
| [17 Diagnostic LXC Alpine](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services) | Réseau et services d'un LXC Alpine | — | OK structure | À revoir | À tester |
| [18 Sauvegarde LXC Alpine](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production) | Sauvegarde et restauration LXC Alpine | — | OK structure | À revoir | À tester |
| [19 BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12) | Sauvegarde et restauration Debian 12 avec BorgBackup | — | OK structure | À revoir | À tester |
| [20 Pile LEMP Ubuntu 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb) | Ubuntu Server 24.04, Nginx, PHP et MariaDB | — | OK structure | À revoir | À tester |
| [21 Pile Web Ubuntu 26.04](/02-fiches-completes/ubuntu/26-04/installation-deploiement/21-pile-web-ubuntu-server-26-04-nginx-php85-postgresql18) | Ubuntu Server 26.04, Nginx, PHP et PostgreSQL | — | OK structure | À revoir | À tester |
| [22 Migration Ubuntu 24.04 vers 26.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/22-migration-ubuntu-server-24-04-vers-26-04-lts) | Migration LTS Ubuntu Server | — | OK structure | À revoir | À tester |
| [23 Pile Web Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb) | Rocky Linux 9, Nginx, PHP-FPM et MariaDB | — | OK structure | À revoir | À tester |
| [24 Hardening Rocky Linux 9](/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9) | Sécurisation d'un serveur Rocky Linux 9 | — | OK structure | À revoir | À tester |
| [25 Déploiement Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production) | Déploiement d'un poste Windows 11 géré | — | OK structure | À revoir | À tester |
| [26 Reprise de forêt AD DS](/02-fiches-completes/windows/server-2022/autres/26-reprise-foret-ad-ds-windows-server-2022) | Reprise après sinistre d'une forêt Windows Server 2022 | — | OK structure | À revoir | À tester |
| [27 Sauvegarde données utilisateur Windows](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows) | Sauvegarde et restauration de fichiers Windows | — | OK structure | À revoir | À tester |
| [28 Installation Wiki.js](/02-fiches-completes/transverses/docker/installation-deploiement/28-installation-wikijs-docker-postgresql-traefik) | Wiki.js 2.x, Docker Compose, PostgreSQL 17 et Traefik | — | OK structure | À revoir | À tester |
| [29 Sauvegarde Ubuntu Server avec Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic) | Ubuntu Server 24.04/26.04, Restic, dépôt chiffré | [R49] [R50] | OK structure | À revoir | À tester |
| [30 Déploiement Windows Server 2025](/02-fiches-completes/windows/server-2025/installation-deploiement/30-deploiement-windows-server-2025-production) | Installation et réception d'un serveur Windows Server 2025 | [R51] [R52] | OK structure | À revoir | À tester |
| [31 Hardening Windows Server 2025](/02-fiches-completes/windows/server-2025/autres/31-hardening-windows-server-2025-production) | Contrôles de sécurité SMB, LDAP, OpenSSH et socle | [R51] [R53] [R54] | OK structure | À revoir | À tester |
| [32 Hardening hôte Docker](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production) | Réduction des risques sur un hôte Docker Linux | [R55] [R56] | OK structure | À revoir | À tester |
| [33 Installation OPNsense](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production) | Installation et configuration initiale d'une appliance OPNsense | [R60] [R61] | OK structure | À revoir | À tester |
| [34 Diagnostic Proxmox VE](/02-fiches-completes/proxmox/toutes-versions/diagnostic/34-diagnostic-proxmox-ve-cluster-stockage-vm) | Diagnostic cluster, réseau, stockage et invités Proxmox VE | [R57] [R58] [R59] | OK structure | À revoir | À tester |
| [35 Diagnostic OPNsense](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn) | Analyse de flux, DNS, VPN et CARP | [R62] [R63] | OK structure | À revoir | À tester |
| [36 Sauvegarde OPNsense](/02-fiches-completes/opnsense/toutes-versions/autres/36-sauvegarde-restauration-configuration-opnsense) | Export, protection et restauration de configuration OPNsense | [R64] [R65] [R66] | OK structure | À revoir | À tester |
| [37 Sauvegarde des stacks Docker](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker) | Dump de base, sauvegarde des volumes et test de restauration | [R14] [R67] | OK structure | À revoir | À tester |
| [38 Diagnostic NAS/SAN](/02-fiches-completes/transverses/multi-os/diagnostic/38-diagnostic-nas-san-samba-nfs-iscsi) | Pannes SMB/Samba, NFSv4, iSCSI et multipath | [R16] [R17] [R18] | OK structure | À revoir | À tester |
| [39 Déploiement Snipe-IT](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik) | Snipe-IT 8.8.3, Docker, MariaDB et Traefik | [R68] [R69] [R70] | OK structure | À revoir | À tester |
| [40 Déploiement iTop](/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404) | iTop 3.3.0 sur Debian 12 / Ubuntu 24.04 | [R71] [R72] [R73] | OK structure | À revoir | À tester |
| [41 Déploiement OCS Inventory](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13) | OCS Inventory 3.0 sur Debian 13 | [R74] [R75] [R76] | OK structure | À revoir | À tester |
| [42 Déploiement Znuny](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12) | Znuny 7.3.8 sur Debian 12 | [R77] [R78] | OK structure | À revoir | À tester |
| [43 Jira Service Management Cloud](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm) | Mise en service SaaS, projet, portail et contrôles d'accès | [R79] [R80] [R81] | OK structure | À revoir | À tester |
| [44 Lansweeper Classic](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server) | Installation Windows Server et scan pilote maîtrisé | [R82] [R83] [R84] | OK structure | À revoir | À tester |
| [45 Prometheus et Grafana](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13) | Prometheus 3.15.1, Grafana OSS, Node Exporter sur Debian 13 | [R85] [R86] [R87] | OK structure | À revoir | À tester |
| [46 LibreNMS](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04) | LibreNMS 26.10.2 sur Ubuntu Server 26.04, SNMPv3 | [R88] [R89] [R90] | OK structure | À revoir | À tester |
| [47 PRTG Network Monitor](/02-fiches-completes/windows/server-2022/installation-deploiement/47-deploiement-prtg-network-monitor-windows-server) | PRTG sur Windows Server, déploiement et pilote | [R96] [R97] [R98] | OK structure | À revoir | À tester |
| [48 Centreon](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13) | Centreon 26.10 Central sur Debian 13 | [R91] [R92] [R93] | OK structure | À revoir | À tester |
| [49 Graylog](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04) | Graylog 7.2, MongoDB et Data Node sur Ubuntu Server 24.04 | [R99] [R100] [R101] [R102] | OK structure | À revoir | À tester |
| [50 Elastic Stack](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13) | Elasticsearch et Kibana 9.5.x sur Debian 13 | [R103] [R104] [R105] [R106] | OK structure | À revoir | À tester |
| [51 Cacti](/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12) | Cacti 1.2.31, MariaDB et poller Debian 12 | [R107] [R108] [R109] [R110] [R111] | OK structure | À revoir | À tester |
| [52 Datadog Agent](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas) | Déploiement Linux pilote et Fleet Automation SaaS | [R112] [R113] [R114] [R115] | OK structure | À revoir | À tester |
| [53 Dynatrace OneAgent](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas) | Déploiement Linux pilote et gouvernance OneAgent SaaS | [R116] [R117] [R118] [R119] [R120] | OK structure | À revoir | À tester |
| [54 Splunk Enterprise](/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12) | Splunk Enterprise 10.2 autonome sur Debian 12 x86-64 | [R121] [R122] [R123] [R124] [R125] [R126] | OK structure | À revoir | À tester |
| [55 Hyper-V](/02-fiches-completes/windows/server-2022/installation-deploiement/55-deploiement-hyper-v-windows-server-2022) | Rôle Hyper-V et VM pilote sur Windows Server 2022 | [R127] [R128] [R129] [R130] | OK structure | À revoir | À tester |
| [56 VMware ESXi](/02-fiches-completes/vmware/esxi-8/installation-deploiement/56-deploiement-vmware-esxi-8-0) | Hôte VMware ESXi 8.0, mise en service initiale | [R131] [R132] [R133] | OK structure | À revoir | À tester |
| [57 Podman](/02-fiches-completes/rocky-linux/9/installation-deploiement/57-deploiement-podman-quadlet-rocky-linux-9) | Podman rootless et Quadlet sur Rocky Linux 9 | [R134] [R135] [R136] | OK structure | À revoir | À tester |
| [58 Veeam Backup & Replication](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022) | Veeam 13.1.2.57 sur Windows Server 2022 et job Hyper-V pilote | [R137] [R138] [R139] [R140] | OK structure | À revoir | À tester |
| [59 Bareos](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13) | Bareos 25 Director/Storage/File Daemon et catalogue PostgreSQL sur Debian 13 | [R141] [R142] [R143] [R144] [R145] | OK structure | À revoir | À tester |
| [60 TrueNAS SCALE](/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10) | NAS ZFS TrueNAS SCALE 25.10, pool, partage et sauvegarde | [R146] [R147] [R148] [R149] | OK structure | À revoir | À tester |
| [61 HashiCorp Vault](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13) | Vault Community avec Integrated Storage/Raft sur Debian 13 | [R150] [R151] [R152] [R153] | OK structure | À revoir | À tester |
| [62 Bitwarden](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker) | Bitwarden self-hosted Docker sur Linux | [R154] [R155] [R156] [R157] [R158] | OK structure | À revoir | À tester |
| [63 BIND 9](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13) | BIND 9 autoritatif, zones directe et inverse, Debian 13 | [R159] [R160] [R161] | OK structure | À revoir | À tester |
| [64 Kea DHCPv4](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13) | Kea DHCPv4, memfile et VLAN de laboratoire, Debian 13 | [R162] [R163] [R164] | OK structure | À revoir | À tester |
| [65 Samba AD DC](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13) | Domaine de laboratoire Samba AD DC avec DNS interne, Debian 13 | [R165] [R166] [R167] | OK structure | À revoir | À tester |
| [66 OpenMediaVault 8](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13) | OpenMediaVault 8 Synchrony sur Debian 13, stockage séparé et partage SMB pilote | [R168] [R169] [R170] [R171] [R172] [R173] [R174] | OK structure | À revoir | À tester |
| [67 Ceph Tentacle](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04) | Cephadm 20.2.4 sur Ubuntu 22.04, trois hôtes, OSD explicites et RBD pilote | [R175] [R176] [R177] [R178] [R179] [R180] [R181] [R182] | OK structure | À revoir | À tester |
| [68 Bacula Community](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports) | Bacula 15.0.3 Director/Storage/File Daemon et catalogue PostgreSQL sur Debian 12 Backports | [R183] [R184] [R185] [R186] [R187] [R188] [R189] [R190] | OK structure | À revoir | À tester |
| [69 Observium Community](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13) | Observium Community sur Debian 13, Apache/PHP, MariaDB, poller et pilote SNMPv3 | [R191] [R192] [R193] [R194] [R195] [R196] [R197] | OK structure | À revoir | À tester |
| [70 pfSense CE](/02-fiches-completes/pfsense/toutes-versions/installation-deploiement/70-deploiement-pfsense-ce-2-9-0-proxmox-lab) | pfSense CE 2.9.0 en VM Proxmox VE, deux interfaces isolées, règles et restauration de configuration | [R198] [R199] [R200] [R201] [R202] [R203] [R204] [R205] [R206] [R207] | OK structure | À revoir | À tester |
| [71 Suricata](/02-fiches-completes/debian/13/installation-deploiement/71-deploiement-suricata-8-debian-13-backports) | Suricata 8.0.7 sur Debian 13, règles ET Open et capture AF_PACKET IDS passive | [R208] [R209] [R210] [R211] [R212] [R213] [R214] [R215] | OK structure | À revoir | À tester |
| [72 Zeek](/02-fiches-completes/debian/13/installation-deploiement/72-deploiement-zeek-8-lts-debian-13) | Zeek 8.0 LTS standalone sur Debian 13, OBS, ZeekControl et capture AF_PACKET passive | [R216] [R217] [R218] [R219] [R220] [R221] | OK structure | À revoir | À tester |
| [73 NetBox](/02-fiches-completes/debian/13/installation-deploiement/73-deploiement-netbox-4-7-4-debian-13) | NetBox 4.7.4 sur Debian 13, PostgreSQL, Redis local, Gunicorn/Nginx et pilote IPAM | [R222] [R223] [R224] [R225] [R226] [R227] [R228] [R229] | OK structure | À revoir | À tester |
| [74 phpIPAM](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13) | phpIPAM 1.8.3 sur Debian 13, MariaDB, PHP-FPM/Nginx, saisie IPAM manuelle | [R230] [R231] [R232] [R233] [R234] [R235] | OK structure | À revoir | À tester |
| [75 QGIS](/02-fiches-completes/debian/13/installation-deploiement/75-deploiement-qgis-3-44-ltr-debian-13) | QGIS 3.44 LTR sur Debian 13, dépôt officiel signé, projet pilote et vérification CRS | [R236] [R237] [R238] [R239] [R240] [R241] | OK structure | À revoir | À tester |
| [76 draw.io Desktop](/02-fiches-completes/debian/13/installation-deploiement/76-deploiement-draw-io-desktop-32-6-1-debian-13) | draw.io Desktop 32.6.1 hors ligne sur Debian 13, paquet amd64 avec digest et projet local | [R242] [R243] [R244] [R245] [R246] [R247] | OK structure | À revoir | À tester |
| [77 GNS3](/02-fiches-completes/debian/13/installation-deploiement/77-deploiement-gns3-2-2-61-debian-13) | GNS3 2.2.61 stable sur Debian 13, GUI/serveur `pipx`, QEMU/KVM et laboratoire local isolé | [R248] [R249] [R250] [R251] [R252] [R253] [R254] | OK structure | À revoir | À tester |
| [78 Cisco Packet Tracer](/02-fiches-completes/ubuntu/24-04/installation-deploiement/78-deploiement-cisco-packet-tracer-9-0-1-ubuntu-24-04) | Cisco Packet Tracer 9.0.1 sur Ubuntu 24.04, téléchargement NetAcad et topologie pédagogique locale | [R255] [R256] [R257] [R258] | OK structure | À revoir | À tester |
| [79 KeePassXC](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13) | KeePassXC 2.8.0 AppImage sur Debian 13, vérification PGP/SHA-256, coffre KDBX et restauration | [R259] [R260] [R261] [R262] [R263] [R264] | OK structure | À revoir | À tester |
| [80 Visual Studio Code](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13) | VS Code Stable 1.143.1 sur Debian 13 amd64, dépôt APT Microsoft, Workspace Trust et contrôle des extensions | [R265] [R266] [R267] [R268] [R269] [R270] | OK structure | À revoir | À tester |
| [81 Python 3](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx) | Python Debian 13, bibliothèques APT, dépendances projet en venv et outils CLI via pipx | [R271] [R272] [R273] [R274] [R275] | OK structure | À revoir | À tester |
| [82 Git client](/02-fiches-completes/debian/13/installation-deploiement/82-administration-git-client-debian-13) | Client Git Debian 13, dépôt autorisé, revue de diff, commit et push sans credentials en clair | [R276] [R277] [R278] [R279] [R280] | OK structure | À revoir | À tester |
| [83 Wireshark](/02-fiches-completes/debian/13/installation-deploiement/83-installation-wireshark-debian-13-analyse-capture) | Wireshark/TShark Debian 13, analyse hors ligne et capture live à privilèges minimaux | [R281] [R282] [R283] [R284] [R285] [R286] [R287] | OK structure | À revoir | À tester |
| [84 PuTTY](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11) | PuTTY 0.85 sur Windows 11, MSI signé, clé utilisateur et vérification SSH host key | [R288] [R289] [R290] [R291] [R292] | OK structure | À revoir | À tester |
| [85 PowerShell](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11) | PowerShell 7.6.9 sur Windows 11, installation signée, shell, diagnostic local et scripts prudents | [R293] [R294] [R295] [R296] [R297] | OK structure | À revoir | À tester |
| [86 DMZ](/02-fiches-completes/transverses/multi-os/autres/86-conception-dmz-segmentation-flux-multi-os) | Conception multi-OS d'une DMZ, matrice de flux interzones, contrôles IPv4/IPv6 et validation en lab | [R298] [R299] [R300] [R301] [R302] | OK structure | À revoir | À tester |

## Classement logique par OS et type

Dans le pack local, chaque fiche est rangée sous `02-Fiches-Completes/<OS>/<Type>/`; les liens ci-dessous suivent cette arborescence. Ce rangement ne renomme pas les titres ni les URL des pages déjà publiées dans Wiki.js. Utiliser les trois mêmes types pour chaque OS : **Installation/Déploiement**, **Diagnostic**, **Autres** (architecture, stockage, sauvegarde, haute disponibilité ou sécurité).

| OS / plateforme | Installation / Déploiement | Diagnostic | Autres |
|---|---|---|---|
| Alpine Linux | [Installation LXC](/02-fiches-completes/alpine/toutes-versions/installation-deploiement/16-installation-lxc-alpine-proxmox) | [Diagnostic LXC](/02-fiches-completes/alpine/toutes-versions/diagnostic/17-diagnostic-lxc-alpine-reseau-services) | [Sauvegarde/restauration LXC](/02-fiches-completes/alpine/toutes-versions/autres/18-alpine-lxc-sauvegarde-restauration-production) |
| Debian 12 | [GLPI](/02-fiches-completes/debian/12/installation-deploiement/03-helpdesk-itsm-glpi-11-12-debian-12-13), [Zabbix](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12), [Wazuh](/02-fiches-completes/debian/12/installation-deploiement/11-siem-xdr-centralise-wazuh-4x-debian-12), [FreePBX/Asterisk](/02-fiches-completes/debian/12/installation-deploiement/13-telephonie-ip-freepbx-asterisk-20-debian-12), [Znuny](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12), [Cacti](/02-fiches-completes/debian/12/installation-deploiement/51-deploiement-cacti-1-2-31-debian-12), [Splunk Enterprise](/02-fiches-completes/debian/12/installation-deploiement/54-deploiement-splunk-enterprise-10-2-debian-12), [Bacula 15](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [BorgBackup](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12) |
| Debian 13 | [LEMP](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb), [K3s](/02-fiches-completes/debian/13/installation-deploiement/14-orchestration-cluster-k3s-kubernetes-debian-13), [OCS Inventory](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13), [Prometheus/Grafana](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13), [Centreon](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13), [Elastic Stack](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13), [Bareos](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13), [Vault](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13), [BIND 9](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13), [Kea](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13), [Samba AD DC](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13), [OpenMediaVault 8](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13), [Observium Community](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Haute disponibilité](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy) |
| Debian 13 | [LEMP](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb), [K3s](/02-fiches-completes/debian/13/installation-deploiement/14-orchestration-cluster-k3s-kubernetes-debian-13), [OCS Inventory](/02-fiches-completes/debian/13/installation-deploiement/41-deploiement-ocs-inventory-3-debian-13), [Prometheus/Grafana](/02-fiches-completes/debian/13/installation-deploiement/45-deploiement-prometheus-grafana-debian-13), [Centreon](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13), [Elastic Stack](/02-fiches-completes/debian/13/installation-deploiement/50-deploiement-elastic-stack-9-5-debian-13), [Bareos](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13), [Vault](/02-fiches-completes/debian/13/installation-deploiement/61-deploiement-hashicorp-vault-raft-debian-13), [BIND 9](/02-fiches-completes/debian/13/installation-deploiement/63-deploiement-bind9-autoritatif-debian-13), [Kea](/02-fiches-completes/debian/13/installation-deploiement/64-deploiement-kea-dhcpv4-debian-13), [Samba AD DC](/02-fiches-completes/debian/13/installation-deploiement/65-deploiement-samba-ad-dc-debian-13), [OpenMediaVault 8](/02-fiches-completes/debian/13/installation-deploiement/66-deploiement-openmediavault-8-debian-13) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Haute disponibilité](/02-fiches-completes/transverses/multi-os/autres/08-haute-disponibilite-keepalived-vrrp-haproxy) |
| Ubuntu Server 22.04 | [Ceph Tentacle](/02-fiches-completes/ubuntu/22-04/installation-deploiement/67-deploiement-ceph-tentacle-20-2-4-ubuntu-22-04) | [Contrôles de santé Ceph](/01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-verifier-sante-cluster) | — |
| Ubuntu Server 24.04 / 26.04 | [Pile LEMP 24.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/20-pile-lemp-ubuntu-server-24-04-nginx-php83-mariadb), [Pile Web 26.04](/02-fiches-completes/ubuntu/26-04/installation-deploiement/21-pile-web-ubuntu-server-26-04-nginx-php85-postgresql18), [Migration 24.04 vers 26.04](/02-fiches-completes/ubuntu/24-04/installation-deploiement/22-migration-ubuntu-server-24-04-vers-26-04-lts), [LibreNMS 26.04](/02-fiches-completes/ubuntu/26-04/installation-deploiement/46-deploiement-librenms-26-10-2-ubuntu-26-04), [Graylog 7.2](/02-fiches-completes/ubuntu/24-04/installation-deploiement/49-deploiement-graylog-7-2-ubuntu-24-04) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Sauvegarde Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic) |
| Rocky Linux 9 | [Pile Web](/02-fiches-completes/rocky-linux/9/installation-deploiement/23-pile-web-rocky-linux-9-nginx-php-mariadb), [Podman rootless/Quadlet](/02-fiches-completes/rocky-linux/9/installation-deploiement/57-deploiement-podman-quadlet-rocky-linux-9) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Hardening production](/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9) |
| Windows 10/11 | [Déploiement poste Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Sauvegarde/restauration fichiers](/02-fiches-completes/windows/toutes-versions/autres/27-sauvegarde-restauration-donnees-utilisateur-windows) |
| Windows Server 2022 | [AD DS, DNS et DHCP](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022), [Lansweeper Classic](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server), [PRTG](/02-fiches-completes/windows/server-2022/installation-deploiement/47-deploiement-prtg-network-monitor-windows-server), [Hyper-V](/02-fiches-completes/windows/server-2022/installation-deploiement/55-deploiement-hyper-v-windows-server-2022), [Veeam](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Reprise forêt AD DS](/02-fiches-completes/windows/server-2022/autres/26-reprise-foret-ad-ds-windows-server-2022) |
| Windows Server 2025 | [Déploiement production](/02-fiches-completes/windows/server-2025/installation-deploiement/30-deploiement-windows-server-2025-production) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Hardening et compatibilité](/02-fiches-completes/windows/server-2025/autres/31-hardening-windows-server-2025-production) |
| Debian 13 poste | [KeePassXC 2.8.0](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13), [validation du coffre](/01-fiches-simples/debian/13/vie-du-logiciel/keepassxc/fiche-simple-vm-debian-13-keepassxc-valider-coffre) | — | — |
| Debian 13 poste | [Visual Studio Code Stable](/02-fiches-completes/debian/13/installation-deploiement/80-deploiement-visual-studio-code-1-143-1-debian-13), [validation de l'installation](/01-fiches-simples/debian/13/vie-du-logiciel/vs-code/fiche-simple-vm-debian-13-vscode-valider-installation) | — | — |
| Debian 13 poste | [Python 3, venv et pipx](/02-fiches-completes/debian/13/installation-deploiement/81-administration-python-3-debian-13-venv-pipx), [validation venv/pipx](/01-fiches-simples/debian/13/vie-du-logiciel/python/fiche-simple-vm-debian-13-python-valider-venv-pipx) | — | — |
| Debian 13 poste | [Git client](/02-fiches-completes/debian/13/installation-deploiement/82-administration-git-client-debian-13), [validation clone/commit](/01-fiches-simples/debian/13/vie-du-systeme/fiches-par-theme/administration-systeme/fiche-simple-vm-debian-13-git-valider-clone-commit) | — | — |
| Debian 13 poste | [Wireshark](/02-fiches-completes/debian/13/installation-deploiement/83-installation-wireshark-debian-13-analyse-capture), [validation de capture locale](/01-fiches-simples/debian/13/vie-du-logiciel/wireshark/fiche-simple-vm-debian-13-wireshark-valider-capture-locale) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | — |
| Windows 11 poste | [PuTTY 0.85](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11), [validation SSH/host key](/01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-valider-ssh-hostkey) | — | — |
| Windows 11 poste | [Administration PowerShell 7.6.9](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11), [validation du shell](/01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-powershell-valider-shell-admin) | [Déploiement Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production) | — |
| Docker / conteneurs | [Nextcloud](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis), [Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker), [Wiki.js](/02-fiches-completes/transverses/docker/installation-deploiement/28-installation-wikijs-docker-postgresql-traefik), [Snipe-IT](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik), [Bitwarden self-hosted](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker) | [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [Hardening hôte Docker](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production), [Sauvegarde/restauration stacks](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker) |
| Proxmox VE | [Hyperviseur et cluster](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync) | [Diagnostic Proxmox](/02-fiches-completes/proxmox/toutes-versions/diagnostic/34-diagnostic-proxmox-ve-cluster-stockage-vm) | [Proxmox Backup Server](/02-fiches-completes/proxmox/toutes-versions/autres/12-proxmox-backup-server-3x-pbs-deduplication) |
| VMware ESXi | [Installation et mise en service ESXi 8.0](/02-fiches-completes/vmware/esxi-8/installation-deploiement/56-deploiement-vmware-esxi-8-0) | — | — |
| OPNsense | [Installation appliance](/02-fiches-completes/opnsense/toutes-versions/installation-deploiement/33-installation-appliance-opnsense-production) | [Diagnostic réseau](/02-fiches-completes/opnsense/toutes-versions/diagnostic/35-diagnostic-reseau-opnsense-flux-dns-vpn) | [Sauvegarde/restauration](/02-fiches-completes/opnsense/toutes-versions/autres/36-sauvegarde-restauration-configuration-opnsense), [HA CARP/pfSync](/02-fiches-completes/opnsense/toutes-versions/autres/10-pare-feu-appliance-opnsense-carp-pfsync-ha) |
| Multi-OS / SaaS / stockage | [Samba, NFSv4 et iSCSI](/02-fiches-completes/transverses/multi-os/installation-deploiement/07-stockage-reseau-nas-san-samba-nfsv4-iscsi), [iTop](/02-fiches-completes/transverses/multi-os/installation-deploiement/40-deploiement-itop-3-3-debian12-ubuntu2404), [TrueNAS SCALE](/02-fiches-completes/truenas/scale-25-10/installation-deploiement/60-deploiement-truenas-scale-25-10), [Jira Service Management Cloud](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/43-deploiement-jira-service-management-cloud-itsm), [Datadog Agent](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/52-deploiement-datadog-agent-linux-saas), [Dynatrace OneAgent](/02-fiches-completes/transverses/cloud-saas/installation-deploiement/53-deploiement-dynatrace-oneagent-linux-saas) | [Diagnostic NAS/SAN](/02-fiches-completes/transverses/multi-os/diagnostic/38-diagnostic-nas-san-samba-nfs-iscsi), [Dépannage réseau](/02-fiches-completes/transverses/multi-os/diagnostic/15-depannage-reseau-diagnostic-complet-multi-os) | [NAS/SAN, Samba, NFSv4, iSCSI](/02-fiches-completes/transverses/multi-os/installation-deploiement/07-stockage-reseau-nas-san-samba-nfsv4-iscsi) |

## Questions/Réponses et réparations

| Fiche | Sujet | Sources primaires à confronter | Structure | Revue technique | Essai cible |
|---|---|---|---|---|---|
| [QA Bash](/04-questions-reponses/fiche-qa-bash-lecture-et-analyse-script) | Lire et analyser un script Bash | [R33] [R34] | OK structure | À revoir | À tester |
| [QA disque plein](/04-questions-reponses/fiche-qa-depannage-disque-plein-purge-apt-journalctl) | Diagnostic disque, APT et journal | [R35] [R36] [R37] | OK structure | À revoir | À tester |
| [QA Dockerfile](/04-questions-reponses/fiche-qa-dockerfile-best-practices-security) | Bonnes pratiques et sécurité Dockerfile | [R14] [R38] | OK structure | À revoir | À tester |
| [QA SSH/Fail2ban](/04-questions-reponses/fiche-qa-ssh-ed25519-et-fail2ban-security) | Clés SSH ED25519 et Fail2ban | [R39] [R40] [R41] | OK structure | À revoir | À tester |
| [QA YAML/Compose](/04-questions-reponses/fiche-qa-yaml-docker-compose-lecture-et-validation) | Lire et valider Docker Compose/YAML | [R42] [R43] | OK structure | À revoir | À tester |
| [Réparation DNS Linux](/04-questions-reponses/reparation-dns-linux-resolution-echec) | Résolution DNS Linux en échec | [R35] [R44] [R45] | OK structure | À revoir | À tester |
| [Réparation Docker](/04-questions-reponses/reparation-docker-conteneur-redemarrage-boucle) | Conteneur en boucle de redémarrage | [R14] [R46] | OK structure | À revoir | À tester |
| [Réparation Nginx/PHP-FPM](/04-questions-reponses/reparation-nginx-php-fpm-502-bad-gateway) | Erreur HTTP 502 | [R4] [R7] [R36] | OK structure | À revoir | À tester |
| [Réparation SSH](/04-questions-reponses/reparation-ssh-acces-distant-impossible) | Accès distant SSH impossible | [R39] [R40] [R36] | OK structure | À revoir | À tester |
| [Réparation systemd](/04-questions-reponses/reparation-service-systemd-echec-demarrage) | Service systemd en échec | [R36] [R37] | OK structure | À revoir | À tester |
| [Réparation domaine Windows](/04-questions-reponses/reparation-windows-echec-joindre-domaine-ad) | Poste Windows impossible à joindre au domaine AD | [R1] [R3] [R47] | OK structure | À revoir | À tester |

## Références officielles

Les pages ci-dessous ont été consultées le 27 octobre 2026. Avant toute validation, vérifier qu'elles s'appliquent bien à la version exacte visée par la fiche; les liens `latest` évoluent.

| ID | Documentation primaire |
|---|---|
| R1 | [Microsoft Learn — Vue d'ensemble AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) |
| R2 | [Microsoft Learn — Install-ADDSDomainController](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsdomaincontroller?view=windowsserver2022-ps) |
| R3 | [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/) |
| R4 | [NGINX — Documentation](https://nginx.org/en/docs/) |
| R5 | [PHP — Documentation officielle](https://www.php.net/manual/en/) |
| R6 | [MariaDB — Documentation Server](https://mariadb.com/docs/server/) |
| R7 | [PHP — PHP-FPM](https://www.php.net/manual/en/install.fpm.php) |
| R8 | [GLPI — Documentation d'installation](https://glpi-install.readthedocs.io/en/latest/) |
| R9 | [GLPI — Documentation projet](https://glpi-project.org/documentation/) |
| R10 | [Zabbix 7.0 — Manuel officiel](https://www.zabbix.com/documentation/7.0/en/manual) |
| R11 | [Debian — Documentation officielle](https://www.debian.org/doc/) |
| R12 | [Nextcloud 29 — Manuel d'administration](https://docs.nextcloud.com/server/29/admin_manual/) |
| R13 | [Nextcloud — Documentation Docker](https://github.com/nextcloud/docker) |
| R14 | [Docker — Documentation officielle](https://docs.docker.com/) |
| R15 | [Traefik 3.1 — Documentation officielle](https://doc.traefik.io/traefik/v3.1/) |
| R16 | [Samba — Documentation officielle](https://www.samba.org/samba/docs/) |
| R17 | [nfs-utils — exports(5)](https://man7.org/linux/man-pages/man5/exports.5.html) |
| R18 | [open-iscsi — Documentation du projet](https://github.com/open-iscsi/open-iscsi) |
| R19 | [Keepalived — Documentation](https://keepalived.readthedocs.io/en/latest/) |
| R20 | [HAProxy — Tutoriels de configuration](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/) |
| R21 | [Proxmox VE — Documentation officielle](https://pve.proxmox.com/pve-docs/) |
| R22 | [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/pve-admin-guide.html) |
| R23 | [OPNsense — Haute disponibilité CARP/pfSync](https://docs.opnsense.org/manual/hacarp.html) |
| R24 | [OPNsense — Guide de configuration CARP](https://docs.opnsense.org/manual/how-tos/carp.html) |
| R25 | [Wazuh — Documentation officielle](https://documentation.wazuh.com/current/) |
| R26 | [Wazuh — Notes de version](https://documentation.wazuh.com/current/release-notes/index.html) |
| R27 | [Proxmox Backup Server — Documentation officielle](https://pbs.proxmox.com/docs/) |
| R28 | [Proxmox Backup Server — Stockage et protection des sauvegardes](https://pbs.proxmox.com/docs/storage.html) |
| R29 | [Asterisk 20 — Documentation officielle](https://docs.asterisk.org/Asterisk_20_Documentation/) |
| R30 | [FreePBX — Base de connaissances officielle Sangoma](https://sangomakb.atlassian.net/wiki/spaces/FP/) |
| R31 | [K3s — Documentation officielle](https://docs.k3s.io/) |
| R32 | [Kubernetes — Documentation officielle](https://kubernetes.io/docs/) |
| R33 | [GNU Bash — Manuel de référence](https://www.gnu.org/software/bash/manual/bash.html) |
| R34 | [The Open Group — POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html) |
| R35 | [Debian — Documentation officielle](https://www.debian.org/doc/) |
| R36 | [systemd — systemctl(1)](https://www.freedesktop.org/software/systemd/man/latest/systemctl.html) |
| R37 | [systemd — journalctl(1)](https://www.freedesktop.org/software/systemd/man/latest/journalctl.html) |
| R38 | [Docker — Bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/) |
| R39 | [OpenBSD — ssh(1)](https://man.openbsd.org/ssh) |
| R40 | [OpenBSD — sshd_config(5)](https://man.openbsd.org/sshd_config) |
| R41 | [Fail2ban — Projet officiel](https://github.com/fail2ban/fail2ban) |
| R42 | [Docker — Référence Compose](https://docs.docker.com/compose/compose-file/) |
| R43 | [YAML — Spécification 1.2.2](https://yaml.org/spec/1.2.2/) |
| R44 | [systemd — systemd-resolved(8)](https://www.freedesktop.org/software/systemd/man/latest/systemd-resolved.html) |
| R45 | [Linux man-pages — resolv.conf(5)](https://man7.org/linux/man-pages/man5/resolv.conf.5.html) |
| R46 | [Docker — Redémarrage automatique des conteneurs](https://docs.docker.com/engine/containers/start-containers-automatically/) |
| R47 | [Microsoft Learn — Joindre un ordinateur à un domaine](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/join-computer-to-domain) |
| R48 | [Microsoft Learn — DHCP Server dans Windows Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top) |
| R49 | [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/) |
| R50 | [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/) |
| R51 | [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025) |
| R52 | [Microsoft Learn — Options d'installation Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server) |
| R53 | [Microsoft Learn — Sécuriser le trafic SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic) |
| R54 | [Microsoft Learn — Signature LDAP pour AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-signing) |
| R55 | [Docker — Sécurité du moteur](https://docs.docker.com/engine/security/) |
| R56 | [Docker — Bonnes pratiques de build](https://docs.docker.com/build/building/best-practices/) |
| R57 | [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager) |
| R58 | [Proxmox VE — Configuration réseau](https://pve.proxmox.com/wiki/Network_Configuration) |
| R59 | [Proxmox VE — Stockage](https://pve.proxmox.com/wiki/Storage) |
| R60 | [OPNsense — Installation](https://docs.opnsense.org/manual/install.html) |
| R61 | [OPNsense — Configuration initiale](https://docs.opnsense.org/manual/setup.html) |
| R62 | [OPNsense — Outils de diagnostic réseau](https://docs.opnsense.org/manual/diagnostics_interfaces.html) |
| R63 | [OPNsense — Dépannage général](https://docs.opnsense.org/troubleshooting.html) |
| R64 | [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html) |
| R65 | [OPNsense — Sauvegarde via SFTP](https://docs.opnsense.org/manual/sftp-backup.html) |
| R66 | [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html) |
| R67 | [Docker — Volumes, sauvegarde et restauration](https://docs.docker.com/engine/storage/volumes/) |
| R68 | [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker) |
| R69 | [Snipe-IT — Prérequis](https://snipe-it.readme.io/docs/requirements) |
| R70 | [Snipe-IT — Sauvegarde et restauration](https://snipe-it.readme.io/docs/backups) |
| R71 | [iTop — Installation et mise à niveau](https://www.itophub.io/wiki/page?id=latest:install:start) |
| R72 | [iTop — Compatibilité et prérequis](https://www.itophub.io/wiki/page?id=latest:install:requirements) |
| R73 | [iTop — Tâches planifiées et sauvegardes](https://www.itophub.io/wiki/page?id=latest:admin:cron) |
| R74 | [OCS Inventory — Installation sur Debian/Ubuntu et dépôts officiels](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/installation-methods/using-official-repositories.md) |
| R75 | [OCS Inventory — Prérequis système](https://documentation.ocsinventory-ng.org/administrator-docs/system-requirements.md) |
| R76 | [OCS Inventory — Sécuriser le serveur par TLS](https://documentation.ocsinventory-ng.org/administrator-docs/server-setup/security/securing-ocs-with-ssl.md) |
| R77 | [Znuny — Instructions d'installation](https://doc.znuny.org/znuny/installation/index.html) |
| R78 | [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html) |
| R79 | [Atlassian — Démarrer avec Jira Service Management](https://support.atlassian.com/jira-service-management-cloud/docs/get-started-with-jira-service-management/) |
| R80 | [Atlassian — Bases d'un projet ITSM](https://support.atlassian.com/jira-service-management-cloud/docs/itsm-project-basics/) |
| R81 | [Atlassian — Permissions clients JSM](https://support.atlassian.com/jira-service-management-cloud/docs/customer-permissions-for-your-service-project-and-jira-site/) |
| R82 | [Lansweeper Classic — Prérequis d'installation](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md) |
| R83 | [Lansweeper Classic — Installer on-premises](https://docs.lansweeper.com/classic/docs/install-lansweeper-on-prem.md) |
| R84 | [Lansweeper Classic — Identifiants de scan](https://docs.lansweeper.com/classic/docs/create-and-map-scanning-credentials.md) |
| R85 | [Prometheus — Version 3.15.1](https://github.com/prometheus/prometheus/releases/tag/v3.15.1) |
| R86 | [Grafana — Installer sur Debian/Ubuntu](https://grafana.com/docs/grafana/latest/setup-grafana/installation/debian/) |
| R87 | [Grafana — Configurer la datasource Prometheus](https://grafana.com/docs/grafana/latest/datasources/prometheus/configure/) |
| R88 | [LibreNMS — Installation](https://docs.librenms.org/Installation/Install-LibreNMS/) |
| R89 | [LibreNMS — SNMPv3](https://docs.librenms.org/Support/SNMP-Configuration-Examples/) |
| R90 | [LibreNMS — Ajouter un appareil](https://docs.librenms.org/Support/Adding-a-Device/) |
| R91 | [Centreon 26.10 — Installation unattended](https://docs.centreon.com/docs/installation/installation-of-a-central-server/unattended-install-central/) |
| R92 | [Centreon 26.10 — Installation par paquets](https://docs.centreon.com/docs/installation/installation-of-a-central-server/using-packages/) |
| R93 | [Centreon — Installation Web et post-installation](https://docs.centreon.com/docs/installation/web-and-post-installation/) |
| R96 | [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements) |
| R97 | [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server) |
| R98 | [Paessler — Appareils et capteurs](https://www.paessler.com/manuals/prtg/device_and_sensor_setup) |
| R99 | [Graylog 7.2 — Installation Ubuntu](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm) |
| R100 | [Graylog — Sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm) |
| R101 | [Graylog — Matrice de compatibilité](https://go2docs.graylog.org/current/downloading_and_installing_graylog/compatibility_matrix.htm) |
| R102 | [MongoDB — Installer sur Ubuntu](https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-ubuntu/) |
| R103 | [Elastic — Installer Elasticsearch avec un paquet Debian](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package) |
| R104 | [Elastic — Installer Kibana avec un paquet Debian](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package) |
| R105 | [Elastic — Configuration système importante](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/important-system-configuration) |
| R106 | [Elastic — Guide de production](https://www.elastic.co/docs/deploy-manage/production-guidance) |
| R107 | [Cacti — Documentation officielle](https://docs.cacti.net/) |
| R108 | [Cacti — Installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md) |
| R109 | [Cacti — Prérequis](https://docs.cacti.net/Requirements.md) |
| R110 | [Cacti — Release 1.2.31](https://www.cacti.net/info/changelog) |
| R111 | [Cacti — Gestion des appareils et SNMP](https://docs.cacti.net/Devices.md) |
| R112 | [Datadog — Agent Linux](https://docs.datadoghq.com/agent/basic_agent_usage/ubuntu/) |
| R113 | [Datadog — Fleet Automation](https://docs.datadoghq.com/agent/fleet_automation/) |
| R114 | [Datadog — Configuration de l'Agent](https://docs.datadoghq.com/agent/configuration/agent-configuration-files/) |
| R115 | [Datadog — Sécurité de l'Agent](https://docs.datadoghq.com/agent/security/) |
| R116 | [Dynatrace — Installer OneAgent Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/install-oneagent-on-linux) |
| R117 | [Dynatrace — Paramètres OneAgent Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux) |
| R118 | [Dynatrace — Mode non privilégié Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged) |
| R119 | [Dynatrace — Désinstaller OneAgent Linux](https://docs.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux) |
| R120 | [Dynatrace — Support des technologies](https://docs.dynatrace.com/docs/ingest-from/technology-support) |
| R121 | [Splunk 10.2 — Installer sur Linux](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/install-on-linux) |
| R122 | [Splunk 10.2 — Systèmes supportés et exigences](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/plan-your-splunk-enterprise-installation/system-requirements-for-use-of-splunk-enterprise-on-premises) |
| R123 | [Splunk 10.2 — Premier démarrage](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/start-using-splunk-enterprise/start-splunk-enterprise-for-the-first-time) |
| R124 | [Splunk 10.2 — Exécuter avec un compte non-root](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/install-splunk-enterprise-on-linux-or-macos/run-splunk-enterprise-as-a-different-or-non-root-user) |
| R125 | [Splunk 10.2 — Vérifier l'intégrité de l'installation](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/secure-your-splunk-enterprise-installation/install-splunk-enterprise-securely) |
| R126 | [Splunk 10.2 — Sécuriser le système avant installation](https://help.splunk.com/en/splunk-enterprise/get-started/install-and-upgrade/10.2/secure-your-splunk-enterprise-installation/secure-your-system-before-you-install-splunk-enterprise) |
| R127 | [Microsoft — Installer Hyper-V sur Windows Server](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v) |
| R128 | [Microsoft — Créer une VM Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-machine-in-hyper-v) |
| R129 | [Microsoft — Créer un commutateur virtuel Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/create-a-virtual-switch-for-hyper-v-virtual-machines) |
| R130 | [Microsoft — Planifier le réseau Hyper-V](https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/plan/plan-hyper-v-networking-in-windows-server) |
| R131 | [Broadcom — ESXi Installation and Setup 8.0](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0.html) |
| R132 | [Broadcom — Parcours d'installation et configuration ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/overview-of-the-installation-and-setup-process_esx-install.html) |
| R133 | [Broadcom — Installer et configurer ESXi](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/esxi-installation-and-setup-8-0/installing-and-setting-up-esxi-install.html) |
| R134 | [Podman — Référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html) |
| R135 | [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html) |
| R136 | [Podman — Introduction](https://docs.podman.io/en/latest/Introduction.html) |
| R137 | [Veeam 13 — Installer Backup & Replication sous Windows](https://helpcenter.veeam.com/docs/vbr/userguide/install_vbr.html) |
| R138 | [Veeam 13 — Exigences du serveur de sauvegarde](https://helpcenter.veeam.com/docs/vbr/userguide/system_requirements_backup_server.html) |
| R139 | [Veeam 13 — Dépôts de sauvegarde](https://helpcenter.veeam.com/docs/vbr/userguide/backup_repository.html) |
| R140 | [Veeam 13 — Créer des jobs Hyper-V](https://helpcenter.veeam.com/docs/vbr/userguide/backup_job_hv.html) |
| R141 | [Bareos 25 — Installer le serveur](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareos.html) |
| R142 | [Bareos — Installer un client](https://docs.bareos.org/IntroductionAndTutorial/InstallingBareosClient.html) |
| R143 | [Bareos — Démarrage et validation des configurations](https://docs.bareos.org/IntroductionAndTutorial/GettingStartedWithBareos.html) |
| R144 | [Bareos — Commande de restauration](https://docs.bareos.org/TasksAndConcepts/TheRestoreCommand.html) |
| R145 | [Bareos — Éléments critiques avant production](https://docs.bareos.org/IntroductionAndTutorial/CriticalItemsToImplementBeforeProduction.html) |
| R146 | [TrueNAS SCALE 25.10 — Installation](https://www.truenas.com/docs/scale/25.10/gettingstarted/install/installingscale/) |
| R147 | [TrueNAS SCALE 25.10 — Guide matériel](https://www.truenas.com/docs/scale/25.10/gettingstarted/scalehardwareguide/) |
| R148 | [TrueNAS SCALE 25.10 — Mise en place du stockage](https://www.truenas.com/docs/scale/25.10/gettingstarted/configure/setupstoragescale/) |
| R149 | [TrueNAS SCALE 25.10 — Sauvegarde](https://www.truenas.com/docs/scale/25.10/gettingstarted/configure/setupbackupscale/) |
| R150 | [HashiCorp — Installer Vault](https://developer.hashicorp.com/vault/install) |
| R151 | [HashiCorp — Déployer Vault avec Integrated Storage/Raft](https://developer.hashicorp.com/vault/tutorials/day-one-raft/raft-deployment-guide) |
| R152 | [HashiCorp — Durcissement production](https://developer.hashicorp.com/vault/docs/concepts/production-hardening) |
| R153 | [HashiCorp — Configuration Integrated Storage](https://developer.hashicorp.com/vault/docs/configuration/storage/raft) |
| R154 | [Bitwarden — Déploiement Linux standard](https://bitwarden.com/help/install-on-premise-linux/) |
| R155 | [Bitwarden — Héberger une organisation](https://bitwarden.com/help/self-host-an-organization/) |
| R156 | [Bitwarden — Sauvegarder le serveur](https://bitwarden.com/help/backup-on-premise/) |
| R157 | [Bitwarden — Mise à jour du serveur](https://bitwarden.com/help/updating-on-premise/) |
| R158 | [Bitwarden — Exigences réseau](https://bitwarden.com/help/networking-requirements/) |
| R159 | [ISC BIND 9 — Configurations et fichiers de zone](https://bind9.readthedocs.io/en/latest/chapter3.html) |
| R160 | [ISC BIND 9 — Sécurité](https://bind9.readthedocs.io/en/latest/chapter7.html) |
| R161 | [Debian 13 — Paquet BIND 9](https://packages.debian.org/trixie/bind9) |
| R162 | [ISC Kea — Installation et paquets](https://kea.readthedocs.io/en/latest/arm/install.html) |
| R163 | [ISC Kea — Serveur DHCPv4](https://kea.readthedocs.io/en/latest/arm/dhcp4-srv.html) |
| R164 | [ISC Kea — Sécurité](https://kea.readthedocs.io/en/latest/arm/security.html) |
| R165 | [Debian 13 — Samba AD DC, samba(8)](https://manpages.debian.org/trixie/samba-ad-dc/samba.8.en.html) |
| R166 | [Debian 13 — Outil samba-tool(8)](https://manpages.debian.org/trixie/python3-samba/samba-tool.8.en.html) |
| R167 | [Debian 13 — Validation Samba, testparm(1)](https://manpages.debian.org/trixie/samba-common-bin/testparm.1.en.html) |
| R168 | [OpenMediaVault 8 — Versions et Debian de base](https://docs.openmediavault.org/en/latest/releases.html) |
| R169 | [OpenMediaVault — Installation sur Debian](https://docs.openmediavault.org/en/latest/installation/on_debian.html) |
| R170 | [OpenMediaVault — Prérequis](https://docs.openmediavault.org/en/latest/prerequisites.html) |
| R171 | [OpenMediaVault — Systèmes de fichiers et montages](https://docs.openmediavault.org/en/latest/administration/storage/filesystems.html) |
| R172 | [OpenMediaVault — Dossiers partagés et permissions](https://docs.openmediavault.org/en/latest/administration/storage/sharedfolders.html) |
| R173 | [OpenMediaVault — Service Samba](https://docs.openmediavault.org/en/latest/administration/services/samba.html) |
| R174 | [OpenMediaVault — Gestion des mises à jour](https://docs.openmediavault.org/en/latest/various/apt.html) |
| R175 | [Ceph Tentacle — Versions actives et cycle de vie](https://docs.ceph.com/en/tentacle/releases/) |
| R176 | [Ceph Tentacle — Recommandations OS](https://docs.ceph.com/en/tentacle/start/os-recommendations/) |
| R177 | [Ceph Tentacle — Déployer avec cephadm](https://docs.ceph.com/en/tentacle/cephadm/install/) |
| R178 | [Ceph Tentacle — Gestion des hôtes](https://docs.ceph.com/en/tentacle/cephadm/host-management/) |
| R179 | [Ceph Tentacle — Service Monitor](https://docs.ceph.com/en/tentacle/cephadm/services/mon/) |
| R180 | [Ceph Tentacle — Service OSD](https://docs.ceph.com/en/tentacle/cephadm/services/osd/) |
| R181 | [Ceph Tentacle — Recommandations matérielles](https://docs.ceph.com/en/tentacle/start/hardware-recommendations/) |
| R182 | [Ceph Tentacle — Health checks](https://docs.ceph.com/en/tentacle/rados/operations/health-checks/) |
| R183 | [Bacula Community 15.0.3 — annonce et plateformes binaires](https://www.bacula.org/bacula-community-15-0-3-released/) |
| R184 | [Debian Backports — bacula-dir 15.0.3](https://manpages.debian.org/bookworm-backports/bacula-director/bacula-dir.8.en.html) |
| R185 | [Bacula Community — paquets binaires et conditions d'accès/support](https://www.bacula.org/bacula-binary-package-download/) |
| R186 | [Bacula 15.0.x — configuration du Director](https://www.bacula.org/15.0.x-manuals/en/main/Configuring_Director.html) |
| R187 | [Bacula 15.0.x — chiffrement TLS](https://www.bacula.org/15.0.x-manuals/en/main/Bacula_TLS_Communications_E.html) |
| R188 | [Bacula 15.0.x — maintenance et sauvegarde du catalogue](https://www.bacula.org/15.0.x-manuals/en/main/Catalog_Maintenance.html) |
| R189 | [Debian Backports — bacula-sd 15.0.3](https://manpages.debian.org/bookworm-backports/bacula-sd/bacula-sd.8.en.html) |
| R190 | [Debian Backports — bacula-fd 15.0.3](https://manpages.debian.org/bookworm-backports/bacula-fd/bacula-fd.8.en.html) |
| R191 | [Observium — distributions Debian/Ubuntu compatibles et installation](https://docs.observium.org/install_debian/) |
| R192 | [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/) |
| R193 | [Observium — configuration et paramètres SNMP](https://docs.observium.org/config_options/) |
| R194 | [Observium — ajout d'équipements](https://docs.observium.org/add_device/) |
| R195 | [Observium — configuration Net-SNMP Linux](https://docs.observium.org/device_linux/) |
| R196 | [Observium — mise à niveau Community et Subscription](https://docs.observium.org/updating/) |
| R197 | [Observium — dimensionnement](https://docs.observium.org/hardware_scaling/) |
| R198 | [Netgate — versions pfSense prises en charge](https://docs.netgate.com/pfsense/en/latest/releases/index.html) |
| R199 | [Netgate — pfSense CE 2.9.0](https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html) |
| R200 | [Netgate — exigences matérielles minimales](https://docs.netgate.com/pfsense/en/latest/hardware/minimum-requirements.html) |
| R201 | [Netgate — télécharger l'image et vérifier SHA-256](https://docs.netgate.com/pfsense/en/latest/install/download-installer-image.html) |
| R202 | [Netgate — walkthrough d'installation](https://docs.netgate.com/pfsense/en/latest/install/install-walkthrough.html) |
| R203 | [Netgate — virtualisation Proxmox VE](https://docs.netgate.com/pfsense/en/latest/recipes/virtualize-proxmox-ve.html) |
| R204 | [Netgate — identifiants par défaut](https://docs.netgate.com/pfsense/en/latest/usermanager/defaults.html) |
| R205 | [Netgate — bonnes pratiques firewall](https://docs.netgate.com/pfsense/en/latest/firewall/best-practices.html) |
| R206 | [Netgate — sauvegarde de configuration GUI](https://docs.netgate.com/pfsense/en/latest/backup/configuration.html) |
| R207 | [Netgate — restaurer une configuration](https://docs.netgate.com/pfsense/en/latest/backup/restore.html) |
| R208 | [Debian Backports — Suricata 8.0.7](https://manpages.debian.org/trixie-backports/suricata/suricata.1.en.html) |
| R209 | [Debian Backports — suricata-update 1.3.8](https://manpages.debian.org/trixie-backports/suricata-update/suricata-update.1.en.html) |
| R210 | [Suricata — paquets Debian](https://docs.suricata.io/en/latest/install/debian.html) |
| R211 | [Suricata — Quickstart IDS/EVE](https://docs.suricata.io/en/latest/quickstart.html) |
| R212 | [Suricata — configuration YAML](https://docs.suricata.io/en/latest/configuration/suricata-yaml.html) |
| R213 | [Suricata — AF_PACKET](https://docs.suricata.io/en/latest/capture-hardware/af-packet.html) |
| R214 | [Suricata — règles et suricata-update](https://docs.suricata.io/en/latest/rule-management/suricata-update.html) |
| R215 | [Suricata — options de ligne de commande](https://docs.suricata.io/en/latest/command-line-options.html) |
| R216 | [Zeek — installation et lignes binaires LTS](https://docs.zeek.org/en/stable/install.html) |
| R217 | [OBS — dépôt Zeek Debian 13](https://download.opensuse.org/repositories/security:/zeek/Debian_13/) |
| R218 | [Zeek — guide de démarrage et logs](https://docs.zeek.org/en/stable/quickstart.html) |
| R219 | [Zeek — supervision passive et sources réseau](https://docs.zeek.org/en/stable/monitoring.html) |
| R220 | [Zeek — cluster et acquisition AF_PACKET](https://docs.zeek.org/en/stable/cluster-setup.html) |
| R221 | [Zeek — logs communs](https://docs.zeek.org/en/stable/logs/index.html) |
| R222 | [NetBox — releases officielles](https://github.com/netbox-community/netbox/releases) |
| R223 | [NetBox — exigences de version](https://netbox.readthedocs.io/en/stable/installation/) |
| R224 | [NetBox — installation depuis une archive de release](https://netbox.readthedocs.io/en/stable/installation/3-netbox/) |
| R225 | [NetBox — installation PostgreSQL](https://netbox.readthedocs.io/en/stable/installation/1-postgresql/) |
| R226 | [NetBox — installation Redis et restriction réseau](https://netbox.readthedocs.io/en/stable/installation/2-redis/) |
| R227 | [NetBox — Gunicorn et services systemd](https://netbox.readthedocs.io/en/stable/installation/4a-gunicorn/) |
| R228 | [NetBox — serveur HTTP Nginx](https://netbox.readthedocs.io/en/stable/installation/5-http-server/) |
| R229 | [NetBox — configuration, permissions et IPAM](https://netbox.readthedocs.io/en/stable/configuration/required-parameters/) |
| R230 | [phpIPAM — releases et empreintes SHA-256](https://github.com/phpipam/phpipam/releases) |
| R231 | [phpIPAM 1.8.3 — notes de version](https://github.com/phpipam/phpipam/releases/tag/v1.8.3) |
| R232 | [phpIPAM 1.8.3 — versions PHP et bases compatibles](https://github.com/phpipam/phpipam/blob/v1.8.3/README.md) |
| R233 | [phpIPAM — installation et prérequis](https://phpipam.net/documents/installation/) |
| R234 | [phpIPAM — mise à niveau et restauration](https://phpipam.net/documents/upgrade/) |
| R235 | [phpIPAM 1.8.3 — configuration de référence](https://github.com/phpipam/phpipam/blob/v1.8.3/config.dist.php) |
| R236 | [QGIS — releases officielles et versions LTR](https://github.com/qgis/QGIS/releases) |
| R237 | [QGIS — installation Linux et dépôt Debian officiel](https://qgis.org/resources/installation-guide/) |
| R238 | [QGIS 3.44 — fichiers de projet et chemins de couches](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/project_files.html) |
| R239 | [QGIS 3.44 — configuration, CRS et profils utilisateur](https://docs.qgis.org/3.44/en/docs/user_manual/introduction/qgis_configuration.html) |
| R240 | [QGIS 3.44 — projections et transformations](https://docs.qgis.org/3.44/en/docs/user_manual/working_with_projections/working_with_projections.html) |
| R241 | [QGIS 3.44 — système d'authentification](https://docs.qgis.org/3.44/en/docs/user_manual/auth_system/index.html) |
| R242 | [draw.io Desktop — releases officielles](https://github.com/jgraph/drawio-desktop/releases) |
| R243 | [draw.io Desktop 32.6.1 — notes de release](https://github.com/jgraph/drawio-desktop/releases/tag/v32.6.1) |
| R244 | [GitHub API — assets et digest SHA-256 draw.io 32.6.1](https://api.github.com/repos/jgraph/drawio-desktop/releases/tags/v32.6.1) |
| R245 | [draw.io — diagrammes locaux et usage hors ligne](https://www.drawio.com/docs/security/diagrams-offline/) |
| R246 | [draw.io — formats source et export](https://www.drawio.com/docs/manual/export/export-diagram/) |
| R247 | [draw.io — sécurité et confidentialité des diagrammes](https://www.drawio.com/docs/security/) |
| R248 | [GNS3 — version stable et téléchargement](https://www.gns3.com/software/download) |
| R249 | [GNS3 — installation Linux et instructions Debian](https://docs.gns3.com/docs/getting-started/installation/linux) |
| R250 | [GNS3 GUI 2.2.61 — release stable](https://github.com/GNS3/gns3-gui/releases/tag/v2.2.61) |
| R251 | [GNS3 Server — releases](https://github.com/GNS3/gns3-server/releases) |
| R252 | [GNS3 — télécharger la VM et formats d'hyperviseur](https://www.gns3.com/software/download-vm) |
| R253 | [GNS3 — Marketplace des appliances](https://www.gns3.com/marketplace/appliances) |
| R254 | [GNS3 — registre et politique sur les images d'appliances](https://github.com/GNS3/gns3-registry) |
| R255 | [Cisco Networking Academy — téléchargement de Packet Tracer](https://www.netacad.com/resources/lab-downloads) |
| R256 | [Cisco Networking Academy — cours gratuit de démarrage](https://www.netacad.com/courses/getting-started-cisco-packet-tracer) |
| R257 | [Cisco — instructions d'installation Packet Tracer](https://www.netacad.com/skillsforall/files/Cisco_Packet_Tracer_Download_and_Installation_Instructions.pdf) |
| R258 | [Cisco Networking Academy — conditions d'utilisation](https://www.netacad.com/netacad/tnc/netacad-terms-and-conditions-en.pdf) |
| R259 | [KeePassXC — téléchargements Linux et AppImage](https://keepassxc.org/download/) |
| R260 | [KeePassXC — release 2.8.0 et correctifs](https://github.com/keepassxreboot/keepassxc/releases/tag/2.8.0) |
| R261 | [KeePassXC — vérification des signatures et empreinte de la clé](https://keepassxc.org/verifying-signatures/) |
| R262 | [KeePassXC — création de base et paramètres Argon2id](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_creating_your_first_database) |
| R263 | [KeePassXC — sauvegardes de base et écritures sûres](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_database_backup_options) |
| R264 | [KeePassXC — import CSV et avertissement sur le clair](https://keepassxc.org/docs/KeePassXC_UserGuide.html#_importing_csv_file) |
| R265 | [Visual Studio Code — installation Linux, dépôt Debian/Ubuntu et mises à jour](https://code.visualstudio.com/docs/setup/linux) |
| R266 | [Visual Studio Code — version Stable 1.143.1 et notes de mise à jour](https://code.visualstudio.com/updates) |
| R267 | [Visual Studio Code — Workspace Trust et Restricted Mode](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) |
| R268 | [Visual Studio Code — Marketplace, installation et signatures d'extensions](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace) |
| R269 | [Visual Studio Code — sécurité d'exécution et droits des extensions](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security) |
| R270 | [Visual Studio Code — licence du produit Microsoft](https://code.visualstudio.com/License) |
| R271 | [Debian Wiki — Python et intégration des paquets](https://wiki.debian.org/Python) |
| R272 | [Python — module venv et environnement virtuel](https://docs.python.org/3/library/venv.html) |
| R273 | [Python Packaging User Guide — installation pip dans un environnement virtuel](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) |
| R274 | [Python Packaging User Guide — environnements gérés par le système d'exploitation](https://packaging.python.org/en/latest/specifications/externally-managed-environments/) |
| R275 | [pipx — guide d'installation](https://pipx.pypa.io/stable/installation/) |
| R276 | [Git — installer Git sous Linux](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) |
| R277 | [Git — configuration, identité et credentials URL](https://git-scm.com/docs/git-config) |
| R278 | [Git — gestion des credentials](https://git-scm.com/docs/gitcredentials) |
| R279 | [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) |
| R280 | [Git — signatures de commits et de tags](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work) |
| R281 | [Wireshark — téléchargements, versions stables et signatures](https://www.wireshark.org/download.html) |
| R282 | [Wireshark User's Guide — installation de paquets Debian](https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixInstallBins.html#_installing_from_debs_under_debian_ubuntu_and_other_debian_derivatives) |
| R283 | [Wireshark — README Debian pour les privilèges dumpcap](https://gitlab.com/wireshark/wireshark/-/raw/master/packaging/debian/README.Debian) |
| R284 | [Wireshark Wiki — privilèges et groupes de capture](https://wiki.wireshark.org/CaptureSetup/CapturePrivileges) |
| R285 | [Wireshark User's Guide — options et limites de capture](https://www.wireshark.org/docs/wsug_html_chunked/ChCapCaptureOptions.html) |
| R286 | [Wireshark User's Guide — filtres d'affichage](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html) |
| R287 | [Wireshark FAQ — capture, formats et sensibilité des traces](https://www.wireshark.org/faq.html) |
| R288 | [PuTTY — téléchargement officiel Stable 0.85 et signatures MSI](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) |
| R289 | [PuTTY — clés de téléchargement, empreinte Release 2026 et rotation](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html) |
| R290 | [PuTTY — FAQ officielle, empreinte de clé d'hôte et contrôle de confiance](https://www.chiark.greenend.org.uk/~sgtatham/putty/faq.html) |
| R291 | [PuTTY — documentation officielle et manuel](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html) |
| R292 | [PuTTY — licence officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/licence.html) |
| R293 | [Microsoft Learn — installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows) |
| R294 | [PowerShell — publication v7.6.9 et sommes SHA-256 officielles](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9) |
| R295 | [Microsoft Learn — stratégies d'exécution PowerShell](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy) |
| R296 | [Microsoft Learn — compatibilité des modules PowerShell 7](https://learn.microsoft.com/en-us/powershell/whats-new/module-compatibility) |
| R297 | [Microsoft Learn — Get-AuthenticodeSignature](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-authenticodesignature) |
| R298 | [NIST SP 800-41 Rev. 1 — Guidelines on Firewalls and Firewall Policy](https://csrc.nist.gov/pubs/sp/800/41/r1/final) |
| R299 | [NIST SP 800-207 — Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final) |
| R300 | [IETF RFC 1918 — Address Allocation for Private Internets](https://datatracker.ietf.org/doc/html/rfc1918) |
| R301 | [OPNsense — Firewall rules](https://docs.opnsense.org/manual/firewall.html) |
| R302 | [Proxmox VE — Firewall](https://pve.proxmox.com/pve-docs/chapter-pve-firewall.html) |

## Suivi des revues

| Date | Fiche | Version/environnement | Relecteur | Résultat et preuve | Action restante |
|---|---|---|---|---|---|
| À renseigner | À renseigner | À renseigner | À renseigner | Lien vers les résultats de tests et anomalies | À renseigner |

> **Règle de statut :** aucune fiche ne passe à `Validée` sur la seule base de son existence, de son titre/tags ou d'une recherche Web. Conserver `À revoir` et `À tester` tant que les preuves de validation ne sont pas renseignées.