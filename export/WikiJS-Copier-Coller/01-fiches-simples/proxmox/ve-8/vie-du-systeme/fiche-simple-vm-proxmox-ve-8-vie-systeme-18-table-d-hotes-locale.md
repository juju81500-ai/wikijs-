# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_18_Table_D_Hotes_Locale

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 18 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Garantir la résolution du FQDN de l'hôte et des nœuds du cluster sans DNS.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Nœud > System > Hosts > Edit**. En ligne de commande :
   ```bash
   nano /etc/hosts
   ```
   👉 Explication : ajouter la ligne `IP_HOTE pve01.domaine.local pve01` pour chaque nœud du cluster.

2. Vérifier :
   ```bash
   getent hosts pve01.domaine.local
   ```
   👉 Explication : doit renvoyer l'IP de gestion.

3. Ne pas laisser le FQDN sur `127.0.1.1`.
   👉 Explication : la communication du cluster (corosync) échoue si le nom pointe vers le bouclage.

## 2. Production — Contrôles

Garder les nœuds dans `/etc/hosts` même avec un DNS, pour la résilience du cluster.

## 3. Production — Sécurité

Contrôler le fichier après chaque modification.

## Validation et retour arrière

- **Validation** : Chaque nœud résout ses pairs.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Preparer](</01-fiches-simples/proxmox/ve-8/vie-du-logiciel/cluster-corosync/fiche-simple-hote-proxmox-ve-8-cluster-preparer>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)