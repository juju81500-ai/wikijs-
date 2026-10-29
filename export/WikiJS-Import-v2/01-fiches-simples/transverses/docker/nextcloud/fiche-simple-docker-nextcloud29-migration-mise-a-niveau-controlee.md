---
title: "Fiche Simple - Docker Nextcloud29 Migration Mise A Niveau Controlee"
description: "Mettre à niveau Nextcloud version par version avec des images épinglées."
published: true
date: 2026-10-29T19:42:44Z
tags: ["nextcloud", "docker", "migration", "mariadb", "redis", "tls"]
editor: markdown
dateCreated: 2026-10-29T19:42:44Z
dateModified: 2026-10-29T19:42:44Z
---

# Fiche_Simple_-_Docker_Nextcloud29_Migration_Mise_A_Niveau_Controlee.md

- **Environnement** : Hôte Linux avec Nextcloud 29, MariaDB, Redis et proxy TLS en conteneurs Docker Compose
- **OS / Version** : Linux serveur; Nextcloud 29 (branche ancienne) vers une version maintenue
- **Catégorie** : conteneurs / migration
- **Tags** : `nextcloud`, `docker`, `migration`, `mariadb`, `redis`, `tls`

---

## Problème précis à résoudre

Mettre à niveau Nextcloud version par version avec des images épinglées.

## 1. Hors-Production (Lab / Test / POC)

1. Choisir une version Nextcloud maintenue, compatible avec les versions PHP, MariaDB et Redis retenues.
   👉 Explication : la compatibilité évite une base ou un runtime non supporté.

2. Dans le fichier Compose, remplacer le tag de l'image Nextcloud par la version explicite suivante (jamais `latest`); ne changer qu'une version majeure à la fois.
   👉 Explication : les sauts de versions majeures ne sont pas supportés.

3. Valider le fichier puis lancer la mise à niveau :
   ```bash
   docker compose config --quiet
   docker compose pull
   docker compose up -d
   docker compose logs -f --tail 100 app
   ```
   👉 Explication : l'image applique la mise à niveau au démarrage selon sa documentation; suivre les journaux (Ctrl+C pour quitter le suivi).

4. N'ouvrir le trafic utilisateur qu'après contrôle d'intégrité et vérification des applications dans **Administration settings > Overview**.
   👉 Explication : on valide avant d'exposer.

## 2. Production — Contrôles

Ne pas modifier en même temps le moteur de base et Nextcloud sans plan de compatibilité indépendant.

## 3. Production — Sécurité

- Images épinglées par version explicite.
- Garder le mode maintenance actif jusqu'à validation.

## Validation et retour arrière

- **Validation** : Journaux sans erreur, version attendue affichée, applications compatibles.
- **Retour arrière** : Remettre l'ensemble cohérent images + base + volumes sauvegardés; ne pas restaurer seulement l'image applicative.

## Si le problème n'est pas résolu

- [Nextcloud — Admin manual : upgrade](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/upgrade.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet migration Nextcloud 29 conteneurisé](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis#3-mise-a-niveau-controlee)