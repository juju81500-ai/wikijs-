# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `proxmoxve8`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Installer fail2ban :
   ```bash
   apt install -y fail2ban
   ```
   👉 Explication : bannit les adresses qui échouent plusieurs fois.

2. Créer `/etc/fail2ban/jail.local` pour SSH et l'interface web Proxmox :
   ```bash
   [sshd]
   enabled = true
   maxretry = 3
   bantime = 1h

   [proxmox]
   enabled = true
   port = https,http,8006
   filter = proxmox
   backend = systemd
   maxretry = 3
   bantime = 1h
   ```
   👉 Explication : le filtre `proxmox` doit être créé dans `/etc/fail2ban/filter.d/proxmox.conf` avec `failregex = pvedaemon\[.*authentication failure; rhost=<HOST> user=.* msg=.*`.

3. Activer et contrôler :
   ```bash
   systemctl enable --now fail2ban
   fail2ban-client status
   ```
   👉 Explication : liste les prisons actives.

## 2. Production — Contrôles

Exclure le réseau d'administration (`ignoreip`).

## 3. Production — Sécurité

Journaliser et alerter sur les bannissements.

## Validation et retour arrière

- **Validation** : `fail2ban-client status sshd` affiche la prison.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Proxmox VE 8](./Sommaire_-_Vie_du_systeme_Proxmox_VE_8.md)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)
