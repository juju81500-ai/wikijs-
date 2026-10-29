# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_04_Preparation_Du_Support_D

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 04 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-04`

---

## Problème précis à résoudre

Rendre l'ISO démarrable sur serveur physique ou VM.

## 1. Hors-Production (Lab / Test / POC)

1. Clé USB : repérer la clé, puis écrire l'image (remplacer `sdX` par la clé; **efface tout**) :
   ```bash
   lsblk -o NAME,SIZE,MODEL,TRAN
   sudo dd if=~/iso/debian-13.X.Y-amd64-netinst.iso of=/dev/sdX bs=4M status=progress conv=fsync
   ```
   👉 Explication : `lsblk` évite de cibler le mauvais disque; `dd` copie l'image.

2. VM : monter l'ISO (Proxmox : **VM > Hardware > CD/DVD Drive > Use CD/DVD disc image file**), ou en ligne de commande (remplacer `VMID` et le stockage) :
   ```bash
   qm set VMID --ide2 local:iso/debian-13.X.Y-amd64-netinst.iso,media=cdrom
   qm set VMID --boot order='ide2;scsi0'
   ```
   👉 Explication : attache l'ISO et place le CD en premier dans l'ordre d'amorçage.

## 2. Production — Contrôles

Pour un serveur physique, utiliser la console distante (iDRAC, iLO, IPMI) pour monter l'image.

## 3. Production — Sécurité

Retirer l'ISO et la clé après l'installation.

## Validation et retour arrière

- **Validation** : La machine démarre sur le menu d'installation Debian.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Debian 13](./Sommaire_-_Vie_du_systeme_Debian_13.md)
- [Documentation officielle](https://www.debian.org/doc/)
