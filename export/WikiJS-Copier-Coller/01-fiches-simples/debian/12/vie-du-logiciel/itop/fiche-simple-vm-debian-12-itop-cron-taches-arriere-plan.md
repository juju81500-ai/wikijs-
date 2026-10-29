# 📄 Fiche_Simple_-_VM_Debian_12_iTop_Cron_Taches_Arriere_Plan.md

- **Environnement** : VM Debian dédiée à iTop 3.3
- **OS / Version** : Debian 12 Bookworm; PHP 8.2; compte de service Apache `www-data`
- **Catégorie** : Système / tâches planifiées

---

## 🎯 Problème précis à résoudre

Activer les tâches de fond iTop (SLA, notifications, sauvegardes planifiées) sans exposer de mot de passe dans la ligne de commande.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état des tâches depuis le compte web :
   ```bash
   sudo -u www-data php /var/www/itop/webservices/cron.php --status_only=1
   ```
   👉 Explication : adapter `/var/www/itop`; si iTop n'est pas à cet emplacement, ne pas lancer la commande.

## ⚡ 2. Production — Façon Simplifiée

1. Créer le fichier de paramètres hors du site :
   ```bash
   sudo install -d -o root -g www-data -m 0750 /etc/itop
   sudo install -o www-data -g www-data -m 0600 /dev/null /etc/itop/cron.params
   sudoedit /etc/itop/cron.params
   ```
   👉 Explication : le fichier est hors du DocumentRoot et lisible par le seul processus web.

2. Contenu du fichier, avec un compte dédié aux tâches d'arrière-plan :
   ```ini
   auth_user = itop-cron
   auth_pwd = SECRET_DEDIE
   ```
   👉 Explication : remplacer par la valeur réelle (sans chevrons); jamais dans la crontab.

3. Tester l'exécution :
   ```bash
   sudo -u www-data /usr/bin/php /var/www/itop/webservices/cron.php --param_file=/etc/itop/cron.params --status_only=1
   ```
   👉 Explication : doit afficher l'état sans erreur d'authentification.

4. Planifier chaque minute :
   ```bash
   sudoedit /etc/cron.d/itop
   ```
   Ajouter :
   ```cron
   * * * * * www-data /usr/bin/php /var/www/itop/webservices/cron.php --param_file=/etc/itop/cron.params >> /var/log/itop-cron.log 2>&1
   ```
   👉 Explication : exécuté par `www-data` (jamais root); prévoir la rotation de `/var/log/itop-cron.log`.

## 🔒 3. Production — Façon Sécurisée

- Utiliser un compte iTop dédié et de privilèges minimaux; ne pas réutiliser le compte personnel d'un administrateur.
- Garder `cron.params` hors du DocumentRoot, lisible uniquement par le processus web et protégé contre les modifications non autorisées.
- Le fichier doit contenir les valeurs réelles, pas les chevrons `<...>`; ne jamais mettre le secret dans la crontab.
- Ne pas exécuter `cron.php` en root. Surveiller la croissance du journal et configurer sa rotation.
- Contrôler `cron_max_execution_time` dans la configuration iTop et surveiller les tâches qui restent bloquées.

## ✅ Validation et retour arrière

- **Précontrôles** : vérifier le chemin, `www-data`, PHP CLI et le compte `itop-cron`.
- **Validation** : `sudo -u www-data ... --status_only=1`, puis vérifier `/var/log/itop-cron.log` et l'heure de dernière exécution dans iTop.
- **Retour arrière** : retirer `/etc/cron.d/itop`, puis contrôler avec `sudo crontab -u www-data -l` si une ancienne tâche utilisateur existait. Garder le fichier de paramètres sécurisé pour réactivation.

## 🔗 Si le problème n'est pas résolu

- **Fiche de résolution complémentaire** : [[Debian12_iTop_Cron_Tache_Echec]]
- [Documentation officielle iTop — Tâches planifiées](https://www.itophub.io/wiki/page?id=latest:admin:cron)