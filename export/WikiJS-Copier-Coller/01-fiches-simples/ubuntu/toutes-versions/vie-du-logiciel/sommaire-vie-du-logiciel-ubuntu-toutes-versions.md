# Vie du logiciel : Ubuntu Toutes versions

Logiciels qui s'installent et se gèrent sur Ubuntu Toutes versions. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Ceph

- Fiche d'entrée : [catalogue Ceph](</01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-ceph>) (statut : Couvert)
- [VM Ubuntu Ceph Ajouter Noeuds Monitors](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-ajouter-noeuds-monitors>)
- [VM Ubuntu Ceph Ajouter OSD](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-ajouter-osd>)
- [VM Ubuntu Ceph Cadrer Perimetre](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-cadrer-perimetre>)
- [VM Ubuntu Ceph Controler Exploiter](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-controler-exploiter>)
- [VM Ubuntu Ceph Installer Cephadm Bootstrap](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-installer-cephadm-bootstrap>)
- [VM Ubuntu Ceph Limites Validation](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-limites-validation>)
- [VM Ubuntu Ceph Pool RBD Pilote](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-pool-rbd-pilote>)
- [VM Ubuntu Ceph Preparer Noeuds](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-preparer-noeuds>)
- [VM Ubuntu Ceph Sauvegarde Upgrade Retrait](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-sauvegarde-upgrade-retrait>)
- [VM Ubuntu Ceph Verifier Sante Cluster](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/ceph/fiche-simple-vm-ubuntu-ceph-verifier-sante-cluster>)

### Restic

- Fiche d'entrée : [catalogue Restic](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-restic>) (statut : Couvert)
- [VM Ubuntu Restic Definir Donnees Depot](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-definir-donnees-depot>)
- [VM Ubuntu Restic Effectuer Sauvegarde](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-effectuer-sauvegarde>)
- [VM Ubuntu Restic Exercices Exploitation](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-exercices-exploitation>)
- [VM Ubuntu Restic Initialiser Depot](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-initialiser-depot>)
- [VM Ubuntu Restic Installer Proteger Secret](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-installer-proteger-secret>)
- [VM Ubuntu Restic Restaurer Sans Ecraser](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-restaurer-sans-ecraser>)
- [VM Ubuntu Restic Retention Integrite](</01-fiches-simples/ubuntu/toutes-versions/vie-du-logiciel/restic/fiche-simple-vm-ubuntu-restic-retention-integrite>)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.

### Automatisation, déploiement et IaC

- [Ansible](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-ansible>) — Couvert
- [FOG-Project](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-fog-project>) — Couvert — Debian 13 (7 fiches); support officiel de Debian 13 à confirmer auprès du projet FOG avant déploiement.
- [Git](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-git>) — Couvert
- [GitHub](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-github>) — Couvert
- [GitLab](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-gitlab>) — Couvert
- [Gitea](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-gitea>) — Couvert
- [Packer](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-packer>) — Guide pilote — Packer sur Debian 13 avec plugin Docker local
- [Terraform-OpenTofu](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-terraform-opentofu>) — Couvert
- [WDS-MDT](</01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt>) — Couvert — Windows Server 2022 (7 fiches). Windows Server 2025 non couvert : limite WDS documentée par Microsoft (voir Couverture).

### Cloud public et hybride

- [Proxmox-OpenStack](</01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-proxmox-openstack>) — Partiel

### Gestion de parc, ticketing et inventaire

- [GLPI](</01-fiches-simples/logiciels/01-gestion-de-parc-ticketing-et-inventaire/fiche-logiciel-glpi>) — Couvert
- [OCS-Inventory](</01-fiches-simples/logiciels/01-gestion-de-parc-ticketing-et-inventaire/fiche-logiciel-ocs-inventory>) — Couvert
- [OTRS](</01-fiches-simples/logiciels/01-gestion-de-parc-ticketing-et-inventaire/fiche-logiciel-otrs>) — Couvert
- [Snipe-IT](</01-fiches-simples/logiciels/01-gestion-de-parc-ticketing-et-inventaire/fiche-logiciel-snipe-it>) — Couvert
- [Znuny](</01-fiches-simples/logiciels/01-gestion-de-parc-ticketing-et-inventaire/fiche-logiciel-znuny>) — Couvert
- [iTop](</01-fiches-simples/logiciels/01-gestion-de-parc-ticketing-et-inventaire/fiche-logiciel-itop>) — Couvert

### Gestion des secrets et mots de passe

- [Bitwarden](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-bitwarden>) — Couvert
- [HashiCorp-Vault](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-hashicorp-vault>) — Couvert
- [KeePass-KeePassXC](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-keepass-keepassxc>) — Couvert
- [Passbolt](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-passbolt>) — Couvert
- [Vaultwarden](</01-fiches-simples/logiciels/08-gestion-des-secrets-et-mots-de-passe/fiche-logiciel-vaultwarden>) — Couvert

### Messagerie et collaboratif

- [BleuKango](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-bleukango>) — Manquant
- [BlueMind](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-bluemind>) — Couvert
- [Dovecot](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-dovecot>) — Couvert
- [Nextcloud](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-nextcloud>) — Couvert
- [Postfix](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-postfix>) — Couvert
- [Zimbra](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-zimbra>) — Manquant
- [ownCloud](</01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-owncloud>) — Couvert

### Poste de travail et VDI

- [Apache-Guacamole](</01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-apache-guacamole>) — Guide complet — Guacamole 1.6.0 avec Docker Compose, PostgreSQL et reverse proxy HTTPS
- [Citrix-Virtual-Apps-and-Desktops](</01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops>) — Couvert

### Réseau et cybersécurité

- [Authelia](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-authelia>) — Documentation défensive — administration et gouvernance
- [Authentik](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-authentik>) — Documentation défensive — administration et gouvernance
- [Bitdefender-GravityZone](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-bitdefender-gravityzone>) — Documentation défensive — administration et gouvernance
- [BloodHound](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-bloodhound>) — Documentation défensive — administration et gouvernance
- [Cisco-AnyConnect](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-cisco-anyconnect>) — Documentation défensive — administration et gouvernance
- [DMZ](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-dmz>) — Couvert
- [FortiClient](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-forticlient>) — Documentation défensive — administration et gouvernance
- [FreeRADIUS](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-freeradius>) — Documentation défensive — administration et gouvernance
- [GlobalProtect](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-globalprotect>) — Documentation défensive — administration et gouvernance
- [Kaspersky-Endpoint-Security](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-kaspersky-endpoint-security>) — Documentation défensive — administration et gouvernance
- [Keycloak](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-keycloak>) — Documentation défensive — administration et gouvernance
- [Nessus](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-nessus>) — Documentation défensive — administration et gouvernance
- [Nmap](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-nmap>) — Défensif uniquement
- [OpenVAS](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvas>) — Documentation défensive — administration et gouvernance
- [OpenVPN](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-openvpn>) — Couvert
- [PingCastle](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-pingcastle>) — Documentation défensive — administration et gouvernance
- [Snort](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-snort>) — Couvert
- [Suricata](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-suricata>) — Couvert
- [Wazuh](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wazuh>) — Couvert
- [WireGuard](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireguard>) — Couvert
- [Wireshark](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-wireshark>) — Couvert
- [Zeek](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zeek>) — Couvert
- [Zenmap](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-zenmap>) — Défensif uniquement
- [segmentation-des-zones](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-segmentation-des-zones>) — Couvert
- [tcpdump](</01-fiches-simples/logiciels/04-reseau-et-cybersecurite/fiche-logiciel-tcpdump>) — Couvert

### Sauvegarde, restauration et PRA / PCA

- [Bacula](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bacula>) — Couvert
- [Bareos](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bareos>) — Couvert
- [BorgBackup](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-borgbackup>) — Couvert
- [Nakivo-Altaro](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro>) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24.04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
- [Proxmox-Backup-Server](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-proxmox-backup-server>) — Couvert
- [Robocopy](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-robocopy>) — Couvert
- [rsync](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-rsync>) — Couvert

### Scripting, développement et administration

- [Bash-Shell](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-bash-shell>) — Couvert
- [Postman](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman>) — Couvert
- [PowerShell](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-powershell>) — Couvert
- [Python](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-python>) — Couvert
- [Visual-Studio-Code](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-visual-studio-code>) — Couvert
- [cURL](</01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-curl>) — Couvert

### Services Web et bases de données

- [Apache](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-apache>) — Couvert
- [Caddy](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-caddy>) — Couvert
- [HAProxy](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-haproxy>) — Couvert
- [IIS](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-iis>) — Guide complet — installation du rôle IIS et site pilote Windows Server 2022
- [InfluxDB](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-influxdb>) — Couvert
- [MariaDB](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-mariadb>) — Couvert
- [MongoDB](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-mongodb>) — Couvert
- [MySQL](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-mysql>) — Couvert
- [Nginx](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-nginx>) — Couvert
- [PostgreSQL](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-postgresql>) — Couvert
- [Redis](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-redis>) — Couvert
- [SQL-Server](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-sql-server>) — Couvert
- [Traefik](</01-fiches-simples/logiciels/14-services-web-et-bases-de-donnees/fiche-logiciel-traefik>) — Couvert

### Stockage et SAN / NAS

- [OpenMediaVault](</01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-openmediavault>) — Couvert
- [StarWind-Virtual-SAN](</01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-starwind-virtual-san>) — Partiel
- [TrueNAS-SCALE](</01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-truenas-scale>) — Couvert

### Supervision, métrologie, logs et observabilité

- [Cacti](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-cacti>) — Couvert
- [Centreon](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-centreon>) — Couvert
- [Cloud](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-cloud>) — Partiel
- [ELK-Stack](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-elk-stack>) — Couvert
- [Graylog](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-graylog>) — Couvert
- [LibreNMS](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-librenms>) — Couvert
- [Observium](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-observium>) — Couvert
- [Prometheus-Grafana](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-prometheus-grafana>) — Couvert
- [Splunk-Enterprise](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-splunk-enterprise>) — Partiel
- [Zabbix](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-zabbix>) — Couvert

### Systèmes, annuaires et services

- [AlmaLinux](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-almalinux>) — Partiel
- [BIND-9](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-bind-9>) — Couvert
- [Debian-Ubuntu-Server](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-debian-ubuntu-server>) — Couvert
- [FreeIPA](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-freeipa>) — Couvert
- [ISC-DHCP-Server](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-isc-dhcp-server>) — Couvert
- [Kea-DHCPv4](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-kea-dhcpv4>) — Couvert
- [OpenLDAP](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-openldap>) — Couvert
- [RHEL](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-rhel>) — Partiel
- [Rocky-Linux](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-rocky-linux>) — Couvert
- [Samba-Samba4](</01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-samba-samba4>) — Couvert

### Topologie, IPAM et outils métiers

- [GNS3](</01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-gns3>) — Couvert
- [NetBox](</01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-netbox>) — Couvert
- [QGIS](</01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-qgis>) — Couvert
- [draw-io-Desktop](</01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-draw-io-desktop>) — Couvert
- [phpIPAM](</01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-phpipam>) — Couvert

### Virtualisation et conteneurisation

- [Docker-Docker-Compose](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-docker-docker-compose>) — Couvert
- [Kubernetes-K3s](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-kubernetes-k3s>) — Couvert
- [Podman-Buildah](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-podman-buildah>) — Couvert