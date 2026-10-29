# Fiche_Simple_-_GitHub_Cles_SSH

- **Environnement** : Poste de travail géré avec OpenSSH et compte GitHub approuvé
- **OS / Version** : GitHub SaaS — interface évolutive
- **Catégorie** : Cloud SaaS / authentification SSH
- **Tags** : `github`, `cloud-saas`, `ssh-cles`, `securite`
---

## Problème précis à résoudre

Créer une clé SSH locale protégée et enregistrer uniquement la clé publique sur le compte GitHub.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier OpenSSH et clés locales existantes
   ```bash
   ssh -V
   ls -la ~/.ssh
   ```
   👉 Explication : ne pas écraser une clé existante; identifier son usage.

2. Générer une clé Ed25519 dédiée au poste
   ```bash
   ssh-keygen -t ed25519 -C "EMAIL_A_REMPLACER"
   ```
   👉 Explication : remplacer l’adresse à remplacer et saisir une phrase secrète à l’invite; ne jamais partager la clé privée.

3. Ajouter uniquement la clé publique dans GitHub
   ```text
   GitHub > avatar > Settings > SSH and GPG keys > New SSH key; coller uniquement le fichier `id_ed25519.pub`.
   ```
   👉 Explication : vérifier l’extension `.pub` et donner un nom permettant la révocation par appareil.

4. Tester l’authentification SSH
   ```bash
   ssh -T git@github.com
   ```
   👉 Explication : lors de la première connexion, comparer l’empreinte serveur à la liste officielle GitHub avant acceptation.

## 2. Production — Contrôles

Appliquer le compte/organisation approuvé, rôles minimaux, revue des accès et procédure de récupération.

## 3. Production — Sécurité

- Ne jamais téléverser `id_ed25519` (clé privée); seule la clé `.pub` est enregistrée.
- Protéger la clé privée par phrase secrète et chiffrement du poste.
- Révoquer clé si poste perdu, réaffecté ou utilisateur parti.

## Validation et retour arrière

- **Validation** : La connexion SSH s’authentifie sur le compte attendu et l’empreinte du serveur a été vérifiée.
- **Retour arrière** : Supprimer la clé publique du compte, retirer la clé de l’agent et en générer une nouvelle sur un poste sain.

## Si le problème n'est pas résolu

- [GitHub Docs — compte](https://docs.github.com/account-and-profile/setting-up-and-managing-your-personal-account-on-github)
- [GitHub Docs — clés SSH](https://docs.github.com/authentication/connecting-to-github-with-ssh)
- [GitHub Docs — secrets Actions](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Fiche connexe](<Fiche_Simple_-_GitHub_Compte.md>)
