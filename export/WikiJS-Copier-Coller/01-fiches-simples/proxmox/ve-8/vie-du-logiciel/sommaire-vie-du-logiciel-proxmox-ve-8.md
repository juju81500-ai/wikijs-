# Vie du logiciel : Proxmox VE 8

Logiciels qui s'installent et se gèrent sur Proxmox VE 8. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Corosync

- [Hote Proxmox VE 8 Cluster Creer](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-creer>)
- [Hote Proxmox VE 8 Cluster Maintenance](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-maintenance>)
- [Hote Proxmox VE 8 Cluster Preparer](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer>)
- [Hote Proxmox VE 8 Cluster Securiser](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser>)
- [Hote Proxmox VE 8 Cluster Valider](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-valider>)

### Proxmox OpenStack

- Fiche d'entrée : [catalogue Proxmox-OpenStack](</01-fiches-simples/logiciels/10-cloud-public-et-hybride/fiche-logiciel-proxmox-openstack>) (statut : Partiel)
- [VM Proxmox VE 8 Proxmox OpenStack Choix Architecture](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-choix-architecture>)
- [VM Proxmox VE 8 Proxmox OpenStack Explorer APIs](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-explorer-apis>)
- [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-mise-a-jour-retour-arriere>)
- [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-nettoyer-retour-arriere>)
- [VM Proxmox VE 8 Proxmox OpenStack Preparer Lab](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-preparer-lab>)
- [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-sauvegarder-restaurer-lab>)
- [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-securiser-valider-lab>)

### Zabbix

- Fiche d'entrée : [catalogue Zabbix](</01-fiches-simples/logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-zabbix>) (statut : Couvert)
- [Proxmox VE 8 Supervision Zabbix Snmp](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/zabbix/fiche-simple-proxmox-ve-8-supervision-zabbix-snmp>)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.

### Sauvegarde, restauration et PRA / PCA

- [Bacula](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bacula>) — Couvert
- [Bareos](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bareos>) — Couvert
- [BorgBackup](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-borgbackup>) — Couvert
- [Nakivo-Altaro](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro>) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24.04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
- [Proxmox-Backup-Server](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-proxmox-backup-server>) — Couvert
- [Restic](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-restic>) — Couvert
- [Robocopy](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-robocopy>) — Couvert
- [Veeam-Backup-Replication](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-veeam-backup-replication>) — Couvert
- [rsync](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-rsync>) — Couvert

### Virtualisation et conteneurisation

- [Docker-Docker-Compose](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-docker-docker-compose>) — Couvert
- [Kubernetes-K3s](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-kubernetes-k3s>) — Couvert
- [Microsoft-Hyper-V](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-microsoft-hyper-v>) — Couvert
- [Nutanix-AHV](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-nutanix-ahv>) — Matériel/éditeur propriétaire — hors périmètre pas à pas
- [Podman-Buildah](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-podman-buildah>) — Couvert
- [Proxmox-VE](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-proxmox-ve>) — Couvert
- [VMware-vSphere](</01-fiches-simples/logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere>) — Couvert — vSphere 8 : ESXi, vCenter Server Appliance (installation, sauvegarde/restauration VAMI, mises à jour, certificats), HA/DRS, réseau, datastore NFS, snapshots, maintenance. Hors périmètre : vSAN, NSX, Lifecycle Manager avancé.