# Fiche_Simple_-_VM_TrueNAS_SCALE_25.10_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Serveur de stockage TrueNAS SCALE 25.10
- **OS / Version** : TrueNAS SCALE 25.10; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Sécuriser le compte d'administration initial.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le mot de passe du compte administrateur dans l'installateur (compte `truenas_admin`), puis le changer si besoin : Identifiants > Utilisateurs > truenas_admin > Modifier.
   ```bash
   sudo midclt call user.query '[["username","=","truenas_admin"]]'
   ```
   👉 Explication : vérifie l'existence du compte sans afficher le mot de passe.

2. Désactiver la connexion SSH par mot de passe de ce compte après dépôt d'une clé (étape 26).
   👉 Explication : le compte reste utilisable uniquement par la console et l'interface web.

## 2. Production — Contrôles

Stocker le mot de passe dans le coffre de l'équipe, jamais dans un fichier.

## 3. Production — Sécurité

Mot de passe long et unique ; double authentification : Système > Sécurité > 2FA.

## Validation et retour arrière

- **Validation** : Connexion à l'interface web réussie.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS SCALE 25.10](/01-fiches-simples/truenas/scale-25-10/vie-du-systeme/sommaire-vie-du-systeme-truenas-scale-25-10)
- [Documentation officielle](https://www.truenas.com/docs/scale/)