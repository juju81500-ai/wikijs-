---
title: "Déployer Vaultwarden avec Docker Compose"
description: "Fiche simple : [périmètre et distinction avec Bitwarden](../../../../01-Fiches-Simples/Transverses/Docker/Vaultwarden/FicheSimple-HoteDockerVaultwardenPerimetre.md)."
published: true
date: 2026-10-29T19:40:03Z
tags: ["vaultwarden", "docker", "compose", "bitwarden-compatible", "secrets", "sqlite", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T19:40:03Z
dateModified: 2026-10-29T19:40:03Z
---

# Déployer Vaultwarden avec Docker Compose

- **OS / Version** : hôte Linux avec Docker Engine et le plugin Compose; image `vaultwarden/server` (tag à figer après validation)
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : serveur Vaultwarden SQLite derrière un reverse proxy HTTPS, jeton d'administration haché, sauvegarde et restauration
- **Catégorie** : gestionnaire de mots de passe d'équipe auto-hébergé
- **Tags** : `vaultwarden`, `docker`, `compose`, `bitwarden-compatible`, `secrets`, `sqlite`, `sauvegarde`

## 1. Périmètre et distinction avec Bitwarden

Fiche simple : [périmètre et distinction avec Bitwarden](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-perimetre).

Vaultwarden est un serveur communautaire, compatible avec les clients Bitwarden, qui n'est pas le produit officiel Bitwarden. Pour le serveur officiel, voir le [guide Bitwarden auto-hébergé](/02-fiches-completes/transverses/docker/installation-deploiement/62-deploiement-bitwarden-self-hosted-linux-docker). Choisir Vaultwarden demande une décision explicite : support communautaire, politique de licence et de mise à jour du projet à valider par la sécurité. Ce guide couvre SQLite; MySQL/PostgreSQL, SSO et conformité ne sont pas traités. Ce guide n'a pas été testé.

Prérequis : hôte Docker durci ([hardening Docker](/02-fiches-completes/transverses/docker/autres/32-hardening-hote-docker-production)), nom DNS dédié, reverse proxy HTTPS (par exemple [Traefik](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker)). Le projet indique que HTTPS est pratiquement obligatoire, car l'interface web utilise des API de chiffrement du navigateur disponibles seulement en contexte sécurisé; il recommande de placer le service derrière un reverse proxy.

## 2. Préparer le jeton d'administration

Fiche simple : [préparer le jeton d'administration](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-jeton-admin).

La page d'administration est inutile pour une première installation; ne l'activer que si elle est nécessaire. Le projet recommande de stocker un jeton haché en Argon2id (chaîne PHC), généré avec la commande intégrée :

```bash
docker run --rm -it vaultwarden/server /vaultwarden hash
```

Saisir un mot de passe long et aléatoire (deux fois). Conserver ce mot de passe dans le gestionnaire de secrets et la chaîne hachée pour le fichier Compose. Dans un fichier Compose, chaque `$` de la chaîne doit être doublé (`$$`) pour ne pas être interprété comme une variable.

## 3. Compose

Fiche simple : [créer le fichier Compose et démarrer](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-compose).

Créer un répertoire dédié (par exemple `/opt/vaultwarden`) avec `compose.yaml`; le port n'est exposé que sur la boucle locale pour que seul le reverse proxy y accède :

```yaml
services:
  vaultwarden:
    image: vaultwarden/server:latest
    container_name: vaultwarden
    restart: always
    environment:
      DOMAIN: "https://vault.example.net"
      SIGNUPS_ALLOWED: "true"
      # ADMIN_TOKEN: "<chaîne PHC avec chaque $ doublé>"
    volumes:
      - ./vw-data:/data
    ports:
      - 127.0.0.1:11001:80
```

L'image `latest` suit la dernière version publiée. Après validation, noter la version/le digest réellement déployé et le figer dans le fichier avant la production, afin de pouvoir revenir en arrière. Configurer le reverse proxy pour envoyer le domaine vers `127.0.0.1:11001`, avec un certificat valide. Démarrer :

```bash
docker compose config
docker compose up -d
docker compose logs -f
```

## 4. Créer le premier compte puis fermer les inscriptions

Fiche simple : [créer le premier compte puis fermer les inscriptions](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-premier-compte).

1. Se connecter à `https://vault.example.net`, créer le compte administrateur avec une phrase secrète forte et conserver sa procédure de récupération (le chiffrement est côté client; l'administrateur du serveur ne peut pas réinitialiser un mot de passe maître perdu).
2. Passer `SIGNUPS_ALLOWED` à `"false"` et recréer le conteneur : `docker compose up -d`. Le projet précise de désactiver cette option après la création du compte pour éviter l'inscription de tiers.
3. Inviter les utilisateurs via les mécanismes documentés par le projet, activer l'authentification à deux facteurs et ne jamais exposer `/admin` sans restriction d'accès.

## 5. Sauvegarder

Fiche simple : [sauvegarder](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-sauvegarder).

Données par défaut dans `vw-data` : `db.sqlite3` (et éventuels `-wal`/`-shm`), `attachments/`, `sends/`, `config.json`, `rsa_key*`. Le projet déconseille de copier le fichier SQLite actif et recommande l'API de sauvegarde SQLite ou la commande intégrée, et déconseille de s'appuyer sur les snapshots de système de fichiers ou de VM :

```bash
docker exec -it vaultwarden /vaultwarden backup
ls -l vw-data
```

Vérifier l'emplacement du fichier produit, puis copier sur un stockage chiffré hors hôte, avec `attachments`, `sends`, `config.json` et les fichiers `rsa_key*` (outil de copie : [Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic) ou [Borg](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)). Les sauvegardes contiennent des données de coffre chiffrées, mais aussi des clés serveur : les protéger comme des secrets. Voir aussi la [sauvegarde de stacks Docker](/02-fiches-completes/transverses/docker/autres/37-sauvegarde-restauration-stacks-docker).

## 6. Restaurer (test sur hôte isolé)

Fiche simple : [restaurer (test sur hôte isolé)](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-restaurer).

Restaurer sur un hôte ou un réseau isolé : copier la sauvegarde dans un nouveau `vw-data`, démarrer avec le même `compose.yaml` et le même `DOMAIN` (ajouter une entrée DNS de test), puis se connecter avec un compte de test. Ne jamais restaurer par-dessus `vw-data` de production sans avoir arrêté le conteneur et conservé une copie de l'état actuel.

## 7. Validation

Fiche simple : [validation](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-validation).

- `docker compose ps` indique le conteneur en cours d'exécution; les journaux ne montrent pas d'erreur.
- Le site est atteint en HTTPS par le nom DNS; un accès direct HTTP au port 11001 depuis un autre hôte échoue.
- Un client Bitwarden se connecte au serveur personnalisé, crée, modifie et lit un élément de test.
- L'inscription ouverte est refusée après le passage à `false`; `/admin` est refusé sans le bon jeton ou est désactivé.
- Une sauvegarde est restaurée sur un hôte isolé et l'élément de test est retrouvé.

## 8. Retour arrière

Fiche simple : [retour arrière et mise à jour](/01-fiches-simples/transverses/docker/vaultwarden/fiche-simple-hote-docker-vaultwarden-retour-arriere).

Avant toute mise à jour : sauvegarde (étape 5), noter le tag/digest actuel. Mise à jour : `docker compose pull && docker compose up -d`. En cas de problème : remettre l'ancien tag/digest dans `compose.yaml`, `docker compose up -d`, et si le schéma de base a été migré, restaurer la sauvegarde d'avant mise à jour (un retour d'image seul peut ne pas suffire). Pour retirer le service : `docker compose down` n'efface pas `vw-data`; ne supprimer ce répertoire qu'après confirmation de la restauration.

## Sources

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Enabling HTTPS](https://github.com/dani-garcia/vaultwarden/wiki/Enabling-HTTPS)
- [Vaultwarden — Enabling admin page et ADMIN_TOKEN](https://github.com/dani-garcia/vaultwarden/wiki/Enabling-admin-page)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Vaultwarden — Which container image to use](https://github.com/dani-garcia/vaultwarden/wiki/Which-container-image-to-use)
- [Vaultwarden — dépôt officiel](https://github.com/dani-garcia/vaultwarden)

La version déployée, la sauvegarde et la restauration n'ont pas été testées. Conserver les statuts **À revoir** et **À tester**.