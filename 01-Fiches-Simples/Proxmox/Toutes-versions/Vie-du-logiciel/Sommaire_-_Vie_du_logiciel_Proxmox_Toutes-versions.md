# Vie du logiciel : Proxmox Toutes versions

- **Tags** : `vie-du-logiciel`, `sommaire`, `proxmoxtoutesversions`

Logiciels qui s'installent et se gèrent sur Proxmox Toutes versions. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Stockage VM

- [Hote Proxmox VE Diagnostic Cloturer](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Cloturer.md>)
- [Hote Proxmox VE Diagnostic Cluster Reseau](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Cluster_Reseau.md>)
- [Hote Proxmox VE Diagnostic Etat General](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Etat_General.md>)
- [Hote Proxmox VE Diagnostic Restaurer](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Restaurer.md>)
- [Hote Proxmox VE Diagnostic Stabiliser](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Stabiliser.md>)
- [Hote Proxmox VE Diagnostic Stockage](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Stockage.md>)
- [Hote Proxmox VE Diagnostic VM CT](<Cluster-Stockage-VM/Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_VM_CT.md>)

### Proxmox Backup Server

- Fiche d'entrée : [catalogue Proxmox-Backup-Server](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Proxmox-Backup-Server.md>) (statut : Couvert)
- [Hote Proxmox Backup Server Exploitation Incident](<Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Exploitation_Incident.md>)
- [Hote Proxmox Backup Server Installer Datastore](<Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Installer_Datastore.md>)
- [Hote Proxmox Backup Server Preparer Infrastructure](<Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Preparer_Infrastructure.md>)
- [Hote Proxmox Backup Server Relier PVE PBS](<Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Relier_PVE_PBS.md>)
- [Hote Proxmox Backup Server Tester Restauration](<Proxmox-Backup-Server/Fiche_Simple_-_Hote_Proxmox_Backup_Server_Tester_Restauration.md>)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.


### Sauvegarde, restauration et PRA / PCA

- [Bacula](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Bacula.md>) — Couvert
- [Bareos](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Bareos.md>) — Couvert
- [BorgBackup](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_BorgBackup.md>) — Couvert
- [Nakivo-Altaro](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Nakivo-Altaro.md>) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24.04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
- [Restic](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Restic.md>) — Couvert
- [Robocopy](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Robocopy.md>) — Couvert
- [Veeam-Backup-Replication](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Veeam-Backup-Replication.md>) — Couvert
- [rsync](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_rsync.md>) — Couvert

### Virtualisation et conteneurisation

- [Docker-Docker-Compose](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Docker-Docker-Compose.md>) — Couvert
- [Kubernetes-K3s](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Kubernetes-K3s.md>) — Couvert
- [Microsoft-Hyper-V](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Microsoft-Hyper-V.md>) — Couvert
- [Nutanix-AHV](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Nutanix-AHV.md>) — Matériel/éditeur propriétaire — hors périmètre pas à pas
- [Podman-Buildah](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Podman-Buildah.md>) — Couvert
- [Proxmox-VE](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_Proxmox-VE.md>) — Couvert
- [VMware-vSphere](<../../../Logiciels/03-Virtualisation-et-conteneurisation/Fiche_Logiciel_-_VMware-vSphere.md>) — Couvert — vSphere 8 : ESXi, vCenter Server Appliance (installation, sauvegarde/restauration VAMI, mises à jour, certificats), HA/DRS, réseau, datastore NFS, snapshots, maintenance. Hors périmètre : vSAN, NSX, Lifecycle Manager avancé.
