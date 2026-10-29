# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir le mode d'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir Fresh Install ou Upgrade, mode UEFI ou BIOS.
   👉 Explication : les paquets FreeBSD ne s'ajoutent pas au système : `pkg` n'est pas supporté sur l'appliance.

2. Lister les services : GUI Services.
   ```sh
   midclt call service.query | grep -E '"service"|"state"'
   ```
   👉 Explication : état de chaque service.

## 2. Production — Contrôles

N'activer que SMB, NFS, iSCSI, SSH nécessaires.

## 3. Production — Sécurité

Ne pas installer de paquet sur le système.

## Validation et retour arrière

- **Validation** : Services documentés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)