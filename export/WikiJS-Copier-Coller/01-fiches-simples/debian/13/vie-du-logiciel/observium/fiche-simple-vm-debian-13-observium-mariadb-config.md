# Fiche_Simple_-_VM_Debian_13_Observium_MariaDB_Config.md

- **Environnement** : Observium Community sur Debian 13 (Apache/PHP, MariaDB, SNMPv3)
- **OS / Version** : Debian 13 Trixie x86-64; Observium Community
- **Catégorie** : supervision réseau / base de données

---

## Problème précis à résoudre

Créer la base et le compte dédiés puis initialiser le schéma sans exposer de secret.

## 1. Hors-Production (Lab / Test / POC)

1. Activer MariaDB :
   ```bash
   sudo systemctl enable --now mariadb
   sudo systemctl --no-pager status mariadb
   ```
   👉 Explication : le service de base doit tourner avant de créer le schéma.

2. Saisir le mot de passe de la base sans l'afficher, puis créer base et compte :
   ```bash
   read -rsp 'Mot de passe base observium : ' OBS_DB_PW; echo
   sudo mariadb <<SQL
   CREATE DATABASE observium DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
   CREATE USER 'observium'@'localhost' IDENTIFIED BY '${OBS_DB_PW}';
   GRANT ALL ON observium.* TO 'observium'@'localhost';
   SQL
   unset OBS_DB_PW
   ```
   👉 Explication : le secret reste en variable de session (jamais en argument de commande) et le compte n'a de droits que sur la base `observium`.

3. Copier la configuration puis éditer le compte base :
   ```bash
   cd /opt/observium
   sudo cp config.php.default config.php
   sudoedit config.php
   ```
   👉 Explication : renseigner `$config['db_user']`, `$config['db_pass']` et `$config['db_name']` avec les valeurs créées.

4. Protéger le fichier et préparer les dossiers :
   ```bash
   sudo chown root:www-data config.php
   sudo chmod 0640 config.php
   sudo install -d -o www-data -g www-data -m 0750 rrd logs
   ```
   👉 Explication : `config.php` contient des identifiants : lecture limitée à root et au groupe web.

5. Initialiser le schéma :
   ```bash
   sudo ./discovery.php -u
   ```
   👉 Explication : la commande crée ou met à jour le schéma; contrôler la sortie, ne pas ignorer d'erreur de base.

## 2. Production — Contrôles

Compte base unique et secret aléatoire, sauvegardes MariaDB testées, sortie de `discovery.php -u` sans erreur.

## 3. Production — Sécurité

- Ne jamais publier le mot de passe base dans un ticket ou script.
- Sauvegarder `/etc/snmp/snmp.conf` avant toute modification de la directive `mibs :`.

## Validation et retour arrière

- **Validation** : `sudo mariadb -e 'SHOW TABLES' observium` liste des tables et `config.php` est en 0640.
- **Retour arrière** : `sudo mariadb -e 'DROP DATABASE observium; DROP USER observium@localhost'` en lab uniquement, après sauvegarde si des données existent.

## Si le problème n'est pas résolu

- [Observium — installation Debian/Ubuntu](https://docs.observium.org/install_debian/)
- [Observium — prérequis logiciels](https://docs.observium.org/software_requirements/)
- [Observium — ajouter un équipement](https://docs.observium.org/add_device/)
- [Guide complet — étape 4](/02-fiches-completes/debian/13/installation-deploiement/69-deploiement-observium-community-debian-13#4-preparer-mariadb-et-la-configuration)