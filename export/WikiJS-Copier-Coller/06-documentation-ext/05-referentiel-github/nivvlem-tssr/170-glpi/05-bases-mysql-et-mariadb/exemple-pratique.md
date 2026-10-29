# TP – Requêtes SQL sur la base GLPI
## 🏗️ Étapes détaillées

### 1️⃣ Connexion à la base de données GLPI

```bash
mysql -u root -p
```

---

### 2️⃣ Afficher les bases existantes

```sql
SHOW DATABASES;
```

---

### 3️⃣ Connexion à la base `glpidata`

```sql
USE glpidata;
```

### Afficher les tables de la base

```sql
SHOW TABLES;
```

---

### 4️⃣ Afficher les attributs de la table des calendriers

```sql
SELECT * FROM glpi_calendars;
```

---

### 5️⃣ Afficher les noms et prénoms des utilisateurs de GLPI

```sql
SELECT name, firstname FROM glpi_users;
```

---

### 6️⃣ Afficher le nom des utilisateurs en anglais (en_GB)

```sql
SELECT name FROM glpi_users WHERE language = 'en_GB';
```

---

### 7️⃣ Afficher les catégories de tickets enfants (niveau > 1)

#### Option 1 : Comparaison des noms

```sql
SELECT name, completename FROM glpi_itilcategories WHERE completename <> name;
```

#### Option 2 : Utiliser le champ `level`

```sql
SELECT name, completename FROM glpi_itilcategories WHERE level > '1';
```

---

### 8️⃣ Afficher les switches réseau non gabarits liés au modèle `GAB-JL356A-ARUBA-2540-24P`

Conditions :

- **is_template** = 0 (non gabarit)
- **networkequipmentmodels_id** = 2

```sql
SELECT name FROM glpi_networkequipments WHERE is_template = '0' AND networkequipmentmodels_id = '2';
```

---

### 9️⃣ Compter le nombre de SLMs (avec alias)

```sql
SELECT COUNT(name) AS nb_de_SLMs FROM glpi_slms;
```

---

### 1️⃣0️⃣ Afficher le switch avec le plus grand nom (MAX)

```sql
SELECT MAX(name) FROM glpi_networkequipments WHERE networkequipmentmodels_id = '2';
```

---

## 🏅 BONUS : Jointures internes

### 1️⃣1️⃣ Afficher le(s) nom(s) de la catégorie de ticket et le nom du gabarit utilisé pour les demandes

```sql
SELECT glpi_tickettemplates.name, glpi_itilcategories.name
FROM glpi_tickettemplates
INNER JOIN glpi_itilcategories ON glpi_itilcategories.tickettemplates_id_demand = glpi_tickettemplates.id
WHERE glpi_itilcategories.tickettemplates_id_demand = '3';
```

---

### 1️⃣2️⃣ Compter les catégories utilisant un gabarit de demande

```sql
SELECT COUNT(glpi_tickettemplates.name) AS 'nombre de catégories qui utilise un gabarit de demande',
       glpi_tickettemplates.name
FROM glpi_tickettemplates
INNER JOIN glpi_itilcategories ON glpi_itilcategories.tickettemplates_id_demand = glpi_tickettemplates.id
WHERE glpi_itilcategories.tickettemplates_id_demand = '3';
```

---

## ✅ À retenir pour les révisions

- Le **SELECT** est la base de toute interrogation
- **WHERE** permet de filtrer les résultats
- Les **alias** (AS) rendent les résultats plus lisibles
- Les **jointures (JOIN)** permettent de croiser plusieurs tables
- Les **fonctions d’agrégation** (COUNT, MAX) permettent des statistiques simples

---

## 📌 Bonnes pratiques professionnelles

- Toujours utiliser `USE glpidata;` avant toute requête
- Tester les requêtes d’abord en **sélection simple** avant de complexifier
- Vérifier les relations entre les tables avec **JOIN**
- Écrire les requêtes de manière lisible (retours à la ligne, alias)
- Automatiser les requêtes utiles dans des **vues** ou des **rapports externes**
- Sauvegarder la base avant d’utiliser des requêtes de modification (UPDATE, DELETE)
- Utiliser des **outils graphiques** (ex : phpMyAdmin, DBeaver, HeidiSQL) en complément pour l’exploration