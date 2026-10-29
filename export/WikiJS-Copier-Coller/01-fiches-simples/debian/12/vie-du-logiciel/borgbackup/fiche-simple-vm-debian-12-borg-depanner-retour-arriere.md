# Fiche_Simple_-_VM_Debian_12_Borg_Depanner_Retour_Arriere.md

- **Environnement** : Debian 12 et dépôt Borg en erreur; opérateur autorisé avec accès aux journaux
- **OS / Version** : Debian 12 Bookworm
- **Catégorie** : sauvegarde / dépannage et reprise

---

## Problème précis à résoudre

Diagnostiquer un échec Borg sans supprimer les archives nécessaires ni aggraver une erreur de dépôt.

## 1. Hors-Production (Lab / Test / POC)

1. Ne rien supprimer; inventorier :
   ```bash
   borg list "$REPO"
   borg info "$REPO"
   ```
   👉 Explication : pas de `prune` ni `delete` avant d'avoir compris l'erreur.

2. Vérifier accès, espace et journaux :
   ```bash
   ssh borgbackup@sauvegarde.example.net 'df -h /srv/borg/depot'
   journalctl -u borg-backup --since '-1 day' --no-pager
   ```
   👉 Explication : les causes fréquentes sont dépôt verrouillé, espace plein, clé SSH ou phrase de passe incorrecte.

3. Si le dépôt est verrouillé après interruption :
   ```bash
   borg break-lock "$REPO"
   ```
   👉 Explication : uniquement si aucun autre `borg` ne tourne.

4. Annuler l'automatisation :
   ```bash
   sudo systemctl disable --now borg-backup.timer
   sudo rm /etc/systemd/system/borg-backup.timer /etc/systemd/system/borg-backup.service
   sudo systemctl daemon-reload
   ```
   👉 Explication : conserver archives et clé; tester une restauration vers une destination de test.

## 2. Production — Contrôles

Appliquer la procédure d'incident, prévenir le propriétaire, préserver les éléments d'analyse et faire approuver toute opération de réparation.

## 3. Production — Sécurité

- Ne pas supprimer le dépôt ou les archives pour résoudre un problème d'accès.
- Ne pas transmettre clés, phrases de passe ou journaux complets hors des canaux protégés.
- Ne pas lancer une réparation destructive sur l'unique copie.
- Protéger les archives et les clés selon leur classification.

## Validation et retour arrière

- **Validation** : cause identifiée, dépôt préservé et restauration testée avant remise en production.
- **Retour arrière** : désactiver l'automatisation fautive, conserver les archives et revenir à la méthode précédente approuvée.

## Si le problème n'est pas résolu

- [BorgBackup — dépannage et documentation](https://borgbackup.readthedocs.io/en/stable/)
- [BorgBackup — vérifier un dépôt](https://borgbackup.readthedocs.io/en/stable/usage/check.html)
- [Guide complet BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)