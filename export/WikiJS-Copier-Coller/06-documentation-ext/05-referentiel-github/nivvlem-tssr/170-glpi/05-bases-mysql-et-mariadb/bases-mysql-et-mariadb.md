# Les bases de MySQL et MariaDB
## 🧩 Rappels sur les SGBD

### Qu’est-ce qu’un SGBD ?

**Système de Gestion de Base de Données (SGBD)** :

- Permet de **stocker**, **organiser**, **manipuler** et **sécuriser** les données.

### SGBD relationnel (SGBDR)

- Les données sont organisées en **tables** (relationnelles)
- Chaque table est composée :
    - d’un **en-tête** : les colonnes (attributs)
    - d’un **corps** : les lignes (enregistrements)

### Exemples de SGBD

|SGBD|Caractéristiques|
|---|---|
|MySQL|SGBDR propriétaire / open source (Oracle)|
|MariaDB|Fork de MySQL, **100% open source** (Widenius)|
|PostgreSQL|Avancé, puissant, open source|
|Oracle DB|Propriétaire, hautes performances|
|SQL Server|Microsoft, intégré aux outils MS|

---

## 🗃️ Structure d’une base de données

- Une **base** contient plusieurs **tables**
- Une **table** contient des **colonnes** (attributs) et des **lignes** (enregistrements)
- Exemple :

|ID|Prénom|Nom|Ville|Âge|
|---|---|---|---|---|
|1|Fred|Enlefrigau|Stockholm|45|
|2|François|Belététoi|Pyongyang|26|

---

## 🔑 Clés dans une table

### Clé primaire (PRIMARY KEY)

- Identifie de manière **unique** chaque enregistrement
- Ne peut pas être **NULL**
- Génère un **index** pour accélérer les recherches

### Clé étrangère (FOREIGN KEY)

- Crée une relation **entre plusieurs tables**
- Assure l’**intégrité référentielle**
- Exemple : table des commandes fait référence à la table des clients

---

## 🔄 Commandes de base de MySQL/MariaDB

### Connexion

```bash
mysql -u root -p
```

### Afficher les bases existantes

```sql
SHOW DATABASES;
```

### Se connecter à une base

```sql
USE glpidata;
```

### Lister les tables d’une base

```sql
SHOW TABLES;
```

### Supprimer une base (⚠️ IRREVERSIBLE)

```sql
DROP DATABASE glpidata;
```

---

## 🔍 Commandes SQL de lecture (SELECT)

### SELECT basique

```sql
SELECT * FROM clients;
```

### Sélection de colonnes spécifiques

```sql
SELECT Nom, Ville FROM clients;
```

### Condition avec WHERE

```sql
SELECT Prenom, Nom FROM clients WHERE Ville = 'Caen';
```

### Opérateurs de comparaison

|Opérateur|Signification|
|---|---|
|=|égal|
|>|supérieur|
|<|inférieur|
|>=|supérieur ou égal|
|<=|inférieur ou égal|
|<> ou !=|différent|
|IS NULL / IS NOT NULL|Nullité|

### Combinaison de critères (AND / OR)

```sql
SELECT Prenom, Nom FROM clients WHERE ID >= 2 AND Ville = 'Caen';
```

### Tri des résultats

```sql
SELECT Prenom FROM clients ORDER BY age DESC;
```

### Limiter le nombre de lignes

```sql
SELECT Prenom FROM clients ORDER BY age LIMIT 2 OFFSET 1;
```

### Compter le nombre de lignes

```sql
SELECT COUNT(age) FROM clients;
```

### Alias (renommer une colonne)

```sql
SELECT Prenom AS Firstname FROM clients;
```

---

## 🧮 Fonctions d’agrégation

|Fonction|Description|
|---|---|
|MAX(colonne)|Valeur maximale|
|MIN(colonne)|Valeur minimale|
|SUM(colonne)|Somme totale|
|AVG(colonne)|Moyenne|

Exemple :

```sql
SELECT AVG(age) FROM clients;
```

---

## 🤝 Jointures (JOINS)

### Concept

- Permettent de **relier plusieurs tables** dans une même requête
- Exemple : récupérer les achats de chaque client

### INNER JOIN (jointure interne)

```sql
SELECT achat.nom
FROM achat
INNER JOIN client ON client.id = achat.id_client
WHERE client.Prenom = 'Yann';
```

### Résultat :

|Nom|
|---|
|Overwatch|
|League of Legends|
|Mario Kart 8 DELUXE|

---

## 🛠️ Requêtes utiles pour GLPI

### Lister les utilisateurs GLPI

```sql
USE glpidata;

SELECT name, realname, firstname, email
FROM glpi_users
ORDER BY name;
```

### Lister les tickets ouverts

```sql
SELECT id, name, status
FROM glpi_tickets
WHERE status < 6;
```

### Lister les équipements d’un utilisateur

```sql
SELECT glpi_computers.name AS ordinateur, glpi_users.name AS utilisateur
FROM glpi_computers
INNER JOIN glpi_users ON glpi_computers.users_id = glpi_users.id;
```

---

## 💾 Sauvegarde de la base GLPI

### Commande de sauvegarde (dump)

```bash
mysqldump -u root -p glpidata > /var/backups/glpidata-$(date +%F).sql
```

### Restauration

```bash
mysql -u root -p glpidata < glpidata-YYYY-MM-DD.sql
```

---

## ✅ À retenir pour les révisions

- MariaDB / MySQL est un **SGBDR** utilisé par GLPI pour stocker les données
- La commande **SELECT** permet d’extraire des informations
- Les **clés primaires** assurent l’unicité, les **clés étrangères** créent des relations
- Les **jointures** permettent de croiser les données entre plusieurs tables
- Il est essentiel de **sauvegarder régulièrement** la base GLPI

---

## 📌 Bonnes pratiques professionnelles

- Toujours utiliser `mysqldump` pour les sauvegardes **avant une mise à jour GLPI**
- Ne jamais faire de `DROP` sans **double vérification**
- Tester les requêtes dans un **environnement de test** avant en prod
- Automatiser la **sauvegarde quotidienne** via un cron
- Protéger les sauvegardes avec des droits restreints et un chiffrement si nécessaire
- Documenter les **requêtes fréquentes** utiles pour l’exploitation GLPI (rapports personnalisés)
- Surveiller les **performances de la base** (indexation, lenteurs)