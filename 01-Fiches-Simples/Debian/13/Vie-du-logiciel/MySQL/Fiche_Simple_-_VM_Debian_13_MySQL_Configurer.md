# Fiche_Simple_-_VM_Debian_13_MySQL_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; MySQL Community (dépôt officiel Oracle)
- **Catégorie** : base de données / MySQL / Configurer
- **Tags** : `debian13`, `mysql`, `configuration`

---

## Problème précis à résoudre

Configurer MySQL (écoute, jeu de caractères, journaux) et créer une base et un compte applicatif.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un fichier de configuration local :
   ```bash
   sudo tee /etc/mysql/mysql.conf.d/60-local.cnf >/dev/null <<'EOF'
   [mysqld]
   bind-address = 127.0.0.1
   character-set-server = utf8mb4
   slow_query_log = 1
   long_query_time = 2
   EOF
   sudo systemctl restart mysql
   ```
   👉 Explication : vérifier que le répertoire `mysql.conf.d` existe avec le paquet installé (sinon utiliser le répertoire indiqué par `mysql --help`).

2. Créer une base et un compte applicatif :
   ```bash
   read -rsp 'Mot de passe du compte applicatif : ' DBPW; echo
   mysql -u root -p <<SQL
   CREATE DATABASE APPDB CHARACTER SET utf8mb4;
   CREATE USER 'APPUSER'@'localhost' IDENTIFIED BY '${DBPW}';
   GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,ALTER,INDEX ON APPDB.* TO 'APPUSER'@'localhost';
   SQL
   unset DBPW
   ```
   👉 Explication : remplacer `APPDB` et `APPUSER` (à remplacer) ; mots de passe saisis, jamais écrits en dur.

3. Contrôler les droits :
   ```bash
   mysql -u root -p -e "SHOW GRANTS FOR 'APPUSER'@'localhost';"
   ```
   👉 Explication : droits limités à `APPDB`.

## 2. Production — Contrôles

Configuration versionnée, un compte par application, jamais de `GRANT ALL`.

## 3. Production — Sécurité

- Pas de compte anonyme ni de compte sans mot de passe.
- Ne pas passer de mot de passe en argument de commande.
- Pas de privilège global pour une application.

## Validation et retour arrière

- **Validation** : connexion applicative réussie, droits limités.
- **Retour arrière** : supprimer `60-local.cnf`, redémarrer, supprimer base et compte de test.

## Si le problème n'est pas résolu

- [MySQL — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_MySQL_Prerequis_Limites.md)
- [MySQL — Installer](Fiche_Simple_-_VM_Debian_13_MySQL_Installer.md)
- [MySQL — Sécuriser (TLS, comptes, pare-feu)](Fiche_Simple_-_VM_Debian_13_MySQL_Securiser.md)
- [MySQL — Valider (recette)](Fiche_Simple_-_VM_Debian_13_MySQL_Valider.md)
- [MySQL — Sauvegarder et restaurer](Fiche_Simple_-_VM_Debian_13_MySQL_Sauvegarder_Restaurer.md)
- [MySQL — Mise à jour et retour arrière](Fiche_Simple_-_VM_Debian_13_MySQL_Mettre_A_Jour.md)
- [MySQL — documentation officielle](https://dev.mysql.com/doc/)
- [Alternative MariaDB (fiches du pack)](../MariaDB/Fiche_Simple_-_VM_Debian_13_MariaDB_Prerequis_Limites.md)
