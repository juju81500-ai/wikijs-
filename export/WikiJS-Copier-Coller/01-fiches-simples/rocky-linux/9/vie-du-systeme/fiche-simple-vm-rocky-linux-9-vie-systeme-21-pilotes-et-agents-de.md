# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer l'agent de l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier l'hyperviseur :
   ```bash
   systemd-detect-virt
   ```
   👉 Explication : renvoie `kvm`, `vmware`, `microsoft`...

2. Installer l'agent adapté (KVM/Proxmox ici) :
   ```bash
   sudo dnf install -y qemu-guest-agent
   sudo systemctl enable --now qemu-guest-agent
   ```
   👉 Explication : permet arrêt propre et informations depuis l'hôte; pour VMware : `open-vm-tools`.

3. Contrôler le service :
   ```bash
   systemctl status qemu-guest-agent --no-pager
   ```
   👉 Explication : doit être `active (running)`.

## 2. Production — Contrôles

Activer l'agent côté hyperviseur également.

## 3. Production — Sécurité

N'installer que l'agent nécessaire.

## Validation et retour arrière

- **Validation** : L'hyperviseur voit l'adresse IP de la VM.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Systeme Qemu Guest Agent](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/qemu/fiche-simple-vm-rocky-9-systeme-qemu-guest-agent>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)