# Fiche_Simple_-_Docker_Snipe-IT_Mise_A_Jour_Retour.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs

---

## Problème précis à résoudre

Mettre à jour vers un tag précis et savoir revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder et tester le restore avant toute mise à jour.
   👉 Explication : condition préalable à tout changement de version.

2. Dans `.env`, remplacer `APP_VERSION` par un tag précis validé (jamais `latest`).
   👉 Explication : garde un déploiement reproductible.

3. Appliquer la mise à jour :
   ```bash
   sudo docker compose pull
   sudo docker compose up -d
   ```
   👉 Explication : Récupère l'image et recrée les conteneurs; un simple `restart` ne recharge pas l'environnement.

4. Contrôler :
   ```bash
   sudo docker compose ps
   sudo docker compose logs --tail=100 app
   ```
   👉 Explication : Contrôle l'état après mise à jour.

## 2. Production — Contrôles

Lire les notes de version avant de changer de tag.

## 3. Production — Sécurité

- Ne pas utiliser `latest` en production.

## Validation et retour arrière

- **Validation** : la nouvelle version démarre et la recette passe.
- **Retour arrière** : remettre l'ancien `APP_VERSION`, refaire `docker compose up -d`, puis restaurer la sauvegarde si la base a migré.

## Si le problème n'est pas résolu

- [Snipe-IT — Sauvegarde et restauration](https://snipe-it.readme.io/docs/backups)
- [Snipe-IT — Version 8.8.3](https://github.com/grokability/snipe-it/releases/tag/v8.8.3)
- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 7](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik#7-mise-a-jour-et-retour-arriere)