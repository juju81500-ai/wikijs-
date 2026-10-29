---
title: "Déployer Graylog 7.2 sur Ubuntu Server 24.04"
description: "Fiche simple : [cadrer et vérifier les prérequis](../../../../01-Fiches-Simples/Ubuntu/24.04/Vie-du-logiciel/Graylog/FicheSimple-VMUbuntu24.04GraylogCadrerPrerequis.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["graylog", "ubuntu2404", "logs", "siem", "datanode", "mongodb"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Graylog 7.2 sur Ubuntu Server 24.04

- **OS / Version** : Ubuntu Server 24.04 LTS; Graylog 7.2
- **Type de fiche** : Installation/Déploiement
- **Architecture** : un nœud Graylog + MongoDB et un Data Node pour un laboratoire représentatif
- **Catégorie** : Centralisation et analyse des journaux
- **Tags** : `graylog`, `ubuntu2404`, `logs`, `siem`, `datanode`, `mongodb`

## 1. Cadrage et prérequis

Fiche simple : [cadrer et vérifier les prérequis](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-cadrer-prerequis).

Cette fiche suit l'architecture Graylog Core décrite par l'éditeur : Graylog Server et MongoDB sur un hôte, Data Node sur un hôte séparé. Pour la production, dimensionner les nœuds selon le débit EPS, la taille moyenne des événements, la rétention, les index et la charge de recherche. Utiliser une zone de stockage dédiée, idéalement XFS pour les données du Data Node.

Vérifier la matrice de compatibilité Graylog 7.2 pour les versions d'Ubuntu et MongoDB avant la fenêtre de changement. Préparer DNS, NTP, certificats TLS, sauvegarde et capacité disque. Une installation mono-nœud n'est pas une architecture HA.

## 2. Réseau et secrets

Fiche simple : [réseau et secrets](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-reseau-secrets).

Créer des règles limitées aux adresses des composants et des postes d'administration. N'exposer ni MongoDB `27017`, ni les interfaces de recherche/OpenSearch du Data Node au réseau utilisateur ou à Internet. N'autoriser que les ports Graylog réellement activés et les sources de journaux explicitement prévues; les ports et protocoles dépendent des inputs retenus.

Préparer un secret aléatoire `password_secret` identique sur Graylog Server et Data Node, et un secret administrateur fort. Les conserver dans le coffre d'équipe. Ne pas utiliser les valeurs de démonstration ni recopier de secrets dans la fiche.

## 3. Installer MongoDB sur le nœud Graylog

Fiche simple : [installer MongoDB sur le nœud Graylog](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-mongodb).

L'éditeur donne MongoDB 8.0 pour cette procédure Ubuntu. Configurer le dépôt MongoDB correspondant à Ubuntu 24.04 (`noble`), installer les paquets `mongodb-org`, puis maintenir la version après vérification de la matrice Graylog.

Garder MongoDB lié à l'interface locale lorsqu'il réside sur le même hôte. Activer l'authentification, créer un compte de service limité à la base Graylog et utiliser une URI authentifiée dans les configurations Data Node et Server. La procédure MongoDB de l'éditeur Graylog décrit le mécanisme d'authentification.

```bash
sudo systemctl enable --now mongod
sudo systemctl --no-pager status mongod
```

## 4. Installer Data Node

Fiche simple : [installer Data Node](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-data-node).

Sur son hôte dédié, récupérer le paquet de dépôt Graylog 7.2 depuis `packages.graylog2.org`, contrôler l'origine et installer le paquet de dépôt puis `graylog-datanode`. Ne pas déployer OpenSearch séparément avec cette architecture Data Node.

Définir `vm.max_map_count` à au moins `262144` dans un fichier sous `/etc/sysctl.d/` puis appliquer `sysctl --system`. Renseigner dans `/etc/graylog/datanode/datanode.conf` le secret partagé, l'URI MongoDB authentifiée et la taille de heap adaptée à la mémoire. L'éditeur recommande environ la moitié de la RAM, avec un plafond de 31 Go.

```bash
sudo systemctl enable --now graylog-datanode
sudo systemctl --no-pager status graylog-datanode
```

## 5. Installer Graylog Server

Fiche simple : [installer Graylog Server](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-installer-server).

Sur le nœud Graylog/MongoDB, installer le dépôt Graylog 7.2 puis le paquet `graylog-server`. Configurer `/etc/graylog/server/server.conf` : `password_secret` partagé avec Data Node, hash SHA-256 du secret admin dans `root_password_sha2`, URI MongoDB authentifiée, adresse d'écoute limitée à l'interface interne prévue et rétention du journal d'entrée dimensionnée.

Pour calculer `root_password_sha2`, suivre la méthode de la documentation Graylog sans placer le secret en clair dans l'historique shell. Régler la JVM selon la mémoire disponible; la recommandation Graylog est environ la moitié de la RAM, jusqu'à 16 Go.

```bash
sudo systemctl enable --now graylog-server
sudo systemctl --no-pager status graylog-server
sudo journalctl -u graylog-server -b --no-pager
```

## 6. Terminer le preflight et activer les entrées

Fiche simple : [terminer le preflight et activer les entrées](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-preflight-entrees).

Accéder à l'interface depuis le réseau d'administration et terminer le preflight avec le mot de passe temporaire fourni dans le journal initial, conformément à la procédure officielle. Après la première connexion, vérifier l'accès avec le mot de passe défini et supprimer de manière sécurisée toute note temporaire.

Créer un input correspondant à un flux de test autorisé, puis configurer un seul hôte source. Utiliser Syslog TLS ou un mécanisme chiffré approprié pour les données sensibles; documenter le port, le format, la source et la règle de pare-feu. Ne pas créer un listener ouvert à toutes les interfaces sans filtrage réseau.

## 7. Vérifications, exploitation et sauvegardes

Fiche simple : [vérifications, exploitation et sauvegardes](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/graylog/fiche-simple-vm-ubuntu-24-04-graylog-verifier-exploiter-sauvegarder).

- Confirmer que Graylog, MongoDB et Data Node sont actifs et que l'état du cluster est sain dans l'interface.
- Rechercher un événement de test avec horodatage, hôte et champs attendus; vérifier aussi le débit et l'espace restant.
- Contrôler les journaux avec `journalctl -u graylog-server`, `journalctl -u graylog-datanode` et `journalctl -u mongod`.
- Configurer TLS pour l'interface, les inputs et les communications inter-composants; isoler les interfaces d'administration.
- Configurer chiffrement au repos au niveau stockage : Graylog ne chiffre pas nativement les journaux au repos.
- Sauvegarder MongoDB, configurations, certificats et secrets, ainsi que les données et métadonnées Data Node selon la procédure Graylog; tester une restauration isolée.
- Définir rotation, rétention, seuils disque et revue des comptes; appliquer les correctifs selon la compatibilité publiée.

## Sources

- [Graylog 7.2 — Installation Ubuntu, nœud unique](https://go2docs.graylog.org/current/downloading_and_installing_graylog/ubuntu_installation.htm)
- [Graylog — Sécuriser l'environnement](https://go2docs.graylog.org/current/planning_your_deployment/secure_your_graylog_environment.htm)
- [Graylog — Matrice de compatibilité](https://go2docs.graylog.org/current/downloading_and_installing_graylog/compatibility_matrix.htm)
- [MongoDB — Installer sur Ubuntu](https://www.mongodb.com/docs/v8.0/tutorial/install-mongodb-on-ubuntu/)
- [Graylog — Authentification MongoDB](https://go2docs.graylog.org/current/setting_up_graylog/configure_graylog_to_use_mongodb_password_authentication.htm)