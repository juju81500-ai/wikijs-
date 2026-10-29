# Fiche_Simple_-_VM_Debian_13_rsync_Retour_Arriere.md

- **Environnement** : Debian 13; destination rsync et copies de sécurité accessibles à l'administrateur
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : sauvegarde de fichiers / retour arrière

---

## Problème précis à résoudre

Récupérer une destination affectée par une synchronisation incorrecte sans écraser d'autres données.

## 1. Hors-Production (Lab / Test / POC)

1. Sans `--delete`, lister les fichiers copiés à tort depuis le journal :
   ```bash
   grep '^>f+++++++++' /var/log/rsync-backup.log | head
   ```
   👉 Explication : les lignes `>f+++++++++` correspondent aux nouveaux fichiers; relire la liste avant toute suppression.

2. Supprimer uniquement ces fichiers après relecture (à la destination) :
   ```bash
   ssh utilisateur@sauvegarde.example.net 'rm -v /srv/backup/data/CHEMIN/FICHIER'
   ```
   👉 Explication : remplacer le chemin; aucune suppression récursive à l'aveugle.

3. Avec `--backup-dir`, remettre en place les fichiers conservés :
   ```bash
   ssh utilisateur@sauvegarde.example.net 'ls /srv/backup/deleted-AAAA-MM-JJ | head'
   rsync -aHAX --numeric-ids --dry-run --itemize-changes -e ssh utilisateur@sauvegarde.example.net:/srv/backup/deleted-AAAA-MM-JJ/ /srv/backup/data/
   ```
   👉 Explication : remplacer la date; relire l'aperçu avant de retirer `--dry-run`.

4. Prévoir une sauvegarde indépendante de la destination.
   👉 Explication : sans elle, une suppression par `--delete` n'est pas récupérable.

## 2. Production — Contrôles

Définir autorité d'arrêt, approbation de restauration, sources de récupération, propriétaires des données et critères de clôture d'incident.

## 3. Production — Sécurité

- Ne pas lancer une seconde synchronisation miroir pour « réparer » sans analyse.
- Ne pas supprimer la destination ou le dossier de sauvegarde avant préservation des preuves.
- Isoler la tâche si une suppression/chiffrement inexpliqué est suspecté.
- Respecter les règles de conservation et de protection des données restaurées.

## Validation et retour arrière

- **Validation** : fichiers restaurés depuis une source indépendante vérifiée, intégrité et permissions conformes.
- **Retour arrière** : garder un snapshot de l'état actuel avant restauration; revenir à celui-ci si la restauration détériore la situation.

## Si le problème n'est pas résolu

- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13#7-retour-arriere)