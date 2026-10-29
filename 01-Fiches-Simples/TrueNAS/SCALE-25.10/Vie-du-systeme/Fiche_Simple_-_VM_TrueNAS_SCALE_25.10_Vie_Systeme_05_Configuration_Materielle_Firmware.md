# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-05`

---

## Problème précis à résoudre

Préparer le BIOS/UEFI et les contrôleurs de disques pour ZFS.

## 1. Hors-Production (Lab / Test / POC)

1. Activer UEFI, la virtualisation (si besoin) et désactiver le Secure Boot si l'installation ne démarre pas. Mettre à jour le firmware BIOS/BMC.
   👉 Explication : chemin variable selon constructeur : menu BIOS/UEFI > Boot.

2. Passer le contrôleur de disques en mode HBA/IT (JBOD), sans RAID matériel :
   ```bash
   sudo lspci | grep -i -E 'sas|raid|sata'
   sudo storcli /c0 show
   ```
   👉 Explication : ZFS doit voir les disques bruts ; `storcli`/`sas3flash` selon le contrôleur LSI/Broadcom.

3. Vérifier que chaque disque est visible avec son numéro de série :
   ```bash
   lsblk -d -o NAME,MODEL,SERIAL,SIZE
   sudo smartctl -i /dev/sdX
   ```
   👉 Explication : le numéro de série sert à identifier le disque lors d'un remplacement (SDX est un disque à contrôler).

## 2. Production — Contrôles

Mettre à jour le firmware HBA et BMC en fenêtre de maintenance ; ne jamais utiliser de RAID matériel avec ZFS.

## 3. Production — Sécurité

Protéger le BIOS/BMC par mot de passe et isoler le BMC sur un VLAN d'administration.

## Validation et retour arrière

- **Validation** : Tous les disques apparaissent sans couche RAID.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
