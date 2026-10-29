# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Rendre l'ISO démarrable sur serveur physique ou VM.

## 1. Hors-Production (Lab / Test / POC)

1. Clé USB : repérer la clé, puis écrire l'image (remplacer `sdX` par la clé et `26.04.X` par la version de l'ISO; **efface tout**) :
   ```bash
   lsblk -o NAME,SIZE,MODEL,TRAN
   sudo dd if=~/iso/ubuntu-26.04.X-live-server-amd64.iso of=/dev/sdX bs=4M status=progress conv=fsync
   ```
   👉 Explication : `lsblk` évite de cibler le mauvais disque; `dd` copie l'image.

2. VM : monter l'ISO (Proxmox : **VM > Hardware > CD/DVD Drive > Use CD/DVD disc image file**), ou en ligne de commande (remplacer `VMID` et le stockage) :
   ```bash
   qm set VMID --ide2 local:iso/ubuntu-26.04.X-live-server-amd64.iso,media=cdrom
   qm set VMID --boot order='ide2;scsi0'
   ```
   👉 Explication : attache l'ISO et place le CD en premier dans l'ordre d'amorçage.

## 2. Production — Contrôles

Pour un serveur physique, utiliser la console distante (iDRAC, iLO, IPMI) pour monter l'image.

## 3. Production — Sécurité

Retirer l'ISO et la clé après l'installation.

## Validation et retour arrière

- **Validation** : La machine démarre sur le programme d'installation d'Ubuntu Server (Subiquity).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)