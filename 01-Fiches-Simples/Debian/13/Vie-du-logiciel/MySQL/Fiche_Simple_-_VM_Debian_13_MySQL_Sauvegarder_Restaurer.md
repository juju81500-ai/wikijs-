# Fiche_Simple_-_VM_Debian_13_MySQL_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Sauvegarder et restaurer
- **Tags** : `debian13`, `mysql`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder MySQL de façon cohérente avec `mysqldump` et restaurer sur un serveur de test.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier d'identifiants protégé :
   ```bash
   umask 077
   sudo install -d -m 0700 /var/backups/mysql
   sudo tee /root/.my-backup.cnf >/dev/null <<'EOF'
   [client]
   user=COMPTE_SAUVEGARDE
   password=MOT_DE_PASSE_A_SAISIR
   EOF
   sudo chmod 0600 /root/.my-backup.cnf
   ```
   👉 Explication : remplacer `COMPTE_SAUVEGARDE` par un compte dédié (droits `SELECT, SHOW VIEW, TRIGGER, EVENT, LOCK TABLES`) et saisir le mot de passe dans le fichier avec l'éditeur : ne jamais le valider dans un dépôt.

2. Sauvegarder toutes les bases :
   ```bash
   sudo sh -c 'mysqldump --defaults-extra-file=/root/.my-backup.cnf --single-transaction --routines --events --all-databases | gzip > /var/backups/mysql/all-$(date +%F).sql.gz'
   ```
   👉 Explication : instantané cohérent pour InnoDB.

3. Contrôler l'archive :
   ```bash
   gzip -t /var/backups/mysql/all-$(date +%F).sql.gz && echo OK
   ```
   👉 Explication : intégrité de la compression.

4. Restaurer sur un serveur de test :
   ```bash
   sudo sh -c 'gunzip -c /var/backups/mysql/all-DATE.sql.gz | mysql -u root -p'
   ```
   👉 Explication : remplacer `DATE` (à remplacer) ; jamais sur la production sans validation préalable.

## 2. Production — Contrôles

Sauvegarde planifiée et chiffrée, copie hors site, test de restauration régulier ; pour de gros volumes, étudier MySQL Shell dump utilities ou Percona XtraBackup.

## 3. Production — Sécurité

- Chiffrer les copies.
- `/root/.my-backup.cnf` en `0600`.
- Ne pas stocker sur le même disque.

## Validation et retour arrière

- **Validation** : restauration testée sur un serveur distinct.
- **Retour arrière** : reprendre la sauvegarde précédente.

## Si le problème n'est pas résolu

- [MySQL — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MySQL_Prerequis_Limites.md)
- [MySQL — Installer](Fiche_Simple_-_VM_Debian_13_MySQL_Installer.md)
- [MySQL — Configurer](Fiche_Simple_-_VM_Debian_13_MySQL_Configurer.md)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](Fiche_Simple_-_VM_Debian_13_MySQL_Securiser.md)
- [MySQL — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MySQL_Valider.md)
- [MySQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MySQL_Mettre_A_Jour.md)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](../MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites.md)
