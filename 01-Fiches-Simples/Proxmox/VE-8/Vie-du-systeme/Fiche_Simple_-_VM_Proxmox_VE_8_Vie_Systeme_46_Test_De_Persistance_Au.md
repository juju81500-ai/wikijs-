# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-46`

---

## Problème précis à résoudre

Vérifier que la configuration survit à un redémarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Migrer ou arrêter proprement les VM, puis redémarrer :
   ```bash
   qm list
   reboot
   ```
   👉 Explication : en cluster, migrer d'abord (GUI : **VM > Migrate**).

2. Après redémarrage, vérifier :
   ```bash
   uptime
   ip -br a
   systemctl --failed
   pvecm status
   qm list
   ```
   👉 Explication : IP, services, quorum et VM configurées en démarrage automatique.

3. Contrôler le démarrage automatique des VM (GUI : **VM > Options > Start at boot**) :
   ```bash
   qm config VMID | grep onboot
   qm set VMID --onboot 1
   ```
   👉 Explication : `VMID` = numéro de la VM; `onboot: 1` démarre la VM au boot.

## 2. Production — Contrôles

Redémarrer en fenêtre de maintenance.

## 3. Production — Sécurité

Garder l'accès console pour dépanner.

## Validation et retour arrière

- **Validation** : Tout est revenu comme avant le redémarrage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
