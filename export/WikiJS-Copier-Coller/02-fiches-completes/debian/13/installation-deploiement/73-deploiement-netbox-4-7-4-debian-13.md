# Déployer NetBox 4.7.4 sur Debian 13

- **OS / Version** : Debian 13 Trixie x86-64; NetBox 4.7.4
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : application NetBox, PostgreSQL, Redis local, Gunicorn, Nginx et pilote IPAM/DCIM
- **Catégorie** : IPAM, DCIM et source de vérité réseau

## 1. Cadrer l'installation

Fiche simple : [cadrer le pilote NetBox](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-cadrer).

NetBox est une source de vérité IPAM/DCIM, pas un outil qui découvre automatiquement le réseau. Les données doivent avoir un propriétaire et un processus de revue avant de devenir la référence pour d'autres systèmes.

Au 27 octobre 2026, la release stable publiée est NetBox 4.7.4. Les exigences de la documentation stable sont Python 3.12+, PostgreSQL 15+ et Redis 6+; Debian 13 fournit Python 3.13 et PostgreSQL 17. Cette procédure choisit une archive de version fixe, une base PostgreSQL locale, Redis lié localement et Nginx devant Gunicorn. Elle vise une petite instance dédiée, pas une architecture haute disponibilité.

Définir avant l'installation le FQDN, l'adresse de gestion, le réseau d'administration, les propriétaires du service, les règles de conservation et l'emplacement des sauvegardes. N'exposer l'interface et l'API qu'en HTTPS sur le réseau autorisé.

## 2. Installer PostgreSQL et Redis

Fiche simple : [installer PostgreSQL et Redis](/01-fiches-simples/debian/13/vie-du-logiciel/postgresql/fiche-simple-vm-debian-13-netbox-installer-postgresql-redis).

Installer les prérequis système et services depuis Debian 13 :

```bash
sudo apt update
sudo apt install -y postgresql redis-server nginx python3 python3-pip python3-venv python3-dev build-essential libxml2-dev libxslt1-dev libffi-dev libpq-dev libssl-dev zlib1g-dev curl ca-certificates
python3 --version
psql --version
redis-server --version
```

Vérifier que Python est au moins en version 3.12, PostgreSQL au moins 15 et Redis au moins 6. Démarrer les services et confirmer leur disponibilité :

```bash
sudo systemctl enable --now postgresql redis-server nginx
sudo -u postgres psql -c 'SELECT version();'
redis-cli ping
```

Créer le rôle et la base dédiés. Remplacer le secret d'exemple par une valeur aléatoire unique, la saisir dans une console locale contrôlée et la conserver dans le coffre de secrets :

```bash
sudo -u postgres psql
```

Dans `psql` :

```sql
CREATE DATABASE netbox;
CREATE USER netbox WITH PASSWORD 'REMPLACER_PAR_UN_SECRET_ALEATOIRE';
ALTER DATABASE netbox OWNER TO netbox;
\connect netbox
GRANT CREATE ON SCHEMA public TO netbox;
\q
```

Conserver Redis lié à localhost; ne pas publier son port 6379 sur le réseau. NetBox emploie deux bases Redis différentes pour la file de tâches et le cache.

## 3. Télécharger et installer NetBox 4.7.4

Fiche simple : [installer l'archive NetBox versionnée](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-installer-release).

Télécharger la release fixe depuis les sources officielles, vérifier le tag et le contenu avant extraction. L'archive locale doit être consignée avec son SHA-256; cette empreinte calculée localement ne remplace pas une signature publiée.

```bash
cd /tmp
curl --fail --location --proto '=https' --tlsv1.2 -o netbox-v4.7.4.tar.gz https://github.com/netbox-community/netbox/archive/refs/tags/v4.7.4.tar.gz
sha256sum netbox-v4.7.4.tar.gz
tar -tzf netbox-v4.7.4.tar.gz | head
sudo tar -xzf netbox-v4.7.4.tar.gz -C /opt
sudo ln -s /opt/netbox-4.7.4 /opt/netbox
```

Si `/opt/netbox` ou `/opt/netbox-4.7.4` existe déjà, arrêter et suivre la procédure de mise à niveau; ne pas écraser l'instance en place. Créer le compte de service et donner au serveur web l'accès en écriture uniquement aux dossiers de données requis :

```bash
sudo adduser --system --group netbox
sudo chown -R netbox:netbox /opt/netbox/netbox/media /opt/netbox/netbox/reports /opt/netbox/netbox/scripts
```

Ne pas attribuer à `www-data` l'écriture sur l'ensemble du code NetBox.

## 4. Configurer les secrets et la base de données

Fiche simple : [configurer les secrets NetBox](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-config-secrets).

Créer `configuration.py` à partir de l'exemple fourni :

```bash
sudo cp /opt/netbox/netbox/netbox/configuration_example.py /opt/netbox/netbox/netbox/configuration.py
sudoedit /opt/netbox/netbox/netbox/configuration.py
```

Définir les cinq paramètres requis selon la version installée :

- `ALLOWED_HOSTS` : FQDN et adresse de service prévus, jamais `['*']` en production.
- `API_TOKEN_PEPPERS` : au moins un pepper aléatoire de 50 caractères minimum, protégé comme un secret.
- `DATABASES` : moteur PostgreSQL, base/rôle `netbox`, mot de passe réservé, hôte `localhost`.
- `REDIS` : deux entrées distinctes `tasks` et `caching`, localhost, bases Redis différentes.
- `SECRET_KEY` : valeur générée par `/opt/netbox/netbox/generate_secret_key.py`, unique à l'instance, au moins 50 caractères.

Protéger la configuration, qui contient des secrets :

```bash
sudo chown root:netbox /opt/netbox/netbox/netbox/configuration.py
sudo chmod 0640 /opt/netbox/netbox/netbox/configuration.py
```

Le rôle NetBox doit pouvoir lire la configuration via son groupe. Ne jamais copier les secrets d'exemple de la documentation dans une vraie instance.

## 5. Exécuter les migrations et créer le compte administrateur

Fiche simple : [exécuter les migrations et créer l'administrateur](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-migrations-admin).

Lancer le script de mise à niveau NetBox pour créer l'environnement Python virtuel, installer les dépendances, effectuer les migrations et collecter les ressources statiques :

```bash
sudo /opt/netbox/upgrade.sh
```

Ne pas poursuivre si le script retourne une erreur ou une migration incomplète. Créer ensuite un compte superutilisateur interactif, sans passer son mot de passe comme argument shell :

```bash
sudo -u netbox /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py createsuperuser
```

## 6. Activer les services systemd

Fiche simple : [activer les services NetBox](/01-fiches-simples/debian/13/vie-du-systeme/fiches-par-theme/systemd/fiche-simple-vm-debian-13-netbox-activer-systemd).

Copier les unités livrées par la release et les activer :

```bash
sudo cp -v /opt/netbox/contrib/*.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now netbox netbox-rq
sudo systemctl --no-pager --full status netbox netbox-rq
```

Les unités prévues par NetBox utilisent l'utilisateur et le groupe `netbox`. Si les noms ou le préfixe diffèrent, examiner les unités avant activation plutôt que de lancer le serveur de développement. En cas d'échec, consulter `journalctl -eu netbox` et `journalctl -eu netbox-rq`.

## 7. Configurer Nginx avec TLS

Fiche simple : [publier NetBox avec Nginx et TLS](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-nginx-tls).

Installer un certificat TLS valide et protéger sa clé privée. Copier la configuration Nginx de NetBox, puis remplacer le nom de serveur par le FQDN autorisé dans `ALLOWED_HOSTS` :

```bash
sudo cp /opt/netbox/contrib/nginx.conf /etc/nginx/sites-available/netbox
sudoedit /etc/nginx/sites-available/netbox
sudo ln -s /etc/nginx/sites-available/netbox /etc/nginx/sites-enabled/netbox
sudo nginx -t
sudo systemctl reload nginx
```

La configuration fournie est un minimum; ajouter TLS, le certificat, les en-têtes et les restrictions d'accès selon la politique locale. Supprimer le site Nginx par défaut seulement après validation du nouveau VirtualHost et s'assurer de conserver un accès d'administration de secours.

Limiter le pare-feu au HTTPS depuis le réseau d'administration. PostgreSQL et Redis doivent rester liés à localhost. Ne pas publier les ports 5432, 6379 ou Gunicorn sur le réseau.

## 8. Vérifier un flux IPAM pilote

Fiche simple : [valider les données IPAM du pilote](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-valider-ipam-pilote).

Se connecter au FQDN HTTPS depuis un poste du réseau d'administration. Créer d'abord un site ou tenant de laboratoire, un aggregate explicitement détenu, puis un prefix parent et ses sous-réseaux enfants en respectant le plan d'adressage approuvé. Ajouter ensuite quelques adresses de test et confirmer l'affichage de la hiérarchie et de l'utilisation du prefix.

Ne pas importer le plan complet avant d'avoir défini les conventions d'état, rôles, VRF, tenants, propriétaires et source d'autorité. Vérifier que les sous-réseaux ne se chevauchent pas hors VRF et que les champs obligatoires sont compris par les opérateurs.

Valider la tâche de fond par l'état du service `netbox-rq` et vérifier qu'une tâche (par exemple une importation de petit fichier de test) se termine sans erreur. Tester l'API avec un compte dédié à privilèges limités; protéger les jetons API et les révoquer après les essais.

## 9. Sauvegardes, restauration et mises à niveau

Fiche simple : [sauvegarder, restaurer et mettre à niveau](/01-fiches-simples/debian/13/vie-du-logiciel/netbox/fiche-simple-vm-debian-13-netbox-sauvegarder-mettre-a-jour).

Sauvegarder au minimum PostgreSQL, `/opt/netbox/netbox/netbox/configuration.py`, les fichiers média, la configuration Nginx et les éventuels scripts/plugins locaux. Stocker les sauvegardes chiffrées hors du serveur.

Exemple de dump PostgreSQL cohérent :

```bash
sudo -u postgres pg_dump --format=custom --file=/var/backups/netbox-$(date +%F).dump netbox
```

Protéger ce fichier, puis restaurer le dump sur une instance de test avant d'accepter la sauvegarde. NetBox 4.7 s'appuie sur PostgreSQL 15+ et l'extension ltree est requise; une restauration de base doit inclure son schéma et ses extensions. Répéter un test de connexion, une consultation d'objets et une exportation d'inventaire sur l'instance restaurée.

Pour une mise à niveau, sauvegarder d'abord la base, la configuration, les médias et les fichiers locaux. Installer la nouvelle version dans un répertoire versionné distinct, relier les données et la configuration selon la procédure NetBox, exécuter son `upgrade.sh`, puis basculer le lien et redémarrer les services après vérification. Ne pas supprimer l'ancienne version tant que la nouvelle n'est pas validée.

NetBox 4.7.2 corrige un problème des releases 4.7.0/4.7.1 qui pouvait exposer des jetons API créés via certaines tâches de masse dans les résultats de jobs. En cas de migration depuis ces versions, considérer ces jetons comme compromis et les renouveler.

## Sources

- [NetBox — releases](https://github.com/netbox-community/netbox/releases)
- [NetBox 4.7 — exigences de version](https://netbox.readthedocs.io/en/stable/installation/)
- [NetBox — installer depuis une archive de release](https://netbox.readthedocs.io/en/stable/installation/3-netbox/)
- [NetBox — PostgreSQL](https://netbox.readthedocs.io/en/stable/installation/1-postgresql/)
- [NetBox — Redis](https://netbox.readthedocs.io/en/stable/installation/2-redis/)
- [NetBox — Gunicorn et systemd](https://netbox.readthedocs.io/en/stable/installation/4a-gunicorn/)
- [NetBox — serveur HTTP Nginx](https://netbox.readthedocs.io/en/stable/installation/5-http-server/)
- [NetBox — paramètres requis](https://netbox.readthedocs.io/en/stable/configuration/required-parameters/)
- [NetBox — permissions d'objet](https://netbox.readthedocs.io/en/stable/administration/permissions/)
- [NetBox — IPAM](https://netbox.readthedocs.io/en/stable/features/ipam/)

La documentation d'installation détaillée est testée sur Ubuntu 24.04; les commandes de paquets de ce guide sont adaptées à Debian 13 et doivent être validées en préproduction. Aucun service NetBox ni test de restauration n'a été exécuté par cette fiche.