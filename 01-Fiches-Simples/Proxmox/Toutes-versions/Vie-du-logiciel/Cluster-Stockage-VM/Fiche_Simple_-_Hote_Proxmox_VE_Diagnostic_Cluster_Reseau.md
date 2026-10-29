# Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Cluster_Reseau.md

- **Environnement** : Nœud autonome ou cluster Proxmox VE, accès console disponible
- **OS / Version** : Proxmox VE 8.x (adapter à la version installée)
- **Catégorie** : virtualisation / diagnostic
- **Tags** : `proxmox-ve`, `diagnostic`, `cluster`, `corosync`, `quorum`

---

## Problème précis à résoudre

Contrôler quorum, liens Corosync et réseau entre nœuds.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'interface, ouvrir **Datacenter > Cluster** pour voir l'état des nœuds.
   👉 Explication : un nœud rouge ou un quorum perdu apparaît ici.

2. Afficher l'état du cluster et des nœuds :
   ```bash
   pvecm status
   pvecm nodes
   ```
   👉 Explication : on lit le quorum, le nombre de votes et la liste des membres.

3. Contrôler les liens Corosync :
   ```bash
   corosync-cfgtool -s
   ```
   👉 Explication : on voit si chaque lien est connecté.

4. Contrôler adresses, routes et résolution (remplacer `pve02` par le nom d'un autre nœud) :
   ```bash
   ip -br address
   ip route
   getent hosts pve02
   ```
   👉 Explication : on vérifie que les adresses sont fixes et que les noms se résolvent.

5. Si le cluster est non-quorate, conserver l'état en lecture et rétablir d'abord le réseau ou le nœud manquant.
   👉 Explication : `pvecm expected 1` n'est pas une réparation générique; ne l'utiliser que selon la procédure Proxmox après analyse de split-brain et approbation.

## 2. Production — Contrôles

Vérifier aussi synchronisation horaire, pertes et latence sur le réseau cluster. Corosync utilise UDP 5405–5412 selon la configuration.

## 3. Production — Sécurité

- Les changements de réseau peuvent couper l'accès et l'appartenance : utiliser la console et le processus de staging.
- Ne pas forcer le quorum sans approbation.

## Validation et retour arrière

- **Validation** : Le quorum est compris et la cause réseau ou nœud identifiée.
- **Retour arrière** : Annuler tout changement réseau récent via la console si c'est la cause.

## Si le problème n'est pas résolu

- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Guide complet — diagnostiquer cluster et réseau](../../../../../02-Fiches-Completes/Proxmox/Toutes-versions/Diagnostic/34_Diagnostic_Proxmox_VE_Cluster_Stockage_VM.md#3-diagnostiquer-cluster-et-reseau)
