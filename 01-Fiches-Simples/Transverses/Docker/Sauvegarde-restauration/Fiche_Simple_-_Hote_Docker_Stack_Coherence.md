# Fiche_Simple_-_Hote_Docker_Stack_Coherence.md

- **Environnement** : Hôte Linux Docker avec stacks Compose et volumes persistants
- **OS / Version** : Distribution maintenue; Docker Engine et Compose v2
- **Catégorie** : conteneurs / sauvegarde-restauration
- **Tags** : `docker`, `compose`, `sauvegarde`, `coherence`

---

## Problème précis à résoudre

Choisir comment obtenir une sauvegarde cohérente selon le type de données.

## 1. Hors-Production (Lab / Test / POC)

1. Pour les bases de données, faire un dump logique avec l'outil de la base (exemple MariaDB; remplacer le nom du conteneur) :
   ```bash
   docker exec NOM_CONTENEUR_DB sh -c 'mariadb-dump --single-transaction --all-databases -uroot -p"$MARIADB_ROOT_PASSWORD"' > dump.sql
   ```
   👉 Explication : le mot de passe est lu dans l'environnement du conteneur, jamais tapé en clair; un snapshot brut d'un volume actif n'est pas cohérent.

2. Pour les fichiers applicatifs, arrêter les écritures avant copie :
   ```bash
   docker compose stop APPLICATION
   ```
   👉 Explication : remplacer `APPLICATION` par le service du fichier `docker-compose.yml`; ou activer le mode maintenance de l'application.

3. Pour une stack à plusieurs services, sauvegarder ensemble base, fichiers et configuration :
   ```bash
   docker compose config > compose.resolved.yml
   tar -czf stack-$(date +%F).tar.gz dump.sql compose.resolved.yml volumes/
   ```
   👉 Explication : `compose.resolved.yml` fixe la configuration utilisée; ne pas y laisser de secrets en clair dans l'archive partagée. Adapter `volumes/` à l'arborescence réelle.

4. Envoyer vers une destination séparée, chiffrée et protégée contre l'effacement :
   ```bash
   restic -r DEPOT backup stack-AAAA-MM-JJ.tar.gz
   ```
   👉 Explication : remplacer `DEPOT` et la date; le mot de passe du dépôt est fourni via `RESTIC_PASSWORD_FILE`.

## 2. Production — Contrôles

Documenter la méthode retenue par stack, la fenêtre de sauvegarde et la rétention.

## 3. Production — Sécurité

- Chiffrer la destination et séparer les clés des archives.
- Protéger la destination contre l'effacement.

## Validation et retour arrière

- **Validation** : Méthode écrite et validée pour chaque stack.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [Docker — Volumes et sauvegarde/restauration](https://docs.docker.com/engine/storage/volumes/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet — définir la méthode de cohérence](../../../../02-Fiches-Completes/Transverses/Docker/Autres/37_Sauvegarde_Restauration_Stacks_Docker.md#2-definir-la-methode-de-coherence)
