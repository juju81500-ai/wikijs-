# Administrer Git en client sur Debian 13

- **OS / Version** : Debian 13 Trixie amd64; paquet Git fourni par Debian
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : installation APT, configuration utilisateur, clone, revue, commit et push vers un dépôt autorisé
- **Catégorie** : gestion de versions / développement
- **Tags** : `git`, `debian13`, `gestion-versions`, `ssh`, `secrets`, `workflow`

## 1. Périmètre

Fiche simple : [cadrer le périmètre du client Git](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Perimetre.md).

Cette fiche installe et utilise le client Git Debian pour des dépôts auxquels l'utilisateur est autorisé à accéder. Elle ne déploie pas de forge, serveur Git, GitLab, GitHub, Gitea, CI/CD ou politique de gouvernance. Utiliser les consignes de branche, revue, signature et protection du dépôt définies par son propriétaire.

Git versionne les fichiers ajoutés aux commits; `.gitignore` n'empêche pas l'ajout explicite d'un secret et ne retire pas un fichier déjà commité de l'historique. Une clé ou un jeton publié dans un dépôt doit être considéré compromis : le révoquer/renouveler et suivre la procédure de l'organisation pour traiter l'historique.

## 2. Installer le client Git

Fiche simple : [installer le client Git](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Installer.md).

Installer Git et le client OpenSSH depuis les dépôts Debian approuvés :

```bash
sudo apt update
sudo apt install -y git openssh-client ca-certificates
git --version
apt-cache policy git
```

Consigner la version Candidate et la source du paquet. Préférer le paquet Debian aux scripts d'installation tiers ou aux compilations manuelles, sauf exigence de version et procédure d'approbation explicites.

## 3. Définir l'identité de commit

Fiche simple : [définir l'identité de commit Git](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Identite.md).

Configurer le nom et l'adresse autorisés pour cet utilisateur. L'adresse apparaît dans les métadonnées des commits; si le dépôt exige une adresse dédiée ou masquée, suivre cette politique :

```bash
git config --global user.name "Nom approuvé"
git config --global user.email "adresse-approuvee@example.invalid"
git config --global init.defaultBranch main
git config --global --show-origin --get-regexp '^user\.(name|email)$|^init\.defaultbranch$'
```

Remplacer les exemples avant usage. Pour des identités distinctes entre clients ou projets, configurer `user.name` et `user.email` au niveau local du dépôt (`git config --local`) plutôt que d'inscrire une identité erronée globalement. Ne pas mettre de secret dans la configuration Git ou dans l'URL distante.

## 4. Cloner et contrôler un dépôt autorisé

Fiche simple : [cloner et contrôler un dépôt Git](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Cloner.md).

Cloner uniquement l'URL validée par l'équipe ou le propriétaire du projet, en HTTPS avec certificat vérifié ou en SSH avec clé gérée par l'agent autorisé :

```bash
mkdir -p "$HOME/src"
cd "$HOME/src"
git clone <URL-du-depot-approuve>
cd <nom-du-depot>
git remote -v
git status --short --branch
```

Ne jamais inclure un mot de passe ou un token dans l'URL (`https://utilisateur:secret@...`), les arguments de commande, un script, le shell history ou un fichier de configuration versionné. Utiliser le flux d'authentification recommandé par le service, un gestionnaire de credentials approuvé ou `ssh-agent`. Pour SSH, vérifier l'empreinte de l'hôte par un canal officiel avant de l'accepter dans `known_hosts`; ne pas désactiver la validation de certificat ou de clé d'hôte.

Avant d'exécuter un script, une tâche, un hook ou une commande de construction provenant d'un dépôt récemment reçu, examiner les fichiers pertinents et leur provenance. Dans VS Code, conserver un dépôt inconnu en Restricted Mode jusqu'à revue; la confiance Git de propriété (`safe.directory`) et Workspace Trust sont des contrôles distincts.

## 5. Préparer un commit relu

Fiche simple : [préparer un commit Git relu](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Commit.md).

Créer une branche selon la convention du projet. Après modification, inspecter l'état et les changements, puis n'indexer que les chemins attendus :

```bash
git switch -c <branche-conforme-a-la-politique>
git status --short
git diff --check
git diff
git add <chemin-approuve>
git diff --cached --check
git diff --cached
```

Vérifier le diff indexé pour fichiers inattendus, données personnelles, clés, tokens, certificats privés, exports, fichiers de sauvegarde et artefacts générés. Les secrets ne deviennent pas sûrs parce qu'ils sont ajoutés à `.gitignore`. Exécuter les tests autorisés du projet, puis créer un commit au message explicite :

```bash
git commit -m "Décrire le changement"
git status --short --branch
git log -1 --show-signature
```

Les signatures de commits sont utiles si le projet les exige et si l'identité de signature est configurée et vérifiable. Une signature confirme une clé; elle ne remplace ni la revue du contenu ni les contrôles de dépôt.

## 6. Synchroniser sans écraser le travail distant

Fiche simple : [synchroniser Git sans écraser le travail distant](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Synchroniser.md).

Vérifier la branche et le remote avant toute synchronisation. Récupérer d'abord les nouveautés, examiner l'état divergent, puis utiliser le mode d'intégration prescrit par le projet :

```bash
git status --short --branch
git remote -v
git fetch origin
git log --oneline --graph --decorate --left-right HEAD...@{upstream}
```

Utiliser ensuite `git pull --ff-only` si une avance rapide suffit ou la méthode documentée (merge/rebase) si les branches ont divergé. En cas de conflit, examiner les marqueurs et résoudre chaque fichier, puis lancer les tests. Ne pas employer `push --force`, `reset --hard` ou des suppressions massives comme raccourci; faire valider les opérations qui réécrivent l'historique ou écrasent le remote.

Après validation et selon la procédure de revue du projet, pousser uniquement la branche de travail :

```bash
git push --set-upstream origin <branche-conforme-a-la-politique>
```

Ne pas pousser directement sur une branche protégée ou de production si le workflow exige une revue par merge/pull request.

## 7. Maintenance et vérifications

Fiche simple : [maintenir et vérifier le client Git](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/Git/Fiche_Simple_-_VM_Debian_13_Git_Maintenance.md).

- Maintenir Git à jour via APT et vérifier `git --version` après les mises à jour.
- Inventorier les remotes et les configurations non usuelles avec `git remote -v` et `git config --show-origin --list`; vérifier qu'aucune donnée d'authentification n'y figure.
- Vérifier régulièrement `git status --short --branch`, les clés/permissions de `known_hosts`, la disponibilité du gestionnaire de credentials et la procédure de révocation.
- Sauvegarder le travail non poussé et les dépôts locaux selon la politique de conservation; un commit local n'est pas une sauvegarde indépendante.

## Sources

- [Git — installer Git, Linux/Debian](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration et portées](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — gestion des credentials](https://git-scm.com/docs/gitcredentials)
- [Git — signature du travail et vérification](https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work)
- [Git — format de l'URL et credentials en clair](https://git-scm.com/docs/git-config#Documentation/git-config.txt-transfercredentialsInUrl)

La configuration SSH, l'authentification sur un service hébergé et les commandes de commit/push ne sont pas exécutées ni validées par cette fiche. Tester avec un dépôt non sensible et autorisé avant tout usage de production.