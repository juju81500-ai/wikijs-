# Migrer un cloud Nextcloud 29 conteneurisé

- **Statut** : Nextcloud 29 est une branche ancienne ; ne pas en faire une nouvelle installation exposée en production.
- **Cible** : migrer vers une version maintenue après vérification des chemins de mise à niveau supportés
- **Composants** : Nextcloud, base de données, Redis, proxy TLS, volumes persistants

## 1. Préparer la migration

Fiche simple : [préparer la migration](/01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-preparer).

Relever les versions de l'image, du moteur de base, des applications et du proxy. Lire les notes de version et les prérequis de chaque étape de migration : les sauts de versions majeures peuvent être interdits. Mettre à jour les images uniquement dans un environnement de test avant production.

```bash
docker compose ps
docker compose images
docker compose config --quiet
docker system df
```

Identifier explicitement les volumes de configuration, données utilisateurs, base, Redis et certificats. Prévoir une fenêtre de maintenance et un espace de sauvegarde distinct du stockage Docker.

## 2. Sauvegarder et tester la restauration

Fiche simple : [sauvegarder et tester la restauration](/01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-sauvegarder-tester-restauration).

Activer le mode maintenance Nextcloud via la méthode prise en charge par l'image déployée. Arrêter les écritures, exporter la base avec l'outil natif de cette base et sauvegarder les volumes persistants avec une procédure documentée. Vérifier les sommes de contrôle et restaurer cette sauvegarde dans un environnement isolé avant toute mise à niveau.

Ne pas utiliser `docker compose down -v`, `docker volume prune` ou `docker system prune --volumes` dans cette procédure.

## 3. Mise à niveau contrôlée

Fiche simple : [mettre à niveau de façon contrôlée](/01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-mise-a-niveau-controlee).

- Choisir une version Nextcloud maintenue, compatible avec PHP, MariaDB et Redis retenus.
- Épingler les images par version explicite ; éviter `latest`.
- Modifier une version majeure à la fois selon les étapes officiellement supportées.
- Lancer la mise à niveau avec la commande recommandée par la version du conteneur et suivre les journaux.
- N'activer le trafic utilisateur qu'après validation du contrôle d'intégrité et des applications.

Ne pas modifier simultanément le moteur de base et Nextcloud sans plan de compatibilité indépendant.

## 4. Contrôles

Fiche simple : [contrôler après migration](/01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-controles).

```bash
docker compose ps
docker compose logs --tail 200 app db redis
```

Vérifier connexion, téléversement/téléchargement d'un fichier de test, tâches de fond, aperçu des erreurs d'administration, TLS, envoi de courriels et accès aux partages. Contrôler que Redis est utilisé pour le verrouillage transactionnel si l'architecture le prévoit.

## 5. Retour arrière

Fiche simple : [revenir en arrière en cas d'échec](/01-fiches-simples/transverses/docker/nextcloud/fiche-simple-docker-nextcloud29-migration-retour-arriere).

En cas d'échec, remettre en service l'ensemble cohérent des images, de la base et des volumes sauvegardés. Ne pas restaurer uniquement l'image applicative après migration du schéma de base. Conserver le mode maintenance jusqu'à validation, puis documenter la version cible et la date de retrait de Nextcloud 29.