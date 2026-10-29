# Fiche_Simple_-_GitHub_Actions_Secrets

- **Environnement** : Dépôt GitHub de test dans une organisation autorisée
- **OS / Version** : GitHub SaaS — interface évolutive
- **Catégorie** : Cloud SaaS / CI/CD et gestion des secrets
- **Tags** : `github`, `cloud-saas`, `actions-secrets`, `securite`
---

## Problème précis à résoudre

Stocker un secret Actions au périmètre minimal puis le consommer sans l’inclure dans le dépôt ou les logs.

## 1. Hors-Production (Lab / Test / POC)

1. Limiter permissions du workflow et actions autorisées
   ```text
   Repository > Settings > Actions > General; limiter les permissions de GITHUB_TOKEN et les actions tierces.
   ```
   👉 Explication : n’autoriser que les workflows nécessaires et épingler les actions tierces approuvées.

2. Créer un secret dans le périmètre minimal
   ```text
   Repository > Settings > Secrets and variables > Actions > New repository secret.
   Au niveau organisation, limiter les dépôts autorisés.
   ```
   👉 Explication : ne pas inclure la valeur dans YAML, issue, commit ou ticket.

3. Consommer le secret via un environnement de l’étape
   ```yaml
   steps:
     - name: Appel autorisé
       env:
         API_TOKEN: ${{ secrets.API_TOKEN }}
       run: ./scripts/deploiement-test.sh
   ```
   👉 Explication : remplacer nom du secret et script à remplacer; ne pas afficher l’environnement ou activer debug sensible.

4. Vérifier logs, forks et approbations d’environnement
   ```text
   Actions > exécution > vérifier logs, restrictions sur forks et approbations d’environnement.
   ```
   👉 Explication : le masquage automatique n’est pas une garantie contre toute fuite; éviter toute sortie du secret.

## 2. Production — Contrôles

Appliquer le compte/organisation approuvé, rôles minimaux, revue des accès et procédure de récupération.

## 3. Production — Sécurité

- Ne jamais coder un secret dans YAML, un commit, un artefact ou les logs.
- Ne pas exposer secrets aux workflows de forks non fiables.
- Préférer OIDC lorsque le fournisseur le permet.

## Validation et retour arrière

- **Validation** : Workflow de test utilise le secret sans le journaliser et aucun dépôt non autorisé ne peut y accéder.
- **Retour arrière** : Révoquer/remplacer tout secret exposé, nettoyer les artefacts et auditer les exécutions.

## Si le problème n'est pas résolu

- [GitHub Docs — compte](https://docs.github.com/account-and-profile/setting-up-and-managing-your-personal-account-on-github)
- [GitHub Docs — clés SSH](https://docs.github.com/authentication/connecting-to-github-with-ssh)
- [GitHub Docs — secrets Actions](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Fiche connexe](<Fiche_Simple_-_GitHub_Compte.md>)
