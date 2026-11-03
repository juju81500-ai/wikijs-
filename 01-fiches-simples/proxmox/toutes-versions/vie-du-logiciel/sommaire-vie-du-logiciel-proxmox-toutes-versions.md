# Vie du logiciel : Proxmox Toutes versions

- **Tags** : `vie-du-logiciel`, `sommaire`, `proxmoxtoutesversions`

Logiciels qui s'installent et se gèrent sur Proxmox Toutes versions. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Stockage VM

- [Hote Proxmox VE Diagnostic Cloturer](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-cloturer.md)
- [Hote Proxmox VE Diagnostic Cluster Reseau](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-cluster-reseau.md)
- [Hote Proxmox VE Diagnostic Etat General](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-etat-general.md)
- [Hote Proxmox VE Diagnostic Restaurer](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-restaurer.md)
- [Hote Proxmox VE Diagnostic Stabiliser](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-stabiliser.md)
- [Hote Proxmox VE Diagnostic Stockage](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-stockage.md)
- [Hote Proxmox VE Diagnostic VM CT](cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-vm-ct.md)

### Proxmox Backup Server

- Fiche d'entrée : [catalogue Proxmox-Backup-Server](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-proxmox-backup-server.md) (statut : Couvert)
- [Hote Proxmox Backup Server Exploitation Incident](proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-exploitation-incident.md)
- [Hote Proxmox Backup Server Installer Datastore](proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-installer-datastore.md)
- [Hote Proxmox Backup Server Preparer Infrastructure](proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-preparer-infrastructure.md)
- [Hote Proxmox Backup Server Relier PVE PBS](proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-relier-pve-pbs.md)
- [Hote Proxmox Backup Server Tester Restauration](proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-tester-restauration.md)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.


### Sauvegarde, restauration et PRA / PCA

- [Bacula](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bacula.md) — Couvert
- [Bareos](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-bareos.md) — Couvert
- [BorgBackup](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-borgbackup.md) — Couvert
- [Nakivo-Altaro](../../../logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro.md) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24-04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
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
