# Fiche_Simple_-_VM_Debian_12_Znuny_MariaDB.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing
- **Tags** : `debian12`, `znuny`, `mariadb`, `sql`

---

## Problème précis à résoudre

Régler MariaDB pour Znuny et créer une base et un compte dédiés.

## 1. Hors-Production (Lab / Test / POC)

1. Créer la configuration de limites adaptée à Znuny :
   ```bash
   sudo tee /etc/mysql/mariadb.conf.d/60-znuny.cnf >/dev/null <<'EOF'
   [mysqld]
   max_allowed_packet=256M
   innodb_log_file_size=256M
   EOF
   ```
   👉 Explication : Znuny stocke des pièces jointes volumineuses; ces valeurs évitent des erreurs de taille de paquet.

2. Redémarrer MariaDB :
   ```bash
   sudo systemctl restart mariadb
   ```
   👉 Explication : la nouvelle configuration est lue.

3. Ouvrir le client local :
   ```bash
   sudo mariadb
   ```
   👉 Explication : on se connecte en administrateur local via le socket, sans mot de passe en argument.

4. Dans le prompt MariaDB, créer la base et le compte dédiés (remplacer `CHANGER_CE_SECRET` par un secret long et unique issu du coffre) :
   ```sql
   CREATE DATABASE znuny CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   CREATE USER 'znuny'@'localhost' IDENTIFIED BY 'CHANGER_CE_SECRET';
   GRANT ALL PRIVILEGES ON znuny.* TO 'znuny'@'localhost';
   FLUSH PRIVILEGES;
   EXIT;
   ```
   👉 Explication : la base utilise utf8mb4 et le compte n'a de droits que sur cette base.

## 2. Production — Contrôles

Stocker le secret du compte `znuny` dans le coffre d'entreprise et prévoir sa rotation.

## 3. Production — Sécurité

- Ne jamais utiliser l'utilisateur `root` de MariaDB dans l'application.
- Limiter le compte à `localhost` et la base `znuny`.
- Ne pas écrire le mot de passe dans l'historique shell ni en argument de commande.

## Validation et retour arrière

- **Validation** : `sudo mariadb -e "SHOW DATABASES LIKE 'znuny';"` liste la base `znuny`.
- **Retour arrière** : `DROP DATABASE znuny; DROP USER 'znuny'@'localhost';` sur une installation vide, puis supprimer `/etc/mysql/mariadb.conf.d/60-znuny.cnf` et redémarrer MariaDB.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — préparer MariaDB](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/42_Deploiement_Znuny_7_3_8_Debian_12.md#3-preparer-mariadb)
