# Fiche_Simple_-_VM_Debian_12_Znuny_Scheduler.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing

---

## Problème précis à résoudre

Démarrer le scheduler Znuny pour les tâches de traitement et de maintenance.

## 1. Hors-Production (Lab / Test / POC)

1. Démarrer le script Cron de l'application avec le compte de service :
   ```bash
   sudo -u znuny /opt/znuny/bin/Cron.sh start
   ```
   👉 Explication : les tâches planifiées de Znuny s'exécutent sous le compte `znuny`.

2. Vérifier les tâches de l'application :
   ```bash
   sudo -u znuny /opt/znuny/bin/znuny.Console.pl List
   ```
   👉 Explication : la liste des commandes s'affiche si l'environnement Znuny est sain.

3. Rendre le démarrage persistant selon le mécanisme prévu par la version installée.
   👉 Explication : sans cela, les tâches s'arrêtent au redémarrage; ne pas lancer plusieurs schedulers concurrents.

## 2. Production — Contrôles

Surveiller les processus et logs du scheduler après chaque redémarrage.

## 3. Production — Sécurité

- Exécuter le scheduler uniquement avec le compte `znuny`.
- Ne pas lancer plusieurs instances concurrentes.

## Validation et retour arrière

- **Validation** : Les processus du scheduler apparaissent et les logs ne montrent pas d'erreur.
- **Retour arrière** : `sudo -u znuny /opt/znuny/bin/Cron.sh stop` pour arrêter les tâches.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Guide complet — activer les tâches de fond](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12#7-activer-les-taches-de-fond)