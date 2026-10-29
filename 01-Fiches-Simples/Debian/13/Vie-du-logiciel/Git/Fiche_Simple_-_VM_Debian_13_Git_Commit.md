# Fiche_Simple_-_VM_Debian_13_Git_Commit.md

- **Environnement** : Poste Debian 13, client Git
- **OS / Version** : Debian 13 Trixie amd64; paquet Git Debian
- **Catégorie** : gestion de versions / commit
- **Tags** : `debian13`, `git`, `commit`, `diff`, `revue`

---

## Problème précis à résoudre

Préparer et relire un commit sans fichier ou secret inattendu.

## 1. Hors-Production (Lab / Test / POC)

1. Créer une branche (nom d'exemple à remplacer, selon la convention du projet) :
   ```bash
   git switch -c fonctionnalite/exemple
   ```
   👉 Explication : la branche isole le travail.

2. Inspecter les changements :
   ```bash
   git status --short
   git diff --check
   git diff
   ```
   👉 Explication : on repère erreurs d'espaces et modifications inattendues.

3. Indexer uniquement les chemins attendus puis relire l'index (chemin d'exemple à remplacer) :
   ```bash
   git add docs/exemple.md
   git diff --cached --check
   git diff --cached
   ```
   👉 Explication : on vérifie l'absence de clés, jetons, certificats privés, exports ou sauvegardes.

4. Créer le commit et le contrôler :
   ```bash
   git commit -m "Décrire le changement"
   git status --short --branch
   git log -1 --show-signature
   ```
   👉 Explication : le message doit être explicite; la signature n'est utile que si le projet l'exige.

## 2. Production — Contrôles

Exécuter les tests autorisés du projet avant le commit.

## 3. Production — Sécurité

- Un secret ajouté à `.gitignore` n'est pas pour autant protégé.

## Validation et retour arrière

- **Validation** : `git log -1` montre le commit attendu.
- **Retour arrière** : avant push : `git reset --soft HEAD~1` annule le commit en gardant les changements.

## Si le problème n'est pas résolu

- [Git — installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — credentials](https://git-scm.com/docs/gitcredentials)
- [Guide complet — étape 5](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/82_Administration_Git_Client_Debian_13.md#5-preparer-un-commit-relu)
