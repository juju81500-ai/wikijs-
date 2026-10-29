# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Créer le stockage, les réseaux et les modèles de VM.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter un stockage (GUI : **Datacenter > Storage > Add**) ou en ligne de commande :
   ```bash
   pvesm status
   pvesm add dir ISO --path /mnt/iso --content iso,vztmpl
   ```
   👉 Explication : affiche les stockages puis ajoute un répertoire pour les ISO et modèles.

2. Télécharger un modèle de conteneur (GUI : **Stockage > CT Templates > Templates**) :
   ```bash
   pveam update
   pveam available --section system | head
   pveam download local debian-12-standard_12.7-1_amd64.tar.zst
   ```
   👉 Explication : `pveam` gère les modèles LXC; le nom exact vient de `pveam available`.

3. Créer une VM de test (GUI : **Create VM**) :
   ```bash
   qm create 9000 --name modele --memory 2048 --cores 2 --net0 virtio,bridge=vmbr0 --scsihw virtio-scsi-single --scsi0 local-lvm:16 --ostype l26
   ```
   👉 Explication : 9000 = numéro réservé aux modèles; à convertir en modèle avec `qm template 9000`.

## 2. Production — Contrôles

Réserver une plage de numéros (VMID) par usage.

## 3. Production — Sécurité

Isoler les VM par VLAN (GUI : **VM > Hardware > Network Device > VLAN Tag**).

## Validation et retour arrière

- **Validation** : Une VM de test démarre (`qm start VMID`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)