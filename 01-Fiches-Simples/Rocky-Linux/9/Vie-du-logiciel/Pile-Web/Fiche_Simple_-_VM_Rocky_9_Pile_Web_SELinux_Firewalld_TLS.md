# Fiche_Simple_-_VM_Rocky_9_Pile_Web_SELinux_Firewalld_TLS.md

- **Environnement** : VM ou serveur Rocky Linux 9 hébergeant une application PHP avec MariaDB locale
- **OS / Version** : Rocky Linux 9 / RHEL 9; Nginx, PHP-FPM et MariaDB des dépôts actifs
- **Catégorie** : services web / sécurité
- **Tags** : `rocky9`, `nginx`, `php-fpm`, `mariadb`, `selinux`

---

## Problème précis à résoudre

Garder SELinux et firewalld actifs et préparer le TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler SELinux :
   ```bash
   getenforce
   ```
   👉 Explication : Doit afficher `Enforcing`.

2. Restaurer les contextes :
   ```bash
   sudo restorecon -Rv /var/www/app
   ```
   👉 Explication : Réapplique les contextes SELinux par défaut sur le répertoire web (chemin à adapter).

3. Contrôler le pare-feu :
   ```bash
   sudo firewall-cmd --get-active-zones
   sudo firewall-cmd --list-all
   ```
   👉 Explication : Affiche les zones actives et les services autorisés de la zone par défaut.

4. Ouvrir HTTP/HTTPS :
   ```bash
   sudo firewall-cmd --permanent --add-service=http --add-service=https
   sudo firewall-cmd --reload
   ```
   👉 Explication : Ouvre seulement HTTP/HTTPS dans la zone par défaut; ajouter `--zone=` si la zone active est autre.

5. Configurer TLS avec une autorité et un certificat approuvés, avec procédure de renouvellement.
   👉 Explication : le chiffrement doit être en place avant l'ouverture aux utilisateurs.

## 2. Production — Contrôles

Pour un chemin web personnalisé, créer un contexte persistant et valider l'absence de refus AVC.

## 3. Production — Sécurité

- Ne jamais désactiver SELinux ni firewalld pour dépanner.

## Validation et retour arrière

- **Validation** : SELinux en Enforcing, seuls les services nécessaires sont ouverts, TLS fonctionnel.
- **Retour arrière** : `sudo firewall-cmd --permanent --remove-service=http --remove-service=https` puis `--reload`.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet — étape 5](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/23_Pile_Web_Rocky_Linux_9_Nginx_PHP_MariaDB.md#5-selinux-firewalld-et-tls)
