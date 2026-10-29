# Fiche_Simple_-_VM_Debian_13_phpIPAM_Sauvegarder.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / sauvegarde

---

## Problème précis à résoudre

Sauvegarder la base et `config.php`, puis savoir restaurer.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   sudo install -d -m 0700 /var/backups/phpipam
   ```
   👉 Explication : crée un dossier de sauvegarde réservé à root.

2. Exécuter :
   ```bash
   sudo mariadb-dump --single-transaction phpipam | gzip | sudo tee /var/backups/phpipam/phpipam-$(date +%F).sql.gz >/dev/null
   ```
   👉 Explication : exporte la base de façon cohérente et la compresse.

3. Exécuter :
   ```bash
   sudo cp /var/www/phpipam/config.php /var/backups/phpipam/config.php
   sudo chmod 0600 /var/backups/phpipam/*
   ```
   👉 Explication : copie la configuration et protège les deux fichiers.

4. Copier les fichiers chiffrés hors de l'hôte et tester la restauration dans une base de laboratoire isolée.
   👉 Explication : une sauvegarde non restaurée n'est pas fiable.

## 2. Production — Contrôles

Avant mise à niveau : sauvegarder base et `config.php`, remplacer le code en gardant la configuration, exécuter la migration par l'interface, conserver l'ancien code et son dump jusqu'à validation.

## 3. Production — Sécurité

- Sauvegardes chiffrées, `config.php` contient l'accès SQL.
- Ne pas restaurer une base de production par-dessus une instance active.

## Validation et retour arrière

- **Validation** : le dump et `config.php` existent et une restauration isolée est validée.
- **Retour arrière** : restaurer le code de la version, le dump et la configuration, après arrêt des écritures.

## Si le problème n'est pas résolu

- [phpIPAM — mise à niveau et restauration](https://phpipam.net/documents/upgrade/)
- [phpIPAM — configuration de référence 1.8.3](https://github.com/phpipam/phpipam/blob/v1.8.3/config.dist.php)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13#7-sauvegarder-et-restaurer)