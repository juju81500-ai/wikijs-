# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Contrôle d'accès obligatoire : sans objet sur TrueNAS SCALE.

## 1. Hors-Production (Lab / Test / POC)

1. Constater qu'aucun module AppArmor/SELinux n'est administrable sur l'appliance :
   ```bash
   sudo aa-status 2>&1 | head -3
   getenforce 2>&1
   ```
   👉 Explication : l'absence de commande est normale.

2. À la place, utiliser les ACL ZFS, les rôles et l'isolation par jeu de données : GUI Jeux de données > Permissions.
   ```bash
   sudo zfs get acltype POOL/DATASET
   ```
   👉 Explication : les ACL NFSv4 contrôlent l'accès aux données.

## 2. Production — Contrôles

Documenter que le MAC n'est pas applicable.

## 3. Production — Sécurité

Compenser par ACL strictes et comptes dédiés.

## Validation et retour arrière

- **Validation** : ACL conformes.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
