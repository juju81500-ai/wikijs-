# Fiche simple — Sauvegarder et restaurer InfluxDB 3 Core

- **Environnement** : instance pilote InfluxDB 3 Core avec stockage fichier local
- **OS / Version** : Debian 13; InfluxDB 3 Core
- **Catégorie** : base de données / sauvegarde et restauration
- **Tags** : `debian13`, `influxdb3-core`, `backup`, `restore`, `stockage-local`

---

## Problème précis à résoudre

Préparer une sauvegarde cohérente des données et démontrer la restauration dans un environnement isolé.

## 1. Hors-Production (Lab / Test / POC)

1. Arrêter proprement le service (pilote) :
   ```bash
   sudo systemctl stop influxdb3-core
   ```
   👉 Explication : garantit une copie cohérente des fichiers.

2. Copier les répertoires dans l'ordre officiel :
   ```bash
   sudo install -d -m 0700 /var/backups/influxdb3
   cd /var/lib/influxdb3/data
   sudo tar -czf /var/backups/influxdb3/influx-$(date +%F).tar.gz snapshots dbs wal catalog _catalog_checkpoint
   sudo systemctl start influxdb3-core
   ```
   👉 Explication : l'ordre `snapshots`, `dbs`, `wal`, `catalog`, `_catalog_checkpoint` suit la documentation; `/var/backups` reste accessible à `root` seulement.

3. Vérifier l'archive et conserver son empreinte :
   ```bash
   sudo tar -tzf /var/backups/influxdb3/influx-$(date +%F).tar.gz | head
   sudo sha256sum /var/backups/influxdb3/influx-$(date +%F).tar.gz
   ```
   👉 Explication : chiffrer l'archive et la transférer hors machine; sauvegarder séparément jetons et configuration.

4. Restaurer uniquement sur une instance isolée (jamais sur l'instance active sans approbation) :
   ```bash
   sudo systemctl stop influxdb3-core
   sudo tar -xzf /var/backups/influxdb3/influx-AAAA-MM-JJ.tar.gz -C /var/lib/influxdb3/data
   sudo chown -R influxdb3:influxdb3 /var/lib/influxdb3/data
   sudo systemctl start influxdb3-core
   ```
   👉 Explication : remplacer la date; la restauration écrase les données présentes. Vérifier ensuite une lecture de `tssr_pilote` et mesurer le point de reprise obtenu.

## 2. Production — Contrôles

Avant mise en production, consigner le propriétaire, les sources et consommateurs, la rétention, la capacité, le RPO/RTO, les sauvegardes testées, les clients autorisés et la politique de jetons. Vérifier que les limites de l’édition Core répondent au besoin.

## 3. Production — Sécurité

- Garder l’API liée à loopback tant qu’un proxy TLS et un filtrage réseau approuvés ne sont pas en place.
- Ne jamais partager le jeton opérateur; stocker les secrets dans le coffre et les révoquer en cas d’exposition.
- Utiliser uniquement des données synthétiques dans le pilote et protéger les copies de données/journaux.
- Ne pas restaurer sur l’instance active sans copie préalable, validation de la cible et changement approuvé.

## Validation et retour arrière

- **Validation** : restauration isolée réussie, données lisibles, propriétaire et permissions corrects, RPO mesuré.
- **Sécurité** : une restauration écrase les données. Ne jamais cibler l'instance active sans approbation, copie d'état préalable et procédure dédiée.

## Si le problème n'est pas résolu

- [InfluxData — sauvegarde et restauration](https://docs.influxdata.com/influxdb3/core/admin/backup-restore/)
- [Guide complet InfluxDB 3 Core Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/125_Deploiement_InfluxDB_3_Core_Debian_13.md#7-sauvegarde-et-restauration)
