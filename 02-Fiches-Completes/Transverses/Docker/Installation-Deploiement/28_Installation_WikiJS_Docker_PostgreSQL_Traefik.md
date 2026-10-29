# Installer Wiki.js avec PostgreSQL et Traefik

- **Type de fiche** : Installation / Déploiement
- **Environnement** : Hôte Linux avec Docker Engine, Compose v2 et Traefik déjà opérationnel
- **OS / Version** : Linux serveur; Wiki.js 2.x; PostgreSQL 17
- **Rôle** : Déployer une base documentaire accessible en HTTPS, avec base persistante et secrets séparés
- **Tags** : `wikijs`, `docker`, `compose`, `postgresql`, `traefik`, `tls`, `installation`

## 1. Préparer l'hôte et le DNS

Fiche simple : [préparer l'hôte et le DNS](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Preparer_Hote_DNS.md).

Cette fiche suppose que Docker Compose et Traefik sont déjà installés et maintenus. Pour l'installation de l'hôte, du pare-feu, du DNS et du reverse proxy, suivre les fiches correspondantes.

- Prévoir au moins 2 vCPU, 1 Go de RAM minimum et du stockage selon le volume de documents et pièces jointes.
- Créer un enregistrement DNS `A`/`AAAA` pour `wiki.example.net` vers l'adresse du reverse proxy.
- Vérifier que les ports 80/443 et le certificat ACME fonctionnent déjà pour un autre service.
- Créer le réseau Docker externe nommé ci-dessous, ou remplacer son nom par le réseau partagé existant de Traefik.
- Garder la console de l'hôte disponible pendant la mise en service.

Wiki.js ne crée pas lui-même la base de données. PostgreSQL est recommandé; ce déploiement utilise un service de base distinct et un volume persistant.

## 2. Créer le répertoire et le secret

Fiche simple : [créer le répertoire et le secret](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Repertoire_Secret.md).

```bash
sudo install -d -m 0750 /opt/docker/wikijs
sudo install -d -m 0700 /opt/docker/wikijs/secrets
cd /opt/docker/wikijs
sudo sh -c 'umask 077; openssl rand -base64 36 > secrets/db_password'
sudo chmod 0444 secrets/db_password
```

Le répertoire parent du secret reste accessible uniquement à root sur l'hôte; le mode du fichier permet au processus Wiki.js non-root de lire le secret monté dans le conteneur. Ne pas copier ce fichier dans un dépôt ni dans un ticket. En environnement multi-hôte, préférer le gestionnaire de secrets de la plateforme.

## 3. Définir la stack Compose

Fiche simple : [définir la stack Compose](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Definir_Stack_Compose.md).

Créer `/opt/docker/wikijs/docker-compose.yml` :

```yaml
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
```

Remplacer `wiki.example.net`, `websecure`, `letsencrypt` et `traefik_proxy` par les noms réellement définis dans Traefik. Le port 3000 n'est pas publié sur l'hôte : l'accès externe passe par le réseau du reverse proxy. La base n'est attachée qu'au réseau interne `backend`.

La référence `ghcr.io/requarks/wiki:2` suit la branche majeure 2, conformément à la recommandation Wiki.js d'éviter `latest`. Pour une livraison strictement reproductible, épingler une version mineure/patch ou un digest validé, puis piloter les mises à jour.

## 4. Valider et démarrer

Fiche simple : [valider et démarrer](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Valider_Demarrer.md).

Vérifier que le réseau externe existe puis contrôler la configuration rendue :

```bash
docker network inspect traefik_proxy >/dev/null
cd /opt/docker/wikijs
sudo docker compose config --quiet
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100 db wiki
```

Ouvrir `https://wiki.example.net`. Terminer l'assistant initial, créer le compte administrateur avec un mot de passe unique, définir l'URL publique canonique, puis configurer SMTP et les mécanismes d'authentification nécessaires. Ne pas laisser un compte administrateur partagé.

## 5. Recette

Fiche simple : [réaliser la recette](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Recette.md).

- Vérifier que le certificat présenté correspond au nom DNS et que HTTP redirige vers HTTPS selon la politique Traefik.
- Créer une page de test, la modifier, joindre un fichier puis confirmer sa présence après redémarrage des services.
- Vérifier `docker compose ps`, les journaux sans erreur persistante et l'état de santé PostgreSQL.
- Confirmer qu'aucun port PostgreSQL ou port 3000 n'est publié sur l'interface publique.
- Tester la création d'un compte utilisateur non administrateur et ses permissions.

## 6. Sauvegarder et restaurer

Fiche simple : [sauvegarder et restaurer](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Sauvegarder_Restaurer.md).

Sauvegarder la base et les données de fichiers configurées par les modules de stockage Wiki.js. Les documents et pièces jointes peuvent être placés dans un stockage local ou distant selon les modules activés : inclure la cible réelle de stockage dans le plan de sauvegarde, pas seulement la base.

Exemple de dump PostgreSQL vers un répertoire protégé :

```bash
sudo install -d -m 0700 /var/backups/wikijs
sudo sh -c 'cd /opt/docker/wikijs && docker compose exec -T db pg_dump -U wikijs -d wiki -Fc > "/var/backups/wikijs/wiki-$(date +%F-%H%M).dump"'
```

Chiffrer et copier les dumps hors de l'hôte, définir une rétention, et tester régulièrement une restauration sur une stack isolée. Inclure également le secret DB et toute configuration/secret du stockage distant dans le coffre de sauvegarde approprié. Un volume Docker seul n'est pas une sauvegarde.

## 7. Mise à jour et retour arrière

Fiche simple : [mettre à jour avec retour arrière](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Mise_A_Jour_Retour_Arriere.md).

Avant toute mise à jour, effectuer et vérifier une sauvegarde restaurable, lire les notes de version Wiki.js et noter les références d'images courantes. Puis :

```bash
cd /opt/docker/wikijs
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100 wiki db
```

Ne pas changer la version majeure de PostgreSQL en réutilisant directement le volume existant : une migration de données dédiée est nécessaire. En cas d'échec Wiki.js, conserver les volumes, revenir aux images et configuration précédentes, puis restaurer la base uniquement si la migration a modifié son schéma.

## 8. Diagnostic rapide

Fiche simple : [diagnostiquer rapidement](../../../../01-Fiches-Simples/Transverses/Docker/WikiJS/Fiche_Simple_-_Docker_WikiJS_Diagnostic_Rapide.md).

```bash
sudo docker compose ps
sudo docker compose logs --tail=200 wiki
sudo docker compose logs --tail=200 db
docker network inspect traefik_proxy
```

- **Wiki.js ne joint pas PostgreSQL** : vérifier `DB_HOST: db`, le réseau `backend`, l'état healthy et le montage `DB_PASS_FILE`.
- **Erreur 404 ou 502** : vérifier DNS, labels Traefik, réseau Docker réellement partagé et port amont 3000.
- **Certificat invalide** : diagnostiquer Traefik et ACME; ne pas activer TLS directement dans Wiki.js lorsque TLS est terminé par le reverse proxy.
- **Pièce jointe perdue après recréation** : vérifier le module de stockage choisi et sa persistance; le dump SQL seul peut ne pas contenir les fichiers.

## Sources

- [Wiki.js — Docker](https://docs.requarks.io/install/docker)
- [Wiki.js — Prérequis](https://docs.requarks.io/install/requirements)
- [Wiki.js — Configuration et reverse proxy](https://docs.requarks.io/install/config)
- [Docker — Compose secrets](https://docs.docker.com/compose/how-tos/use-secrets/)
- [PostgreSQL — Images Docker officielles](https://hub.docker.com/_/postgres)