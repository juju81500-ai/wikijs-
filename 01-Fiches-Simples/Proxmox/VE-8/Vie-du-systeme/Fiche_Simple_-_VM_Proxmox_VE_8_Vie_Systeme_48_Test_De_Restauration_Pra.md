# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver qu'une sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Stockage PBS > Content > sélectionner la sauvegarde > Restore** (nouvel VMID). En ligne de commande :
   ```bash
   qmrestore PBS:backup/vm/100/DATE 9100 --storage local-lvm
   ```
   👉 Explication : restaure sous un nouveau numéro (`9100`) pour ne pas écraser la VM d'origine; `DATE` = horodatage de la sauvegarde.

2. Démarrer la VM restaurée sans réseau de production (GUI : retirer la carte réseau) et contrôler son contenu :
   ```bash
   qm start 9100
   qm status 9100
   ```
   👉 Explication : évite un conflit d'adresse IP avec la VM d'origine.

3. Mesurer la durée et noter le résultat; supprimer la VM de test :
   ```bash
   qm destroy 9100
   ```
   👉 Explication : la durée donne le RTO réel.

## 2. Production — Contrôles

Test de restauration au moins trimestriel.

## 3. Production — Sécurité

Supprimer la VM restaurée après le test.

## Validation et retour arrière

- **Validation** : La VM restaurée démarre et ses données sont intactes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Maintenance](<../Vie-du-logiciel/Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Maintenance.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
