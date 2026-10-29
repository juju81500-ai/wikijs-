# Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Stockage.md

- **Environnement** : Nœud autonome ou cluster Proxmox VE, accès console disponible
- **OS / Version** : Proxmox VE 8.x (adapter à la version installée)
- **Catégorie** : virtualisation / diagnostic
- **Tags** : `proxmox-ve`, `diagnostic`, `stockage`, `pvesm`

---

## Problème précis à résoudre

Vérifier montage, capacité et erreurs d'E/S des stockages.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'interface, ouvrir **Datacenter > Storage** puis la vue **Node > Disks**.
   👉 Explication : on voit l'état et le remplissage des stockages.

2. Afficher l'état des stockages Proxmox :
   ```bash
   pvesm status
   ```
   👉 Explication : un stockage `inactive` ou plein est visible.

3. Contrôler montages et disques :
   ```bash
   findmnt
   lsblk -f
   ```
   👉 Explication : on vérifie que les points de montage attendus existent.

4. Lire le journal du service de statistiques :
   ```bash
   journalctl -b -u pvestatd --no-pager
   ```
   👉 Explication : pvestatd signale les stockages injoignables.

5. Comparer l'état du stockage partagé depuis tous les nœuds concernés.
   👉 Explication : un stockage vu différemment selon les nœuds oriente vers le réseau ou l'export.

## 2. Production — Contrôles

Surveiller capacité, latence et erreurs d'E/S.

## 3. Production — Sécurité

- Ne pas retirer puis recréer une définition de stockage avant d'avoir prouvé où résident les volumes.

## Validation et retour arrière

- **Validation** : L'état de chaque stockage est connu et la cause identifiée.
- **Retour arrière** : Lecture seule : rien à annuler.

## Si le problème n'est pas résolu

- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Guide complet — diagnostiquer le stockage](../../../../../02-Fiches-Completes/Proxmox/Toutes-versions/Diagnostic/34_Diagnostic_Proxmox_VE_Cluster_Stockage_VM.md#4-diagnostiquer-le-stockage)
