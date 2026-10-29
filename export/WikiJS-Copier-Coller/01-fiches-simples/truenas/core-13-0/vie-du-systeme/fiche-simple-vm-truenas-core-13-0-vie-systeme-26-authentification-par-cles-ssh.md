# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Remplacer le mot de passe SSH par une clé.

## 1. Hors-Production (Lab / Test / POC)

1. Générer une clé sur le poste d'administration :
   ```sh
   ssh-keygen -t ed25519 -C ADMIN1@POSTE
   ```
   👉 Explication : crée la paire de clés.

2. GUI : Compte > Utilisateurs > ADMIN1 > Modifier > Clé publique SSH.
   ```sh
   midclt call user.update ID_UTILISATEUR '{"sshpubkey": "CLE_PUBLIQUE"}'
   ```
   👉 Explication : ID_UTILISATEUR vient de `user.query`; CLE_PUBLIQUE est le contenu du fichier `.pub`.

3. Tester :
   ```sh
   ssh ADMIN1@ADRESSE_NAS
   ```
   👉 Explication : connexion sans mot de passe.

## 2. Production — Contrôles

Une clé par administrateur.

## 3. Production — Sécurité

Clé privée protégée par phrase secrète.

## Validation et retour arrière

- **Validation** : Connexion par clé réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)