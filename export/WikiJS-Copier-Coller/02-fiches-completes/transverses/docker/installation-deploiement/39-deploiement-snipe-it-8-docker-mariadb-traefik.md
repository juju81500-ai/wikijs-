# Déployer Snipe-IT 8.8.3 avec Docker, MariaDB et Traefik

- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Docker Compose v2, réseau Traefik existant
- **Machine ciblée** : Hôte Docker d'inventaire
- **Catégorie** : ITSM / gestion des actifs

## 1. Préparer l'architecture

Fiche simple : [préparer l'architecture Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-preparer-architecture).

Ce guide utilise uniquement l'image officielle `snipe/snipe-it`, épinglée à `v8.8.3`, et la stack Docker officielle comme base. La version a été relevée le 27 octobre 2026; revalider la dernière version maintenue et ses prérequis avant un nouveau déploiement.

Prévoir DNS `assets.example.net`, TLS terminé par Traefik, un réseau proxy existant, volumes Docker sauvegardés hors hôte et envoi SMTP. Garder la base dans un réseau privé et ne pas publier son port.

## 2. Récupérer les fichiers officiels

Fiche simple : [récupérer les fichiers officiels Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-recuperer-fichiers-officiels).

```bash
sudo install -d -m 0750 /opt/docker/snipe-it
cd /opt/docker/snipe-it
sudo curl -fL https://raw.githubusercontent.com/grokability/snipe-it/master/docker-compose.yml -o docker-compose.yml
sudo curl -fL https://raw.githubusercontent.com/grokability/snipe-it/master/.env.docker -o .env
sudo chmod 0600 .env
```

Les fichiers amont évoluent : examiner le Compose et `.env` avant démarrage. Ne pas lancer un fichier récupéré sans contrôle.

## 3. Configurer l'image, les secrets et Traefik

Fiche simple : [configurer l'image, les secrets et Traefik pour Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-configurer-image-secrets-traefik).

Dans `.env`, remplacer les valeurs d'exemple et définir au minimum :

```dotenv
APP_VERSION=v8.8.3
APP_ENV=production
APP_DEBUG=false
APP_URL=https://assets.example.net
APP_TIMEZONE=Europe/Paris
SECURE_COOKIES=true
DB_DATABASE=snipeit
DB_USERNAME=snipeit
```

Générer des valeurs distinctes et aléatoires pour `DB_PASSWORD` et `MYSQL_ROOT_PASSWORD`, puis conserver `.env` en mode `0600` hors dépôt Git. Générer `APP_KEY` avec la commande officielle suivante et copier le résultat dans `.env` avant la première initialisation :

```bash
docker compose run --rm app php artisan key:generate --show
```

Conserver la clé `APP_KEY` dans le coffre de secrets : elle est nécessaire pour déchiffrer certains champs de la base après restauration. Utiliser les labels Traefik déjà en vigueur pour router le service `app` vers le port 80 du conteneur; connecter `app` au réseau `traefik_proxy`, mais ne pas exposer MariaDB.

Si la stack officielle publie le port 8000, retirer ce port hôte lorsqu'on utilise Traefik et attacher l'application au réseau partagé. Définir `APP_TRUSTED_PROXIES` selon le CIDR réel du réseau proxy, sans faire confiance à des réseaux non maîtrisés.

## 4. Valider et démarrer

Fiche simple : [valider et démarrer Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-valider-demarrer).

```bash
docker network inspect traefik_proxy >/dev/null
cd /opt/docker/snipe-it
sudo docker compose config --quiet
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail=100 app db
```

Ouvrir `https://assets.example.net`, terminer le prévol, créer un compte administrateur nominatif, configurer SMTP, les rôles, les catégories, les modèles, les statuts et les lieux. L'import d'inventaire vient après la validation de cette structure.

## 5. Recette

Fiche simple : [recette Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-recette).

- Vérifier certificat, URL publique, cookies sécurisés et absence d'accès direct à MariaDB.
- Créer un modèle, un statut déployable, un lieu et un actif de test.
- Tester permissions d'un compte non administrateur et envoi d'une notification.
- Redémarrer la stack et confirmer que base, images et pièces jointes persistent.

## 6. Sauvegarde et restauration

Fiche simple : [sauvegarde et restauration Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-sauvegarde-restauration).

L'outil Snipe-IT génère une archive contenant dump SQL et pièces jointes : lancer **Admin > Backups** ou, en maintenance planifiée :

```bash
docker compose exec -T app php artisan snipeit:backup
```

Copier l'archive hors hôte, chiffrer, protéger et tester la restauration sur une stack isolée. Sauvegarder séparément `.env`, la clé `APP_KEY`, le Compose utilisé et les références d'image. Une restauration ne réécrit pas `.env` et déconnecte les utilisateurs.

## 7. Mise à jour et retour arrière

Fiche simple : [mise à jour et retour arrière Snipe-IT](/01-fiches-simples/transverses/docker/snipe-it/fiche-simple-docker-snipe-it-mise-a-jour-retour).

Avant toute mise à jour, sauvegarder et tester le restore. Mettre à jour `APP_VERSION` vers un tag précis validé, récupérer l'image, puis recréer la stack avec `docker compose up -d`. Ne jamais remplacer la version par `latest` pour une production reproductible. Les modifications de `.env` exigent une recréation de conteneur; un simple `restart` ne recharge pas l'environnement.

## Sources

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Snipe-IT — Prérequis](https://snipe-it.readme.io/docs/requirements)
- [Snipe-IT — Clé applicative](https://snipe-it.readme.io/docs/generate-your-app-key)
- [Snipe-IT — Sauvegarde et restauration](https://snipe-it.readme.io/docs/backups)
- [Snipe-IT — Version 8.8.3](https://github.com/grokability/snipe-it/releases/tag/v8.8.3)