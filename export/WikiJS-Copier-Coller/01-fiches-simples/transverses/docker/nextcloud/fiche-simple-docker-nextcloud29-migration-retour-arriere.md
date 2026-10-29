# Fiche_Simple_-_Docker_Nextcloud29_Migration_Retour_Arriere.md

- **Environnement** : Hôte Linux avec Nextcloud 29, MariaDB, Redis et proxy TLS en conteneurs Docker Compose
- **OS / Version** : Linux serveur; Nextcloud 29 (branche ancienne) vers une version maintenue
- **Catégorie** : conteneurs / migration

---

## Problème précis à résoudre

Revenir à un état cohérent si la migration échoue.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter la stack sans supprimer les volumes :
   ```bash
   docker compose stop
   docker compose ps
   ```
   👉 Explication : les données restent intactes.

2. Remettre l'ensemble cohérent : images précédentes dans le fichier Compose, base et volumes restaurés depuis la sauvegarde de l'étape 2.
   👉 Explication : restaurer uniquement l'image après migration du schéma casserait la base.

3. Redémarrer et contrôler :
   ```bash
   docker compose up -d
   docker compose ps
   docker compose logs --tail 100 app
   ```
   👉 Explication : l'ancienne version doit redémarrer normalement.

4. Conserver le mode maintenance jusqu'à validation, puis documenter la version cible et la date de retrait de Nextcloud 29.
   👉 Explication : la branche 29 doit être remplacée.

## 2. Production — Contrôles

Documenter la cause de l'échec avant une nouvelle tentative.

## 3. Production — Sécurité

- Ne jamais restaurer partiellement (image seule ou base seule).
- Ne pas supprimer les volumes d'origine avant validation.

## Validation et retour arrière

- **Validation** : La version précédente fonctionne avec ses données.
- **Retour arrière** : Cette fiche est le retour arrière : en cas de doute, rester sur la restauration complète d'une sauvegarde testée.

## Si le problème n'est pas résolu

- [Nextcloud — Admin manual : upgrade](https://docs.nextcloud.com/server/latest/admin_manual/maintenance/upgrade.html)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet migration Nextcloud 29 conteneurisé](/02-fiches-completes/transverses/docker/installation-deploiement/05-cloud-prive-nextcloud-29-docker-mariadb-redis#5-retour-arriere)