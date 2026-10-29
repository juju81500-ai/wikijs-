# Fiche_Simple_-_VM_Debian_12_Cacti_Base_et_Credential.md

- **Environnement** : VM Debian 12 dédiée (Apache, PHP, MariaDB, poller local)
- **OS / Version** : Debian 12 Bookworm; Cacti 1.2.31
- **Catégorie** : supervision / base de données
- **Tags** : `debian12`, `cacti`, `snmp`, `rrdtool`, `mariadb`

---

## Problème précis à résoudre

Créer la base `cacti` et un compte dédié sans mot de passe d'exemple.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir MariaDB en administrateur local :
   ```bash
   sudo mariadb
   ```
   👉 Explication : connexion par socket, sans mot de passe en argument.

2. Dans l'invite MariaDB, créer la base en `utf8mb4` :
   ```sql
   CREATE DATABASE cacti CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   👉 Explication : crée la base applicative.

3. Créer un compte dédié à localhost avec un secret aléatoire issu du coffre :
   ```sql
   CREATE USER 'cacti'@'localhost' IDENTIFIED BY 'SECRET_A_REMPLACER';
   GRANT ALL PRIVILEGES ON cacti.* TO 'cacti'@'localhost';
   FLUSH PRIVILEGES;
   ```
   👉 Explication : `SECRET_A_REMPLACER` est une valeur d'exemple : la remplacer par un mot de passe aléatoire propre; ne jamais garder `cactiuser`. Accorder aussi la lecture de la table timezone comme l'indique la documentation Cacti.

4. Importer le schéma de la même release :
   ```bash
   sudo mariadb cacti < /var/www/html/cacti/cacti.sql
   ```
   👉 Explication : charge les tables; le schéma doit venir de la même version que le code.

5. Renseigner les identifiants dans `include/config.php` puis restreindre ses droits :
   ```bash
   sudo chmod 640 /var/www/html/cacti/include/config.php
   ```
   👉 Explication : seuls le propriétaire et le groupe web lisent le secret.

## 2. Production — Contrôles

Stocker le secret dans le coffre de l'organisation.

## 3. Production — Sécurité

- Aucun mot de passe en argument de commande ni dans l'historique.
- MariaDB n'écoute que sur localhost.

## Validation et retour arrière

- **Validation** : `sudo mariadb -e 'SHOW DATABASES LIKE "cacti";'` retourne la base.
- **Retour arrière** : En test : `DROP DATABASE cacti;` et `DROP USER 'cacti'@'localhost';` — destructif, uniquement avant mise en service.

## Si le problème n'est pas résolu

- [Cacti — documentation officielle](https://docs.cacti.net/)
- [Cacti — installation Ubuntu/Debian](https://docs.cacti.net/Installing-Under-Ubuntu-Debian.md)
- [Guide complet — 4. Créer la base et la credential applicative](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/51_Deploiement_Cacti_1.2.31_Debian_12.md#4-creer-la-base-et-la-credential-applicative)
