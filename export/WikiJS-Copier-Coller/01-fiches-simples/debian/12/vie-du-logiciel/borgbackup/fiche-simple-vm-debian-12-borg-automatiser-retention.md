# Fiche_Simple_-_VM_Debian_12_Borg_Automatiser_Retention.md

- **Environnement** : Debian 12 avec compte de sauvegarde dédié, unité/timer systemd ou ordonnanceur approuvé
- **OS / Version** : Debian 12; BorgBackup
- **Catégorie** : sauvegarde / automatisation et rétention

---

## Problème précis à résoudre

Automatiser les archives et appliquer une rétention sans supprimer de sauvegardes avant d'avoir examiné les effets.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le service systemd :
   ```bash
   sudo tee /etc/systemd/system/borg-backup.service >/dev/null <<'EOF'
   [Unit]
   Description=Sauvegarde Borg

   [Service]
   Type=oneshot
   EnvironmentFile=/etc/borg/borg.env
   ExecStart=/usr/bin/borg create --stats --compression zstd,3 ${REPO}::{hostname}-{now:%%Y-%%m-%%d_%%H:%%M} /etc /home /var/www
   EOF
   ```
   👉 Explication : `/etc/borg/borg.env` (0600, root) contient `REPO=` et `BORG_PASSCOMMAND=`; aucun secret dans l'unité. Les `%%` sont requis par systemd.

2. Créer le timer et l'activer :
   ```bash
   sudo tee /etc/systemd/system/borg-backup.timer >/dev/null <<'EOF'
   [Timer]
   OnCalendar=*-*-* 02:00:00
   Persistent=true

   [Install]
   WantedBy=timers.target
   EOF
   sudo systemctl daemon-reload
   sudo systemctl enable --now borg-backup.timer
   systemctl list-timers borg-backup.timer
   ```
   👉 Explication : vérifier ensuite code retour, `journalctl -u borg-backup` et l'espace du dépôt.

3. Simuler la rétention :
   ```bash
   sudo -E borg prune --dry-run --list --keep-daily=7 --keep-weekly=4 --keep-monthly=12 "$REPO"
   ```
   👉 Explication : relire la liste des archives conservées et supprimées.

4. Appliquer, en retirant `--dry-run`, seulement après validation et copie indépendante :
   ```bash
   sudo -E borg prune --list --keep-daily=7 --keep-weekly=4 --keep-monthly=12 "$REPO"
   ```
   👉 Explication : la suppression est définitive.

## 2. Production — Contrôles

Valider calendrier, rétention, alerte, accès, charge, journaux, plafond d'espace et procédure de désactivation.

## 3. Production — Sécurité

- Ne pas retirer `--dry-run` avant examen des archives concernées.
- Séparer les privilèges de création d'archive et de purge si la conception le permet.
- Ne pas stocker les secrets en clair dans un script ou timer accessible aux utilisateurs.
- Ne pas supprimer la seule copie restaurable par une politique mal comprise.

## Validation et retour arrière

- **Validation** : tâche exécutée, alerte vérifiée, liste de rétention approuvée et copie indépendante présente.
- **Retour arrière** : désactiver la planification créée et conserver journaux/scripts jusqu'à validation d'une méthode de remplacement.

## Si le problème n'est pas résolu

- [BorgBackup — prune](https://borgbackup.readthedocs.io/en/stable/usage/prune.html)
- [BorgBackup — documentation](https://borgbackup.readthedocs.io/en/stable/)
- [Guide complet BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)