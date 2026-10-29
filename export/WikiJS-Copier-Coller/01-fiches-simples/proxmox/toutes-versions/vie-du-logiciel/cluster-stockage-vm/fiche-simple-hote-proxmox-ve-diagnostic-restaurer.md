# Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Restaurer.md

- **Environnement** : Nœud autonome ou cluster Proxmox VE, accès console disponible
- **OS / Version** : Proxmox VE 8.x (adapter à la version installée)
- **Catégorie** : virtualisation / diagnostic

---

## Problème précis à résoudre

Corriger une seule cause à la fois et valider après chaque modification.

## 1. Hors-Production (Lab / Test / POC)

1. Commencer par le changement réversible le plus simple (réseau, montage, redémarrage d'une VM).
   👉 Explication : on limite le risque.

2. Après chaque modification, relancer l'état du cluster et des stockages :
   ```bash
   pvecm status
   pvesm status
   ```
   👉 Explication : on valide l'effet avant d'enchaîner.

3. Si un nœud est suspect, isoler son accès sans le supprimer du cluster.
   👉 Explication : supprimer un nœud est irréversible.

4. Pour une VM critique, restaurer depuis une sauvegarde testée vers un emplacement contrôlé.
   👉 Explication : on évite de manipuler directement les disques.

## 2. Production — Contrôles

Obtenir l'approbation avant toute action sur le quorum ou le stockage partagé.

## 3. Production — Sécurité

- Ne corriger qu'une cause à la fois.
- Garder un accès console pendant les changements.

## Validation et retour arrière

- **Validation** : Cluster quorate, stockages actifs, VM concernées démarrées.
- **Retour arrière** : Annuler le dernier changement réversible effectué.

## Si le problème n'est pas résolu

- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Guide complet — restaurer le service de façon contrôlée](/02-fiches-completes/proxmox/toutes-versions/diagnostic/34-diagnostic-proxmox-ve-cluster-stockage-vm#6-restaurer-le-service-de-facon-controlee)