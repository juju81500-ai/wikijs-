# Vie du logiciel : Proxmox VE 8

- **Tags** : `vie-du-logiciel`, `sommaire`, `proxmoxve8`

Logiciels qui s'installent et se gèrent sur Proxmox VE 8. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Corosync

- [Hote Proxmox VE 8 Cluster Creer](cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-creer.md)
- [Hote Proxmox VE 8 Cluster Maintenance](cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-maintenance.md)
- [Hote Proxmox VE 8 Cluster Preparer](cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer.md)
- [Hote Proxmox VE 8 Cluster Securiser](cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-securiser.md)
- [Hote Proxmox VE 8 Cluster Valider](cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-valider.md)

### Proxmox OpenStack

- Fiche d'entrée : [catalogue Proxmox-OpenStack](../../../logiciels/10-cloud-public-et-hybride/fiche-logiciel-proxmox-openstack.md) (statut : Partiel)
- [VM Proxmox VE 8 Proxmox OpenStack Choix Architecture](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-choix-architecture.md)
- [VM Proxmox VE 8 Proxmox OpenStack Explorer APIs](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-explorer-apis.md)
- [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-mise-a-jour-retour-arriere.md)
- [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-nettoyer-retour-arriere.md)
- [VM Proxmox VE 8 Proxmox OpenStack Preparer Lab](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-preparer-lab.md)
- [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-sauvegarder-restaurer-lab.md)
- [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](proxmox-openstack/fiche-simple-vm-proxmox-ve-8-proxmox-openstack-securiser-valider-lab.md)

### Zabbix

- Fiche d'entrée : [catalogue Zabbix](../../../logiciels/02-supervision-metrologie-logs-et-observabilite/fiche-logiciel-zabbix.md) (statut : Couvert)
- [Proxmox VE 8 Supervision Zabbix Snmp](zabbix/fiche-simple-proxmox-ve-8-supervision-zabbix-snmp.md)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.


### Sauvegarde, restauration et PRA / PCA

- [Bacula](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bacula.md) — Couvert
- [Bareos](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bareos.md) — Couvert
- [BorgBackup](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-borgbackup.md) — Couvert
- [Nakivo-Altaro](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro.md) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24-04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
- [Proxmox-Backup-Server](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-proxmox-backup-server.md) — Couvert
- [Restic](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-restic.md) — Couvert
- [Robocopy](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-robocopy.md) — Couvert
- [Veeam-Backup-Replication](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-veeam-backup-replication.md) — Couvert
- [rsync](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-rsync.md) — Couvert

### Virtualisation et conteneurisation

- [Docker-Docker-Compose](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-docker-docker-compose.md) — Couvert
- [Kubernetes-K3s](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-kubernetes-k3s.md) — Couvert
- [Microsoft-Hyper-V](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-microsoft-hyper-v.md) — Couvert
- [Nutanix-AHV](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-nutanix-ahv.md) — Matériel/éditeur propriétaire — hors périmètre pas à pas
- [Podman-Buildah](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-podman-buildah.md) — Couvert
- [Proxmox-VE](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-proxmox-ve.md) — Couvert
- [VMware-vSphere](../../../logiciels/03-virtualisation-et-conteneurisation/fiche-logiciel-vmware-vsphere.md) — Couvert — vSphere 8 : ESXi, vCenter Server Appliance (installation, sauvegarde/restauration VAMI, mises à jour, certificats), HA/DRS, réseau, datastore NFS, snapshots, maintenance. Hors périmètre : vSAN, NSX, Lifecycle Manager avancé.
