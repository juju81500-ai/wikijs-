# Fiche_Simple_-_Hote_Docker_Stack_Inventorier.md

- **Environnement** : Hôte Linux Docker avec stacks Compose et volumes persistants
- **OS / Version** : Distribution maintenue; Docker Engine et Compose v2
- **Catégorie** : conteneurs / sauvegarde-restauration
- **Tags** : `docker`, `compose`, `sauvegarde`, `inventaire`

---

## Problème précis à résoudre

Relever tout ce qui compose la stack avant de la sauvegarder.

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans le dossier du projet (`/opt/docker/mon-projet` est un exemple à remplacer) :
   ```bash
   cd /opt/docker/mon-projet
   ```
   👉 Explication : les commandes Compose s'appliquent au projet courant.

2. Valider la configuration sans l'afficher :
   ```bash
   docker compose config --quiet
   ```
   👉 Explication : la commande signale une erreur sans afficher les valeurs sensibles.

3. Lister services et volumes :
   ```bash
   docker compose ps
   docker volume ls
   ```
   👉 Explication : on repère conteneurs, volumes nommés et état.

4. Inspecter un conteneur (`mon-projet-db-1` est un exemple à remplacer) :
   ```bash
   docker inspect mon-projet-db-1
   ```
   👉 Explication : on relève images, montages, réseaux et ports.

5. Relever fichiers `.env`, secrets, images et versions, bind mounts, bases, dépendances externes et ordre de démarrage dans un inventaire protégé.
   👉 Explication : l'inventaire guide la sauvegarde et la restauration.

## 2. Production — Contrôles

Protéger l'inventaire : il peut contenir des secrets.

## 3. Production — Sécurité

- Ne pas partager la sortie complète de `docker compose config` : l'interpolation peut révéler des valeurs sensibles.

## Validation et retour arrière

- **Validation** : Inventaire complet des services, volumes, secrets et dépendances.
- **Retour arrière** : Lecture seule : rien à annuler.

## Si le problème n'est pas résolu

- [Docker — Volumes et sauvegarde/restauration](https://docs.docker.com/engine/storage/volumes/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Guide complet — inventorier la stack](../../../../02-Fiches-Completes/Transverses/Docker/Autres/37_Sauvegarde_Restauration_Stacks_Docker.md#1-inventorier-la-stack)
