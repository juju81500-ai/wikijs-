# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Désactiver ce qui n'est pas utile sur l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les ports en écoute :
   ```bash
   ss -tulpn
   ```
   👉 Explication : identifie les services ouverts (SSH 22, 8006, 3128 spiceproxy, 111 rpcbind, 25 postfix local).

2. Désactiver les services inutiles (remplacer `SERVICE`) :
   ```bash
   systemctl disable --now rpcbind.service rpcbind.socket
   systemctl disable --now SERVICE
   ```
   👉 Explication : ne désactiver `rpcbind` que si aucun stockage NFS n'est monté.

3. Désactiver l'accès SPICE/console si inutile (GUI : **Datacenter > Options**) et supprimer les ISO et templates inutilisés (GUI : **Stockage > ISO Images > Remove**).
   👉 Explication : moins de fichiers et de services exposés.

## 2. Production — Contrôles

Liste des ports autorisés documentée.

## 3. Production — Sécurité

Chaque port ouvert doit avoir un propriétaire.

## Validation et retour arrière

- **Validation** : `ss -tulpn` ne montre que les ports attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
