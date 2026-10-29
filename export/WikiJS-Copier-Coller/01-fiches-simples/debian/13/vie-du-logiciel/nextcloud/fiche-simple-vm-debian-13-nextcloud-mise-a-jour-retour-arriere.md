# Fiche_Simple_-_VM_Debian_13_Nextcloud_Mise_A_Jour_Retour_Arriere

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Mise à jour et retour arrière

---

## Problème précis à résoudre

Mettre à jour Nextcloud avec l'updater officiel et prévoir le retour arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder (fiche Sauvegarder / restaurer) et prendre un snapshot de VM.
   👉 Explication : le retour arrière fiable repose sur la sauvegarde complète : base et fichiers.

2. Vérifier la compatibilité de la version cible (PHP, BDD, applications tierces) dans les notes de version.
   👉 Explication : Nextcloud n'autorise pas de sauter une version majeure : mettre à jour une majeure à la fois.

3. Lancer l'updater en ligne de commande :
   ```bash
   cd /var/www/nextcloud
   sudo -u www-data php updater/updater.phar
   ```
   👉 Explication : l'updater télécharge, vérifie et applique la version suivante ; suivre les questions affichées.

4. Terminer les migrations :
   ```bash
   sudo -u www-data php occ upgrade
   sudo -u www-data php occ maintenance:mode --off
   sudo -u www-data php occ db:add-missing-indices
   ```
   👉 Explication : `upgrade` applique les migrations de base ; vérifier ensuite la page Vue d'ensemble.

5. Rejouer la recette (fiche Valider).
   👉 Explication : version, état, cron, fichier de test.

## 2. Production — Contrôles

Fenêtre de maintenance, utilisateurs prévenus, applications tierces compatibles, mises à jour PHP/OS gérées séparément (fiche Debian).

## 3. Production — Sécurité

- Utiliser uniquement l'updater officiel ou l'archive vérifiée.
- Désactiver temporairement les applications tierces non compatibles.

## Validation et retour arrière

- **Validation** : `occ status` affiche la version cible, mode maintenance désactivé, recette OK.
- **Retour arrière** : mode maintenance activé, restauration des fichiers, de la base et de la configuration issus de la sauvegarde d'avant mise à jour (voir la fiche Sauvegarder / restaurer), ou restauration du snapshot.

## Si le problème n'est pas résolu

- [Nextcloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-prerequis-limites)
- [Nextcloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-installer)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)