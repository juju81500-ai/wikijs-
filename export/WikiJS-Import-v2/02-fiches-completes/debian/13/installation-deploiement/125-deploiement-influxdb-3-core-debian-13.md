---
title: "Déployer InfluxDB 3 Core sur Debian 13"
description: "Fiche simple de cette étape : [cadrer le pilote InfluxDB 3 Core](../../../../01-Fiches-Simples/Debian/13/Vie-du-logiciel/InfluxDB3-Core/FicheSimple-InfluxDB3CoreDebian13CadrerPilote.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["influxdb3", "influxdb3-core", "debian13", "timeseries", "systemd", "token", "backup"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer InfluxDB 3 Core sur Debian 13

- **OS / Version** : Debian 13 Trixie avec systemd; paquet DEB officiel `influxdb3-core`
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : instance mono-nœud de laboratoire/pilote, stockage local, écoute loopback, authentification par jeton
- **Catégorie** : base de données de séries temporelles
- **Tags** : `influxdb3`, `influxdb3-core`, `debian13`, `timeseries`, `systemd`, `token`, `backup`

## 1. Périmètre et limites

Fiche simple de cette étape : [cadrer le pilote InfluxDB 3 Core](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-cadrer-pilote).

Cette procédure installe InfluxDB 3 Core depuis le dépôt officiel InfluxData sur un serveur Debian 13. Elle prépare un pilote local avec stockage fichier. Elle ne configure pas Telegraf, Grafana, stockage objet, haute disponibilité, réplication, SSO, chiffrement TLS de bout en bout ni supervision de production.

InfluxDB 3 Core est une édition distincte d'InfluxDB Enterprise. Vérifier les limites de l'édition avant conception : Core est mono-nœud, limite le nombre de bases et ne fournit pas les fonctionnalités Enterprise de haute disponibilité. Le stockage local exige une stratégie de capacité, sauvegarde et restauration soigneusement testée.

Prérequis : VM Debian 13 approuvée, architecture prise en charge, accès administrateur, horloge synchronisée, espace disque dédié surveillé et procédure de changement. Ne pas exposer l'API sur un réseau avant d'avoir défini TLS, contrôle d'accès, sauvegarde, rétention et règles de pare-feu.

## 2. Ajouter le dépôt APT officiel

Fiche simple de cette étape : [installer InfluxDB 3 Core depuis le dépôt officiel](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-installer-depot).

Vérifier la clé du dépôt avec son empreinte officielle avant de la faire confiance :

```bash
cd /tmp
curl --silent --location --fail --show-error \
  -O https://repos.influxdata.com/influxdata-archive.key
gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key
```

Vérifier que l'empreinte affichée correspond à celle publiée par InfluxData (`24C975CBA61A024EE1B631787C3D57159FC2F927`). Si elle diffère, arrêter et ne pas installer la clé. Ajouter ensuite le dépôt et installer le paquet :

```bash
gpg --dearmor < ./influxdata-archive.key \
  | sudo tee /usr/share/keyrings/influxdata-archive.gpg >/dev/null
echo 'deb [signed-by=/usr/share/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' \
  | sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt update
apt-cache policy influxdb3-core
sudo apt install influxdb3-core
influxdb3 --version
```

Valider que le candidat vient bien du dépôt InfluxData attendu. En environnement maîtrisé, figer le paquet via la politique de versions de l'organisation plutôt que suivre silencieusement les versions amont. L'installation DEB fournit un service systemd avec sandboxing; conserver ses réglages de sécurité.

## 3. Restreindre l'écoute avant le premier jeton

Fiche simple de cette étape : [restreindre l'écoute à loopback](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-limiter-ecoute).

Le service peut écouter sur toutes les interfaces par défaut. Avant tout démarrage ou exposition réseau, inspecter `/etc/influxdb3/influxdb3-core.conf` et définir les options sans effacer les autres valeurs générées par le paquet :

```toml
http-bind = "127.0.0.1:8181"
object-store = "file"
data-dir = "/var/lib/influxdb3/data"
node-id = "node0"
```

Le paquet Debian fournit la configuration TOML et son unité systemd. Vérifier que le service lit ce fichier et que le chemin de données appartient au compte système `influxdb3`; ne pas remplacer l'unité fournie pour ce pilote.

```bash
sudo systemctl cat influxdb3-core
sudo systemctl restart influxdb3-core
sudo systemctl --no-pager --full status influxdb3-core
sudo ss -ltnp | grep ':8181'
```

Vérifier que l'écoute est exclusivement sur `127.0.0.1:8181` avant de continuer. Si le service écoute sur une adresse différente ou si le démarrage échoue, arrêter et consulter `journalctl -u influxdb3-core`; ne pas ouvrir le port au pare-feu pour contourner le problème.

## 4. Initialiser le jeton opérateur

Fiche simple de cette étape : [créer et protéger le jeton opérateur](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-creer-jeton-operateur).

Le tout premier jeton admin est privilégié et ne peut pas être récupéré s'il est perdu. Comme l'API de création initiale n'est pas encore protégée par un jeton, cette opération doit se faire seulement après avoir confirmé l'écoute loopback :

```bash
curl --fail --silent --show-error \
  --request POST http://127.0.0.1:8181/api/v3/configure/token/admin \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json'
```

La réponse contient un jeton secret. Le copier immédiatement dans le coffre approuvé, avec accès strictement limité. Ne pas l'inscrire dans le wiki, un ticket, l'historique shell, un script, un journal ou un dépôt. Si la sortie a été perdue, suivre la procédure officielle de régénération et contrôler les accès; ne pas relancer à l'aveugle la création initiale.

Vérifier ensuite qu'une requête protégée sans jeton est refusée et qu'une requête avec le jeton depuis localhost est autorisée. Toute erreur d'authentification doit être traitée explicitement; ne pas désactiver l'authentification pour le pilote.

## 5. Créer une base de test et vérifier l'écriture

Fiche simple de cette étape : [valider une écriture de test](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-valider-ecriture).

Lire le jeton depuis le coffre approuvé dans une session shell locale non partagée. La saisie masquée ci-dessous évite de l'ajouter à l'historique :

```bash
read -rsp 'Jeton opérateur InfluxDB: ' INFLUXDB3_AUTH_TOKEN
echo
export INFLUXDB3_AUTH_TOKEN
```

Ne pas passer la valeur littérale du jeton comme argument de commande. Créer la base :

```bash
influxdb3 create database tssr_pilote --retention-period 30d
```

Écrire un point synthétique sur loopback sans données personnelles :

```bash
curl --fail --silent --show-error \
  'http://127.0.0.1:8181/api/v3/write_lp?db=tssr_pilote' \
  --header "Authorization: Bearer ${INFLUXDB3_AUTH_TOKEN}" \
  --data-binary 'validation,source=pilote valeur=1i'
```

Confirmer depuis la CLI ou l'API SQL que le point est lisible, puis exécuter `unset INFLUXDB3_AUTH_TOKEN` lorsque la session de test est terminée. Ne jamais activer le mode trace dans un terminal partagé; les arguments, environnements et sorties peuvent révéler des secrets.

## 6. Exploitation et exposition réseau

Fiche simple de cette étape : [contrôler l'exploitation](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-exploitation).

- Laisser le service sous le compte système non privilégié et conserver les options de sandbox systemd livrées par le paquet.
- Pour un pilote, garder loopback. Pour un accès distant, placer l'API derrière un proxy TLS approuvé, appliquer des règles réseau source/destination minimales et protéger les jetons; ne pas exposer directement TCP/8181.
- Créer des jetons séparés et limités aux usages nécessaires; conserver l'opérateur dans le coffre et ne pas le distribuer aux clients de collecte.
- Définir une rétention explicite. Sans rétention, les données ne sont pas supprimées automatiquement. Contrôler les limites Core et la cardinalité des tables avant ingestion.
- Surveiller espace libre, croissance des données, état du service, journaux systemd, échecs d'écriture et expiration/révocation des jetons.
- Avant mise à jour, lire les notes de version et tester migration, compatibilité client, restauration et retour arrière sur un clone.

## 7. Sauvegarde et restauration

Fiche simple de cette étape : [sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-sauvegarder-restaurer).

InfluxDB 3 Core n'inclut pas de commandes intégrées de sauvegarde/restauration. Avec le stockage local, la documentation recommande de copier les données par nœud dans l'ordre suivant : `snapshots`, `dbs`, `wal`, `catalog`, puis `_catalog_checkpoint`. Réaliser cette copie durant une fenêtre de faible activité ou après arrêt propre du service pour le pilote; transférer la sauvegarde chiffrée hors machine et protéger séparément les jetons/configurations.

Une restauration écrase les données présentes. La tester dans une instance isolée et compatible, en suivant l'ordre officiel de restauration (checkpoint, catalogue, WAL, bases, snapshots), avec arrêt du service et droits système corrects. Ne pas lancer de suppression récursive ni restaurer sur l'instance active sans procédure approuvée, copie de l'état courant et vérification de la cible. Mesurer le point de reprise obtenu; une sauvegarde ne garantit pas la récupération des écritures postérieures à l'état sauvegardé.

## 8. Retour arrière

Fiche simple de cette étape : [préparer le retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/influxdb3-core/fiche-simple-influxdb3-core-debian-13-retour-arriere).

Avant une mise à niveau, conserver le paquet précédent approuvé, la configuration, les journaux nécessaires et une sauvegarde cohérente des données. Si une version ou configuration est défectueuse, arrêter le service, restaurer conjointement configuration et données compatibles sur un clone, vérifier les jetons, une lecture/écriture pilote et les journaux, puis planifier la bascule. Ne pas supposer qu'un simple downgrade du paquet est compatible avec un format de données migré.

## Sources

- [InfluxData — installation InfluxDB 3 Core](https://docs.influxdata.com/influxdb3/core/install/)
- [InfluxData — options de configuration](https://docs.influxdata.com/influxdb3/core/reference/config-options/)
- [InfluxData — sécurité et sandboxing systemd](https://docs.influxdata.com/influxdb3/core/admin/security/)
- [InfluxData — gestion des jetons admin](https://docs.influxdata.com/influxdb3/core/admin/tokens/admin/)
- [InfluxData — écriture de données](https://docs.influxdata.com/influxdb3/core/write-data/)
- [InfluxData — sauvegarde et restauration](https://docs.influxdata.com/influxdb3/core/admin/backup-restore/)

Cette fiche est un pilote local mono-nœud. Les procédures de sauvegarde, restauration, exposition distante et mise à niveau doivent être testées avant tout service de production.