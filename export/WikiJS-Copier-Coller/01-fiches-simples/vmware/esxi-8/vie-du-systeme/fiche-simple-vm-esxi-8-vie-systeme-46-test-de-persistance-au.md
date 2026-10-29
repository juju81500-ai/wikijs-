# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier que la configuration survit à un redémarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Passer l'hôte en maintenance (migrer les VM) puis redémarrer :
   ```sh
   esxcli system maintenanceMode set --enable true
   esxcli system shutdown reboot -d 60 -r 'test persistance'
   ```
   👉 Explication : `-d 60` = délai de 60 s; l'hôte doit être en maintenance (VM arrêtées ou migrées).

2. Après redémarrage, vérifier :
   ```sh
   uptime
   esxcli network ip interface ipv4 get
   esxcli storage filesystem list
   esxcli system ntp get
   ```
   👉 Explication : IP, datastores, NTP.

3. Contrôler le démarrage automatique des VM (Host Client : **Hôte > Gérer > Système > Démarrage automatique**) :
   ```sh
   vim-cmd hostsvc/autostartmanager/get_autostartseq
   esxcli system maintenanceMode set --enable false
   ```
   👉 Explication : les VM marquées démarrent dans l'ordre; sortir ensuite du mode maintenance.

## 2. Production — Contrôles

Redémarrer en fenêtre de maintenance.

## 3. Production — Sécurité

Garder l'accès console pour dépanner.

## Validation et retour arrière

- **Validation** : Tout est revenu comme avant le redémarrage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)