# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_26_Authentification_Par_Cles_Ssh

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenasscale2510`, `vie-du-systeme`, `cycle-de-vie`, `etape-26`

---

## Problème précis à résoudre

Remplacer le mot de passe SSH par une clé.

## 1. Hors-Production (Lab / Test / POC)

1. Générer une clé sur le poste d'administration :
   ```bash
   ssh-keygen -t ed25519 -C ADMIN1@POSTE
   ```
   👉 Explication : crée la paire de clés ; ADMIN1@POSTE est un commentaire.

2. GUI : Identifiants > Utilisateurs > ADMIN1 > Modifier > Clé publique SSH (coller le contenu de `~/.ssh/id_ed25519.pub`).
   ```bash
   sudo midclt call user.update ID_UTILISATEUR '{"sshpubkey": "CLE_PUBLIQUE"}'
   ```
   👉 Explication : ID_UTILISATEUR est l'identifiant numérique retourné par `user.query` ; CLE_PUBLIQUE est le contenu du fichier `.pub`.

3. Tester la connexion :
   ```bash
   ssh ADMIN1@ADRESSE_NAS
   ```
   👉 Explication : doit se connecter sans mot de passe.

## 2. Production — Contrôles

Une clé par administrateur.

## 3. Production — Sécurité

Protéger la clé privée par une phrase secrète.

## Validation et retour arrière

- **Validation** : Connexion par clé réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire TrueNAS SCALE 25.10](./Sommaire_-_Vie_du_systeme_TrueNAS_SCALE_25.10.md)
- [Documentation officielle](https://www.truenas.com/docs/scale/)
