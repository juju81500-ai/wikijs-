# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Limiter les droits et chiffrer les données sensibles.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Jeux de données > Ajouter un jeu de données > Options de chiffrement (Inherit/Encryption).
   ```bash
   sudo zfs create -o encryption=on -o keyformat=passphrase POOL/CHIFFRE
   ```
   👉 Explication : POOL est le nom du pool, CHIFFRE le dataset ; la phrase secrète est demandée à la saisie.

2. Définir les ACL : Jeux de données > Permissions > Modifier.
   ```bash
   sudo zfs get acltype,aclmode POOL/DATASET
   ```
   👉 Explication : vérifie le type d'ACL (NFSv4 pour SMB).

3. Limiter l'espace : GUI Jeux de données > Modifier > quota.
   ```bash
   sudo zfs set quota=500G POOL/DATASET
   ```
   👉 Explication : empêche un dataset de remplir le pool.

## 2. Production — Contrôles

Sauvegarder les clés de chiffrement hors du NAS.

## 3. Production — Sécurité

La perte de la clé signifie la perte des données.

## Validation et retour arrière

- **Validation** : Les datasets sensibles sont chiffrés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)