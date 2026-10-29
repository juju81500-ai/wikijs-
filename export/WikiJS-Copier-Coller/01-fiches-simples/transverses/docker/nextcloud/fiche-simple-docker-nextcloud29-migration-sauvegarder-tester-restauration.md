# Fiche_Simple_-_Docker_Nextcloud29_Migration_Sauvegarder_Tester_Restauration.md

- **Environnement** : Hôte Linux avec Nextcloud 29, MariaDB, Redis et proxy TLS en conteneurs Docker Compose
- **OS / Version** : Linux serveur; Nextcloud 29 (branche ancienne) vers une version maintenue
- **Catégorie** : conteneurs / migration

---

## Problème précis à résoudre

Obtenir une sauvegarde cohérente et prouver qu'elle se restaure.

## 1. Hors-Production (Lab / Test / POC)

1. Activer le mode maintenance Nextcloud avec la méthode prise en charge par l'image déployée (voir la documentation de votre image; `occ maintenance:mode --on` exécuté dans le conteneur applicatif).
   👉 Explication : on arrête les écritures utilisateur.

2. Exporter la base avec l'outil natif de la base de données (par exemple `mariadb-dump` ou `mysqldump` exécuté dans le conteneur `db`, selon l'image) et sauvegarder chaque volume persistant listé à l'étape 1.
   👉 Explication : la sauvegarde combine base et fichiers au même instant.

3. Calculer les sommes de contrôle des archives (nom de fichier d'exemple à remplacer) :
   ```bash
   sha256sum sauvegarde-nextcloud.tar.gz > sauvegarde-nextcloud.tar.gz.sha256
   sha256sum -c sauvegarde-nextcloud.tar.gz.sha256
   ```
   👉 Explication : la commande doit afficher OK.

4. Restaurer cette sauvegarde dans un environnement isolé et vérifier la connexion et les fichiers.
   👉 Explication : une sauvegarde non testée n'est pas fiable.

## 2. Production — Contrôles

Stocker la sauvegarde hors du stockage Docker et noter la durée de restauration.

## 3. Production — Sécurité

- Ne pas utiliser `docker compose down -v`, `docker volume prune` ni `docker system prune --volumes` dans cette procédure.
- Chiffrer et protéger les sauvegardes (elles contiennent les données utilisateurs).

## Validation et retour arrière

- **Validation** : Restauration isolée réussie, sommes de contrôle correctes.
- **Retour arrière** : Désactiver le mode maintenance (`occ maintenance:mode --off`) si la migration est abandonnée à ce stade.

## Si le problème n'est pas résolu

- [Nextcloud — Admin manual : upgrade](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/upgrade.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet migration Nextcloud 29 conteneurisé](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis#2-sauvegarder-et-tester-la-restauration)