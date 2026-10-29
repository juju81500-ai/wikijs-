# Vie du logiciel : VMware ESXi 8

Logiciels qui s'installent et se gèrent sur VMware ESXi 8. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### vSphere

- [VM ESXi 8 VMware vSphere Certificats](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-certificats>)
- [VM ESXi 8 VMware vSphere DRS](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-drs>)
- [VM ESXi 8 VMware vSphere Datastore NFS](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-datastore-nfs>)
- [VM ESXi 8 VMware vSphere HA](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-ha>)
- [VM ESXi 8 VMware vSphere Maintenance Hote](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-maintenance-hote>)
- [VM ESXi 8 VMware vSphere Snapshots](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-snapshots>)
- [VM ESXi 8 VMware vSphere VCSA Installer](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-installer>)
- [VM ESXi 8 VMware vSphere VCSA Mises A Jour](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-mises-a-jour>)
- [VM ESXi 8 VMware vSphere VCSA Sauvegarde Restauration VAMI](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vcsa-sauvegarde-restauration-vami>)
- [VM ESXi 8 VMware vSphere vMotion VMkernel](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vmotion-vmkernel>)
- [VM ESXi 8 VMware vSphere vSwitch Standard](</01-fiches-simples/vmware/esxi-8/vie-du-logiciel/vsphere/fiche-simple-vm-esxi-8-vmware-vsphere-vswitch-standard>)

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