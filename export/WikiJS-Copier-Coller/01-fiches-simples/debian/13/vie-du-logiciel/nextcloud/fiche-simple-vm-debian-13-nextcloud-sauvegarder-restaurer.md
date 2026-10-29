# Fiche_Simple_-_VM_Debian_13_Nextcloud_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13; Nextcloud (archive officielle), Apache, PHP 8.4 et MariaDB
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / Nextcloud — Sauvegarder / restaurer

---

## Problème précis à résoudre

Sauvegarder et restaurer Nextcloud (code, config, données, base) de façon cohérente.

## 1. Hors-Production (Lab / Test / POC)

1. Activer le mode maintenance :
   ```bash
   cd /var/www/nextcloud
   sudo -u www-data php occ maintenance:mode --on
   ```
   👉 Explication : fige l'état de l'application pendant la sauvegarde.

2. Copier fichiers et configuration :
   ```bash
   sudo rsync -aAX /var/www/nextcloud/ /var/backups/nextcloud/app/
   sudo rsync -aAX /srv/nextcloud-data/ /var/backups/nextcloud/data/
   ```
   👉 Explication : conserve droits et attributs ; le dossier `config/` est dans l'application.

3. Sauvegarder la base :
   ```bash
   sudo mariadb-dump --single-transaction nextcloud | gzip > /var/backups/nextcloud/nextcloud-db-$(date +%F).sql.gz
   ```
   👉 Explication : la sauvegarde ne contient pas le mot de passe ; l'accès se fait via le compte root local (socket).

4. Désactiver le mode maintenance :
   ```bash
   sudo -u www-data php occ maintenance:mode --off
   ```
   👉 Explication : retour à l'état normal.

5. Restaurer (sur une VM de lab, puis en production si nécessaire) :
   ```bash
   sudo rsync -aAX /var/backups/nextcloud/app/ /var/www/nextcloud/
   sudo rsync -aAX /var/backups/nextcloud/data/ /srv/nextcloud-data/
   zcat /var/backups/nextcloud/nextcloud-db-DATE.sql.gz | sudo mariadb nextcloud
   sudo -u www-data php /var/www/nextcloud/occ maintenance:data-fingerprint
   ```
   👉 Explication : `DATE` est à remplacer ; la base doit exister et être vide ; `data-fingerprint` signale aux clients de synchronisation qu'une restauration a eu lieu.

## 2. Production — Contrôles

Planifier la sauvegarde, la chiffrer et l'externaliser (voir [Restic — dépôt de sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot)), tester la restauration, conserver base et fichiers du même instant.

## 3. Production — Sécurité

- Archives de données en droits restreints (contiennent des fichiers utilisateurs).
- Chiffrer toute copie hors serveur.
- Ne pas laisser le mode maintenance actif.

## Validation et retour arrière

- **Validation** : restauration testée en lab : connexion OK et fichiers lisibles.
- **Retour arrière** : remettre la sauvegarde précédente ou restaurer le snapshot de VM.

## Si le problème n'est pas résolu

- [Nextcloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-prerequis-limites)
- [Nextcloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nextcloud/fiche-simple-vm-debian-13-nextcloud-installer)
- [Restic — dépôt de sauvegarde](/01-fiches-simples/debian/13/vie-du-logiciel/restic/fiche-simple-vm-debian-13-sauvegarde-restic-depot)
- [Nextcloud — manuel d'administration](https://docs.nextcloud.com/server/latest/admin_manual/)
- [Nextcloud — prérequis système](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html)