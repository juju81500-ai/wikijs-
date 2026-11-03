---
title: "Leçon — Bases de données relationnelles pour l'administrateur (MariaDB / PostgreSQL)"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "services-infrastructure", "base-de-donnees", "mariadb", "postgresql", "sql", "sauvegarde", "droits"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Bases de données relationnelles pour l'administrateur (MariaDB / PostgreSQL)

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `services-infrastructure`, `base-de-donnees`, `mariadb`, `postgresql`, `sql`, `sauvegarde`, `droits`
- **Niveau** : intermédiaire
- **Durée estimée** : 4 à 5 heures (cours 1 h 30, laboratoire 2 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. décrire le modèle relationnel (tables, clés primaires, clés étrangères) et le rôle d'un SGBD ;
2. installer MariaDB ou PostgreSQL sur Debian/Ubuntu et situer données, configuration et journaux ;
3. créer des **comptes et des droits** selon le principe du moindre privilège ;
4. limiter l'écoute réseau et contrôler les accès distants ;
5. écrire les **requêtes [[Glossary:SQL]] de base** : `SELECT`, `INSERT`, `UPDATE`, `DELETE`, jointures, regroupements ;
6. réaliser et **tester** une sauvegarde logique, puis une restauration ;
7. superviser simplement le service : connexions, espace disque, requêtes lentes, état de santé.

## Prérequis et durée

- Terminal Linux, `sudo`, `systemctl`, notions de réseau (port, adresse [[Glossary:IP]]).
- Une **[[Glossary:VM]] jetable** Debian 12 ou Ubuntu 22-04/24-04 sans donnée réelle. Durée : 4 à 5 heures.
- Les adresses `192.0.2.0/24`, `203.0.113.0/24` et les noms `example.test` sont des valeurs de documentation. **Aucun mot de passe réel n'apparaît** : les valeurs entre chevrons (`<mot_de_passe>`) sont à remplacer par un secret généré par vous et jamais enregistré dans un document.

## L'essentiel en bref

- Une base relationnelle range les données en **tables** reliées par des **clés** ; on l'interroge en **SQL**.
- MariaDB (compatible MySQL) et PostgreSQL sont deux SGBD libres très répandus ; les requêtes de base sont presque identiques, l'administration diffère.
- **Un compte par usage**, avec le **minimum de droits** ; jamais l'administrateur dans une application.
- Par défaut, n'écoutez que sur `127.0.0.1` ; ouvrez le réseau seulement si nécessaire, avec filtrage par adresse et pare-feu.
- Une **sauvegarde logique** (`mysqldump`/`mariadb-dump`, `pg_dump`) exporte la structure et les données en texte SQL ; **une sauvegarde non restaurée n'est pas une sauvegarde**.
- Supervisez : service actif, connexions, espace disque, requêtes lentes, journaux d'erreurs.

---

## 1. Le modèle relationnel en images

### 1.1 Tables, lignes, clés

Imaginez un classeur de fiches. Chaque **table** est un tiroir (`clients`, `commandes`) ; chaque **ligne** est une fiche ; chaque **colonne** est une rubrique typée (texte, entier, date, nombre décimal). La **clé primaire** est le numéro unique d'une fiche. Une **clé étrangère** est un renvoi : dans `commandes`, la colonne `client_id` contient le numéro d'une fiche de `clients`. Le SGBD **garantit** ce lien : il refuse une commande pour un client inexistant.

![Deux tables, clients et commandes, reliées par une clé étrangère client_id qui référence clients.id, avec une requête de jointure en exemple](images/bases-de-donnees-relationnelles-1.svg)

*Figure 1 — Clé primaire, clé étrangère et jointure. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

Cela évite les doublons : l'adresse d'un client n'est écrite qu'une fois. Les **transactions ACID** garantissent qu'un ensemble d'opérations est appliqué entièrement ou pas du tout, et survit à une panne une fois validé.

### 1.2 Architecture client-serveur

Le SGBD est un **service** qui écoute sur un port (3306 pour MariaDB, 5432 pour PostgreSQL) : il authentifie les clients, vérifie les droits, exécute le SQL et lit ou écrit données et journaux.

![Trois types de clients, outil en ligne de commande, application web et tâche de sauvegarde, connectés à un serveur SGBD qui gère les données, les journaux et la configuration](images/bases-de-donnees-relationnelles-2.svg)

*Figure 2 — Architecture client-serveur d'une base relationnelle. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

**Règle fondamentale** : ne copiez jamais le répertoire de données d'un SGBD en fonctionnement en espérant obtenir une sauvegarde : le contenu serait incohérent. On utilise un export logique ou un outil de sauvegarde physique prévu pour cela.

---

## 2. Installation et premiers repères

### 2.1 MariaDB

```bash
sudo apt update
sudo apt install mariadb-server
systemctl status mariadb --no-pager
sudo mariadb -e "SELECT VERSION();"
```

👉 Explication : installe le serveur (le service démarre automatiquement) ; vérifie son état ; `sudo mariadb` ouvre le client avec le compte administrateur local `root` de la base, authentifié par le **socket Unix** (pas de mot de passe, mais obligation d'être administrateur du système) ; `-e` exécute une requête et quitte. Sur les versions antérieures à 10.5, le client s'appelle `mysql`.

```bash
sudo mariadb-secure-installation
```

👉 Explication : script interactif de durcissement : retire les comptes anonymes et la base de test, interdit `root` à distance ; lisez chaque question.

### 2.2 PostgreSQL

```bash
sudo apt install postgresql
systemctl status postgresql --no-pager
sudo -u postgres psql -c "SELECT version();"
```

👉 Explication : installe PostgreSQL et un **cluster** par défaut (sous Debian, la version majeure est dans les chemins, par exemple `15`) ; `sudo -u postgres` exécute `psql` sous le compte système `postgres`, que le mode d'authentification « peer » associe au rôle de base de même nom. Le service `postgresql` est un lanceur qui gère les instances (`postgresql@15-main`).

### 2.3 Où se trouve quoi (Debian)

| Élément | MariaDB | PostgreSQL |
|---|---|---|
| Configuration | `/etc/mysql/mariadb.conf.d/50-server.cnf` | `/etc/postgresql/15/main/postgresql.conf` et `pg_hba.conf` |
| Données | `/var/lib/mysql` | `/var/lib/postgresql/15/main` |
| Journaux | `journalctl -u mariadb` ou `/var/log/mysql/` | `/var/log/postgresql/` |
| Port par défaut | 3306 | 5432 |
| Client | `mariadb` | `psql` |
| Export logique | `mariadb-dump` (`mysqldump`) | `pg_dump`, `pg_dumpall` |

Le `15` du chemin PostgreSQL dépend de votre version.

### 2.4 Qui écoute, et sur quelle interface ?

```bash
sudo ss -lntp | grep -E ':(3306|5432)\b'
```

👉 Explication : liste les sockets en écoute avec leur processus ; `127.0.0.1` = local uniquement, `0.0.0.0` ou `*` = toutes les interfaces.

Pour MariaDB, le paramètre `bind-address` (section `[mysqld]`) fixe l'adresse d'écoute ; pour PostgreSQL, c'est `listen_addresses` dans `postgresql.conf`. Dans les deux cas, **la valeur locale est le bon point de départ**. Si une application distante doit se connecter, écoutez sur l'adresse privée du serveur (par exemple `192.0.2.20`) et **filtrez** ensuite : pare-feu limitant le port à l'adresse de l'application, et restriction côté SGBD (section 3).

---

## 3. Comptes, droits et authentification

### 3.1 Le principe du moindre privilège

Analogie : les **clés d'un immeuble**. Le gardien a un passe général ; le facteur n'ouvre que les boîtes aux lettres ; le plombier n'a que la clé du local technique. De même :

- un compte **administrateur** pour l'administration (jamais utilisé par une application) ;
- un compte **applicatif** par application, avec les droits `SELECT/INSERT/UPDATE/DELETE` sur **sa** base seulement ;
- un compte **de sauvegarde** en lecture seule ;
- un compte **de supervision** avec droits minimaux.

Les droits de structure (`CREATE`, `ALTER`, `DROP`) sont réservés aux comptes de migration, utilisés ponctuellement.

### 3.2 MariaDB : créer base, compte et droits

Dans `sudo mariadb` :

```sql
CREATE DATABASE appdb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'app'@'192.0.2.30' IDENTIFIED BY '<mot_de_passe_application>';
GRANT SELECT, INSERT, UPDATE, DELETE ON appdb.* TO 'app'@'192.0.2.30';
SHOW GRANTS FOR 'app'@'192.0.2.30';
```

👉 Explication : crée une base `utf8mb4` (Unicode complet) ; crée `app`, qui ne peut se connecter **que depuis** `192.0.2.30` (l'identité d'un compte MariaDB est le couple nom + hôte) ; accorde seulement lecture/écriture de données sur cette base ; `SHOW GRANTS` affiche l'accordé réel. Choisissez vous-même un mot de passe robuste, stocké dans un gestionnaire de secrets.

```sql
CREATE USER 'sauvegarde'@'localhost' IDENTIFIED BY '<mot_de_passe_sauvegarde>';
GRANT SELECT, SHOW VIEW, TRIGGER, EVENT, LOCK TABLES ON appdb.* TO 'sauvegarde'@'localhost';
REVOKE DELETE ON appdb.* FROM 'app'@'192.0.2.30';
DROP USER IF EXISTS 'ancien'@'localhost';
```

👉 Explication : compte de sauvegarde en lecture seule (droits suffisants pour exporter vues, déclencheurs et événements) ; `REVOKE` retire un droit ; `DROP USER` supprime un compte inutile. Évitez `GRANT OPTION`, `ALL PRIVILEGES` et `*.*` hors administration.

### 3.3 PostgreSQL : rôles, bases, droits

Dans `sudo -u postgres psql` :

```sql
CREATE ROLE app LOGIN;
\password app
CREATE DATABASE appdb OWNER app;
\c appdb
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT USAGE, CREATE ON SCHEMA public TO app;
```

👉 Explication : PostgreSQL n'a que des **rôles** (un rôle avec `LOGIN` joue le rôle d'un utilisateur) ; `\password` demande le mot de passe de façon interactive, ce qui évite qu'il apparaisse dans l'historique ou les journaux ; la base appartient à `app` ; on retire les droits par défaut du groupe `PUBLIC` sur le schéma `public` puis on accorde explicitement l'usage à `app`. Un compte de sauvegarde ou de lecture se crée de même, avec `GRANT SELECT ON ALL TABLES IN SCHEMA public TO lecteur;` et `ALTER DEFAULT PRIVILEGES` pour les futures tables.

### 3.4 Contrôler qui peut se connecter depuis le réseau (PostgreSQL)

Le fichier `pg_hba.conf` (host-based authentication) est évalué **ligne par ligne, de haut en bas** ; la première ligne correspondante s'applique :

```text
# TYPE   DATABASE  USER  ADDRESS          METHOD
local    all       postgres                peer
host     appdb     app   192.0.2.30/32    scram-sha-256
```

👉 Explication : la première ligne autorise le compte système `postgres` par socket local ; la seconde autorise **uniquement** le rôle `app` à joindre la base `appdb` depuis `192.0.2.30`, avec mot de passe haché `scram-sha-256` (méthode moderne, à préférer à `md5`). Toute connexion non listée est refusée. Après modification : `sudo systemctl reload postgresql`.

### 3.5 Hygiène des mots de passe

Évitez `-p<mot_de_passe>` en ligne de commande : le secret apparaît dans la liste des processus et l'historique. Préférez un fichier d'options en `chmod 600` (`~/.my.cnf`, section `[client]`), `~/.pgpass` ou l'authentification « peer », et un **gestionnaire de secrets** pour les applications.

---

## 4. SQL de base : l'essentiel de l'administrateur

Les exemples fonctionnent à l'identique sous MariaDB et PostgreSQL (hors types spécifiques).

### 4.1 Créer des tables

```sql
CREATE TABLE clients (
  id    INTEGER PRIMARY KEY,
  nom   VARCHAR(80) NOT NULL,
  ville VARCHAR(60)
);
CREATE TABLE commandes (
  id        INTEGER PRIMARY KEY,
  client_id INTEGER NOT NULL REFERENCES clients(id),
  montant   DECIMAL(10,2) NOT NULL
);
```

👉 Explication : `PRIMARY KEY` impose l'unicité de l'identifiant ; `NOT NULL` interdit l'absence de valeur ; `REFERENCES` déclare la clé étrangère. Pour numéroter automatiquement : `AUTO_INCREMENT` (MariaDB) ou `GENERATED ALWAYS AS IDENTITY` (PostgreSQL). Avec MariaDB, créez les tables avec le moteur InnoDB (par défaut) pour que les clés étrangères soient vérifiées.

### 4.2 Insérer, lire, modifier, supprimer

```sql
INSERT INTO clients (id, nom, ville) VALUES (1,'Atelier Exemple','Lyon'),(2,'Boutique Test','Nantes'),(3,'Cabinet Demo','Lyon');
INSERT INTO commandes (id, client_id, montant) VALUES (1,1,120.50),(2,1,80.00),(3,3,45.90);
SELECT nom, ville FROM clients WHERE ville = 'Lyon' ORDER BY nom;
UPDATE commandes SET montant = 90.00 WHERE id = 2;
DELETE FROM commandes WHERE id = 3;
```

👉 Explication : les deux `INSERT` ajoutent des fiches ; `SELECT … WHERE … ORDER BY` filtre et trie ; `UPDATE` et `DELETE` **sans clause `WHERE` touchent toute la table** : relisez systématiquement la condition, et testez d'abord par un `SELECT` équivalent. Utilisez une transaction (`BEGIN;` … `ROLLBACK;`/`COMMIT;`) pour pouvoir annuler.

### 4.3 Jointures et regroupements

```sql
SELECT c.nom, o.montant
FROM clients c
JOIN commandes o ON o.client_id = c.id
WHERE c.ville = 'Lyon'
ORDER BY o.montant DESC;

SELECT c.ville, COUNT(*) AS nb, SUM(o.montant) AS total
FROM clients c JOIN commandes o ON o.client_id = c.id
GROUP BY c.ville
HAVING SUM(o.montant) > 100;

SELECT c.nom FROM clients c LEFT JOIN commandes o ON o.client_id = c.id WHERE o.id IS NULL;
```

👉 Explication : la première requête associe chaque commande à son client (`JOIN … ON`) ; la deuxième regroupe par ville, compte et somme, puis `HAVING` filtre **après** regroupement (à la différence de `WHERE`, appliqué avant) ; la troisième utilise `LEFT JOIN` pour trouver les clients sans aucune commande. Ces trois requêtes ont été exécutées avec le moteur SQLite lors de la rédaction ; la syntaxe est la même sous MariaDB et PostgreSQL.

### 4.4 Index et plans d'exécution

Un **index** est comme l'index d'un livre : il évite de lire toute la table, au prix d'espace et d'écritures plus lentes.

```sql
CREATE INDEX idx_commandes_client ON commandes (client_id);
EXPLAIN SELECT * FROM commandes WHERE client_id = 1;
```

👉 Explication : crée un index sur la colonne de jointure ; `EXPLAIN` affiche le plan que le SGBD compte utiliser (parcours complet de la table ou usage de l'index). Une requête lente se diagnostique d'abord avec `EXPLAIN`, avant toute modification de configuration.

### 4.5 Commandes d'exploration

MariaDB : `SHOW DATABASES;`, `USE appdb;`, `SHOW TABLES;`, `DESCRIBE clients;`, `EXIT;`. PostgreSQL (`psql`) : `\l`, `\c appdb`, `\dt`, `\d clients`, `\du` (rôles), `\q`.

---

## 5. Sauvegarde et restauration logiques

### 5.1 Le principe

Une sauvegarde **logique** produit un fichier de texte contenant les ordres SQL qui recréent structure et données. Elle est portable (d'une version à l'autre, souvent d'un système à l'autre), simple, et adaptée aux bases de petite et moyenne taille. Pour de gros volumes ou une restauration à un instant précis, on complète par une sauvegarde **physique** (hors périmètre).

![Cycle de la sauvegarde logique : exporter avec mysqldump ou pg_dump, compresser et contrôler, copier ailleurs, puis tester la restauration sur une base jetable](images/bases-de-donnees-relationnelles-3.svg)

*Figure 3 — Exporter, protéger, copier ailleurs, restaurer pour tester. Création originale du projet Pack Master, dédiée au domaine public (CC0).*

### 5.2 MariaDB

```bash
umask 077
mkdir -p ~/sauvegardes
mariadb-dump --single-transaction --routines --triggers --events --databases appdb | gzip > ~/sauvegardes/appdb_$(date +%Y%m%d_%H%M).sql.gz
gzip -t ~/sauvegardes/appdb_*.sql.gz && echo "archive lisible"
```

👉 Explication : `umask 077` protège les fichiers créés ; `--single-transaction` obtient une image cohérente des tables InnoDB sans bloquer les écritures ; `--routines --triggers --events` incluent les objets programmables ; `--databases` ajoute les ordres de création de la base ; `gzip -t` vérifie l'intégrité de l'archive. Exécutez-la avec un compte autorisé (via le fichier d'options de la section 3.5, ou `sudo` en laboratoire).

Restauration vers une base jetable :

```bash
sed 's/`appdb`/`appdb_restore`/g' <(gunzip -c ~/sauvegardes/appdb_*.sql.gz) | sudo mariadb
sudo mariadb -e "USE appdb_restore; SHOW TABLES; SELECT COUNT(*) FROM clients;"
```

👉 Explication : décompresse, renomme la base cible dans le flux (pour ne pas écraser la base d'origine), puis rejoue le tout ; la seconde commande contrôle tables et nombre de lignes. En production, **ne jamais restaurer par-dessus** une base vivante avant d'avoir validé le fichier sur une copie. Le motif `appdb_*` suppose un seul fichier : précisez le nom exact si vous en avez plusieurs.

### 5.3 PostgreSQL

```bash
umask 077
mkdir -p ~/sauvegardes
sudo -u postgres pg_dump -Fc appdb > ~/sauvegardes/appdb_$(date +%Y%m%d_%H%M).dump
sudo -u postgres pg_dumpall --globals-only > ~/sauvegardes/globals_$(date +%Y%m%d).sql
```

👉 Explication : `pg_dump -Fc` produit un format « custom » compressé, sélectif et restaurable en parallèle ; `pg_dumpall --globals-only` sauvegarde séparément les rôles et objets globaux, absents du `pg_dump` d'une base. La redirection s'exécute sous votre compte (donc vers votre dossier) tandis que `pg_dump` s'exécute sous `postgres`.

```bash
sudo -u postgres createdb appdb_restore
sudo -u postgres pg_restore -d appdb_restore --no-owner < ~/sauvegardes/appdb_*.dump
sudo -u postgres psql -d appdb_restore -c "\dt"
```

👉 Explication : crée une base vide, y rejoue la sauvegarde (`--no-owner` n'exige pas les rôles d'origine) et liste les tables ; supprimez ensuite la base d'essai avec `dropdb`.

### 5.4 Règles de sauvegarde

- Règle **3-2-1** : trois copies, deux supports, une hors site ; **chiffrez** celles qui quittent le serveur.
- Définissez une **rétention** (ex. 7 quotidiennes, 4 hebdomadaires, 6 mensuelles) et planifiez avec `cron` ou un minuteur `systemd` ; **surveillez le résultat**.
- **Testez la restauration** régulièrement en chronométrant : c'est votre durée réelle de reprise.

---

## 6. Supervision simple

### 6.1 État du service et disponibilité

```bash
systemctl is-active mariadb postgresql
pg_isready -h 127.0.0.1 -p 5432
sudo mariadb -e "SELECT 1;" >/dev/null && echo "MariaDB répond"
```

👉 Explication : état des services, disponibilité de PostgreSQL (code 0 s'il accepte les connexions), puis réponse de MariaDB à une requête triviale : `systemctl` dit que le processus existe, une requête dit qu'il **répond**.

### 6.2 Connexions et activité

MariaDB :

```sql
SHOW GLOBAL STATUS LIKE 'Threads_connected';
SHOW VARIABLES LIKE 'max_connections';
SHOW FULL PROCESSLIST;
SHOW GLOBAL STATUS LIKE 'Slow_queries';
```

👉 Explication : nombre de connexions ouvertes face à la limite configurée ; liste des requêtes en cours avec leur durée ; compteur de requêtes lentes. Une valeur proche de `max_connections` annonce des refus de connexion.

PostgreSQL :

```sql
SELECT count(*) FROM pg_stat_activity;
SHOW max_connections;
SELECT pid, usename, state, now() - query_start AS duree, left(query, 60) AS requete
FROM pg_stat_activity WHERE state <> 'idle' ORDER BY duree DESC;
SELECT datname, pg_size_pretty(pg_database_size(datname)) FROM pg_database;
```

👉 Explication : nombre de sessions, limite, sessions actives classées par durée, et taille de chaque base. Une session « idle in transaction » ancienne est suspecte : elle retient des verrous.

### 6.3 Espace disque, journaux, requêtes lentes

```bash
df -h /var/lib
sudo du -sh /var/lib/mysql /var/lib/postgresql 2>/dev/null
sudo journalctl -u mariadb --since "1 hour ago" --no-pager | tail -n 20
```

👉 Explication : un disque plein est la panne la plus fréquente ; ces commandes mesurent espace libre et taille des données puis lisent les derniers messages. Requêtes lentes : MariaDB `slow_query_log=1` et `long_query_time=1` ; PostgreSQL `log_min_duration_statement = 1000` (ms) ; ils augmentent le volume de journaux.

### 6.4 Que surveiller

Service actif, **réponse à une requête**, disque (alerte à 80 %), connexions face au maximum, requête la plus longue, âge de la dernière sauvegarde réussie et **dernière restauration testée** (le plus négligé).

---

## Mise en pratique guidée

**Objectif** : créer une base applicative, un compte à droits limités, tester une requête de jointure, faire une sauvegarde logique puis la restaurer dans une base jetable. **Contexte** : VM Debian 12 jetable, connexions locales uniquement. La procédure est écrite pour MariaDB ; les équivalents PostgreSQL sont donnés en note.

1. **Installer** : `sudo apt install mariadb-server`, puis vérifier avec `systemctl is-active mariadb` et `sudo ss -lntp | grep 3306` (écoute attendue sur `127.0.0.1`).
2. **Créer base et compte** (dans `sudo mariadb`) : les ordres de la section 3.2 en remplaçant l'hôte par `localhost` et en choisissant un mot de passe jetable de laboratoire.
3. **Créer les tables et les données** avec les requêtes des sections 4.1 et 4.2 dans la base `appdb`.
4. **Vérifier les droits** : ouvrez une session avec le compte `app` et essayez une opération interdite.

```bash
mariadb -u app -p appdb -e "SELECT COUNT(*) FROM clients; DROP TABLE clients;"
```

👉 Explication : le mot de passe est demandé de façon interactive ; le `SELECT` doit réussir et le `DROP TABLE` être **refusé** (`DROP command denied`) : le moindre privilège est effectif.

5. **Sauvegarder** avec la commande de la section 5.2, puis vérifier l'archive avec `gzip -t`.
6. **Restaurer** vers `appdb_restore` et comparer : `COUNT(*)` doit être identique dans les deux bases.
7. **Annuler** : `BEGIN; DELETE FROM commandes; SELECT COUNT(*) FROM commandes; ROLLBACK;` puis constatez que les lignes sont revenues.
8. **Superviser** : exécutez les requêtes de la section 6.2 et notez le nombre de connexions.
9. **Nettoyer** :

```bash
sudo mariadb -e "DROP DATABASE appdb_restore; DROP DATABASE appdb; DROP USER 'app'@'localhost';"
rm -rf ~/sauvegardes
```

👉 Explication : supprime les deux bases de laboratoire, le compte de test et les fichiers de sauvegarde.

*Note PostgreSQL* : `createdb`/`CREATE ROLE` (3.3), `pg_dump -Fc` et `pg_restore` (5.3), `pg_stat_activity` (6.2) jouent les rôles correspondants.

---

## Exercices

1. **(Facile)** Quelle est la différence entre clé primaire et clé étrangère ?
2. **(Facile)** Pourquoi ne pas copier `/var/lib/mysql` à chaud comme sauvegarde ?
3. **(Facile)** Que se passe-t-il avec `UPDATE commandes SET montant = 0;` ?
4. **(Moyen)** Écrivez les ordres MariaDB créant le compte `lecteur` autorisé à lire (seulement) `appdb` depuis `198.51.100.15`.
5. **(Moyen)** Écrivez la ligne `pg_hba.conf` autorisant le rôle `rapport` à lire `appdb` depuis `203.0.113.0/24` avec `scram-sha-256`.
6. **(Moyen)** Écrivez une requête listant, par ville, le nombre de clients, uniquement pour les villes ayant au moins deux clients.
7. **(Avancé)** Votre sauvegarde logique nocturne réussit mais la restauration échoue le jour de l'incident. Citez trois causes possibles et la parade.
8. **(Avancé)** Définissez trois indicateurs de supervision avec un seuil d'alerte chacun.

## Corrigés des exercices

1. La clé primaire identifie **de façon unique** une ligne dans sa table ; la clé étrangère est une colonne d'une autre table qui **référence** cette clé primaire et dont le SGBD garantit la validité.
2. Les fichiers changent pendant la copie : on obtient un état incohérent, parfois inutilisable. Utilisez un export logique ou un outil de sauvegarde physique prévu pour cela.
3. **Toutes** les commandes passent à 0, faute de clause `WHERE`. Prévention : `SELECT` de contrôle, transaction, sauvegarde préalable.
4. ```sql
   CREATE USER 'lecteur'@'198.51.100.15' IDENTIFIED BY '<mot_de_passe>';
   GRANT SELECT ON appdb.* TO 'lecteur'@'198.51.100.15';
   ```
   👉 Explication : un compte lié à une adresse, avec le seul droit de lecture.
5. ```text
   host  appdb  rapport  203.0.113.0/24  scram-sha-256
   ```
   👉 Explication : les droits SQL (`GRANT SELECT`) doivent s'ajouter à cette autorisation de connexion.
6. ```sql
   SELECT ville, COUNT(*) AS nb FROM clients GROUP BY ville HAVING COUNT(*) >= 2;
   ```
   👉 Explication : `HAVING` filtre les groupes après le regroupement.
7. Archive corrompue ou tronquée ; sauvegarde incomplète (rôles ou objets globaux oubliés) ; incompatibilité de version, espace disque insuffisant ou clé de chiffrement perdue. Parade : **restauration d'essai régulière** et chronométrée.
8. Exemple : disque ≥ 80 % ; connexions ≥ 80 % de `max_connections` ; dernière sauvegarde réussie vieille de plus de 26 heures.

## Quiz

**1.** Que garantit une clé étrangère ? A. Des requêtes plus rapides — B. La cohérence du lien entre deux tables — C. Le chiffrement — D. La compression. **Réponse : B**.

**2.** Quel paramètre MariaDB limite l'interface d'écoute ? A. `max_connections` — B. `bind-address` — C. `datadir` — D. `log_error`. **Réponse : B**.

**3.** Dans `pg_hba.conf`, comment les lignes sont-elles évaluées ? A. Aléatoirement — B. De haut en bas, la première correspondance s'applique — C. De bas en haut — D. Seule la dernière compte. **Réponse : B**.

**4.** Quelle commande sauvegarde une base PostgreSQL en format compressé ? A. `pg_dump -Fc` — B. `cp -r` — C. `psql -c` — D. `pg_ctl stop`. **Réponse : A**.

**5.** À quoi sert `--single-transaction` de `mariadb-dump` ? A. À chiffrer l'archive — B. À obtenir une image cohérente des tables InnoDB sans bloquer les écritures — C. À supprimer la base — D. À compresser. **Réponse : B**.

**6.** Quel est le principal danger d'un `DELETE` sans `WHERE` ? A. Aucun — B. Il supprime toutes les lignes de la table — C. Il bloque le port — D. Il change le mot de passe. **Réponse : B**.

**7.** Pourquoi éviter `-p<mot_de_passe>` en ligne de commande ? A. Syntaxe invalide — B. Le secret est visible dans la liste des processus et l'historique — C. Cela ralentit — D. Cela chiffre à tort. **Réponse : B**.

**8.** `HAVING` diffère de `WHERE` car… A. Il s'applique après le regroupement — B. Il est réservé à PostgreSQL — C. Il trie — D. Il supprime. **Réponse : A**.

**9.** Quel test prouve qu'une sauvegarde est utilisable ? A. `ls -l` — B. Sa restauration réussie dans une base jetable — C. Sa taille — D. Son nom. **Réponse : B**.

**10.** Quel droit minimal accorde-t-on à une application qui lit et écrit des données sans modifier la structure ? A. `ALL PRIVILEGES` — B. `SELECT, INSERT, UPDATE, DELETE` sur sa base — C. `GRANT OPTION` — D. Aucun droit. **Réponse : B** (moindre privilège).

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification / correction |
|---|---|---|
| `Access denied for user` | Mauvais mot de passe, ou hôte du compte différent de celui du client | `SELECT user,host FROM mysql.user;`, vérifier le couple nom/hôte |
| `Can't connect to local MySQL server through socket` | Service arrêté ou socket différent | `systemctl status mariadb`, journal du service |
| `FATAL: no pg_hba.conf entry for host …` | Adresse, base ou rôle non autorisés | Ajouter la ligne adéquate, `reload`, vérifier l'ordre |
| `FATAL: Peer authentication failed` | Compte système différent du rôle | Utiliser `sudo -u postgres`, ou TCP avec mot de passe |
| Connexion distante impossible | Écoute locale seulement, pare-feu | `ss -lntp`, `bind-address` / `listen_addresses`, règle de pare-feu |
| `Too many connections` | Pool applicatif mal dimensionné ou fuite | `SHOW PROCESSLIST`, corriger l'application avant d'augmenter la limite |
| Disque plein, service arrêté | Journaux, sauvegardes ou données qui croissent | `df -h`, `du -sh`, rotation et purge ; ajouter l'alerte à 80 % |
| Erreur de clé étrangère à l'insertion | Ligne parente absente | Insérer d'abord la ligne de `clients` |
| Restauration en erreur de version | Dump d'une version plus récente | Restaurer avec une version égale ou supérieure ; consulter les notes de version |

Méthode : lire le **message exact** et le journal du service, reproduire avec un client minimal, corriger une chose à la fois, revalider.

## À retenir

- Tables, clés primaires et étrangères : le SGBD garantit la cohérence des liens et des transactions.
- Installer, puis **restreindre l'écoute** (`bind-address`, `listen_addresses`, `pg_hba.conf`, pare-feu).
- **Un compte par usage, droits minimaux** ; secrets hors des lignes de commande et des dépôts.
- SQL de base : `SELECT … WHERE … ORDER BY`, `JOIN`, `GROUP BY … HAVING`, transactions ; `UPDATE`/`DELETE` toujours avec condition vérifiée.
- Sauvegarde logique : `mariadb-dump --single-transaction`, `pg_dump -Fc`, contrôle d'intégrité, copie hors serveur, chiffrement, rétention.
- **Une sauvegarde non testée n'existe pas** : restaurez régulièrement.
- Supervision : réponse réelle du service, connexions, disque, requêtes lentes, âge de la dernière sauvegarde.

## Pour aller plus loin

- Documentation de MariaDB (Knowledge Base) : <https://mariadb.com/kb/en/documentation/>
- Documentation de `mariadb-dump` : <https://mariadb.com/kb/en/mariadb-dump/>
- Documentation de PostgreSQL : <https://www.postgresql.org/docs/current/>
- `pg_hba.conf` : <https://www.postgresql.org/docs/current/auth-pg-hba-conf.html>
- Sauvegarde et restauration PostgreSQL : <https://www.postgresql.org/docs/current/backup.html>
- Rôles et privilèges PostgreSQL : <https://www.postgresql.org/docs/current/user-manag.html>
- RFC 7677, authentification SCRAM-SHA-256 : <https://www.rfc-editor.org/rfc/rfc7677>
- Leçons du même dossier : [Serveur web et reverse proxy](lecon-serveur-web-et-reverse-proxy.md) et [Temps et certificats](lecon-temps-et-certificats.md)

## Crédits des images

| Fichier | Source (URL de la page Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/bases-de-donnees-relationnelles-1.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/bases-de-donnees-relationnelles-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/bases-de-donnees-relationnelles-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Debian 12 / MariaDB / PostgreSQL | Rédaction assistée (Copilot) | Non testé sur plateforme cible |
| 2026-11-01 | SQLite 3 (runtime Flatpak Freedesktop SDK 25.08, base jetable en lecture/écriture locale) | Rédaction assistée (Copilot) | Requêtes SQL des sections 4.1 à 4.3 (création, insertion, jointures, regroupement, `LEFT JOIN`, rejet de clé étrangère) exécutées avec les résultats attendus ; commandes MariaDB/PostgreSQL non testées |