# Sauvegarder et restaurer une stack Docker Compose

- **Type de fiche** : Autres — sauvegarde / reprise
- **Environnement** : Hôte Linux Docker avec stacks Compose et volumes persistants
- **OS / Version** : Distribution maintenue, Docker Engine et Compose v2
- **Rôle** : Sauvegarder les configurations et données applicatives de façon cohérente, puis tester la restauration
- **Tags** : `docker`, `compose`, `sauvegarde`, `restauration`, `volumes`, `production`

## 1. Inventorier la stack

Fiche simple : [inventorier la stack](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Inventorier.md).

Pour chaque projet, relever fichiers Compose, fichiers `.env`, secrets, images et versions, réseaux, ports, bind mounts, volumes nommés, bases, dépendances externes et ordre de démarrage. Protéger l'inventaire : les fichiers de configuration peuvent contenir des secrets.

```bash
docker compose config --quiet
docker compose ps
docker volume ls
docker inspect <NOM_CONTENEUR>
```

Ne pas partager la sortie complète de `docker compose config` : l'interpolation peut révéler des valeurs sensibles.

## 2. Définir la méthode de cohérence

Fiche simple : [définir la méthode de cohérence](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Coherence.md).

- **Bases de données** : créer un dump logique avec l'outil de la base; le snapshot brut d'un volume actif n'est pas nécessairement cohérent.
- **Fichiers applicatifs** : activer le mode maintenance ou arrêter les écritures avant copie.
- **Stacks à plusieurs services** : synchroniser la sauvegarde de la base, des fichiers, de la configuration et des secrets nécessaires.
- **Destination** : écrire vers un stockage séparé de l'hôte, chiffré et protégé contre l'effacement/rançongiciel.

## 3. Sauvegarder une base PostgreSQL

Fiche simple : [sauvegarder une base PostgreSQL](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Dump_PostgreSQL.md).

Exemple pour un service Compose `db` et une base `wikijs`. Adapter le service, le compte et la base; exécuter avec un répertoire de sauvegarde protégé :

```bash
sudo install -d -m 0700 /var/backups/docker/mon-projet
sudo sh -c 'cd /opt/docker/mon-projet && docker compose exec -T db pg_dump -U wikijs -d wiki -Fc > /var/backups/docker/mon-projet/wiki.dump'
```

Vérifier le code retour, la taille et la lisibilité du dump (`pg_restore --list`). Pour MariaDB/MySQL, employer `mariadb-dump`/`mysqldump` avec les options de cohérence et l'authentification sécurisée adaptées.

## 4. Sauvegarder volumes et configuration

Fiche simple : [sauvegarder volumes et configuration](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Volumes_Config.md).

Dans les exemples, remplacer chaque valeur `<...>` par le nom réel du service, volume ou chemin avant exécution; ne pas saisir les chevrons comme faisant partie de la commande.

Arrêter les services qui écrivent dans les volumes, sans supprimer les volumes :

```bash
cd /opt/docker/mon-projet
docker compose stop
docker volume inspect <VOLUME_DOCKER>
```

Exemple d'archive d'un volume nommé vers un répertoire de sauvegarde déjà monté :

```bash
sudo install -d -m 0700 /mnt/backup/mon-projet
sudo docker run --rm \
  --mount type=volume,src=<VOLUME_DOCKER>,dst=/source,readonly \
  --mount type=bind,src=/mnt/backup/mon-projet,dst=/backup \
  ubuntu:24.04 tar --numeric-owner -cpf /backup/<VOLUME_DOCKER>.tar -C /source .
```

Pour un bind mount, sauvegarder le chemin hôte correspondant avec l'outil retenu. Copier Compose, fichiers d'environnement et définitions de secrets dans une archive chiffrée, avec des permissions strictes. Redémarrer ensuite les services et vérifier la santé applicative.

## 5. Vérifier la sauvegarde

Fiche simple : [vérifier la sauvegarde](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Verifier_Sauvegarde.md).

- Comparer les tailles, journaux et sommes de contrôle; tester l'archive et l'inventaire du dump.
- Chiffrer avant transfert externe et séparer les clés des archives.
- Appliquer une rétention documentée et surveiller les échecs.
- Programmer un exercice de restauration sur une stack isolée, sans DNS ni données réelles.

## 6. Restaurer sur un environnement isolé

Fiche simple : [restaurer sur un environnement isolé](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Restaurer.md).

1. Installer une version compatible de Docker/Compose et récupérer les fichiers de stack et secrets depuis le coffre.
2. Créer des volumes vides sous les identifiants attendus; ne jamais extraire par-dessus un volume de production actif.
3. Restaurer les données des volumes. Exemple après vérification de la cible :

```bash
sudo docker volume create <VOLUME_DOCKER>
sudo docker run --rm \
  --mount type=volume,src=<VOLUME_DOCKER>,dst=/restore \
  --mount type=bind,src=/mnt/backup/mon-projet,dst=/backup,readonly \
  ubuntu:24.04 tar --numeric-owner -xpf /backup/<VOLUME_DOCKER>.tar -C /restore
```

4. Démarrer d'abord la base, restaurer le dump sur une base cible vide, puis démarrer l'application.
5. Valider comptes, données, permissions, fichiers, accès réseau et journaux avant tout retour en production.

## 7. Reprise et prévention des pertes

Fiche simple : [reprise et prévention des pertes](../../../../01-Fiches-Simples/Transverses/Docker/Sauvegarde-restauration/Fiche_Simple_-_Hote_Docker_Stack_Reprise.md).

Ne jamais utiliser `docker compose down -v`, `docker volume prune` ou `docker system prune --volumes` comme étape de sauvegarde ou de diagnostic. Ces commandes peuvent supprimer définitivement les données.

Consigner la version des images, le point de restauration, les écarts, le temps de reprise et les résultats métier. En cas de chiffrement ou corruption, isoler l'hôte et préserver les volumes avant toute tentative de nettoyage.

## Sources

- [Docker — Volumes et sauvegarde/restauration](https://docs.docker.com/engine/storage/volumes/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Docker — Secrets Compose](https://docs.docker.com/compose/how-tos/use-secrets/)