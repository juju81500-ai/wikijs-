# Fiche_Simple_-_VM_Debian_13_Git_Cloner.md

- **Environnement** : Poste Debian 13, client Git
- **OS / Version** : Debian 13 Trixie amd64; paquet Git Debian
- **Catégorie** : gestion de versions / clonage
- **Tags** : `debian13`, `git`, `clone`, `ssh`, `https`

---

## Problème précis à résoudre

Cloner un dépôt autorisé sans exposer d'identifiants.

## 1. Hors-Production (Lab / Test / POC)

1. Cloner l'URL validée (URL d'exemple à remplacer) :
   ```bash
   mkdir -p "$HOME/src"
   cd "$HOME/src"
   git clone https://git.example.invalid/equipe/projet.git
   cd projet
   ```
   👉 Explication : HTTPS avec certificat vérifié ou SSH avec clé gérée par l'agent; `projet` est le nom d'exemple du dépôt.

2. Contrôler le remote et l'état :
   ```bash
   git remote -v
   git status --short --branch
   ```
   👉 Explication : on confirme l'URL et la branche, sans mot de passe visible.

3. Pour SSH, vérifier l'empreinte de l'hôte par un canal officiel avant de l'accepter :
   ```bash
   ssh-keyscan -t ed25519 git.example.invalid | ssh-keygen -lf -
   ```
   👉 Explication : on compare l'empreinte affichée avec celle publiée par le service avant de l'accepter.

4. Relire scripts, hooks et tâches du dépôt avant de les exécuter; dans VS Code garder le **Restricted Mode**.
   👉 Explication : un dépôt reçu peut contenir du code non prévu.

## 2. Production — Contrôles

Gestionnaire de credentials approuvé ou `ssh-agent`.

## 3. Production — Sécurité

- Jamais de mot de passe ou jeton dans l'URL, l'historique ou un script.
- Ne pas désactiver la validation de certificat ou de clé d'hôte.

## Validation et retour arrière

- **Validation** : `git status` indique la branche attendue et `git remote -v` l'URL approuvée.
- **Retour arrière** : supprimer le dossier cloné : `rm -r "$HOME/src/projet"` (sans travail non poussé).

## Si le problème n'est pas résolu

- [Git — installer Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Git — configuration](https://git-scm.com/docs/git-config)
- [Git — remotes, fetch, pull et push](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [Git — credentials](https://git-scm.com/docs/gitcredentials)
- [Guide complet — étape 4](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/82_Administration_Git_Client_Debian_13.md#4-cloner-et-controler-un-depot-autorise)
