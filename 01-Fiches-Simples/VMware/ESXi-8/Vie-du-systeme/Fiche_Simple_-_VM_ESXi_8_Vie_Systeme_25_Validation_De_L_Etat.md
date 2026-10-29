# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_25_Validation_De_L_Etat

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 25 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-25`

---

## Problème précis à résoudre

Enregistrer l'état de référence de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter l'état de l'hôte dans un fichier (sur un datastore) :
   ```sh
   (esxcli system version get; esxcli network ip interface ipv4 get; esxcli storage filesystem list; esxcli software vib list) > /vmfs/volumes/DATASTORE/baseline-esxi.txt
   ```
   👉 Explication : fichier de référence pour comparer plus tard.

2. Sauvegarder la configuration de l'hôte :
   ```sh
   vim-cmd hostsvc/firmware/sync_config
   vim-cmd hostsvc/firmware/backup_config
   ```
   👉 Explication : génère une archive `configBundle` téléchargeable depuis l'URL affichée.

3. Contrôler les services (Host Client : **Gérer > Services**).
   ```sh
   esxcli system services list 2>/dev/null | head
   ```
   👉 Explication : vérifier que seuls les services attendus sont démarrés.

## 2. Production — Contrôles

Conserver la baseline avec le dossier.

## 3. Production — Sécurité

Stocker l'archive de configuration hors de l'hôte, chiffrée.

## Validation et retour arrière

- **Validation** : Baseline enregistrée et sauvegarde de configuration réalisée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
