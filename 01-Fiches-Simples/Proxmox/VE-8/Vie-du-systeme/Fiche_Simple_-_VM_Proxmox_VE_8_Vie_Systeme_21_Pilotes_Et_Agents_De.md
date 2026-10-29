# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer les agents pour les invités et vérifier les pilotes de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Sur chaque VM, installer l'agent QEMU (Debian/Ubuntu : `apt install qemu-guest-agent`; Windows : pilotes VirtIO). Côté hôte, l'activer (GUI : **VM > Options > QEMU Guest Agent > Edit > Enabled**) :
   ```bash
   qm set VMID --agent enabled=1
   qm agent VMID ping
   ```
   👉 Explication : `VMID` = numéro de la VM; `ping` vérifie que l'agent répond.

2. Utiliser les pilotes VirtIO pour disque et réseau (GUI : **VM > Hardware > Add > Network Device > Model: VirtIO**).
   👉 Explication : meilleures performances que les pilotes émulés.

3. Contrôler le microcode CPU et les pilotes réseau de l'hôte :
   ```bash
   apt install -y intel-microcode
   lspci -k | grep -A2 -i ethernet
   ```
   👉 Explication : installer `amd64-microcode` pour AMD; `lspci -k` indique le pilote chargé.

## 2. Production — Contrôles

Installer l'agent dans le modèle de VM (template).

## 3. Production — Sécurité

Garder l'agent à jour.

## Validation et retour arrière

- **Validation** : `qm agent VMID ping` répond sans erreur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
