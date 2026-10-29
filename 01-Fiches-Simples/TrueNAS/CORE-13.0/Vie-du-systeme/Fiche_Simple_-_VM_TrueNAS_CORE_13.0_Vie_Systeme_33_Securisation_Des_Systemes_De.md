# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Limiter les droits et chiffrer les données sensibles.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Stockage > Pools > Ajouter un jeu de données > Chiffrement.
   ```sh
   zfs create -o encryption=on -o keyformat=passphrase POOL/CHIFFRE
   ```
   👉 Explication : la phrase secrète est demandée ; POOL est le pool, CHIFFRE le dataset.

2. Définir les ACL : Stockage > Pools > jeu de données > Modifier les permissions.
   ```sh
   zfs get acltype,aclmode POOL/DATASET
   ```
   👉 Explication : type d'ACL du dataset.

3. Limiter l'espace :
   ```sh
   zfs set quota=500G POOL/DATASET
   ```
   👉 Explication : empêche le remplissage du pool.

## 2. Production — Contrôles

Sauvegarder les clés hors du NAS.

## 3. Production — Sécurité

La perte de la clé signifie la perte des données.

## Validation et retour arrière

- **Validation** : Les datasets sensibles sont chiffrés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS CORE 13.0](./Sommaire_-_Vie_du_systeme_TrueNAS_CORE_13.0.md)
- [Documentation officielle](https://www.truenas.com/docs/core/)
