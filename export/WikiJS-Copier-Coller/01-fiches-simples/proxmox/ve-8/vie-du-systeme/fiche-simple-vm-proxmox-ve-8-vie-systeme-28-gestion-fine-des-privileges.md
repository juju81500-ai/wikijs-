# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Donner des droits d'administration précis sans partager root.

## 1. Hors-Production (Lab / Test / POC)

1. Installer sudo et créer un fichier dédié :
   ```bash
   apt install -y sudo
   visudo -f /etc/sudoers.d/admins
   ```
   👉 Explication : `visudo` vérifie la syntaxe avant d'enregistrer.

2. Ajouter la règle (remplacer `ADMIN1`) :
   ```bash
   ADMIN1 ALL=(root) /usr/sbin/qm, /usr/sbin/pct, /usr/bin/pvesh
   ```
   👉 Explication : limite le compte aux commandes Proxmox nécessaires.

3. Préférer les rôles Proxmox (GUI : **Datacenter > Permissions**) pour les actions sur les VM.
   ```bash
   pveum role list
   ```
   👉 Explication : les rôles couvrent l'API et l'interface sans donner de shell.

## 2. Production — Contrôles

Privilèges limités par rôle (exploitation, audit).

## 3. Production — Sécurité

Journaliser les commandes `sudo` (`/var/log/auth.log`).

## Validation et retour arrière

- **Validation** : `sudo -l -U ADMIN1` liste les droits attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)