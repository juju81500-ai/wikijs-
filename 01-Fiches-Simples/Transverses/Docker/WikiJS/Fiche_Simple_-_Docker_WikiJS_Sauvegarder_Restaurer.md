# Fiche_Simple_-_Docker_WikiJS_Sauvegarder_Restaurer.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation
- **Tags** : `wikijs`, `docker`, `compose`, `postgresql`, `traefik`, `tls`

---

## Problème précis à résoudre

Sauvegarder la base Wiki.js et préparer une restauration testée.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire de sauvegarde protégé :
   ```bash
   sudo install -d -m 0700 /var/backups/wikijs
   ```
   👉 Explication : seul root peut lire les dumps.

2. Exporter la base PostgreSQL au format custom :
   ```bash
   sudo sh -c 'cd /opt/docker/wikijs && docker compose exec -T db pg_dump -U wikijs -d wiki -Fc > "/var/backups/wikijs/wiki-$(date +%F-%H%M).dump"'
   ```
   👉 Explication : le dump est horodaté; le mot de passe n'est pas passé en argument.

3. Vérifier que le dump est lisible :
   ```bash
   sudo ls -lh /var/backups/wikijs
   sudo pg_restore --list "$(sudo ls -t /var/backups/wikijs/*.dump | head -n 1)" | head
   ```
   👉 Explication : si `pg_restore` n'est pas installé sur l'hôte, exécuter la commande dans le conteneur `db`; la liste doit afficher des objets de la base.

4. Inclure aussi la cible de stockage réelle des fichiers (module de stockage Wiki.js activé) et le secret `secrets/db_password` dans le plan de sauvegarde.
   👉 Explication : un dump SQL seul peut ne pas contenir les pièces jointes; un volume Docker seul n'est pas une sauvegarde.

## 2. Production — Contrôles

Chiffrer et copier les dumps hors de l'hôte, définir une rétention et tester régulièrement une restauration sur une stack isolée.

## 3. Production — Sécurité

- Dumps et secrets en 0700/0600, copie hors hôte chiffrée.
- Ne jamais restaurer sur la base de production sans sauvegarde préalable.

## Validation et retour arrière

- **Validation** : Un dump récent existe, est listable et une restauration de test a réussi sur une stack isolée.
- **Retour arrière** : Supprimer uniquement le dump défectueux et en refaire un nouveau; la production n'est pas modifiée.

## Si le problème n'est pas résolu

- [PostgreSQL — pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)
- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/28_Installation_WikiJS_Docker_PostgreSQL_Traefik.md#6-sauvegarder-et-restaurer)
