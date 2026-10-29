---
title: "Docker_Conteneur_Cloud_Deploiement-Nextcloud"
description: "Déployer la plateforme de cloud privé Nextcloud en conteneurs Docker avec base de données MariaDB et cache mémoire Redis pour les performances de verrouillage de fichiers, configurer les volumes de persistance et sécuriser l'instance."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[docker]", "[nextcloud]", "[mariadb]", "[redis]", "[cloud-prive]", "[docker-compose]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Docker_Conteneur_Cloud_Deploiement-Nextcloud.md

- **Environnement** : Docker (Hôte Debian / Ubuntu)
- **OS / Version** : Docker Engine 24+ / Compose v2
- **Catégorie** : Cloud Privé & Stockage / Nextcloud
- **Tags** : `[docker]`, `[nextcloud]`, `[mariadb]`, `[redis]`, `[cloud-prive]`, `[docker-compose]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer la plateforme de cloud privé Nextcloud en conteneurs Docker avec base de données MariaDB et cache mémoire Redis pour les performances de verrouillage de fichiers, configurer les volumes de persistance et sécuriser l'instance.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lancement d'un conteneur Nextcloud autonome avec base SQLite :
   `docker run -d --name nextcloud-test -p 127.0.0.1:8080:80 -v nextcloud_test:/var/www/html nextcloud:<VERSION_VALIDEE>-apache`
   👉 Explication : Démarre une instance Nextcloud temporaire accessible sur le port 8080 pour des tests d'interface.

2. Nettoyage du conteneur de test :
   `docker stop nextcloud-test && docker rm nextcloud-test`
   👉 Explication : Supprime l'instance de test après validation.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du dossier d'installation et de la structure des volumes :
   `mkdir -p /opt/nextcloud/{app,db,data} && cd /opt/nextcloud`
   👉 Explication : Isole les données utilisateurs, le code de l'application et la base de données MariaDB.

2. Rédaction du fichier `docker-compose.yml` complet avec MariaDB et Redis :
   ```yaml
   services:
     db:
          image: mariadb:<VERSION_MAJEURE_VALIDEE>
       container_name: nextcloud-db
       command: --transaction-isolation=READ-COMMITTED --log-bin=binlog --binlog-format=ROW
       restart: always
       volumes:
         - ./db:/var/lib/mysql
          environment:
             MYSQL_DATABASE: nextcloud
             MYSQL_USER: nextcloud
             MYSQL_PASSWORD_FILE: /run/secrets/db_password
             MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_root_password
          secrets:
             - db_password
             - db_root_password

     redis:
      image: redis:<VERSION_VALIDEE>
       container_name: nextcloud-redis
       restart: always

     app:
      image: nextcloud:<VERSION_VALIDEE>-apache
       container_name: nextcloud-app
       restart: always
          depends_on:
             - db
             - redis
       volumes:
         - ./app:/var/www/html
         - ./data:/var/www/html/data
       environment:
             MYSQL_HOST: db
             MYSQL_DATABASE: nextcloud
             MYSQL_USER: nextcloud
             MYSQL_PASSWORD_FILE: /run/secrets/db_password
             REDIS_HOST: redis
             NEXTCLOUD_TRUSTED_DOMAINS: cloud.example.net
          ports:
             - "127.0.0.1:8080:80"
          secrets:
             - db_password

       cron:
          image: nextcloud:<VERSION_VALIDEE>-apache
          restart: unless-stopped
          entrypoint: /cron.sh
          depends_on:
             - app
          volumes:
             - ./app:/var/www/html
             - ./data:/var/www/html/data

    secrets:
       db_password:
          file: ./secrets/db_password
       db_root_password:
          file: ./secrets/db_root_password
   ```
   👉 Explication : Déploie l'architecture multi-conteneurs Nextcloud recommandée avec base MariaDB et cache Redis.

3. Démarrage de la stack :
   `docker compose up -d`
   👉 Explication : Lance l'ensemble des conteneurs interconnectés en arrière-plan.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Ajouter `cloud.example.net` au proxy TLS et à la liste des domaines de confiance, puis vérifier la configuration effective :
   `docker compose exec -u www-data app php occ config:system:get trusted_domains`
   👉 Explication : Restreint l'accès HTTP uniquement au nom de domaine officiel FQDN pour parer le détournement d'en-tête HTTP Host.

2. Configurer APCu pour le cache local et Redis pour le verrouillage transactionnel après vérification de leur disponibilité :
   ```bash
   docker compose exec -u www-data app php occ config:system:set memcache.local --value='\\OC\\Memcache\\APCu'
   docker compose exec -u www-data app php occ config:system:set memcache.locking --value='\\OC\\Memcache\\Redis'
   docker compose exec -u www-data app php occ config:system:set redis host --value=redis
   ```
   👉 Explication : Évite les conflits d'accès simultanés aux fichiers et accélère le chargement de l'interface Web.

3. Le service `cron` défini dans Compose exécute `/cron.sh`, qui lance les tâches Nextcloud. Vérifier le journal et l'état de cette tâche ; ne pas utiliser `occ status` comme tâche cron.

4. Créer les fichiers de secrets sous `/opt/nextcloud/secrets`, hors du dépôt, accessibles seulement à l'administrateur (`chmod 600`). Vérifier que les volumes ont les UID/GID attendus par l'image ; éviter un `chmod -R` sur les données existantes.

5. Valider les fichiers de secrets, la configuration et le démarrage avant exposition : `docker compose config --quiet`, `docker compose ps`, `docker compose logs --tail 100 app db redis cron`. Sauvegarder ensemble la base et les données, puis tester une restauration.