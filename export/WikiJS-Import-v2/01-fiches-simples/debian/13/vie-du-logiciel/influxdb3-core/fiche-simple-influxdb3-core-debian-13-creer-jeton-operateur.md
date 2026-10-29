---
title: "Fiche simple — Créer et protéger le jeton opérateur InfluxDB"
description: "Créer le premier jeton opérateur seulement lorsque l'API est prouvée locale et protéger immédiatement ce secret."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "influxdb3-core", "token", "secret", "loopback"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche simple — Créer et protéger le jeton opérateur InfluxDB

- **Environnement** : instance InfluxDB 3 Core locale, accès shell administrateur approuvé
- **OS / Version** : Debian 13; InfluxDB 3 Core
- **Catégorie** : base de données / gestion des secrets
- **Tags** : `debian13`, `influxdb3-core`, `token`, `secret`, `loopback`

---

## Problème précis à résoudre

Créer le premier jeton opérateur seulement lorsque l'API est prouvée locale et protéger immédiatement ce secret.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer l'écoute loopback avant de créer le jeton :
   ```bash
   sudo ss -ltnp | grep ':8181'
   ```
   👉 Explication : la création initiale n'est pas protégée par un jeton; elle doit rester locale.

2. Créer le jeton administrateur (une seule fois) :
   ```bash
   curl --fail --silent --show-error --request POST http://127.0.0.1:8181/api/v3/configure/token/admin --header 'Accept: application/json' --header 'Content-Type: application/json'
   ```
   👉 Explication : la réponse contient le jeton secret, non récupérable ensuite; le copier immédiatement dans le coffre approuvé, pas dans le wiki, un ticket ou l'historique shell.

3. Charger le jeton en saisie masquée :
   ```bash
   read -rsp 'Jeton opérateur InfluxDB: ' INFLUXDB3_AUTH_TOKEN
   echo
   export INFLUXDB3_AUTH_TOKEN
   ```
   👉 Explication : `-s` masque la saisie et évite d'inscrire le jeton dans l'historique.

4. Vérifier qu'une requête sans jeton est refusée et qu'avec le jeton elle est acceptée :
   ```bash
   curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8181/api/v3/configure/database?format=json
   curl -s -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer $INFLUXDB3_AUTH_TOKEN" 'http://127.0.0.1:8181/api/v3/configure/database?format=json'
   unset INFLUXDB3_AUTH_TOKEN
   ```
   👉 Explication : le premier appel doit renvoyer `401`, le second `200`; ne jamais désactiver l'authentification.

## 2. Production — Contrôles

Avant mise en production, consigner le propriétaire, les sources et consommateurs, la rétention, la capacité, le RPO/RTO, les sauvegardes testées, les clients autorisés et la politique de jetons. Vérifier que les limites de l’édition Core répondent au besoin.

## 3. Production — Sécurité

- Garder l’API liée à loopback tant qu’un proxy TLS et un filtrage réseau approuvés ne sont pas en place.
- Ne jamais partager le jeton opérateur; stocker les secrets dans le coffre et les révoquer en cas d’exposition.
- Utiliser uniquement des données synthétiques dans le pilote et protéger les copies de données/journaux.
- Ne pas restaurer sur l’instance active sans copie préalable, validation de la cible et changement approuvé.

## Validation et retour arrière

- **Validation** : jeton présent dans le coffre, propriétaire et droits consignés; requêtes protégées contrôlées.
- **Incident** : si le jeton a été exposé, le révoquer/régénérer selon la documentation et analyser l'accès; ne pas poursuivre avec le secret compromis.

## Si le problème n'est pas résolu

- [InfluxData — jetons administrateur](https://docs.influxdata.com/influxdb3/core/admin/tokens/admin/)
- [InfluxData — authentification](https://docs.influxdata.com/influxdb3/core/admin/tokens/)
- [Guide complet InfluxDB 3 Core Debian 13](/02-fiches-completes/debian/13/installation-deploiement/125-deploiement-influxdb-3-core-debian-13#4-initialiser-le-jeton-operateur)