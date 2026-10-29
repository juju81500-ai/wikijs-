# 📄 Fiche_Simple_-_Proxmox_VE_8_Securite_Pare_Feu_Datacenter.md

- **Environnement** : Nœud ou cluster Proxmox VE 8 (pare-feu datacenter, pare-feu hôte et pare-feu des VM)
- **OS / Version** : Proxmox VE 8.x - Debian 12 Bookworm
- **Catégorie** : Sécurité réseau / Pare-feu hyperviseur

---

## 🎯 Problème précis à résoudre
Activer le pare-feu Proxmox au niveau datacenter, n'ouvrir que les flux d'administration et de cluster nécessaires, puis passer la politique entrante en refus par défaut sans couper l'accès à l'hôte.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Contrôler l'état du pare-feu Proxmox :
```bash
pve-firewall status
pvesh get /cluster/firewall/options
```
👉 Explication : `pve-firewall status` indique si le service tourne ; `pvesh get /cluster/firewall/options` affiche les options du datacenter (activation et politiques).

2. Activer le pare-feu au niveau datacenter :
```bash
pvesh set /cluster/firewall/options --enable 1
```
👉 Explication : active le pare-feu datacenter. Tant qu'aucune politique de refus n'est définie, le trafic reste autorisé, donc aucune coupure n'est provoquée à cette étape.

3. Autoriser l'interface web depuis le réseau d'administration :
```bash
pvesh create /cluster/firewall/rules --type in --action ACCEPT --proto tcp --dport 8006 --source <reseau_admin_cidr> --enable 1 --comment "Interface web admin"
```
👉 Explication : crée une règle entrante TCP/8006 (interface web Proxmox) limitée au réseau d'administration, par exemple `192.168.10.0/24`.

4. Vérifier les règles compilées :
```bash
pve-firewall compile
```
👉 Explication : affiche les règles iptables générées à partir des fichiers de configuration ; une erreur de syntaxe ou une règle invalide y est signalée.

---

## ⚡ 2. Production — Façon Simplifiée
1. Définir un alias pour le réseau d'administration :
```bash
pvesh create /cluster/firewall/aliases --name reseau_admin --cidr <reseau_admin_cidr>
```
👉 Explication : nomme le réseau d'administration pour le réutiliser dans toutes les règles au lieu de répéter le CIDR.

2. Autoriser SSH et l'interface web depuis cet alias :
```bash
pvesh create /cluster/firewall/rules --type in --action ACCEPT --proto tcp --dport 22 --source reseau_admin --enable 1 --comment "SSH admin"
pvesh create /cluster/firewall/rules --type in --action ACCEPT --proto tcp --dport 8006 --source reseau_admin --enable 1 --comment "Web admin"
```
👉 Explication : deux règles d'administration limitées à l'alias `reseau_admin`. La règle TCP/8006 de la section précédente peut être supprimée dans l'interface pour éviter les doublons.

3. Autoriser le trafic Corosync entre les nœuds d'un cluster :
```bash
pvesh create /cluster/firewall/rules --type in --action ACCEPT --proto udp --dport 5405:5412 --source <reseau_cluster_cidr> --enable 1 --comment "Corosync cluster"
```
👉 Explication : Corosync utilise les ports UDP 5405 à 5412 pour le quorum et la communication du cluster ; à ignorer sur un nœud autonome. Les migrations de VM entre nœuds nécessitent en plus une règle TCP 60000:60050 depuis le réseau cluster.

4. Activer le pare-feu au niveau de l'hôte :
```bash
pvesh set /nodes/<nom_de_l_hote>/firewall/options --enable 1
```
👉 Explication : active le pare-feu propre au nœud ; les règles datacenter s'appliquent à tous les nœuds, mais le pare-feu du nœud doit aussi être activé pour que ses propres règles soient appliquées.

5. Passer la politique entrante en refus par défaut :
```bash
pvesh set /cluster/firewall/options --enable 1 --policy_in DROP
```
👉 Explication : tout trafic entrant non autorisé par une règle est bloqué. Vérifier au préalable que l'accès SSH et web depuis `reseau_admin` fonctionne, et conserver un accès console (IPMI, iDRAC, iLO ou clavier/écran) en cas d'erreur.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Journaliser les paquets refusés avec limitation de débit :
```bash
pvesh set /cluster/firewall/options --log_ratelimit enable=1,rate=1/second,burst=5
```
👉 Explication : enregistre les refus dans le journal noyau sans saturer les journaux lors d'une attaque par inondation ; consultables avec `journalctl -k | grep -i drop`.

2. Activer le pare-feu sur chaque VM, puis sur chaque carte réseau :
```bash
pvesh set /nodes/<nom_de_l_hote>/qemu/<vmid>/firewall/options --enable 1
```
👉 Explication : active le filtrage des VM au niveau de l'hyperviseur ; la case Firewall doit aussi être cochée sur la carte réseau (net0) de la VM dans l'interface. Pour un conteneur, utiliser `/nodes/<nom_de_l_hote>/lxc/<ctid>/firewall/options`.

3. Vérifier la compilation après ajout des règles :
```bash
pve-firewall compile | head -n 40
pve-firewall status
```
👉 Explication : contrôle que les règles générées correspondent aux intentions (ports ouverts, sources limitées) et que le service est actif.

4. Sauvegarder la configuration du pare-feu :
```bash
tar -czf /root/pve-firewall-$(date +%F).tar.gz /etc/pve/firewall /etc/pve/nodes/<nom_de_l_hote>/host.fw
```
👉 Explication : conserve les fichiers `cluster.fw` et `host.fw` de pmxcfs pour restaurer rapidement la politique après une erreur de manipulation ; ce fichier doit être stocké hors de l'hôte.