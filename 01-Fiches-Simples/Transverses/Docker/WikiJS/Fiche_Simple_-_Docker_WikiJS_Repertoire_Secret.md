# Fiche_Simple_-_Docker_WikiJS_Repertoire_Secret.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation
- **Tags** : `wikijs`, `docker`, `compose`, `postgresql`, `traefik`, `tls`

---

## Problème précis à résoudre

Créer le répertoire de la stack et un secret de base de données hors de tout dépôt.

## 1. Hors-Production (Lab / Test / POC)

1. Créer les répertoires avec des droits restreints :
   ```bash
   sudo install -d -m 0750 /opt/docker/wikijs
   sudo install -d -m 0700 /opt/docker/wikijs/secrets
   ```
   👉 Explication : le répertoire des secrets n'est accessible qu'à root.

2. Générer le mot de passe de la base dans un fichier, sans l'afficher :
   ```bash
   cd /opt/docker/wikijs
   sudo sh -c 'umask 077; openssl rand -base64 36 > secrets/db_password'
   sudo chmod 0444 secrets/db_password
   ```
   👉 Explication : le secret n'apparaît ni en argument ni dans l'historique; le mode 0444 permet au processus non-root du conteneur de lire le fichier monté, le répertoire parent restant protégé.

3. Contrôler les droits obtenus :
   ```bash
   sudo ls -ld /opt/docker/wikijs /opt/docker/wikijs/secrets
   sudo ls -l /opt/docker/wikijs/secrets
   ```
   👉 Explication : vérifier les modes 0750, 0700 et 0444.

## 2. Production — Contrôles

En environnement multi-hôte, préférer le gestionnaire de secrets de la plateforme.

## 3. Production — Sécurité

- Ne jamais copier `db_password` dans un dépôt Git ni dans un ticket.
- Inclure ce secret dans le coffre de sauvegarde approprié.

## Validation et retour arrière

- **Validation** : Le fichier `secrets/db_password` existe, n'est pas vide et le répertoire parent reste en 0700.
- **Retour arrière** : Supprimer `/opt/docker/wikijs` tant que la base n'a pas été créée (`sudo rm -r /opt/docker/wikijs` après vérification du chemin).

## Si le problème n'est pas résolu

- [Docker — Compose secrets](https://docs.docker.com/compose/how-tos/use-secrets/)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/28_Installation_WikiJS_Docker_PostgreSQL_Traefik.md#2-creer-le-repertoire-et-le-secret)
