# Fiche_Simple_-_VM_Debian_13_Nextcloud_Valider

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Valider (recette)
- **Tags** : `debian13`, `nextcloud`, `cloud`, `apache`, `php`, `valider`

---

## Problème précis à résoudre

Recetter l'instance Nextcloud : service, état applicatif, accès web, tâches de fond et dépôt de fichier.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les services :
   ```bash
   systemctl is-active apache2 mariadb
   ```
   👉 Explication : les deux services doivent être `active`.

2. Contrôler l'état applicatif :
   ```bash
   cd /var/www/nextcloud
   sudo -u www-data php occ status
   curl -fsS https://CLOUD.EXAMPLE.NET/status.php
   ```
   👉 Explication : `installed: true`, `maintenance: false` et la version attendue.

3. Contrôler les vérifications d'installation :
   ```bash
   sudo -u www-data php occ setupchecks
   ```
   👉 Explication : commande disponible selon la version ; sinon consulter Administration > Vue d'ensemble. Corriger les avertissements importants.

4. Tester depuis un navigateur : connexion, dépôt/téléchargement d'un fichier de test, déconnexion.
   👉 Explication : vérifie la chaîne complète (HTTPS, PHP, base, stockage).

5. Vérifier le cron :
   ```bash
   sudo -u www-data php occ config:app:get core lastcron
   ```
   👉 Explication : la valeur doit évoluer toutes les 5 minutes (horodatage UNIX).

## 2. Production — Contrôles

Consigner version, date, résultats ; contrôler `data/nextcloud.log` et journaux Apache ; supprimer le fichier de test.

## 3. Production — Sécurité

- Ne pas laisser de compte de test.
- Ne pas diffuser le contenu de `status.php` hors équipe si la version est sensible.

## Validation et retour arrière

- **Validation** : statut applicatif sain, accès HTTPS, cron actif, fichier de test déposé et lu.
- **Retour arrière** : en cas d'échec, revenir à la configuration sauvegardée ou activer le mode maintenance (`occ maintenance:mode --on`) le temps de corriger.

## Si le problème n'est pas résolu

- [Nextcloud — Prérequis et limites](Fiche_Simple_-_VM_Debian_13_Nextcloud_Prerequis_Limites.md)
- [Nextcloud — Installer](Fiche_Simple_-_VM_Debian_13_Nextcloud_Installer.md)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)
