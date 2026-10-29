# Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_Stabiliser.md

- **Environnement** : Nœud autonome ou cluster Proxmox VE, accès console disponible
- **OS / Version** : Proxmox VE 8.x (adapter à la version installée)
- **Catégorie** : virtualisation / diagnostic

---

## Problème précis à résoudre

Cadrer l'incident et éviter d'aggraver une panne de quorum, réseau ou stockage.

## 1. Hors-Production (Lab / Test / POC)

1. Noter le symptôme, l'heure de début, les nœuds et charges concernés, les changements récents et l'impact métier.
   👉 Explication : ces informations orientent le diagnostic.

2. Dans l'interface, ouvrir **Datacenter > Tasks** (ou **Node > Tasks**) pour repérer les tâches récentes en erreur.
   👉 Explication : on voit ce qui a changé ou échoué autour de l'heure d'incident.

3. Suspendre les migrations et tâches de maintenance non urgentes.
   👉 Explication : on évite d'ajouter des variables pendant l'analyse.

4. Ne pas forcer le quorum, supprimer un nœud, redémarrer Corosync ou modifier le stockage avant d'avoir recueilli l'état.
   👉 Explication : ces actions peuvent aggraver la panne ou provoquer un split-brain.

## 2. Production — Contrôles

Désigner un responsable d'incident, ouvrir un ticket et garder un accès console.

## 3. Production — Sécurité

- Ne pas lancer de commande de réparation avant la collecte d'état.
- Ne pas copier de secrets dans le ticket d'incident.

## Validation et retour arrière

- **Validation** : Le périmètre et les changements récents sont documentés.
- **Retour arrière** : Aucune modification n'est faite à cette étape.

## Si le problème n'est pas résolu

- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Guide complet — stabiliser avant d'agir](/02-fiches-completes/proxmox/toutes-versions/diagnostic/34-diagnostic-proxmox-ve-cluster-stockage-vm#1-stabiliser-avant-dagir)