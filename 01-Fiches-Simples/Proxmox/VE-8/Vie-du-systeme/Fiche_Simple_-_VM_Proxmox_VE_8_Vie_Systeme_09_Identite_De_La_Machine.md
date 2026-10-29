# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_09_Identite_De_La_Machine

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 09 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-09`

---

## Problème précis à résoudre

Nommer l'hôte avec un FQDN résolvable (obligatoire sous Proxmox).

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'installateur : champ **Hostname (FQDN)** (par exemple `pve01.domaine.local`).
   👉 Explication : le FQDN doit se résoudre vers l'IP de gestion, sinon les services Proxmox échouent.

2. Après installation, contrôler :
   ```bash
   hostname -f
   getent hosts $(hostname -f)
   cat /etc/hosts
   ```
   👉 Explication : le FQDN doit pointer vers `IP_HOTE`, pas vers 127.0.1.1.

3. Ne pas renommer un nœud après sa création : réinstaller si le nom est faux (GUI : l'interface ne permet pas de renommer).
   👉 Explication : le nom est inscrit dans `/etc/pve` et dans le cluster.

## 2. Production — Contrôles

Nom conforme à la convention de nommage et déclaré dans le DNS (A et PTR).

## 3. Production — Sécurité

Un nom explicite simplifie l'audit.

## Validation et retour arrière

- **Validation** : `hostname -f` renvoie le FQDN attendu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : Hote Proxmox VE 8 Cluster Preparer](<../Vie-du-logiciel/Cluster-Corosync/Fiche_Simple_-_Hote_Proxmox_VE_8_Cluster_Preparer.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
