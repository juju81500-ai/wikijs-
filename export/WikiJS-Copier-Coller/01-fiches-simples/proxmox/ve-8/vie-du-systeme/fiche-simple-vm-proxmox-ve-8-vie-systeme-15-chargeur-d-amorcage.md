# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Contrôler le démarrage de l'hôte (GRUB ou systemd-boot).

## 1. Hors-Production (Lab / Test / POC)

1. Identifier le mode de démarrage et l'outil de gestion :
   ```bash
   proxmox-boot-tool status
   ls /sys/firmware/efi && echo UEFI || echo BIOS
   ```
   👉 Explication : sous ZFS avec UEFI, Proxmox utilise `proxmox-boot-tool` pour synchroniser les partitions ESP.

2. Régénérer la configuration après un changement de noyau ou de paramètre :
   ```bash
   update-grub
   proxmox-boot-tool refresh
   ```
   👉 Explication : met à jour GRUB et copie le noyau sur toutes les ESP.

3. Pour activer l'IOMMU (passthrough), ajouter `intel_iommu=on` (ou `amd_iommu=on`) à `GRUB_CMDLINE_LINUX_DEFAULT` dans `/etc/default/grub` puis relancer `update-grub`.
   👉 Explication : paramètre noyau nécessaire seulement si le passthrough PCI est utilisé.

## 2. Production — Contrôles

Tester un redémarrage après chaque changement du chargeur.

## 3. Production — Sécurité

Protéger l'accès à la console de gestion (accès au menu GRUB).

## Validation et retour arrière

- **Validation** : Redémarrage correct sur le noyau attendu (`uname -r`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)