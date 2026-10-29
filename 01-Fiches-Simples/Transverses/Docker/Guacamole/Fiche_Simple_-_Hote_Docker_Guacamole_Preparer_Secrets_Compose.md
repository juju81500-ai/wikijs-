# Fiche_Simple_-_Hote_Docker_Guacamole_Preparer_Secrets_Compose.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose (Guacamole, guacd, PostgreSQL, reverse proxy HTTPS)
- **OS / Version** : Docker Engine + Compose; images Apache Guacamole 1.6.0, PostgreSQL 16
- **Catégorie** : accès distant / configuration
- **Tags** : `docker`, `apache-guacamole`, `compose`, `postgresql`, `secrets`, `compose`

---

## Problème précis à résoudre

Créer le projet Compose avec un fichier `.env` protégé.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le dossier de projet restreint (chemin d'exemple à remplacer) :
   ```bash
   install -d -m 0700 ~/guacamole
   cd ~/guacamole
   ```
   👉 Explication : accessible uniquement aux administrateurs.

2. Créer `.env` avec un secret aléatoire (remplacer la valeur d'exemple) puis restreindre le mode :
   ```dotenv
   POSTGRES_DB=guacamole_db
   POSTGRES_USER=guacamole
   POSTGRES_PASSWORD=REMPLACER_PAR_UN_SECRET_ALEATOIRE
   ```
   👉 Explication : les secrets ne vont jamais dans le dépôt ni en argument de commande.

3. Appliquer le mode `0600` :
   ```bash
   chmod 0600 .env
   ```
   👉 Explication : seul le propriétaire lit le fichier.

4. Créer `compose.yaml` :
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
   👉 Explication : déclare PostgreSQL, guacd et Guacamole sur un réseau privé; seul le port Web est publié en loopback.

## 2. Production — Contrôles

Pour la production, utiliser le mécanisme de secrets approuvé; vérifier le tag PostgreSQL contre la matrice de compatibilité et le figer; restreindre les flux sortants aux seules cibles nécessaires.

## 3. Production — Sécurité

- Ne pas conserver la valeur d'exemple du mot de passe.
- Ne jamais publier les mots de passe dans le wiki, les journaux CI ou le dépôt.
- Ne pas publier PostgreSQL ou guacd sur l'hôte.

## Validation et retour arrière

- **Validation** : `docker compose config --quiet` ne renvoie aucune erreur.
- **Retour arrière** : `rm compose.yaml .env` dans le dossier de projet si rien n'a été démarré.

## Si le problème n'est pas résolu

- [Apache Guacamole — Docker](https://guacamole.apache.org/doc/gug/guacamole-docker.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet Apache Guacamole Docker](../../../../02-Fiches-Completes/Transverses/Docker/Installation-Deploiement/121_Deploiement_Apache_Guacamole_1.6_Docker.md#2-preparer-les-secrets-et-la-configuration)
