# OpenStack : plateforme de laboratoire et contrôles

- **Environnement** : Cloud privé OpenStack sur Linux, déploiement de laboratoire puis périmètre production
- **Tags** : `openstack`, `cloud`, `keystone`, `nova`, `neutron`, `cinder`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

- Périmètre : conception, déploiement initial de laboratoire (méthode documentée par le projet), contrôles par client `openstack`, premier projet et instance. Hors périmètre : exploitation multi-région, CI/CD de cloud.
- Composants de base : Keystone (identité), Glance (images), Nova (calcul), Neutron (réseau), Cinder (volumes), Horizon (interface). Placement et services de messagerie/base de données à prévoir.
- Matériel/laboratoire : nœud contrôleur et calcul, plusieurs interfaces réseau (gestion, provider, stockage), virtualisation matérielle activée, [[Glossary:DNS]]/NTP, ressources suffisantes selon le guide d'installation.
- Haute disponibilité (contrôleurs multiples, Galera, RabbitMQ) : quorum impair obligatoire pour les clusters de base de données et de messagerie.

## 2. Exigences de version et licence

- **Version/release OpenStack à figer avant déploiement**, avec OS supporté et durée de maintenance de la release, d'après la matrice officielle de la documentation et le calendrier de versions.
- Logiciel sous licence Apache 2.0 ; support commercial via distributions tierces. Vérifier le support de la distribution Linux choisie.

## 3. Procédure

1. Choisir la méthode d'installation documentée pour la release retenue (guide d'installation manuel, ou outil de déploiement supporté).
2. Préparer l'OS : mise à jour, noms d'hôtes, résolution, [[Glossary:NTP]], paquets de base, interfaces réseau.
3. Déployer les services dans l'ordre documenté : base de données, messagerie, Keystone, Glance, Placement, Nova, Neutron, Cinder, Horizon.
4. Charger les identifiants (fichier RC, jamais versionné) puis contrôler :
```bash
openstack service list
openstack compute service list
openstack network agent list
openstack volume service list
```
5. Importer une image de test vérifiée, créer un réseau, un sous-réseau, un groupe de sécurité restrictif et une clé [[Glossary:SSH]] :
```bash
openstack image create --file image.qcow2 --disk-format qcow2 --container-format bare --public=false test-img
openstack network create lab-net
openstack server create --image test-img --flavor <flavor> --network lab-net --key-name <cle> test-vm
```
6. Vérifier l'accès à l'instance et aux journaux de chaque service.

## 4. Vérifications

- Tous les services `up`/`enabled` ; instance `ACTIVE` ; connectivité réseau conforme.
- Volume Cinder créé et attaché à l'instance de test.
- Sauvegarde de la base de données et des fichiers de configuration réalisée.

## 5. Rollback et risques

- Sauvegarder bases et configuration avant chaque montée de version ; migrer release par release, jamais en sautant des versions non documentées.
- Supprimer un projet, un réseau ou un volume est destructif ; contrôler les dépendances.
- Perte de quorum Galera/RabbitMQ : suivre la procédure de récupération officielle, ne pas redémarrer tous les nœuds simultanément.
- Exposer les [[Glossary:API]] et Horizon uniquement derrière [[Glossary:TLS]] et filtrage réseau.

## 6. Documentation officielle

- <https://docs.openstack.org/>
- <https://docs.openstack.org/install-guide/>
