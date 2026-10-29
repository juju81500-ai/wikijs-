# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_21_Pilotes_Et_Agents_De

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 21 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-21`

---

## Problème précis à résoudre

Installer les pilotes constructeur et les VMware Tools des invités.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les pilotes et VIB installés :
   ```sh
   esxcli software vib list | grep -i -E 'nic|net|nvme|lsi|dell|hpe'
   esxcli network nic list
   ```
   👉 Explication : montre les pilotes réseau et leur état (`Up`).

2. Installer un pilote constructeur depuis un bundle :
   ```sh
   esxcli software vib install -d /vmfs/volumes/DATASTORE/PILOTE.zip
   ```
   👉 Explication : à faire en mode maintenance, puis redémarrer.

3. Dans chaque VM, installer VMware Tools (Host Client : **VM > Actions > Invité > Installer VMware Tools**; Linux : `open-vm-tools`) :
   ```sh
   vim-cmd vmsvc/getallvms
   vim-cmd vmsvc/get.guest VMID | grep -i toolsStatus
   ```
   👉 Explication : `VMID` = numéro de la VM; `toolsOk` attendu.

## 2. Production — Contrôles

Utiliser l'image du constructeur pour limiter les pilotes manuels.

## 3. Production — Sécurité

Installer uniquement des pilotes signés.

## Validation et retour arrière

- **Validation** : Tous les ports réseau en `Up` et `toolsOk` sur les VM.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
