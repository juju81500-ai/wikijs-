# Fiche_Simple_-_Docker_WikiJS_Definir_Stack_Compose.md

- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Catégorie** : conteneurs / documentation

---

## Problème précis à résoudre

Écrire le fichier Compose Wiki.js + PostgreSQL derrière Traefik sans publier de port.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le fichier Compose (remplacer `wiki.example.net`, `websecure`, `letsencrypt` et `traefik_proxy` par les noms définis dans Traefik) :
   ```bash
   cd /opt/docker/wikijs
   sudo tee docker-compose.yml >/dev/null <<'EOF'
   services:
     db:
       image: postgres:17-alpine
       restart: unless-stopped
       environment:
         POSTGRES_DB: wiki
         POSTGRES_USER: wikijs
         POSTGRES_PASSWORD_FILE: /run/secrets/db_password
       secrets:
         - db_password
       volumes:
         - db_data:/var/lib/postgresql/data
       networks:
         - backend
       healthcheck:
         test: ["CMD-SHELL", "pg_isready -U wikijs -d wiki"]
         interval: 10s
         timeout: 5s
         retries: 5
         start_period: 20s

     wiki:
       image: ghcr.io/requarks/wiki:2
       init: true
       restart: unless-stopped
       depends_on:
         db:
           condition: service_healthy
       environment:
         DB_TYPE: postgres
         DB_HOST: db
         DB_PORT: 5432
         DB_USER: wikijs
         DB_PASS_FILE: /run/secrets/db_password
         DB_NAME: wiki
       secrets:
         - db_password
       volumes:
         - wiki_data:/wiki/data
       networks:
         - backend
         - proxy
       labels:
         - "traefik.enable=true"
         - "traefik.docker.network=traefik_proxy"
         - "traefik.http.routers.wikijs.rule=Host(`wiki.example.net`)"
         - "traefik.http.routers.wikijs.entrypoints=websecure"
         - "traefik.http.routers.wikijs.tls=true"
         - "traefik.http.routers.wikijs.tls.certresolver=letsencrypt"
         - "traefik.http.services.wikijs.loadbalancer.server.port=3000"

   networks:
     backend:
       internal: true
     proxy:
       external: true
       name: traefik_proxy

   volumes:
     db_data:
     wiki_data:

   secrets:
     db_password:
       file: ./secrets/db_password
   EOF
   ```
   👉 Explication : le fichier déclare la base sur un réseau interne `backend`, Wiki.js sur `backend` et `proxy`, et lit le mot de passe depuis un secret.

2. Contrôler la syntaxe du fichier :
   ```bash
   sudo docker compose config --quiet
   ```
   👉 Explication : aucune sortie signifie que la configuration est valide.

3. Vérifier qu'aucune section `ports:` n'est présente :
   ```bash
   grep -n 'ports:' docker-compose.yml || echo 'aucun port publie'
   ```
   👉 Explication : le port 3000 n'est joignable que par le réseau du reverse proxy.

## 2. Production — Contrôles

L'image `ghcr.io/requarks/wiki:2` suit la branche majeure 2; pour une livraison reproductible, épingler une version mineure/patch ou un digest validé et piloter les mises à jour.

## 3. Production — Sécurité

- Ne pas utiliser `latest`.
- Garder la base sur le réseau `internal: true`; ne pas y publier de port.
- Pas de mot de passe en clair dans `environment`: utiliser `*_FILE` avec secrets.

## Validation et retour arrière

- **Validation** : `docker compose config --quiet` ne retourne aucune erreur et les labels Traefik correspondent à votre configuration.
- **Retour arrière** : Supprimer le fichier `docker-compose.yml` ou restaurer sa copie précédente; rien n'est encore démarré.

## Si le problème n'est pas résolu

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Wiki.js — Configuration et reverse proxy](https://docs.requarks.io/install/config)
- [Guide complet Wiki.js Docker PostgreSQL Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/28-installation-wikijs-docker-postgresql-traefik#3-definir-la-stack-compose)