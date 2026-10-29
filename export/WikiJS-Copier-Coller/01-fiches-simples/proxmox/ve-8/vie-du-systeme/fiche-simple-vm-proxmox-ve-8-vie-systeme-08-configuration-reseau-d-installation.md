# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Donner à l'installateur une adresse IP de gestion.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur, écran **Management Network Configuration** : choisir l'interface de gestion, saisir l'IP en CIDR (`IP_HOTE/24`), la passerelle (`IP_GW`) et le DNS (`IP_DNS`).
   👉 Explication : l'IP saisie sera celle de l'interface web https://IP_HOTE:8006; la passerelle et le DNS doivent être joignables.

2. Depuis la console, contrôler le réseau :
   ```bash
   ip -br a
   ip route
   ping -c 3 IP_GW
   ```
   👉 Explication : `IP_HOTE`, `IP_GW`, `IP_DNS` = adresses de votre plan d'adressage.

3. Noter l'interface choisie (nom `enoX`/`ensX`) dans le dossier.
   👉 Explication : le nom est repris dans le pont `vmbr0`.

## 2. Production — Contrôles

Réseau de gestion isolé (VLAN d'administration).

## 3. Production — Sécurité

Ne jamais exposer l'interface 8006 sur Internet.

## Validation et retour arrière

- **Validation** : `ping` vers la passerelle réussit.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Preparer](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)