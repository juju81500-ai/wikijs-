# Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Maintenance.md

- **Environnement** : Nœuds physiques dédiés, réseau Corosync faible latence
- **OS / Version** : Proxmox VE 8.x
- **Catégorie** : virtualisation / cluster

---

## Problème précis à résoudre

Mettre à jour en sécurité et réagir à une perte de quorum.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder les invités avant toute mise à jour.
   👉 Explication : on garde un point de retour.

2. Suivre les notes de version officielles et mettre à jour un nœud à la fois si la matrice de versions le permet.
   👉 Explication : le cluster reste disponible pendant la mise à jour.

3. Après chaque nœud, vérifier le cluster :
   ```bash
   pvecm status
   ```
   👉 Explication : on confirme le quorum avant de passer au suivant.

4. En cas de perte de quorum, préserver les données, isoler les nœuds et suivre la procédure Proxmox de récupération.
   👉 Explication : forcer arbitrairement le nombre de votes peut corrompre le cluster.

## 2. Production — Contrôles

Planifier fenêtres de maintenance et lire les notes de version par version.

## 3. Production — Sécurité

- Ne pas forcer le quorum sans procédure approuvée.

## Validation et retour arrière

- **Validation** : Quorum rétabli et nœuds à jour, VM fonctionnelles.
- **Retour arrière** : Restaurer les invités depuis les sauvegardes; réinstaller un nœud en échec selon la procédure officielle.

## Si le problème n'est pas résolu

- [Proxmox VE — Cluster Manager](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Guide complet — maintenance et incidents](/02-fiches-completes/proxmox/ve-8/installation-deploiement/09-hyperviseur-proxmox-ve-8x-cluster-corosync#5-maintenance-et-incidents)