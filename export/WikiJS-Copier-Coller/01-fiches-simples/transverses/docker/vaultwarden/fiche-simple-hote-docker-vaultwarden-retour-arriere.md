# Fiche_Simple_-_Hote_Docker_Vaultwarden_Retour_Arriere.md

- **Environnement** : Hôte Linux avec Docker Engine et plugin Compose, Vaultwarden SQLite derrière un reverse proxy HTTPS
- **OS / Version** : Hôte Linux + Docker; image vaultwarden/server (tag à figer après validation)
- **Catégorie** : gestionnaire de mots de passe auto-hébergé

---

## Problème précis à résoudre

Mettre à jour Vaultwarden ou revenir à la version précédente en sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute mise à jour, sauvegarder (voir la fiche Sauvegarder) et noter le tag ou digest actuel.
   👉 Explication : il servira au retour arrière.

2. Mettre à jour :
   ```bash
   docker compose pull
   docker compose up -d
   ```
   👉 Explication : on télécharge la nouvelle image puis on recrée le conteneur.

3. En cas de problème, remettre l'ancien tag ou digest dans `compose.yaml` puis :
   ```bash
   docker compose up -d
   ```
   👉 Explication : le conteneur repart sur l'ancienne image.

4. Si le schéma de base a été migré, restaurer la sauvegarde d'avant mise à jour.
   👉 Explication : un retour d'image seul peut ne pas suffire.

5. Pour retirer le service :
   ```bash
   docker compose down
   ```
   👉 Explication : cela n'efface pas `vw-data`; ne supprimer ce dossier qu'après confirmation de la restauration.

## 2. Production — Contrôles

Documenter la version avant/après chaque mise à jour et la fenêtre de maintenance.

## 3. Production — Sécurité

- Ne jamais supprimer `vw-data` sans sauvegarde restaurée avec succès.
- Ne pas mettre à jour sans sauvegarde récente.

## Validation et retour arrière

- **Validation** : Après mise à jour ou retour, connexion OK et élément de test lisible.
- **Retour arrière** : C'est l'objet même de la fiche : ancien tag + restauration de la sauvegarde.

## Si le problème n'est pas résolu

- [Vaultwarden — Using Docker Compose](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [Vaultwarden — Backing up your vault](https://github.com/dani-garcia/vaultwarden/wiki/Backing-up-your-vault)
- [Guide complet — retour arrière et mise à jour](/02-fiches-completes/transverses/docker/installation-deploiement/94-deploiement-vaultwarden-docker-compose#8-retour-arriere)