# Fiche simple — Restreindre l'écoute InfluxDB avant initialisation

- **Environnement** : Debian 13, service `influxdb3-core`, réseau local de laboratoire
- **OS / Version** : Debian 13; InfluxDB 3 Core
- **Catégorie** : base de données de séries temporelles / durcissement réseau
- **Tags** : `debian13`, `influxdb3-core`, `loopback`, `systemd`, `durcissement`

---

## Problème précis à résoudre

Empêcher toute exposition réseau de l'API avant la création du premier jeton administrateur.

## 1. Hors-Production (Lab / Test / POC)

1. Inspecter la configuration livrée par le paquet :
   ```bash
   sudo cat /etc/influxdb3/influxdb3-core.conf
   sudo systemctl cat influxdb3-core
   ```
   👉 Explication : on identifie les options existantes pour ne pas écraser les valeurs générées.

2. Éditer `/etc/influxdb3/influxdb3-core.conf` (`sudo nano /etc/influxdb3/influxdb3-core.conf`) et définir :
   ```toml
   http-bind = "127.0.0.1:8181"
   object-store = "file"
   data-dir = "/var/lib/influxdb3/data"
   node-id = "node0"
   ```
   👉 Explication : l'API n'écoute que sur loopback; les données sont stockées localement.

3. Vérifier les droits du répertoire de données :
   ```bash
   sudo ls -ld /var/lib/influxdb3 /var/lib/influxdb3/data
   ```
   👉 Explication : le propriétaire doit être le compte système `influxdb3`.

4. Redémarrer et contrôler l'écoute :
   ```bash
   sudo systemctl restart influxdb3-core
   sudo systemctl --no-pager --full status influxdb3-core
   sudo ss -ltnp | grep ':8181'
   ```
   👉 Explication : l'écoute doit être exclusivement sur `127.0.0.1:8181`; en cas d'échec, consulter `sudo journalctl -u influxdb3-core -n 50 --no-pager` sans ouvrir le pare-feu.

## 2. Production — Contrôles

Avant mise en production, consigner le propriétaire, les sources et consommateurs, la rétention, la capacité, le RPO/RTO, les sauvegardes testées, les clients autorisés et la politique de jetons. Vérifier que les limites de l’édition Core répondent au besoin.

## 3. Production — Sécurité

- Garder l’API liée à loopback tant qu’un proxy TLS et un filtrage réseau approuvés ne sont pas en place.
- Ne jamais partager le jeton opérateur; stocker les secrets dans le coffre et les révoquer en cas d’exposition.
- Utiliser uniquement des données synthétiques dans le pilote et protéger les copies de données/journaux.
- Ne pas restaurer sur l’instance active sans copie préalable, validation de la cible et changement approuvé.

## Validation et retour arrière

- **Validation** : service sain et socket uniquement sur la boucle locale.
- **Retour arrière** : conserver la configuration précédente; ne jamais ouvrir le port au pare-feu pour masquer une erreur de configuration.

## Si le problème n'est pas résolu

- [InfluxData — options de configuration](https://docs.influxdata.com/influxdb3/core/reference/config-options/)
- [InfluxData — sécurité et sandboxing](https://docs.influxdata.com/influxdb3/core/admin/security/)
- [Guide complet InfluxDB 3 Core Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/125_Deploiement_InfluxDB_3_Core_Debian_13.md#3-restreindre-lecoute-avant-le-premier-jeton)
