# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_22_Synchronisation_Horaire_Ntp

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 22 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-22`

---

## Problème précis à résoudre

Garder l'heure exacte (essentiel pour le cluster et les certificats).

## 1. Hors-Production (Lab / Test / POC)

1. Proxmox 8 utilise `chrony`. Éditer la source de temps :
   ```bash
   nano /etc/chrony/chrony.conf
   systemctl restart chrony
   ```
   👉 Explication : remplacer la ligne `pool` par `server IP_NTP iburst` (`IP_NTP` = serveur NTP interne).

2. Contrôler la synchronisation :
   ```bash
   chronyc sources -v
   chronyc tracking
   timedatectl
   ```
   👉 Explication : `^*` marque la source choisie; `System clock synchronized: yes`.

3. Appliquer la même source à tous les nœuds.
   👉 Explication : un écart d'heure entre nœuds perturbe le quorum et Ceph.

## 2. Production — Contrôles

Au moins deux sources NTP internes.

## 3. Production — Sécurité

Bloquer NTP sortant sauf vers les sources approuvées.

## Validation et retour arrière

- **Validation** : `chronyc tracking` indique un décalage faible.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
