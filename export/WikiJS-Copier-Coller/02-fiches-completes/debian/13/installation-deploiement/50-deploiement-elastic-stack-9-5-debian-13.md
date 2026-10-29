# Déployer une base Elastic Stack 9.5 sur Debian 13

- **OS / Version** : Debian 13 Trixie; Elasticsearch et Kibana 9.5.x, versions identiques
- **Type de fiche** : Installation/Déploiement
- **Architecture** : nœud unique de validation; architecture de démonstration, pas HA
- **Catégorie** : Centralisation des journaux et recherche

## 1. Cadrage

Fiche simple : [cadrer le déploiement](/01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-cadrer).

Cette fiche installe Elasticsearch et Kibana depuis le dépôt APT officiel. Les deux composants doivent rester à la même version. Vérifier la matrice de systèmes supportés et les prérequis noyau/mémoire avant déploiement. Pour la production, concevoir séparément les rôles master/data/ingest, la haute disponibilité, les snapshots et la capacité de stockage en fonction du débit et de la rétention.

Garder les services internes derrière le réseau de gestion. Ne pas exposer Elasticsearch `9200` ou transport `9300` sur Internet; placer Kibana derrière un proxy TLS ou limiter son accès aux administrateurs.

## 2. Ajouter le dépôt Elastic signé

Fiche simple : [ajouter le dépôt Elastic signé](/01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-depot-apt).

Vérifier l'empreinte de la clé Elastic avec une source officielle indépendante, puis enregistrer la clé dans un keyring dédié et la référence APT `signed-by`. Vérifier qu'un seul dépôt `9.x` est configuré.

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates wget gpg
wget -qO- https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor --yes -o /usr/share/keyrings/elasticsearch-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/9.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-9.x.list
sudo apt-get update
```

Pour un déploiement reproductible, épingler une version 9.5.x validée pour les deux paquets et empêcher une mise à niveau partielle. Ne pas mélanger différentes versions Elastic Stack.

## 3. Installer et démarrer Elasticsearch

Fiche simple : [installer et démarrer Elasticsearch](/01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-installer-elasticsearch).

```bash
sudo apt-get install -y elasticsearch
sudo systemctl daemon-reload
sudo systemctl enable --now elasticsearch.service
sudo systemctl --no-pager status elasticsearch
```

Au premier démarrage, Elasticsearch configure automatiquement la sécurité, les certificats TLS et un enrollment token Kibana. Conserver les certificats et secrets hors des journaux accessibles et du wiki. Régler `cluster.name` et `node.name`; pour un nœud unique, conserver les interfaces locales tant qu'un besoin réseau précis n'a pas été approuvé.

Définir le mot de passe du superutilisateur avec l'outil `elasticsearch-reset-password` et l'enregistrer dans le coffre. Vérifier l'API en HTTPS en faisant confiance au certificat CA local; ne pas désactiver la vérification TLS avec `-k`.

## 4. Installer et enrôler Kibana

Fiche simple : [installer et enrôler Kibana](/01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-installer-kibana).

```bash
sudo apt-get install -y kibana
sudo systemctl daemon-reload
sudo systemctl enable kibana.service
sudo systemctl start kibana.service
sudo systemctl --no-pager status kibana
```

Générer un enrollment token Kibana sur Elasticsearch avec l'outil officiel, puis saisir ce token dans le wizard Kibana avec le code de vérification affiché par le service. Le token expire; en générer un nouveau s'il n'est plus valide. Conserver `server.host` en localhost si l'accès est via proxy local; sinon lier une adresse interne dédiée et contrôler TLS/proxy et pare-feu avant ouverture.

## 5. Vérifier et définir l'ingestion

Fiche simple : [vérifier et définir l'ingestion](/01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-ingestion).

Vérifier la santé de l'API HTTPS et l'accès à Kibana depuis le poste d'administration. Créer un jeu de données de test et vérifier index, fuseau horaire, champs, politiques de cycle de vie et droits de recherche.

Cette installation ne configure pas encore de collecte depuis les serveurs. Ajouter Elastic Agent/Fleet ou un shipper conforme à l'architecture retenue, avec certificat CA et credentials à privilèges limités; valider d'abord un hôte pilote. Ne pas activer un listener réseau générique sans filtrage par source.

## 6. Exploitation et reprise

Fiche simple : [exploitation et reprise](/01-fiches-simples/debian/13/vie-du-logiciel/elastic-stack/fiche-simple-vm-debian-13-elastic-stack-exploitation).

- Utiliser snapshots vers un dépôt externe dédié et tester une restauration avant d'établir la rétention.
- Surveiller espace, shards, heap JVM, latence, sauvegardes, santé de cluster et renouvellement des certificats.
- Tester les upgrades en staging et mettre à niveau les composants selon les chemins supportés; sauvegarder avant toute montée de version.
- Consigner les rôles RBAC, utilisateurs de service, API keys et leurs dates de rotation.
- Pour un cluster multi-nœuds, suivre les procédures de découverte/enrollment et ajouter `discovery.seed_hosts`; ne pas reprendre les réglages nœud unique tels quels.

## Sources

- [Elastic — Installer Elasticsearch avec un paquet Debian](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package)
- [Elastic — Installer Kibana avec un paquet Debian](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-kibana-with-debian-package)
- [Elastic — Configuration système importante](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/important-system-configuration)
- [Elastic — Guide de production](https://www.elastic.co/docs/deploy-manage/production-guidance)