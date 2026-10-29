# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Séparer les accès par application.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Identifiants > Utilisateurs > Ajouter un compte sans shell et sans connexion SMB inutile.
   ```bash
   sudo midclt call user.create '{"username":"SVC_SAUVEGARDE","full_name":"Service","password_disabled":true,"shell":"/usr/sbin/nologin","group_create":true}'
   ```
   👉 Explication : SVC_SAUVEGARDE est le compte de service.

2. Donner uniquement les droits sur le dataset concerné : GUI Jeux de données > Permissions.
   ```bash
   sudo zfs get acltype,mountpoint POOL/DATASET
   ```
   👉 Explication : limite l'accès à un dataset.

## 2. Production — Contrôles

Un compte par application, mot de passe désactivé et clé ou jeton dédié.

## 3. Production — Sécurité

Pas de compte de service membre d'un groupe administrateur.

## Validation et retour arrière

- **Validation** : Les comptes de service n'ont pas de shell.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)