# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Enregistrer l'état de référence de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter l'état du nœud :
   ```bash
   pveversion -v > baseline-pve.txt
   ip -br a >> baseline-pve.txt
   pvesm status >> baseline-pve.txt
   systemctl --failed >> baseline-pve.txt
   ```
   👉 Explication : fichier de référence pour comparer plus tard.

2. Contrôler les services Proxmox :
   ```bash
   systemctl status pve-cluster pvedaemon pveproxy pvestatd --no-pager | grep -E 'Active|●'
   ```
   👉 Explication : tous les services doivent être `active (running)`.

3. Archiver la configuration (GUI : **Datacenter > Backup** pour les VM; pour l'hôte, copier `/etc/pve` et `/etc/network`) :
   ```bash
   tar czf pve-config-$(date +%F).tgz /etc/pve /etc/network /etc/hosts /etc/chrony
   ```
   👉 Explication : sauvegarde des fichiers de configuration de l'hôte.

## 2. Production — Contrôles

Conserver la baseline avec le dossier.

## 3. Production — Sécurité

Stocker l'archive hors de l'hôte, chiffrée.

## Validation et retour arrière

- **Validation** : Services actifs, aucune unité en échec.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
