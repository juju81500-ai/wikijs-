# Déployer Apache Guacamole 1.6.0 avec Docker Compose

- **OS / Version** : Hôte Linux avec Docker Engine et plugin Compose; images Apache Guacamole 1.6.0
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : accès distant via navigateur, guacd, authentification JDBC PostgreSQL, reverse proxy HTTPS
- **Catégorie** : accès distant / VDI

## 1. Périmètre et prérequis

Fiche simple : [cadrer le périmètre et les prérequis](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-cadrer-prerequis).

Guacamole fournit une passerelle web d'accès distant. Cette fiche déploie les composants Guacamole et guacd avec une base PostgreSQL. Elle ne configure pas les systèmes cibles, les identifiants de connexion aux hôtes, SSO/LDAP/MFA, ni la haute disponibilité.

Prérequis : hôte Linux Docker durci, DNS dédié, réseau d'administration, reverse proxy HTTPS géré, stockage persistant sauvegardé et liste de systèmes cibles explicitement autorisés. Traiter Guacamole comme une passerelle privilégiée : comptes personnels, MFA ou SSO approuvé, journalisation, restriction des réseaux et procédure de révocation sont nécessaires avant tout usage de production.

## 2. Préparer les secrets et la configuration

Fiche simple : [préparer les secrets et la configuration](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-preparer-secrets-compose).

Créer un dossier de projet accessible uniquement aux administrateurs et un fichier `.env` non versionné, mode `0600`, contenant des secrets aléatoires :

```dotenv
POSTGRES_DB=guacamole_db
POSTGRES_USER=guacamole
POSTGRES_PASSWORD=REMPLACER_PAR_UN_SECRET_ALEATOIRE
```

Ne pas conserver les valeurs d'exemple. Le fichier d'environnement est lisible en clair et Docker expose les variables du conteneur aux administrateurs de l'hôte; pour une installation de production, suivre le mécanisme de secrets approuvé par l'organisation. Ne jamais publier les mots de passe dans le wiki, les journaux CI ou le dépôt.

Créer `compose.yaml` :

```yaml
services:
  db:
    image: postgres:16
    restart: unless-stopped
    env_file: .env
    volumes:
      - postgres-data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U \"$${POSTGRES_USER}\" -d \"$${POSTGRES_DB}\""]
      interval: 10s
      timeout: 5s
      retries: 5
    networks: [guac-backend]

  guacd:
    image: guacamole/guacd:1.6.0
    restart: unless-stopped
    networks: [guac-backend]

  guacamole:
    image: guacamole/guacamole:1.6.0
    restart: unless-stopped
    depends_on:
      db:
        condition: service_healthy
      guacd:
        condition: service_started
    environment:
      GUACD_HOSTNAME: guacd
      POSTGRESQL_HOSTNAME: db
      POSTGRESQL_DATABASE: ${POSTGRES_DB}
      POSTGRESQL_USERNAME: ${POSTGRES_USER}
      POSTGRESQL_PASSWORD: ${POSTGRES_PASSWORD}
      REMOTE_IP_VALVE_ENABLED: "true"
    ports:
      - "127.0.0.1:8080:8080"
    networks: [guac-backend]

networks:
  guac-backend:
    driver: bridge

volumes:
  postgres-data:
```

Le réseau privé bridge permet à Guacamole/guacd de joindre les systèmes cibles; il ne publie pas les ports PostgreSQL ou guacd sur l'hôte. Restreindre les flux sortants vers les seules cibles et destinations DNS/NTP nécessaires avec le pare-feu hôte ou la politique réseau. Le port Web est publié sur la boucle locale pour le reverse proxy. Le tag PostgreSQL doit être vérifié contre la matrice officielle de compatibilité et figé selon le processus de mise à jour.

## 3. Initialiser le schéma PostgreSQL

Fiche simple : [initialiser le schéma PostgreSQL](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-initialiser-schema-postgresql).

Démarrer uniquement PostgreSQL puis attendre qu'il soit sain :

```bash
docker compose up -d db
docker compose ps
```

Générer le schéma avec l'outil fourni dans l'image Guacamole 1.6.0, puis l'importer dans la base neuve. Conserver le fichier SQL comme artefact de déploiement, sans secret :

```bash
docker run --rm guacamole/guacamole:1.6.0 /opt/guacamole/bin/initdb.sh --postgresql > initdb.sql
docker compose exec -T db psql -U guacamole -d guacamole_db -f - < initdb.sql
```

Remplacer utilisateur/base si les noms ont été adaptés. Cette initialisation est destinée à une base vide; ne pas la répéter sur une base en service. Sauvegarder la base avant toute migration ou réinitialisation de schéma.

## 4. Démarrer et configurer le reverse proxy

Fiche simple : [démarrer et configurer le reverse proxy](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-demarrer-reverse-proxy).

Démarrer les services après vérification de la configuration Compose :

```bash
docker compose config --quiet
docker compose up -d
docker compose ps
docker compose logs --tail=100 guacamole guacd db
```

Ne pas partager la sortie complète de `docker compose config` : elle peut contenir des secrets interpolés. Cet exemple suppose que le reverse proxy s'exécute sur l'hôte. S'il est lui-même conteneurisé, le connecter au service Guacamole sur un réseau privé dédié et retirer la publication loopback; ne pas pointer le proxy vers sa propre adresse `127.0.0.1`. Configurer le reverse proxy pour transmettre HTTPS vers `http://127.0.0.1:8080/guacamole/`. Les en-têtes proxy ne doivent être acceptés que depuis le proxy de confiance. Terminer TLS avec un certificat valide, n'autoriser que les réseaux clients approuvés et ne pas exposer directement le port 8080.

Ouvrir la page de connexion. Sur une base tout juste initialisée, les identifiants initiaux documentés par Guacamole sont `guacadmin` / `guacadmin`; changer immédiatement le mot de passe, créer les comptes nominaux et vérifier les permissions. Ne pas connecter de systèmes réels tant que les comptes et contrôles d'accès ne sont pas validés.

## 5. Sauvegarde et restauration

Fiche simple : [sauvegarde et restauration](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-sauvegarde-restauration).

- Sauvegarder la base PostgreSQL avec une méthode cohérente (par exemple `pg_dump`) et conserver le fichier chiffré hors hôte.
- Sauvegarder la configuration Compose, `.env` via le coffre approuvé, le reverse proxy, les certificats et l'inventaire des connexions; exclure les secrets des dépôts.
- Tester la restauration dans un projet Compose et un réseau isolés. Ne pas restaurer une base sur l'instance active sans fenêtre approuvée et copie de l'état courant.
- Une sauvegarde de la base seule ne restaure pas automatiquement l'accès aux systèmes cibles : tester aussi les extensions, la configuration, les certificats et les dépendances.

## 6. Validation et contrôle d'accès

Fiche simple : [validation et contrôle d'accès](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-valider-controle-acces).

- `docker compose ps` indique les services attendus actifs; les journaux ne montrent pas d'erreur de schéma ou d'authentification.
- Le nom public répond en HTTPS; l'accès direct depuis le réseau au port 8080, au port guacd 4822 et au port PostgreSQL est bloqué.
- Les comptes de démonstration sont supprimés ou désactivés après création de comptes nominatifs; MFA/SSO et groupes sont contrôlés avant l'ouverture aux utilisateurs.
- Une connexion pilote vers un système de laboratoire autorisé fonctionne; les actions et journaux sont conformes à la politique.
- Une sauvegarde de la base est restaurée sur un environnement isolé et un compte de test est retrouvé.

## 7. Mise à jour et retour arrière

Fiche simple : [mise à jour et retour arrière](/01-fiches-simples/transverses/docker/guacamole/fiche-simple-hote-docker-guacamole-mise-a-jour-retour-arriere).

Épingler les images par version (et digest après validation), lire les notes de version et sauvegarder base et configuration avant mise à jour. Effectuer un changement à la fois sur un clone de test. Une migration de schéma peut rendre un retour à l'ancien conteneur impossible sans restauration de la base sauvegardée.

Pour revenir en arrière, restaurer ensemble versions d'images, configuration et base compatibles sur l'environnement de test, vérifier l'authentification et une connexion pilote, puis planifier la bascule. En cas d'incident, couper l'accès utilisateur via le proxy ou le pare-feu, préserver les journaux et révoquer les comptes/identifiants concernés.

## Sources

- [Apache Guacamole 1.6.0 — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Apache Guacamole 1.6.0 — authentification PostgreSQL](https://guacamole.apache.org/doc/gug/postgresql-auth.html)
- [Apache Guacamole 1.6.0 — authentification JDBC](https://guacamole.apache.org/doc/gug/jdbc-auth.html)
- [Apache Guacamole — reverse proxy](https://guacamole.apache.org/doc/gug/reverse-proxy.html)
- [Docker — Compose](https://docs.docker.com/compose/)

La version exacte des images, le reverse proxy, les mécanismes MFA/SSO, la sauvegarde et la restauration doivent être testés avant production. Aucun accès distant réel n'a été exécuté pendant la rédaction.