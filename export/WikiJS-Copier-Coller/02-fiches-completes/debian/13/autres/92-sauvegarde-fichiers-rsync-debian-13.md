# Copier et sauvegarder des fichiers avec rsync sur Debian 13

- **Type de fiche** : Autres — copie / sauvegarde de fichiers
- **Environnement** : serveurs Debian 13 Trixie, transfert local ou via SSH
- **OS / Version** : Debian 13; paquet `rsync` 3.5.0+ds1-0+deb13u1 (version du dépôt Debian vérifiée le 29 octobre 2026)
- **Rôle** : Prévisualiser puis exécuter une copie de fichiers, avec garde-fous contre les suppressions

## 1. Périmètre et limites

Fiche simple : [cadrer le besoin](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-cadrer-besoin).

`rsync` synchronise des arborescences. Une copie miroir n'est pas une sauvegarde historisée : une suppression ou un chiffrement par ransomware se propage à la destination au prochain passage. Pour des versions, de la déduplication et du chiffrement, utiliser [BorgBackup](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12) ou [Restic](/02-fiches-completes/ubuntu/toutes-versions/autres/29-sauvegarde-restauration-ubuntu-server-restic). Ce guide couvre le mode ligne de commande par SSH; le démon `rsyncd` n'est pas traité. Les bases de données en cours d'écriture exigent un dump ou une méthode cohérente préalable. Ce guide n'a pas été testé sur Debian 13.

## 2. Installer et préparer

Fiche simple : [installer et préparer rsync](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-installer-preparer).

```bash
sudo apt update
sudo apt install rsync
rsync --version | head -1
```

Pour une destination distante, utiliser une clé SSH dédiée, limitée à la destination. Tester la connexion avant la première synchronisation. Définir explicitement les variables, sans espaces ambigus :

```bash
SRC=/srv/data/
DST=utilisateur@sauvegarde.example.net:/srv/backup/data/
```

Attention à la barre oblique finale : `/srv/data/` copie le **contenu** du répertoire, `/srv/data` copie le répertoire lui-même. Vérifier chaque chemin avant l'exécution.

## 3. Prévisualiser (mode par défaut)

Fiche simple : [prévisualiser les changements](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-previsualiser).

Toujours commencer avec `--dry-run` (`-n`). Aucun fichier n'est modifié; `--itemize-changes` (`-i`) montre le détail des changements :

```bash
rsync -aHAX --numeric-ids --one-file-system --dry-run --itemize-changes --stats -e ssh "$SRC" "$DST"
```

`-a` préserve permissions, dates, liens symboliques, propriétaire et groupe; `-H` liens physiques; `-A` ACL; `-X` attributs étendus (la destination doit les prendre en charge); `--numeric-ids` évite le remappage des UID/GID; `--one-file-system` empêche de traverser les autres montages. Relire la liste, puis contrôler le nombre de fichiers et le volume dans `--stats`.

## 4. Exécuter la copie sans suppression

Fiche simple : [copier sans suppression](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-copier-sans-suppression).

Après validation de l'aperçu, retirer uniquement `--dry-run` :

```bash
rsync -aHAX --numeric-ids --one-file-system --itemize-changes --stats --partial-dir=.rsync-partial --timeout=60 -e ssh "$SRC" "$DST"
```

Sans `--delete`, les fichiers supprimés à la source restent à la destination. Ce mode est le plus sûr pour une première copie.

## 5. Modes destructifs (à n'utiliser qu'avec une approbation)

Fiche simple : [gérer les suppressions avec prudence](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-gerer-suppressions).

| Option | Effet | Garde-fou |
|---|---|---|
| `--delete` (et variantes `--delete-before/-during/-after`) | Supprime à la destination ce qui n'existe plus à la source | Toujours précédé d'un `--dry-run --itemize-changes`; ajouter `--max-delete=NUM` |
| `--delete-excluded` | Supprime aussi les fichiers exclus côté destination | Ne pas l'employer sans relire toutes les exclusions |
| `--remove-source-files` | Supprime les fichiers sources après transfert | Réserver à un flux de transfert validé, jamais à une sauvegarde |
| `--inplace` | Réécrit les fichiers destination directement | Risque d'état incohérent en cas d'interruption |
| `--backup --backup-dir=DIR` | Conserve les fichiers écrasés ou supprimés | Mode préféré avec `--delete` pour garder une trace |

Exemple de miroir contrôlé, à exécuter d'abord avec `--dry-run` :

```bash
rsync -aHAX --numeric-ids --one-file-system --delete --max-delete=50 --backup --backup-dir=../deleted-$(date +%F) --dry-run --itemize-changes -e ssh "$SRC" "$DST"
```

Un `--backup-dir` relatif se place relativement au répertoire de destination. Si le plafond `--max-delete` est dépassé, rsync interrompt les suppressions : examiner la cause avant de relever la limite. Une source vide ou un montage manquant donne un miroir vide : vérifier que la source est montée avant tout `--delete`.

## 6. Valider et restaurer

Fiche simple : [valider et tester la restauration](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-valider-restaurer).

- Après la copie, relancer la commande avec `--dry-run --itemize-changes` : aucune ligne de changement ne doit apparaître.
- Pour un contrôle plus strict (lecture complète), ajouter `--checksum` (`-c`) en aperçu; coûteux sur gros volumes.
- Restauration : inverser source et destination et **toujours** commencer par `--dry-run`, vers un répertoire de test (`/tmp/restore-test/`), pas vers la source active.
- Contrôler propriétaires, ACL et un échantillon de fichiers ouverts avec leur application.
- Le code retour 0 indique le succès; toute autre valeur doit déclencher une alerte et la lecture du journal. Les statuts d'erreur sont décrits dans la page de manuel.

## 7. Retour arrière

Fiche simple : [préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/rsync/fiche-simple-vm-debian-13-rsync-retour-arriere).

Sans `--delete`, supprimer uniquement les fichiers copiés à tort (liste issue de `--itemize-changes`) après relecture. Avec `--backup-dir`, remettre en place les fichiers conservés dans `deleted-AAAA-MM-JJ`. Sans sauvegarde indépendante de la destination, une suppression par `--delete` n'est pas récupérable : c'est la raison de l'aperçu obligatoire, de `--max-delete` et d'une copie séparée (instantanés du stockage destination, Borg/Restic).

## Sources

- [Debian — paquet rsync (trixie)](https://packages.debian.org/trixie/rsync)
- [rsync — page de manuel officielle (Samba)](https://download.samba.org/pub/rsync/rsync.1.html)
- [rsync — site officiel](https://rsync.samba.org/)

Aucune sauvegarde ou restauration n'a été testée sur Debian 13. Conserver les statuts **À revoir** et **À tester**.