# Fiche simple — Préparer le retour arrière InfluxDB 3 Core

- **Environnement** : pilote InfluxDB 3 Core sur Debian 13, changement ou mise à niveau planifié
- **OS / Version** : Debian 13; InfluxDB 3 Core
- **Catégorie** : base de données / gestion du changement
- **Tags** : `debian13`, `influxdb3-core`, `rollback`, `upgrade`, `changement`

---

## Problème précis à résoudre

Éviter qu'une mise à jour ou configuration défectueuse ne rende les données et le service irrécupérables.

## 1. Hors-Production (Lab / Test / POC)

1. Noter la version actuelle et conserver le paquet :
   ```bash
   influxdb3 --version
   dpkg -l influxdb3-core | tail -1
   ls /var/cache/apt/archives/influxdb3-core*.deb
   ```
   👉 Explication : le paquet précédent doit rester disponible pour un retour arrière.

2. Sauvegarder configuration et données avant la mise à niveau :
   ```bash
   sudo cp -a /etc/influxdb3 /var/backups/influxdb3/etc-$(date +%F)
   sudo systemctl stop influxdb3-core
   sudo tar -czf /var/backups/influxdb3/avant-maj-$(date +%F).tar.gz -C /var/lib/influxdb3/data .
   sudo systemctl start influxdb3-core
   ```
   👉 Explication : sans sauvegarde cohérente, un format de données migré peut empêcher le retour arrière.

3. En cas de défaut, arrêter le service et collecter les journaux :
   ```bash
   sudo systemctl stop influxdb3-core
   sudo journalctl -u influxdb3-core --since "1 hour ago" --no-pager > /tmp/influxdb3-incident.log
   ```
   👉 Explication : les journaux servent à l'analyse; ne pas y laisser de jeton.

4. Restaurer configuration et données compatibles sur un clone, puis contrôler :
   ```bash
   sudo apt install --allow-downgrades influxdb3-core=VERSION_PRECEDENTE
   sudo systemctl start influxdb3-core
   sudo journalctl -u influxdb3-core -n 30 --no-pager
   ```
   👉 Explication : remplacer `VERSION_PRECEDENTE`; un simple downgrade n'est valable que si les données n'ont pas été migrées. Valider lecture/écriture et jetons avant bascule.

## 2. Production — Contrôles

Avant mise en production, consigner le propriétaire, les sources et consommateurs, la rétention, la capacité, le RPO/RTO, les sauvegardes testées, les clients autorisés et la politique de jetons. Vérifier que les limites de l’édition Core répondent au besoin.

## 3. Production — Sécurité

- Garder l’API liée à loopback tant qu’un proxy TLS et un filtrage réseau approuvés ne sont pas en place.
- Ne jamais partager le jeton opérateur; stocker les secrets dans le coffre et les révoquer en cas d’exposition.
- Utiliser uniquement des données synthétiques dans le pilote et protéger les copies de données/journaux.
- Ne pas restaurer sur l’instance active sans copie préalable, validation de la cible et changement approuvé.

## Validation et retour arrière

- **Validation** : essai de restauration documenté, critères de retour arrière et responsable d'astreinte approuvés.
- **Alerte** : un downgrade simple du paquet peut ne pas être compatible avec un format de données migré; ne pas le tenter sur le seul serveur de données.

## Si le problème n'est pas résolu

- [InfluxData — installation et mise à niveau](https://docs.influxdata.com/influxdb3/core/install/)
- [InfluxData — sauvegarde et restauration](https://docs.influxdata.com/influxdb3/core/admin/backup-restore/)
- [Guide complet InfluxDB 3 Core Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/125_Deploiement_InfluxDB_3_Core_Debian_13.md#8-retour-arriere)
