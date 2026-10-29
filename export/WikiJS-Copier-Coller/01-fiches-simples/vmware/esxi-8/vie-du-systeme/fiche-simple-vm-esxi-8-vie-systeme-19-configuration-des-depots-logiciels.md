# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_19_Configuration_Des_Depots_Logiciels

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir la source des correctifs.

## 1. Hors-Production (Lab / Test / POC)

1. ESXi n'utilise pas de dépôt apt : les correctifs viennent de bundles (offline bundle) ou d'un dépôt de profil. Lister les profils disponibles :
   ```sh
   esxcli software sources profile list -d /vmfs/volumes/DATASTORE/VMware-ESXi-8.0-depot.zip
   ```
   👉 Explication : `DATASTORE` = datastore où est copié le bundle; liste les profils d'image.

2. Pour un hôte géré par vCenter, utiliser **vSphere Lifecycle Manager** (vSphere Client : **Menu > Lifecycle Manager > Importer ISO/Dépôt**).
   👉 Explication : centralise les correctifs de tous les hôtes.

3. Télécharger les bundles depuis le portail Broadcom (ou celui du constructeur) et les copier sur un datastore.
   👉 Explication : l'hôte n'a pas besoin d'accès Internet.

## 2. Production — Contrôles

Dépôt interne unique; image de cluster uniforme.

## 3. Production — Sécurité

Utiliser uniquement des bundles signés par VMware/Broadcom ou le constructeur.

## Validation et retour arrière

- **Validation** : Le profil cible est listé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire VMware ESXi 8](/01-fiches-simples/vmware/esxi-8/vie-du-systeme/sommaire-vie-du-systeme-esxi-8)
- [Documentation officielle](https://docs.vmware.com/)