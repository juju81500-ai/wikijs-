# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Contrôler le démarrage de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le mode de démarrage :
   ```sh
   esxcli system boot device get
   esxcli system settings kernel list -o execInstalledOnly
   ```
   👉 Explication : montre le périphérique d'amorçage et la protection `execInstalledOnly`.

2. Console de gestion : vérifier l'ordre de démarrage (BIOS : **Boot Settings**), disque système en premier.
   👉 Explication : un ordre erroné fait démarrer l'ISO à chaque redémarrage.

3. Sauvegarder la configuration avant un changement de démarrage :
   ```sh
   vim-cmd hostsvc/firmware/sync_config
   vim-cmd hostsvc/firmware/backup_config
   ```
   👉 Explication : synchronise puis génère un fichier de sauvegarde téléchargeable.

## 2. Production — Contrôles

Tester un redémarrage après chaque changement.

## 3. Production — Sécurité

Activer Secure Boot si le matériel le permet.

## Validation et retour arrière

- **Validation** : Démarrage correct sur le disque système.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
