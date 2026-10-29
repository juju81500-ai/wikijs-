# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_29_Pare_Feu_Hote

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 29 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Activer le pare-feu Proxmox et filtrer l'accès à l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Datacenter > Firewall > Options > Firewall : Yes**, puis **Datacenter > Firewall > Add** (autoriser SSH et 8006 depuis `RESEAU_ADMIN`), puis **Nœud > Firewall > Options > Firewall : Yes**. En ligne de commande, éditer `/etc/pve/firewall/cluster.fw` :
   ```bash
   [OPTIONS]
   enable: 1

   [RULES]
   IN SSH(ACCEPT) -source RESEAU_ADMIN
   IN ACCEPT -p tcp -dport 8006 -source RESEAU_ADMIN
   ```
   👉 Explication : `RESEAU_ADMIN` = réseau d'administration en CIDR; la politique par défaut est DROP en entrée.

2. Contrôler l'état :
   ```bash
   pve-firewall status
   pve-firewall compile | head
   ```
   👉 Explication : doit afficher `Status: enabled/running`.

3. Avant d'activer, vérifier que les règles SSH et 8006 existent.
   👉 Explication : sinon l'accès à l'hôte est coupé.

## 2. Production — Contrôles

Autoriser aussi corosync (5405-5412/UDP) et migrations entre nœuds en cluster.

## 3. Production — Sécurité

Politique par défaut : refuser en entrée.

## Validation et retour arrière

- **Validation** : L'accès depuis le réseau d'administration fonctionne, un autre réseau est bloqué.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)