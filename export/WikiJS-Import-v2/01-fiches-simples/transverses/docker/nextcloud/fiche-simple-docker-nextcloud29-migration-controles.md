---
title: "Fiche Simple - Docker Nextcloud29 Migration Controles"
description: "Vérifier le bon fonctionnement de Nextcloud après la mise à niveau."
published: true
date: 2026-10-29T19:42:44Z
tags: ["nextcloud", "docker", "migration", "mariadb", "redis", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Docker_Nextcloud29_Migration_Controles.md

- **Environnement** : Hôte Linux avec Nextcloud 29, MariaDB, Redis et proxy TLS en conteneurs Docker Compose
- **OS / Version** : Linux serveur; Nextcloud 29 (branche ancienne) vers une version maintenue
- **Catégorie** : conteneurs / migration
- **Tags** : `nextcloud`, `docker`, `migration`, `mariadb`, `redis`, `tls`

---

## Problème précis à résoudre

Vérifier le bon fonctionnement de Nextcloud après la mise à niveau.

## 1. Hors-Production (Lab / Test / POC)

1. Lire l'état et les journaux :
   ```bash
   docker compose ps
   docker compose logs --tail 200 app db redis
   ```
   👉 Explication : aucun conteneur ne doit redémarrer en boucle.

2. Se connecter, téléverser puis télécharger un fichier de test, et ouvrir **Administration settings > Overview**.
   👉 Explication : on vérifie fichiers, tâches de fond et avertissements d'administration.

3. Tester l'envoi d'un courriel (**Administration settings > Basic settings**), l'accès aux partages et la validité TLS dans le navigateur.
   👉 Explication : ces points cassent souvent après migration.

4. Contrôler que Redis est utilisé pour le verrouillage transactionnel si l'architecture le prévoit.
   👉 Explication : sans Redis, des conflits de verrouillage peuvent apparaître.

## 2. Production — Contrôles

Consigner les résultats et désactiver le mode maintenance seulement après validation.

## 3. Production — Sécurité

- Vérifier que les en-têtes TLS et le certificat restent corrects.
- Ne pas laisser de compte de test actif.

## Validation et retour arrière

- **Validation** : Connexion, transfert, tâches de fond, TLS et courriels fonctionnent.
- **Retour arrière** : Appliquer le plan de retour arrière de l'étape 5.

## Si le problème n'est pas résolu

- [Nextcloud — Admin manual : upgrade](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/upgrade.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet migration Nextcloud 29 conteneurisé](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis#4-controles)