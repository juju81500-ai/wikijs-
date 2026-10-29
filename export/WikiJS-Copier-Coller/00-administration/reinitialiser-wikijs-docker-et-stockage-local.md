# Réinitialiser Wiki.js sous Docker et configurer le stockage local

- **Portée** : Wiki.js 2.5.317 dans Docker Compose avec PostgreSQL
- **Effet** : supprime toutes les pages, tous les comptes Wiki.js, les paramètres et le contenu de la base `wiki`
- **Volumes Docker** : conservés; cette procédure ne supprime pas les volumes
- **Attention** : ne poursuivre qu'après avoir vérifié une sauvegarde restaurable

## Important : stockage local et import sont différents

Le module **Local File System** de Wiki.js conserve une copie des pages créées dans Wiki.js. Copier des fichiers `.md` dans un dossier du conteneur ne les crée pas dans la base. Après une réinitialisation, il faudra créer ou importer à nouveau les pages, puis configurer le stockage local pour conserver leur copie.

Ne monte pas le dossier du pack sur `/wiki/data` : ce chemin contient les données persistantes de l'application.

## 1. Vérifier les noms du déploiement

Les commandes ci-dessous correspondent au Compose de la fiche Wiki.js du pack : service PostgreSQL `db`, rôle `wikijs`, base `wiki` et service applicatif `wiki`. Vérifier ces valeurs dans le `docker-compose.yml` réel avant de continuer.

```bash
cd /opt/docker/wikijs
sudo docker compose ps
sudo docker compose exec -T db psql -U wikijs -d postgres -c '\l'
```

Ne pas continuer si le service, le rôle ou le nom de base sont différents sans adapter toutes les commandes suivantes.

## 2. Sauvegarder la base

La sauvegarde doit être créée avant la suppression et conservée hors du conteneur. Si possible, en copier ensuite une seconde version vers un autre support.

```bash
set -o pipefail
sudo install -d -m 0700 /var/backups/wikijs
BACKUP="/var/backups/wikijs/wiki-pre-reset-$(date +%Y%m%d-%H%M%S).dump"
sudo docker compose exec -T db pg_dump -U wikijs -d wiki -Fc | sudo tee "$BACKUP" >/dev/null
sudo test -s "$BACKUP"
printf 'Sauvegarde créée : %s\n' "$BACKUP"
```

Si une commande échoue ou si le fichier est vide, arrêter ici. Ne pas supprimer la base avant d'avoir vérifié la sauvegarde et sa copie externe.

## 3. Arrêter Wiki.js et recréer uniquement la base

Cette opération est destructive et ne peut pas être annulée sans restaurer la sauvegarde. Elle supprime toutes les pages, les utilisateurs, les paramètres et les données applicatives de Wiki.js.

```bash
sudo docker compose stop wiki
sudo docker compose exec -T db psql -U wikijs -d postgres -c 'DROP DATABASE wiki WITH (FORCE);'
sudo docker compose exec -T db psql -U wikijs -d postgres -c 'CREATE DATABASE wiki OWNER wikijs;'
sudo docker compose start wiki
sudo docker compose logs --tail=100 wiki
```

Wiki.js initialise son schéma au démarrage. Refaire l'assistant d'installation et recréer le compte administrateur. Les conteneurs et volumes PostgreSQL et Wiki.js ne sont pas supprimés.

**Ne pas utiliser** `docker compose down -v`, `docker volume prune` ni `docker system prune --volumes` pour cette opération.

## 4. Activer le stockage local

Dans l'interface d'administration de Wiki.js :

1. Ouvrir **Administration > Storage**.
2. Activer **Local File System**.
3. Choisir un chemin accessible en écriture au processus Wiki.js et situé sur un volume persistant dédié; ne pas remplacer `/wiki/data` avec le dossier du pack.
4. Appliquer les changements et vérifier l'état du module.
5. Créer ou importer les pages dans Wiki.js. Le stockage local conservera ensuite leur copie selon les réglages du module.

Le module de stockage local n'est pas le mécanisme de création/import des pages. Pour créer les 650 pages en lot, utiliser le dépôt dédié avec **Storage > Git > Import Everything**. Pour le collage manuel, utiliser les fichiers sans front matter du dossier `WikiJS-Copier-Coller` et le manifeste CSV.

## Restaurer la sauvegarde

Ne restaurer qu'en cas de besoin, sur la base de destination voulue. Adapter le chemin au nom exact du fichier créé à l'étape 2.

```bash
sudo docker compose stop wiki
sudo docker compose exec -T db dropdb -U wikijs --if-exists wiki
sudo docker compose exec -T db createdb -U wikijs -O wikijs wiki
sudo sh -c 'docker compose exec -T db pg_restore -U wikijs -d wiki --clean --if-exists < /var/backups/wikijs/NOM_DU_FICHIER.dump'
sudo docker compose start wiki
```

## Références du pack

- Déploiement Docker : `02-Fiches-Completes/Docker/Installation-Deploiement/28_Installation_WikiJS_Docker_PostgreSQL_Traefik.md`
- Import par SSH : `00-Administration/Guide_Import_WikiJS_2.5.317_Par_SSH_Docker.md`
- Import manuel : `WikiJS-Copier-Coller/IMPORT-MANIFEST.csv`