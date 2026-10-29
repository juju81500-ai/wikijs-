# Fiche_Simple_-_Hote_Proxmox_VE_Diagnostic_VM_CT.md

- **Environnement** : Nœud autonome ou cluster Proxmox VE, accès console disponible
- **OS / Version** : Proxmox VE 8.x (adapter à la version installée)
- **Catégorie** : virtualisation / diagnostic
- **Tags** : `proxmox-ve`, `diagnostic`, `vm`, `ct`, `qm`, `pct`

---

## Problème précis à résoudre

Inspecter l'état et la configuration d'une VM ou d'un CT en échec.

## 1. Hors-Production (Lab / Test / POC)

1. Lister VM et conteneurs :
   ```bash
   qm list
   pct list
   ```
   👉 Explication : on repère l'état de chacun.

2. Afficher l'état et la configuration d'une VM (100 est un exemple de VMID à remplacer) :
   ```bash
   qm status 100
   qm config 100
   ```
   👉 Explication : on vérifie ressources, disques, pont et VLAN.

3. Afficher la configuration d'un conteneur (101 est un exemple de CTID à remplacer) :
   ```bash
   pct config 101
   ```
   👉 Explication : même contrôle pour un CT.

4. Dans l'interface, sélectionner l'invité puis **Task History** et **Console**.
   👉 Explication : on lit les tâches récentes et l'état de l'invité.

5. Sauvegarder la configuration et confirmer l'existence d'un backup avant toute action destructive ou migration.
   👉 Explication : cela garantit un retour arrière.

## 2. Production — Contrôles

Contrôler pont/VLAN, stockage et ressources de l'invité.

## 3. Production — Sécurité

- Ne pas supprimer ni migrer sans sauvegarde confirmée.

## Validation et retour arrière

- **Validation** : La cause côté invité (ressources, réseau, disque) est identifiée.
- **Retour arrière** : Lecture seule : rien à annuler.

## Si le problème n'est pas résolu

- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Guide complet — diagnostiquer une VM ou un conteneur](../../../../../02-Fiches-Completes/Proxmox/Toutes-versions/Diagnostic/34_Diagnostic_Proxmox_VE_Cluster_Stockage_VM.md#5-diagnostiquer-une-vm-ou-un-conteneur)
