# Fiche_Simple_-_VM_Debian_13_MariaDB_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MariaDB des dépôts Debian
- **Catégorie** : base de données / MariaDB / Configurer
- **Tags** : `debian13`, `mariadb`, `configuration`

---

## Problème précis à résoudre

Appliquer une configuration locale de MariaDB (écoute, jeu de caractères, journaux) et créer une base avec un compte dédié.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de configuration local, sans modifier les fichiers du paquet :
   ```bash
   sudo tee /etc/mysql/mariadb.conf.d/60-local.cnf >/dev/null <<'EOF'
   [mysqld]
   bind-address = 127.0.0.1
   character-set-server = utf8mb4
   collation-server = utf8mb4_general_ci
   slow_query_log = 1
   long_query_time = 2
   EOF
   sudo systemctl restart mariadb
   ```
   👉 Explication : écoute limitée à loopback par défaut ; les journaux de requêtes lentes aident le diagnostic.

2. Créer une base et un compte applicatif :
   ```bash
   read -rsp 'Mot de passe du compte applicatif : ' DBPW; echo
   sudo mariadb <<SQL
   CREATE DATABASE APPDB CHARACTER SET utf8mb4;
   CREATE USER 'APPUSER'@'localhost' IDENTIFIED BY '${DBPW}';
   GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,ALTER,INDEX ON APPDB.* TO 'APPUSER'@'localhost';
   SQL
   unset DBPW
   ```
   👉 Explication : remplacer `APPDB` et `APPUSER` (à remplacer) ; le mot de passe est saisi, jamais écrit dans un fichier ni dans l'historique.

3. Contrôler :
   ```bash
   sudo mariadb -e "SHOW GRANTS FOR 'APPUSER'@'localhost'; SHOW VARIABLES LIKE 'bind_address';"
   ```
   👉 Explication : droits minimaux et écoute loopback.

## 2. Production — Contrôles

Configuration dans `60-local.cnf` versionné, un compte par application, aucun `GRANT ALL`.

## 3. Production — Sécurité

- Pas de compte sans mot de passe ni de compte anonyme.
- Pas de privilège global pour un compte applicatif.
- Ne jamais passer le mot de passe en argument de commande (visible dans `ps`).

## Validation et retour arrière

- **Validation** : connexion applicative réussie avec droits limités à `APPDB`.
- **Retour arrière** : supprimer `60-local.cnf`, redémarrer, puis `DROP USER`/`DROP DATABASE` sur la base de test.

## Si le problème n'est pas résolu

- [MariaDB — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites.md)
- [MariaDB — Sécuriser (TLS, comptes, pare-feu)](Fiche_Simple_-_VM_Debian_13_MariaDB_Securiser.md)
- [MariaDB — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MariaDB_Valider.md)
- [MariaDB — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MariaDB_Sauvegarder_Restaurer.md)
- [MariaDB — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MariaDB_Mettre_A_Jour.md)
- [Guide complet LEMP Debian 13 (MariaDB)](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md)
- [Installation MariaDB 11 (fiche du pack)](Fiche_Simple_-_VM_Debian_13_Database_Installation_MariaDB_11.md)
- [Durcissement MariaDB (fiche du pack)](Fiche_Simple_-_VM_Debian_13_LEMP_Securiser_MariaDB.md)
- [MariaDB — documentation officielle](https://mariadb.com/kb/en/documentation/)
