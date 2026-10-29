# Fiche_Simple_-_VM_Debian_13_rsync_Copier_Sans_Suppression.md

- **Environnement** : Debian 13; copie pilote vers répertoire de destination dédié
- **OS / Version** : Debian 13 Trixie; rsync du dépôt Debian
- **Catégorie** : sauvegarde de fichiers / copie

---

## Problème précis à résoudre

Exécuter une première copie approuvée sans propager les suppressions de la source vers la destination.

## 1. Hors-Production (Lab / Test / POC)

1. Refaire l'aperçu validé :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --dry-run --itemize-changes --stats -e ssh "$SRC" "$DST"
   ```
   👉 Explication : confirmer que rien d'inattendu n'est listé.

2. Exécuter la copie en retirant uniquement `--dry-run` :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --itemize-changes --stats --partial-dir=.rsync-partial --timeout=60 -e ssh "$SRC" "$DST"
   echo "code=$?"
   ```
   👉 Explication : sans `--delete`, les fichiers supprimés à la source restent à la destination; `0` indique le succès.

3. Vérifier la destination :
   ```bash
   ssh utilisateur@sauvegarde.example.net 'du -sh /srv/backup/data; ls -la /srv/backup/data | head'
   ```
   👉 Explication : volume et contenu doivent correspondre à la source.

4. Journaliser le résultat :
   ```bash
   rsync -aHAX --numeric-ids --one-file-system --itemize-changes --log-file=/var/log/rsync-backup.log -e ssh "$SRC" "$DST"
   ```
   👉 Explication : toute valeur de retour autre que `0` doit déclencher une alerte et la lecture du journal.

## 2. Production — Contrôles

Définir fenêtre, débit réseau, surveillance, capacité, responsable, gestion d'erreur et reprise sur interruption.

## 3. Production — Sécurité

- Ne pas exécuter avec des privilèges élevés sans besoin justifié.
- Protéger la destination et les journaux contre l'accès non autorisé.
- Ne pas publier les ports SSH ou rsync au-delà des flux nécessaires.
- Ne pas considérer une commande terminée comme une validation de restauration.

## Validation et retour arrière

- **Validation** : code retour 0, statistiques attendues et fichiers de contrôle présents.
- **Retour arrière** : sans option de suppression, identifier les seuls fichiers ajoutés par l'opération et obtenir validation avant tout nettoyage.

## Si le problème n'est pas résolu

- [rsync — page de manuel officielle](https://download.samba.org/pub/rsync/rsync.1.html)
- [Guide complet rsync Debian 13](/02-fiches-completes/debian/13/autres/92-sauvegarde-fichiers-rsync-debian-13#4-executer-la-copie-sans-suppression)