# Fiche simple — Valider une écriture InfluxDB 3 Core

- **Environnement** : pilote local InfluxDB 3 Core, données entièrement synthétiques
- **OS / Version** : Debian 13; InfluxDB 3 Core
- **Catégorie** : base de données / validation
- **Tags** : `debian13`, `influxdb3-core`, `ecriture`, `validation`, `token`

---

## Problème précis à résoudre

Créer une base de test à rétention définie, écrire un point synthétique et confirmer sa lecture sans exposer de jeton.

## 1. Hors-Production (Lab / Test / POC)

1. Charger le jeton en saisie masquée :
   ```bash
   read -rsp 'Jeton opérateur InfluxDB: ' INFLUXDB3_AUTH_TOKEN
   echo
   export INFLUXDB3_AUTH_TOKEN
   ```
   👉 Explication : ne pas passer le jeton en argument de commande ni utiliser un terminal partagé.

2. Créer la base de test avec rétention :
   ```bash
   influxdb3 create database tssr_pilote --retention-period 30d
   ```
   👉 Explication : la rétention explicite évite une croissance sans limite.

3. Écrire un point synthétique :
   ```bash
   curl --fail --silent --show-error 'http://127.0.0.1:8181/api/v3/write_lp?db=tssr_pilote' --header "Authorization: Bearer $INFLUXDB3_AUTH_TOKEN" --data-binary 'validation,source=pilote valeur=1i'
   ```
   👉 Explication : aucune donnée personnelle ne doit être écrite; l'absence d'erreur confirme l'écriture.

4. Relire le point :
   ```bash
   influxdb3 query --database tssr_pilote "SELECT * FROM validation"
   unset INFLUXDB3_AUTH_TOKEN
   ```
   👉 Explication : la ligne `source=pilote, valeur=1` doit apparaître; `unset` retire le jeton de la session.

## 2. Production — Contrôles

Avant mise en production, consigner le propriétaire, les sources et consommateurs, la rétention, la capacité, le RPO/RTO, les sauvegardes testées, les clients autorisés et la politique de jetons. Vérifier que les limites de l’édition Core répondent au besoin.

## 3. Production — Sécurité

- Garder l’API liée à loopback tant qu’un proxy TLS et un filtrage réseau approuvés ne sont pas en place.
- Ne jamais partager le jeton opérateur; stocker les secrets dans le coffre et les révoquer en cas d’exposition.
- Utiliser uniquement des données synthétiques dans le pilote et protéger les copies de données/journaux.
- Ne pas restaurer sur l’instance active sans copie préalable, validation de la cible et changement approuvé.

## Validation et retour arrière

- **Validation** : base et rétention conformes, point synthétique lisible, aucun secret exposé.
- **Retour arrière** : ne supprimer la base pilote qu'après vérification de son nom et approbation; ne pas utiliser de requête destructive sur une base partagée.

## Si le problème n'est pas résolu

- [InfluxData — écrire des données](https://docs.influxdata.com/influxdb3/core/write-data/)
- [InfluxData — gérer les bases](https://docs.influxdata.com/influxdb3/core/admin/databases/)
- [Guide complet InfluxDB 3 Core Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/125_Deploiement_InfluxDB_3_Core_Debian_13.md#5-creer-une-base-de-test-et-verifier-lecriture)
