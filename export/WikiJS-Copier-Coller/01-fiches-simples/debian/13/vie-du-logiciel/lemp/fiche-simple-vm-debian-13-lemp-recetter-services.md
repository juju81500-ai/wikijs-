# Fiche_Simple_-_VM_Debian_13_LEMP_Recetter_Services.md

- **Environnement** : pile LEMP Debian 13 en lab ou après changement approuvé
- **OS / Version** : Debian 13; Nginx, MariaDB et PHP-FPM
- **Catégorie** : pile Web LEMP / recette

---

## Problème précis à résoudre

Vérifier que Nginx, MariaDB et PHP-FPM fonctionnent ensemble sans masquer d'erreur ni laisser l'endpoint de test en place.

## 1. Hors-Production (Lab / Test / POC)

1. Tester la page PHP :
   ```bash
   curl -fsS -H 'Host: app.example.net' http://127.0.0.1/
   ```
   👉 Explication : réponse attendue `PHP-FPM fonctionne`.

2. Valider Nginx et l'état des services :
   ```bash
   sudo nginx -t
   systemctl --no-pager --full status nginx mariadb php8.4-fpm
   systemctl --no-pager --failed
   ```
   👉 Explication : aucun service en échec.

3. Lire les journaux récents :
   ```bash
   sudo journalctl -u nginx -u mariadb -u php8.4-fpm --since '-15 minutes' --no-pager
   ```
   👉 Explication : repérer les erreurs de socket ou de base.

4. Supprimer le fichier de test avant de déployer l'application :
   ```bash
   sudo rm /var/www/app/public/index.php
   ```
   👉 Explication : un script de test public est une surface d'attaque inutile.

## 2. Production — Contrôles

Effectuer la recette depuis les réseaux approuvés, vérifier les journaux et confirmer que la supervision et les alertes sont opérationnelles.

## 3. Production — Sécurité

- Ne pas renvoyer les erreurs PHP détaillées aux visiteurs.
- Ne pas publier les ports d'administration ou MariaDB au-delà du besoin.
- Ne pas laisser un endpoint de diagnostic accessible après validation.
- Protéger les journaux qui pourraient contenir chemins, requêtes ou données sensibles.

## Validation et retour arrière

- **Validation** : services actifs, requête attendue, journaux propres et endpoint de test retiré.
- **Retour arrière** : désactiver le site concerné après sauvegarde de sa configuration et rétablir la version précédente validée.

## Si le problème n'est pas résolu

- [Nginx — dépannage](https://docs.nginx.com/nginx/admin-guide/monitoring/logging/)
- [MariaDB — documentation](https://mariadb.com/kb/en/documentation/)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb#4-controles-fonctionnels)