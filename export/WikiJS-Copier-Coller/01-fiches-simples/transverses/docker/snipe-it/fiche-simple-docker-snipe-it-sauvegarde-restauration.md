# Fiche_Simple_-_Docker_Snipe-IT_Sauvegarde_Restauration.md

- **Environnement** : Hôte Docker avec Docker Compose v2 et réseau Traefik existant
- **OS / Version** : Hôte Linux maintenu; Snipe-IT 8.8.3; MariaDB 11.4.7
- **Catégorie** : ITSM / gestion des actifs

---

## Problème précis à résoudre

Sauvegarder base, pièces jointes et secrets, et tester la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. **Admin > Backups** pour générer l'archive depuis l'interface.
   👉 Explication : produit une archive avec dump SQL et pièces jointes.

2. Sauvegarde en ligne de commande :
   ```bash
   docker compose exec -T app php artisan snipeit:backup
   ```
   👉 Explication : Équivalent en ligne de commande, à lancer en maintenance planifiée.

3. Copier l'archive hors hôte, chiffrée, et sauvegarder séparément `.env`, `APP_KEY`, le Compose utilisé et les références d'image.
   👉 Explication : ces éléments ne sont pas tous dans l'archive.

4. Tester la restauration sur une stack isolée.
   👉 Explication : une restauration déconnecte les utilisateurs et ne réécrit pas `.env`.

## 2. Production — Contrôles

Planifier la sauvegarde et tester la restauration périodiquement.

## 3. Production — Sécurité

- Archives et `.env` contiennent des secrets : chiffrer et restreindre l'accès.

## Validation et retour arrière

- **Validation** : archive hors hôte et restauration testée.
- **Retour arrière** : restaurer l'archive sur la stack isolée avant toute opération en production.

## Si le problème n'est pas résolu

- [Snipe-IT — Docker Compose](https://snipe-it.readme.io/docs/docker)
- [Guide complet — étape 6](/02-fiches-completes/transverses/docker/installation-deploiement/39-deploiement-snipe-it-8-docker-mariadb-traefik#6-sauvegarde-et-restauration)