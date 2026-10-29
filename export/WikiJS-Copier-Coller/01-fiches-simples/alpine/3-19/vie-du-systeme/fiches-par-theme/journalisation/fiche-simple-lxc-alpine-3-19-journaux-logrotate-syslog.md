# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Journaux_Logrotate_Syslog.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Système & Services / Journaux et centralisation

## 🎯 Problème précis à résoudre
Vérifier la journalisation d'un conteneur Alpine Linux (BusyBox `syslogd`), configurer la rotation des journaux avec `logrotate` et transmettre les événements à un collecteur distant.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier que le service de journalisation tourne et écrit dans `/var/log` :
   ```sh
   rc-service syslog status
   ls -l /var/log
   tail -n 5 /var/log/messages
   ```
   👉 Explication : Sous Alpine, le service `syslog` (BusyBox `syslogd`) écrit par défaut dans `/var/log/messages`. Sans ce fichier, aucun outil de rotation ni de collecte n'a de source.

2. Installer `logrotate` et tester la configuration en mode simulation :
   ```sh
   apk add logrotate
   logrotate -d /etc/logrotate.conf
   ```
   👉 Explication : L'option `-d` (debug) affiche ce que `logrotate` ferait sans rien modifier ni renommer.

---

## ⚡ 2. Production — Façon Simplifiée
1. Envoyer les journaux vers le collecteur distant, en gardant une copie locale :
   ```sh
   cat /etc/conf.d/syslog
   ```
   Ajouter ou remplacer la variable suivante dans `/etc/conf.d/syslog` :
   ```text
   SYSLOGD_OPTS="-L -R <ip_collecteur>:514"
   ```
   👉 Explication : `-R` transmet les messages en UDP au collecteur (SIEM ou rsyslog distant); `-L` conserve aussi l'écriture locale dans `/var/log/messages`.

2. Redémarrer le service et vérifier l'envoi :
   ```sh
   rc-service syslog restart
   logger -t test-collecte "Message de test depuis <nom_du_conteneur>"
   ```
   👉 Explication : Le message de test doit apparaître dans `/var/log/messages` local et sur le collecteur distant.

3. Créer une règle de rotation pour l'application :
   ```text
   /var/log/<nom_application>/*.log {
       weekly
       rotate 8
       compress
       missingok
       notifempty
       create 0640 <service_nom> <service_groupe>
       postrotate
           rc-service <nom_du_service> reload > /dev/null
       endscript
   }
   ```
   Enregistrer ce bloc dans `/etc/logrotate.d/<nom_application>`.
   👉 Explication : Les journaux sont compressés chaque semaine et conservés 8 cycles. La directive `create` recrée le fichier avec le propriétaire du service ; `<service_nom>` et `<service_groupe>` doivent exister.

---

## 🔒 3. Production — Façon Sécurisée
1. Vérifier que `logrotate` est lancé chaque jour par `crond` :
   ```sh
   ls /etc/periodic/daily/
   ```
   👉 Explication : Si `logrotate` n'apparaît pas dans la liste, ajouter une tâche explicite dans la crontab de root avec `echo '0 4 * * * /usr/sbin/logrotate /etc/logrotate.conf' >> /etc/crontabs/root`, puis vérifier avec `crontab -l`. Ne l'ajouter qu'une fois.

2. Limiter les droits des journaux applicatifs et vérifier qu'ils ne sont pas lisibles par tous :
   ```sh
   ls -l /var/log/<nom_application>/
   ```
   👉 Explication : Les journaux peuvent contenir des identifiants, des adresses IP ou des requêtes. Leurs droits doivent exclure les comptes non concernés (ex : `0640`).