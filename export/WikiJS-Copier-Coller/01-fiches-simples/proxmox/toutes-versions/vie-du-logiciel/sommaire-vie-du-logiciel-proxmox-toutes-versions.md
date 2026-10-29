# Vie du logiciel : Proxmox Toutes versions

Logiciels qui s'installent et se gèrent sur Proxmox Toutes versions. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Stockage VM

- [Hote Proxmox VE Diagnostic Cloturer](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-cloturer>)
- [Hote Proxmox VE Diagnostic Cluster Reseau](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-cluster-reseau>)
- [Hote Proxmox VE Diagnostic Etat General](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-etat-general>)
- [Hote Proxmox VE Diagnostic Restaurer](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-restaurer>)
- [Hote Proxmox VE Diagnostic Stabiliser](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-stabiliser>)
- [Hote Proxmox VE Diagnostic Stockage](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-stockage>)
- [Hote Proxmox VE Diagnostic VM CT](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-vm-ct>)

### Proxmox Backup Server

- Fiche d'entrée : [catalogue Proxmox-Backup-Server](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-proxmox-backup-server>) (statut : Couvert)
- [Hote Proxmox Backup Server Exploitation Incident](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-exploitation-incident>)
- [Hote Proxmox Backup Server Installer Datastore](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-installer-datastore>)
- [Hote Proxmox Backup Server Preparer Infrastructure](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-preparer-infrastructure>)
- [Hote Proxmox Backup Server Relier PVE PBS](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-relier-pve-pbs>)
- [Hote Proxmox Backup Server Tester Restauration](</01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-tester-restauration>)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.

### Sauvegarde, restauration et PRA / PCA

- [Bacula](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bacula>) — Couvert
- [Bareos](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bareos>) — Couvert
- [BorgBackup](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-borgbackup>) — Couvert
- [Nakivo-Altaro](</01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro>) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24.04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
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