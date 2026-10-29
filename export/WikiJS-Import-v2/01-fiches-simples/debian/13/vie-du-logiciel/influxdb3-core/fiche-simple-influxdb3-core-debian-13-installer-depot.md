---
title: "Fiche simple — Installer InfluxDB 3 Core depuis le dépôt officiel"
description: "Installer le paquet InfluxDB 3 Core uniquement après validation de la clé et de la provenance APT."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "influxdb3-core", "apt", "signature", "installation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche simple — Installer InfluxDB 3 Core depuis le dépôt officiel

- **Environnement** : Debian 13 Trixie amd64, dépôts APT approuvés
- **OS / Version** : Debian 13; paquet `influxdb3-core`
- **Catégorie** : base de données de séries temporelles / installation
- **Tags** : `debian13`, `influxdb3-core`, `apt`, `signature`, `installation`

---

## Problème précis à résoudre

Installer le paquet InfluxDB 3 Core uniquement après validation de la clé et de la provenance APT.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger la clé du dépôt et afficher son empreinte :
   ```bash
   cd /tmp
   curl --silent --location --fail --show-error -O https://repos.influxdata.com/influxdata-archive.key
   gpg --show-keys --with-fingerprint --with-colons ./influxdata-archive.key
   ```
   👉 Explication : l'empreinte doit correspondre à `24C975CBA61A024EE1B631787C3D57159FC2F927`; sinon, arrêter et ne pas installer la clé.

2. Installer la clé et déclarer le dépôt :
   ```bash
   gpg --dearmor < ./influxdata-archive.key | sudo tee /usr/share/keyrings/influxdata-archive.gpg >/dev/null
   echo 'deb [signed-by=/usr/share/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list
   ```
   👉 Explication : `signed-by` limite la confiance de la clé à ce seul dépôt.

3. Vérifier la source du paquet puis installer :
   ```bash
   sudo apt update
   apt-cache policy influxdb3-core
   sudo apt install influxdb3-core
   influxdb3 --version
   ```
   👉 Explication : le candidat doit provenir de `repos.influxdata.com`; `--version` confirme l'installation.

4. Figer la version selon la politique de l'organisation :
   ```bash
   sudo apt-mark hold influxdb3-core
   ```
   👉 Explication : empêche une mise à jour automatique silencieuse; lever avec `apt-mark unhold` lors d'un changement approuvé.

## 2. Production — Contrôles

Avant mise en production, consigner le propriétaire, les sources et consommateurs, la rétention, la capacité, le RPO/RTO, les sauvegardes testées, les clients autorisés et la politique de jetons. Vérifier que les limites de l’édition Core répondent au besoin.

## 3. Production — Sécurité

- Garder l’API liée à loopback tant qu’un proxy TLS et un filtrage réseau approuvés ne sont pas en place.
- Ne jamais partager le jeton opérateur; stocker les secrets dans le coffre et les révoquer en cas d’exposition.
- Utiliser uniquement des données synthétiques dans le pilote et protéger les copies de données/journaux.
- Ne pas restaurer sur l’instance active sans copie préalable, validation de la cible et changement approuvé.

## Validation et retour arrière

- **Validation** : empreinte conforme, paquet provenant du dépôt attendu, version notée et service vérifié.
- **Retour arrière** : arrêter si origine ou signature inattendue; ne pas lancer le service ni contourner la validation de signature.

## Si le problème n'est pas résolu

- [InfluxData — installation](https://docs.influxdata.com/influxdb3/core/install/)
- [InfluxData — sécurité du paquet Linux](https://docs.influxdata.com/influxdb3/core/admin/security/)
- [Guide complet InfluxDB 3 Core Debian 13](/02-fiches-completes/debian/13/installation-deploiement/125-deploiement-influxdb-3-core-debian-13#2-ajouter-le-depot-apt-officiel)