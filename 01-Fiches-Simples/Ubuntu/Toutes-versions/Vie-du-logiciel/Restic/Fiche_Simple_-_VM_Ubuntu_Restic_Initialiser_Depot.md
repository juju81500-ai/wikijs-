# Fiche_Simple_-_VM_Ubuntu_Restic_Initialiser_Depot.md

- **Environnement** : VM Ubuntu Server avec destination de sauvegarde indépendante
- **OS / Version** : Ubuntu Server (toutes versions supportées); paquet restic des dépôts Ubuntu
- **Catégorie** : sauvegarde / restauration
- **Tags** : `ubuntu`, `restic`, `sauvegarde`, `restauration`, `retention`

---

## Problème précis à résoudre

Créer le dépôt Restic une seule fois.

## 1. Hors-Production (Lab / Test / POC)

1. En session root, définir le dépôt et le fichier de mot de passe (le chemin du dépôt est un exemple à remplacer) :
   ```bash
   export RESTIC_REPOSITORY=/mnt/backup/restic-ubuntu
   export RESTIC_PASSWORD_FILE=/root/.config/restic/password
   ```
   👉 Explication : les variables évitent de saisir le secret en argument.

2. Initialiser puis lister les snapshots :
   ```bash
   restic init
   restic snapshots
   ```
   👉 Explication : `init` crée le dépôt chiffré; `snapshots` doit s'exécuter sans erreur et être vide au départ.

## 2. Production — Contrôles

Pour SFTP ou stockage objet, suivre la documentation Restic du backend choisi et isoler ses identifiants du mot de passe du dépôt.

## 3. Production — Sécurité

- N'exécuter `restic init` qu'une seule fois sur un dépôt neuf.

## Validation et retour arrière

- **Validation** : Le dépôt est initialisé et accessible.
- **Retour arrière** : Supprimer le dépôt neuf seulement s'il est vide et mal créé (`rm -r` du chemin vérifié).

## Si le problème n'est pas résolu

- [Restic — Documentation officielle](https://restic.readthedocs.io/en/stable/)
- [Ubuntu — Documentation serveur](https://documentation.ubuntu.com/server/)
- [Guide complet sauvegarde Ubuntu Server Restic](../../../../../02-Fiches-Completes/Ubuntu/Toutes-versions/Autres/29_Sauvegarde_Restauration_Ubuntu_Server_Restic.md#3-initialiser-le-depot)
