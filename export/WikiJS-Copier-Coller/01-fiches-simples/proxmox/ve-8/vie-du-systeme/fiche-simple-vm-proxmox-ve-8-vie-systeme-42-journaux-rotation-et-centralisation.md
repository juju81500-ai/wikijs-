# Fiche_Simple_-_VM_Proxmox_VE_8_Vie_Systeme_42_Journaux_Rotation_Et_Centralisation

- **Environnement** : Hôte Proxmox VE 8 (hyperviseur)
- **OS / Version** : Proxmox VE 8; étape 42 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Conserver et centraliser les journaux.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le journal et la rotation :
   ```bash
   journalctl -u pvedaemon -u pveproxy --since '-1h' | tail
   cat /etc/logrotate.d/pve
   journalctl --disk-usage
   ```
   👉 Explication : les tâches Proxmox sont dans `/var/log/pve/tasks/` (GUI : **Nœud > Tasks** et **Nœud > System > Syslog**).

2. Limiter la taille du journal : dans `/etc/systemd/journald.conf`, définir `SystemMaxUse=1G` puis `systemctl restart systemd-journald`.
   👉 Explication : évite de remplir le disque système.

3. Envoyer les journaux au serveur central (remplacer `IP_SYSLOG`) :
   ```bash
   apt install -y rsyslog
   echo '*.* @@IP_SYSLOG:514' > /etc/rsyslog.d/90-central.conf
   systemctl restart rsyslog
   ```
   👉 Explication : `@@` = transport TCP; utiliser TLS si le serveur le permet.

## 2. Production — Contrôles

Conserver les journaux selon la politique (90 jours minimum).

## 3. Production — Sécurité

Journaux en lecture seule pour les non-administrateurs.

## Validation et retour arrière

- **Validation** : Les événements de l'hôte arrivent sur le serveur central.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Proxmox VE 8](/01-fiches-simples/proxmox/ve-8/vie-du-systeme/sommaire-vie-du-systeme-proxmox-ve-8)
- [Documentation officielle](https://pve.proxmox.com/pve-docs/)