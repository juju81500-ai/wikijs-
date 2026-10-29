# 📄 Fiche_Simple_-_Docker_Sauvegarder_Restaurer_Volume.md

- **Environnement** : Hôte Docker Debian 12 ou Ubuntu 24.04
- **OS / Version** : Docker Engine avec volumes nommés
- **Catégorie** : Sauvegarde / Conteneurs
- **Tags** : `[docker]`, `[volumes]`, `[sauvegarde]`, `[restauration]`, `[maintenance]`

## 🎯 Problème précis à résoudre
Sauvegarder et restaurer un volume Docker nommé en arrêtant les écritures applicatives, sans copier directement les répertoires internes du démon Docker.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Identifier le volume et préparer un répertoire de sauvegarde :
   ```bash
   docker volume ls
   VOLUME="nom_volume_reel"
   BACKUP_DIR="$PWD/backup"
   mkdir -p "$BACKUP_DIR"
   ```
2. Arrêter l'application qui écrit dans le volume, puis créer une archive :
   ```bash
   docker compose stop
   docker run --rm -v "$VOLUME:/source:ro" -v "$BACKUP_DIR:/backup" alpine:3.20 sh -c 'tar czf /backup/volume.tar.gz -C /source .'
   ```
3. Vérifier que l'archive peut être lue :
   ```bash
   tar tzf "$BACKUP_DIR/volume.tar.gz" | head
   ```
   👉 *Explication : une base de données exige d'abord une sauvegarde native cohérente; l'archive brute seule ne garantit pas sa cohérence transactionnelle.*

## ⚡ 2. Production — Façon Simplifiée
1. Identifier le vrai nom du volume, qui peut inclure le préfixe du projet Compose. Arrêter proprement les services écrivains ou effectuer un dump applicatif cohérent.
2. Créer le répertoire de sauvegarde avec des droits restreints, puis archiver le volume en lecture seule :
   ```bash
   sudo install -d -o root -g root -m 0700 /srv/backups/docker
   VOLUME="nom_volume_reel"
   sudo docker run --rm -v "$VOLUME:/source:ro" -v /srv/backups/docker:/backup alpine:3.20 sh -c 'tar czf /backup/volume-$(date +%F).tar.gz -C /source .'
   ```
3. Tester la restauration dans un nouveau volume, pas sur les données de production :
   ```bash
   docker volume create volume_test_restore
   ARCHIVE="volume-2026-10-27.tar.gz"  # remplacer par le nom exact de l'archive
   sudo docker run --rm -e ARCHIVE="$ARCHIVE" -v volume_test_restore:/target -v /srv/backups/docker:/backup alpine:3.20 sh -c 'tar xzf "/backup/$ARCHIVE" -C /target'
   docker run --rm -v volume_test_restore:/data alpine:3.20 ls -la /data
   ```
   👉 *Explication : remplacer `<date>` par le nom réel de l'archive; vérifier propriétaires, permissions et application avant toute bascule.*

## 🔒 3. Production — Façon Sécurisée
1. Protéger les archives comme les données sources; elles peuvent contenir des secrets et des données personnelles.
2. Copier la sauvegarde hors de l'hôte et appliquer une rétention documentée. Un volume d'archive local n'est pas une sauvegarde indépendante.
3. Pour PostgreSQL, MariaDB et autres bases, privilégier les outils de sauvegarde natifs et tester une restauration complète.

## ✅ Validation et retour arrière
- Vérifier l'intégrité de l'archive et réaliser régulièrement une restauration sur un volume de test.
- Ne pas supprimer le volume d'origine avant validation fonctionnelle de la copie restaurée.
- Redémarrer les services après la sauvegarde et contrôler leurs journaux et leur état de santé.