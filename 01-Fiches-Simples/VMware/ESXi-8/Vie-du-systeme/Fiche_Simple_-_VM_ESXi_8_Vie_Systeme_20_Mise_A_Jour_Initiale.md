# Fiche_Simple_-_VM_ESXi_8_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Hôte VMware ESXi 8 (hyperviseur)
- **OS / Version** : VMware ESXi 8; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `esxi8`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Appliquer les correctifs avant mise en service.

## 1. Hors-Production (Lab / Test / POC)

1. Passer l'hôte en maintenance (Host Client : **Hôte > Actions > Entrer en mode maintenance**), puis mettre à jour depuis le bundle :
   ```sh
   esxcli system maintenanceMode set --enable true
   esxcli software sources profile list -d /vmfs/volumes/DATASTORE/BUNDLE.zip
   esxcli software profile update -d /vmfs/volumes/DATASTORE/BUNDLE.zip -p NOM_PROFIL
   ```
   👉 Explication : `BUNDLE.zip` = bundle, `NOM_PROFIL` = profil listé; `update` conserve les VIB tiers compatibles.

2. Redémarrer l'hôte, puis quitter le mode maintenance :
   ```sh
   reboot
   esxcli system maintenanceMode set --enable false
   ```
   👉 Explication : les VM doivent être arrêtées ou migrées avant de passer en maintenance.

3. Vérifier la version :
   ```sh
   esxcli system version get
   ```
   👉 Explication : le build doit correspondre à celui visé.

## 2. Production — Contrôles

Fenêtre de maintenance; migrer les VM avec vMotion sous vCenter.

## 3. Production — Sécurité

Sauvegarder la configuration de l'hôte avant la mise à jour.

## Validation et retour arrière

- **Validation** : Le build est celui attendu et l'hôte hors maintenance.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire VMware ESXi 8](./Sommaire_-_Vie_du_systeme_ESXi_8.md)
- [Documentation officielle](https://docs.vmware.com/)
