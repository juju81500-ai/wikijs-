# Fiche_Simple_-_VM_Debian_13_Git_Synchroniser.md

- **Environnement** : Poste Debian 13, client Git
- **OS / Version** : Debian 13 Trixie amd64; paquet Git Debian
- **Catégorie** : gestion de versions / synchronisation
- **Tags** : `debian13`, `git`, `fetch`, `pull`, `push`

---

## Problème précis à résoudre

Récupérer, intégrer puis pousser sans écraser l'historique distant.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler branche et remote puis récupérer les nouveautés :
   ```bash
   git status --short --branch
   git remote -v
   git fetch origin
   ```
   👉 Explication : `fetch` ne modifie pas le travail local.

2. Examiner la divergence :
   ```bash
   git log --oneline --graph --decorate --left-right HEAD...@{upstream}
   ```
   👉 Explication : on voit les commits locaux et distants.

3. Intégrer en avance rapide si possible :
   ```bash
   git pull --ff-only
   ```
   👉 Explication : si cela échoue, utiliser la méthode du projet (merge ou rebase) et résoudre les conflits fichier par fichier, puis tester.

4. Pousser la branche de travail (nom d'exemple à remplacer) :
   ```bash
   git push --set-upstream origin fonctionnalite/exemple
   ```
   👉 Explication : on publie uniquement la branche de travail, pour revue.

## 2. Production — Contrôles

Pas de push direct sur une branche protégée ou de production si le workflow impose une revue.

## 3. Production — Sécurité

- Pas de `push --force`, `reset --hard` ou suppression massive sans validation.

## Validation et retour arrière

- **Validation** : la branche distante contient les commits attendus.
- **Retour arrière** : demander la suppression de la branche distante via la procédure du projet; ne pas réécrire l'historique partagé.

## Si le problème n'est pas résolu

- [Git — installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — credentials](https://git-scm.com/docs/gitcredentials)
- [Guide complet — étape 6](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/82_Administration_Git_Client_Debian_13.md#6-synchroniser-sans-ecraser-le-travail-distant)
