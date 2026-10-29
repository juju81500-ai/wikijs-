# Diagnostiquer un incident Proxmox VE : cluster, stockage et VM

- **Type de fiche** : Diagnostic
- **Environnement** : Nœud autonome ou cluster Proxmox VE, accès console disponible
- **OS / Version** : Proxmox VE 8.x; adapter les commandes et procédures à la version installée
- **Rôle** : Isoler un incident sans aggraver une panne de quorum, réseau ou stockage

## 1. Stabiliser avant d'agir

Fiche simple : [stabiliser avant d'agir](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-stabiliser).

Identifier le symptôme, l'heure de début, les nœuds et charges concernés, les changements récents et l'impact métier. Suspendre les migrations et tâches de maintenance non urgentes. Ne pas forcer le quorum, supprimer un nœud, redémarrer Corosync ou modifier le stockage avant d'avoir recueilli l'état et vérifié le nombre de votes.

## 2. Collecter l'état général

Fiche simple : [collecter l'état général](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-etat-general).

Sur chaque nœud touché :

```bash
pveversion -v
uptime
systemctl --failed
journalctl -b -p err --no-pager
df -h
free -h
```

Comparer les résultats entre les nœuds et noter les erreurs autour de l'heure d'incident.

## 3. Diagnostiquer cluster et réseau

Fiche simple : [diagnostiquer cluster et réseau](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-cluster-reseau).

```bash
pvecm status
pvecm nodes
corosync-cfgtool -s
ip -br address
ip route
getent hosts <AUTRE_NOEUD>
```

Vérifier quorum, appartenance et liens Corosync, adresses fixes, résolution, synchronisation horaire et pertes/latence sur le réseau cluster. Les paquets Corosync utilisent UDP 5405–5412 selon la configuration. Les changements de réseau peuvent couper l'accès et l'appartenance; utiliser la console et le processus de staging documenté.

Si le cluster est non-quorate, conserver l'état en lecture et rétablir d'abord le réseau ou le nœud manquant. `pvecm expected 1` n'est pas une réparation générique : ne l'utiliser que selon la procédure Proxmox correspondant au scénario, après analyse de split-brain et approbation.

## 4. Diagnostiquer le stockage

Fiche simple : [diagnostiquer le stockage](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-stockage).

```bash
pvesm status
findmnt
lsblk -f
journalctl -b -u pvestatd --no-pager
```

Vérifier montage, reachability, capacité, latence, erreurs I/O et état du stockage partagé depuis tous les nœuds concernés. Un stockage plein ou indisponible peut bloquer des VM; ne pas retirer puis recréer une définition de stockage avant d'avoir prouvé où résident les volumes.

## 5. Diagnostiquer une VM ou un conteneur

Fiche simple : [diagnostiquer une VM ou un conteneur](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-vm-ct).

```bash
qm list
pct list
qm status <VMID>
qm config <VMID>
pct config <CTID>
```

Lire les tâches récentes depuis l'interface et les journaux liés à la VM. Contrôler le pont/VLAN, le stockage, les ressources et l'état de l'invité. Sauvegarder la configuration et confirmer l'existence d'un backup avant toute action destructive ou migration.

## 6. Restaurer le service de façon contrôlée

Fiche simple : [restaurer le service de façon contrôlée](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-restaurer).

Corriger une seule cause à la fois, commencer par les changements réversibles et valider après chaque modification. Si un nœud est suspect, isoler son accès sans le supprimer du cluster. Pour une VM critique, restaurer depuis une sauvegarde testée vers un emplacement contrôlé plutôt que manipuler directement ses disques.

## 7. Clôturer

Fiche simple : [clôturer](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/cluster-stockage-vm/fiche-simple-hote-proxmox-ve-diagnostic-cloturer).

Consigner les sorties non sensibles, la cause, le changement réalisé, la validation des VM et du stockage et les actions préventives. Retirer toute donnée sensible des journaux partagés.

## Sources

- [Proxmox VE — Guide d'administration](https://pve.proxmox.com/pve-docs/)
- [Proxmox VE — Cluster Manager et quorum](https://pve.proxmox.com/wiki/Cluster_Manager)
- [Proxmox VE — Configuration réseau](https://pve.proxmox.com/wiki/Network_Configuration)
- [Proxmox VE — Stockage](https://pve.proxmox.com/wiki/Storage)