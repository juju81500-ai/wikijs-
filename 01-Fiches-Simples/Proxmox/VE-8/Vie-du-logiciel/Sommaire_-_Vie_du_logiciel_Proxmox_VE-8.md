# Vie du logiciel : Proxmox VE 8

- **Tags** : `vie-du-logiciel`, `sommaire`, `proxmoxve8`

Logiciels qui s'installent et se gèrent sur Proxmox VE 8. Pour chaque logiciel : fiche d'entrée du catalogue, puis les fiches simples (installation, configuration, sécurité, sauvegarde, mise à jour). Le système lui-même se trouve dans le dossier `Vie-du-systeme`.

## Logiciels avec fiches dans ce dossier

### Cluster Corosync

- [Hote Proxmox VE 8 Cluster Creer](<Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Creer.md>)
- [Hote Proxmox VE 8 Cluster Maintenance](<Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Maintenance.md>)
- [Hote Proxmox VE 8 Cluster Preparer](<Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Preparer.md>)
- [Hote Proxmox VE 8 Cluster Securiser](<Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Securiser.md>)
- [Hote Proxmox VE 8 Cluster Valider](<Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Valider.md>)

### Proxmox OpenStack

- Fiche d'entrée : [catalogue Proxmox-OpenStack](<../../../Logiciels/10-Cloud-public-et-hybride/Fiche_Logiciel_-_Proxmox-OpenStack.md>) (statut : Partiel)
- [VM Proxmox VE 8 Proxmox OpenStack Choix Architecture](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Choix_Architecture.md>)
- [VM Proxmox VE 8 Proxmox OpenStack Explorer APIs](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Explorer_APIs.md>)
- [VM Proxmox VE 8 Proxmox OpenStack Mise A Jour Retour Arriere](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Mise_A_Jour_Retour_Arriere.md>)
- [VM Proxmox VE 8 Proxmox OpenStack Nettoyer Retour Arriere](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Nettoyer_Retour_Arriere.md>)
- [VM Proxmox VE 8 Proxmox OpenStack Preparer Lab](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Preparer_Lab.md>)
- [VM Proxmox VE 8 Proxmox OpenStack Sauvegarder Restaurer Lab](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Sauvegarder_Restaurer_Lab.md>)
- [VM Proxmox VE 8 Proxmox OpenStack Securiser Valider Lab](<Proxmox-OpenStack/Fiche_Simple_-_VM_Proxmox_VE_8_Proxmox_OpenStack_Securiser_Valider_Lab.md>)

### Zabbix

- Fiche d'entrée : [catalogue Zabbix](<../../../Logiciels/02-Supervision-metrologie-logs-et-observabilite/Fiche_Logiciel_-_Zabbix.md>) (statut : Couvert)
- [Proxmox VE 8 Supervision Zabbix Snmp](<Zabbix/Fiche_Simple_-_Proxmox_VE_8_Supervision_Zabbix_Snmp.md>)

## Autres logiciels du catalogue compatibles avec cet OS

Cliquer sur le nom pour voir l'état de couverture ; une procédure détaillée peut exister sur une autre version ou en guide complet.


### Sauvegarde, restauration et PRA / PCA

- [Bacula](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Bacula.md>) — Couvert
- [Bareos](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Bareos.md>) — Couvert
- [BorgBackup](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_BorgBackup.md>) — Couvert
- [Nakivo-Altaro](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Nakivo-Altaro.md>) — Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24.04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
- [Proxmox-Backup-Server](<../../../Logiciels/07-Sauvegarde-restauration-et-PRA-PCA/Fiche_Logiciel_-_Proxmox-Backup-Server.md>) — Couvert
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
