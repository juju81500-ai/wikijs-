# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer l'agent adapté à l'hyperviseur.

## 1. Hors-Production (Lab / Test / POC)

1. Proxmox/QEMU :
   ```bash
   sudo apt install qemu-guest-agent
   sudo systemctl enable --now qemu-guest-agent
   ```
   👉 Explication : permet à l'hyperviseur de lire l'IP et d'arrêter proprement la VM (activer **Options > QEMU Guest Agent** côté Proxmox).

2. VMware ou Hyper-V (selon la plateforme) :
   ```bash
   sudo apt install open-vm-tools
   # ou : sudo apt install hyperv-daemons
   ```
   👉 Explication : agents équivalents pour ESXi et Hyper-V.

## 2. Production — Contrôles

Un seul agent, celui de l'hyperviseur réel.

## 3. Production — Sécurité

Mettre à jour l'agent avec le système.

## Validation et retour arrière

- **Validation** : `systemctl status qemu-guest-agent` actif.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Debian 12 Systeme Installation Qemu Guest Age](</01-fiches-simples/debian/12/vie-du-logiciel/qemu/fiche-simple-vm-debian-12-systeme-installation-qemu-guest-age>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)