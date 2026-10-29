# Fiche_Simple_-_VM_Debian_13_LEMP_Sauvegarder_Retour_Arriere.md

- **Environnement** : application LEMP Debian 13; sauvegarde de configuration et export MariaDB vérifiés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : pile Web LEMP / sauvegarde et reprise
- **Tags** : `debian13`, `lemp`, `backup`, `restore`, `rollback`, `mariadb`

---

## Problème précis à résoudre

Pouvoir revenir à une configuration cohérente après un changement Nginx ou une modification de données MariaDB.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder la configuration Nginx :
   ```bash
   sudo tar czf /root/nginx-conf-$(date +%F).tgz /etc/nginx
   ```
   👉 Explication : conserver l'archive hors du serveur.

2. Exporter la base :
   ```bash
   sudo mariadb-dump --single-transaction --routines appdb | gzip > /root/appdb-$(date +%F).sql.gz
   ```
   👉 Explication : `--single-transaction` donne un export cohérent sans verrouiller (InnoDB).

3. Prouver la restauration sur une base de test :
   ```bash
   sudo mariadb -e 'CREATE DATABASE appdb_test'
   gunzip -c /root/appdb-AAAA-MM-JJ.sql.gz | sudo mariadb appdb_test
   sudo mariadb -e 'DROP DATABASE appdb_test'
   ```
   👉 Explication : remplacer la date; une sauvegarde non restaurée n'est pas prouvée.

4. Retour arrière de configuration en cas d'échec :
   ```bash
   sudo rm /etc/nginx/sites-enabled/app
   sudo nginx -t && sudo systemctl reload nginx
   ```
   👉 Explication : retire le site ajouté, ou restaurer l'archive Nginx, puis recharger seulement si le test passe.

## 2. Production — Contrôles

Définir rétention, chiffrement, accès aux sauvegardes, responsables, fréquence des exercices et exigences RPO/RTO.

## 3. Production — Sécurité

- Ne pas stocker l'unique sauvegarde sur le même disque que le serveur.
- Protéger les exports et configurations contenant des secrets; ne pas les déposer dans le wiki.
- Ne pas supprimer une base ou un volume pour tenter de réparer un service.
- Ne pas considérer une archive créée comme restaurable avant un test réel de récupération.

## Validation et retour arrière

- **Validation** : restauration testée, cohérence base/configuration vérifiée et procédure documentée.
- **Retour arrière** : restaurer la configuration précédente, vérifier `nginx -t`, puis recharger; restaurer la base uniquement avec approbation et procédure testée.

## Si le problème n'est pas résolu

- [MariaDB — sauvegarde et restauration](https://mariadb.com/kb/en/backup-and-restore-overview/)
- [Nginx — documentation](https://nginx.org/en/docs/)
- [Guide complet LEMP Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/02_Pile_LEMP_Debian_13_Nginx_PHP_MariaDB.md#6-sauvegarde-et-retour-arriere)
