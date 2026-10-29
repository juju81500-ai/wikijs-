# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Appliquer tous les correctifs avant mise en service.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Nœud > Updates > Refresh**, puis **Upgrade**. En ligne de commande :
   ```bash
   apt update
   apt full-upgrade
   ```
   👉 Explication : utiliser `full-upgrade` (jamais `upgrade` seul) : Proxmox nécessite de nouveaux paquets lors des mises à jour.

2. Redémarrer si le noyau a changé :
   ```bash
   uname -r
   pveversion
   reboot
   ```
   👉 Explication : compare le noyau actif à celui installé.

3. Contrôler après redémarrage :
   ```bash
   pveversion
   systemctl --failed
   ```
   👉 Explication : aucun service en échec.

## 2. Production — Contrôles

Planifier le redémarrage; migrer les VM d'abord si l'hôte est en cluster.

## 3. Production — Sécurité

Prendre une sauvegarde de `/etc/pve` avant la mise à jour.

## Validation et retour arrière

- **Validation** : `apt update` ne signale plus de mise à jour en attente.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
