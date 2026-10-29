# Fiche_Simple_-_VM_Debian_12_Zabbix_Sauvegarder_Mettre_A_Jour.md

- **Environnement** : serveur Zabbix Debian 12; sauvegardes cohérentes de base et configuration
- **OS / Version** : Debian 12; Zabbix 7.0 LTS
- **Catégorie** : supervision / sauvegarde et mise à jour

---

## Problème précis à résoudre

Mettre à jour le serveur Zabbix ou le restaurer à partir d'un point cohérent de base et de configuration.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la base et la configuration :
   ```bash
   sudo mariadb-dump --single-transaction --routines --triggers zabbix | gzip > /root/zabbix-db-$(date +%F).sql.gz
   sudo tar czf /root/zabbix-etc-$(date +%F).tgz /etc/zabbix
   ```
   👉 Explication : `--single-transaction` donne un export cohérent; copier ensuite hors du serveur. Les tables d'historique volumineuses peuvent justifier une stratégie dédiée.

2. Tester la restauration sur une base isolée :
   ```bash
   sudo mariadb -e 'CREATE DATABASE zabbix_test'
   gunzip -c /root/zabbix-db-AAAA-MM-JJ.sql.gz | sudo mariadb zabbix_test
   sudo mariadb -e 'DROP DATABASE zabbix_test'
   ```
   👉 Explication : remplacer la date; documenter la rétention.

3. Avant une mise à jour majeure : consulter la matrice officielle, puis arrêter le serveur :
   ```bash
   sudo systemctl stop zabbix-server
   sudo apt update && apt list --upgradable 2>/dev/null | grep zabbix
   ```
   👉 Explication : sauvegarde faite d'abord; ne mettre à niveau qu'une version majeure à la fois.

4. En cas d'échec : restaurer la base et `/etc/zabbix` sauvegardés :
   ```bash
   sudo systemctl stop zabbix-server
   gunzip -c /root/zabbix-db-AAAA-MM-JJ.sql.gz | sudo mariadb zabbix
   sudo tar xzf /root/zabbix-etc-AAAA-MM-JJ.tgz -C /
   ```
   👉 Explication : réinstaller aussi la version précédente des paquets si besoin, puis redémarrer et valider.

## 2. Production — Contrôles

Faire approuver versions source/cible, fenêtre, sauvegarde restaurable, critères de validation, responsable et durée réelle de reprise.

## 3. Production — Sécurité

- Ne pas mettre à niveau sans sauvegarde vérifiée.
- Ne pas restaurer base et configuration prises à des points incohérents.
- Protéger les sauvegardes de base, secrets et configuration.
- Ne pas supprimer l'ancienne sauvegarde tant que la nouvelle version n'est pas acceptée.

## Validation et retour arrière

- **Validation** : restauration testée, services et données de supervision cohérents après changement.
- **Retour arrière** : restaurer ensemble base et configuration à un point cohérent, puis vérifier collecte et alertes.

## Si le problème n'est pas résolu

- [Zabbix — mise à niveau](https://www.zabbix.com/documentation/7.0/en/manual/installation/upgrade)
- [MariaDB — sauvegarde et restauration](https://mariadb.com/kb/en/backup-and-restore-overview/)
- [Guide complet Zabbix Debian 12](/02-fiches-completes/debian/12/installation-deploiement/04-supervision-centralisee-zabbix-70-lts-debian-12)