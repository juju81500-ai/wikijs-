---
title: "Fiche Simple - VM Debian 13 Git Valider Clone Commit"
description: "Vérifier le client Git, l'identité de commit et le parcours clone, revue, commit et push sans exposer de secrets ni écraser une branche distante."
published: true
date: 2026-10-29T20:22:42Z
tags: ["debian13", "git", "validation", "ssh", "secrets", "workflow"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Debian_13_Git_Valider_Clone_Commit.md

- **Environnement** : Git depuis APT Debian 13, dépôt de test autorisé
- **OS / Version** : Debian 13 Trixie amd64
- **Catégorie** : gestion de versions / développement
- **Tags** : `debian13`, `git`, `validation`, `ssh`, `secrets`, `workflow`

---

## Problème précis à résoudre

Vérifier le client Git, l'identité de commit et le parcours clone, revue, commit et push sans exposer de secrets ni écraser une branche distante.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer installation et provenance :
   ```bash
   git --version
   apt-cache policy git
   ```
   👉 Explication : la version provient des dépôts Debian configurés.

2. Afficher l'identité de commit et la corriger si besoin :
   ```bash
   git config --show-origin --get-regexp '^user\.(name|email)$'
   git config --global user.name "Prénom Nom"
   git config --global user.email "prenom.nom@example.net"
   ```
   👉 Explication : remplacer les valeurs; à faire avant le premier commit.

3. Cloner un dépôt de test approuvé et contrôler :
   ```bash
   git clone https://git.example.net/lab/depot-test.git
   cd depot-test
   git remote -v
   git status --short --branch
   ```
   👉 Explication : remplacer l'URL; aucun jeton dans l'URL (utiliser clé SSH ou gestionnaire d'identifiants).

4. Créer une branche, modifier un fichier fictif et relire :
   ```bash
   git switch -c test/validation
   echo "test" >> FICHIER_TEST.txt
   git diff
   git add FICHIER_TEST.txt
   git diff --cached
   ```
   👉 Explication : relire le diff avant chaque commit.

5. Commiter, récupérer, puis pousser seulement si autorisé :
   ```bash
   git commit -m "Test de validation"
   git fetch origin
   git push -u origin test/validation
   ```
   👉 Explication : jamais de `--force`; pousser uniquement une branche de test autorisée.

## 2. Production — Contrôles

Consigner l'URL distante approuvée, la branche autorisée, la stratégie de merge/rebase, les contrôles de revue, la politique de signature et le gestionnaire de credentials permis.

## 3. Production — Sécurité

- Ne pas mettre de tokens ou mots de passe dans une URL, une commande, `.git/config`, un script ou l'historique du shell.
- Vérifier l'empreinte SSH de l'hôte par une source officielle; ne pas désactiver les contrôles TLS/SSH.
- Inspecter le diff indexé pour détecter secrets, données personnelles, exports et artefacts avant chaque commit.
- Garder les dépôts inconnus en Restricted Mode dans VS Code; examiner tâches, scripts et configurations avant exécution.
- Éviter les pushes forcés et les commits directs sur les branches protégées.

## Validation et retour arrière

- **Validation** : remote attendu, branche de travail correcte, diff relu, commit local identifiable, push vers un dépôt de test autorisé.
- **Retour arrière** : conserver la copie locale et le commit précédent; annuler par une opération Git revue, pas par une réécriture forcée de branche partagée.

## Si le problème n'est pas résolu

- [Git — documentation officielle](https://git-scm.com/docs)
- [Git — travailler avec des remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Guide complet Git client sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/82-administration-git-client-debian-13)