# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Préparer le BIOS/UEFI et le matériel pour la virtualisation.

## 1. Hors-Production (Lab / Test / POC)

1. Au démarrage, entrer dans le Setup (F2 ou F11 selon le constructeur) et activer : Virtualisation (Intel VT-x / AMD-V), VT-d / AMD-Vi (IOMMU), mode UEFI, Secure Boot selon la politique.
   👉 Explication : VT-x/AMD-V est indispensable pour KVM; l'IOMMU sert au passthrough PCI.

2. Configurer le RAID matériel ou passer le contrôleur en mode HBA/IT si ZFS ou Ceph est prévu (iDRAC : **Configuration > Configuration du stockage**).
   👉 Explication : ZFS doit voir les disques bruts, sans RAID matériel entre les deux.

3. Après installation, contrôler la virtualisation et l'IOMMU :
   ```bash
   lscpu | grep -i virtualization
   egrep -c '(vmx|svm)' /proc/cpuinfo
   dmesg | grep -i -e DMAR -e IOMMU | head
   ```
   👉 Explication : un compteur supérieur à 0 confirme la virtualisation; les lignes DMAR/IOMMU confirment VT-d.

4. Mettre à jour firmware BIOS, iDRAC et cartes réseau/RAID avant la mise en production.
   👉 Explication : corrige des défauts connus; à faire avant d'héberger des VM.

## 2. Production — Contrôles

Documenter la version du firmware et les réglages BIOS retenus.

## 3. Production — Sécurité

Protéger le Setup par mot de passe; changer le mot de passe par défaut de l'iDRAC.

## Validation et retour arrière

- **Validation** : `vmx` ou `svm` présent dans `/proc/cpuinfo`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)