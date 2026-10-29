# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Fixer l'IP de gestion et le pont réseau `vmbr0`.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Nœud > System > Network > vmbr0 > Edit** (adresse CIDR, passerelle, ports du pont = interface physique), puis **Apply Configuration**. En ligne de commande, éditer le fichier :
   ```bash
   nano /etc/network/interfaces
   ifreload -a
   ```
   👉 Explication : le pont `vmbr0` porte l'IP de l'hôte et relie les VM au réseau physique; `ifreload -a` applique sans redémarrer.

2. Exemple de contenu pour `vmbr0` (remplacer les placeholders) :
   ```bash
   auto vmbr0
   iface vmbr0 inet static
       address IP_HOTE/24
       gateway IP_GW
       bridge-ports IFACE
       bridge-stp off
       bridge-fd 0
   ```
   👉 Explication : `IFACE` = interface physique (par exemple `eno1`).

3. Contrôler et tester :
   ```bash
   ip -br a
   ping -c 3 IP_GW
   ```
   👉 Explication : confirme l'IP et la sortie réseau.

## 2. Production — Contrôles

Faire la modification avec un accès console hors bande : une erreur coupe l'accès à l'interface web.

## 3. Production — Sécurité

Documenter l'IP dans l'IPAM; VLAN de gestion séparé des VM.

## Validation et retour arrière

- **Validation** : L'interface web répond sur https://IP_HOTE:8006.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Preparer](<../Vie-du-logiciel/Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Preparer.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
