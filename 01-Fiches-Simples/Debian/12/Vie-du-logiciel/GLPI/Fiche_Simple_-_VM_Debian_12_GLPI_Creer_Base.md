# Fiche_Simple_-_VM_Debian_12_GLPI_Creer_Base.md

- **Environnement** : MariaDB local sur VM Debian hébergeant GLPI
- **OS / Version** : Debian 12 ou 13; MariaDB du dépôt approuvé
- **Catégorie** : GLPI / base de données
- **Tags** : `debian12`, `glpi`, `mariadb`, `database`, `least-privilege`

---

## Problème précis à résoudre

Créer une base GLPI dédiée et un compte SQL dont les accès sont limités à cette base.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser MariaDB :
   ```bash
   sudo mariadb-secure-installation
   ```
   👉 Explication : répondre aux questions (comptes anonymes, base de test, accès distant root).

2. Créer base et utilisateur (le mot de passe est saisi, pas écrit en clair) :
   ```bash
   read -rsp "Mot de passe base glpi : " GPW; echo
   sudo mariadb -e "CREATE DATABASE glpi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; CREATE USER 'glpi'@'localhost' IDENTIFIED BY '${GPW}'; GRANT ALL PRIVILEGES ON glpi.* TO 'glpi'@'localhost';"
   unset GPW
   ```
   👉 Explication : conserver le secret dans un coffre, hors dépôt.

3. Vérifier :
   ```bash
   sudo mariadb -e "SHOW GRANTS FOR 'glpi'@'localhost'; SHOW DATABASES LIKE 'glpi';"
   sudo ss -lntp | grep ':3306'
   ```
   👉 Explication : MariaDB doit écouter en local uniquement.

## 2. Production — Contrôles

Valider propriétaire de la base, privilèges, secret, accès réseau, procédure de rotation, sauvegarde et restauration.

## 3. Production — Sécurité

- Ne pas conserver le secret SQL dans le dépôt, le wiki ou l'historique shell.
- Ne pas créer un compte accessible depuis `%`.
- Ne pas donner des droits globaux au compte applicatif.
- Garder MariaDB en écoute locale, sauf architecture distante privée explicitement approuvée.

## Validation et retour arrière

- **Validation** : connexion réussie avec le compte dédié et privilèges limités à la base GLPI.
- **Retour arrière** : conserver export et configuration avant modification; révoquer ou supprimer la base seulement après validation qu'elle ne contient pas de données à conserver.

## Si le problème n'est pas résolu

- [MariaDB — gestion des comptes](https://mariadb.com/kb/en/account-management-sql-commands/)
- [GLPI — prérequis](https://glpi-install.readthedocs.io/en/latest/prerequisites.html)
- [Guide complet GLPI Debian](../../../../../02-Fiches-Completes/Debian/12/Installation-Deploiement/03_Helpdesk_ITSM_GLPI_11_12_Debian_12_13.md)
