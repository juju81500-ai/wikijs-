# 📄 Keycloak

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Keycloak 26.x (distribution zip officielle, numéro exact à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité

## 🎯 Objectif
Installer Keycloak sur Debian 12 comme fournisseur d'identité (SSO, OIDC, SAML), vérifier la console d'administration sur ce même serveur, puis le durcir (compte administrateur dédié, HTTPS, exposition restreinte). Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Java 17 et des outils d'extraction :
```bash
sudo apt update
sudo apt install -y openjdk-17-jre-headless unzip curl
java -version
```
👉 Explication : Keycloak 26 exige Java 17 ou plus récent. `java -version` doit afficher une version 17 au minimum.

2. Téléchargement et extraction de la distribution :
```bash
cd /opt
sudo curl -LO https://github.com/keycloak/keycloak/releases/download/26.0.7/keycloak-26.0.7.zip
sudo unzip keycloak-26.0.7.zip
sudo ln -s /opt/keycloak-26.0.7 /opt/keycloak
ls /opt/keycloak/bin
```
👉 Explication : Télécharge la version 26.0.7 (numéro à vérifier, une version plus récente peut être publiée), l'extrait dans `/opt` et crée le lien `/opt/keycloak`. La commande `ls` doit afficher `kc.sh`.

3. Démarrage en mode développement avec un administrateur de démonstration :
```bash
cd /opt/keycloak
sudo KC_BOOTSTRAP_ADMIN_USERNAME=admin_lab KC_BOOTSTRAP_ADMIN_PASSWORD='<MOT_DE_PASSE_ADMIN_A_REMPLACER>' ./bin/kc.sh start-dev --http-port=8080
```
👉 Explication : Lance Keycloak en mode `start-dev` (HTTP, base H2 intégrée, non prévue pour la production). Le compte `admin_lab` est créé au premier démarrage. Le mot de passe est un mot de passe de laboratoire.

4. Contrôle de la console d'administration :
```bash
curl -I http://127.0.0.1:8080/admin/
```
👉 Explication : Vérifie que la console répond (`HTTP/1.1 200 OK` ou une redirection vers la page de connexion). Ouvrir ensuite `http://<adresse_ip_serveur>:8080/admin/` et se connecter avec `admin_lab`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un compte de service et d'un dossier de données :
```bash
sudo useradd --system --home /opt/keycloak --shell /usr/sbin/nologin keycloak
sudo chown -R keycloak:keycloak /opt/keycloak-26.0.7
```
👉 Explication : Crée un compte système sans shell pour exécuter Keycloak et lui donne la propriété de sa distribution.

2. Compilation de la configuration de production puis démarrage derrière un reverse proxy :
```bash
cd /opt/keycloak
sudo -u keycloak KC_DB=postgres KC_DB_URL=jdbc:postgresql://127.0.0.1:5432/keycloak KC_DB_USERNAME=keycloak KC_DB_PASSWORD='<mot_de_passe_base>' ./bin/kc.sh build
sudo -u keycloak KC_HOSTNAME=auth.entreprise.lan KC_PROXY_HEADERS=xforwarded KC_HTTP_ENABLED=true KC_HEALTH_ENABLED=true KC_DB=postgres KC_DB_URL=jdbc:postgresql://127.0.0.1:5432/keycloak KC_DB_USERNAME=keycloak KC_DB_PASSWORD='<mot_de_passe_base>' ./bin/kc.sh start --optimized --http-port=8080
```
👉 Explication : `build` précompile Keycloak pour la base PostgreSQL. `start --optimized` le lance sans recompilation. `KC_PROXY_HEADERS=xforwarded` indique que le reverse proxy transmet l'adresse d'origine. La base PostgreSQL doit exister au préalable, à vérifier sur l'architecture retenue.

3. Contrôle de santé :
```bash
curl -f http://127.0.0.1:9000/health/ready
```
👉 Explication : Le point de santé est exposé sur le port de gestion 9000. La réponse JSON avec `"status": "UP"` est attendue.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Remplacement du compte `admin_lab` par un administrateur nommé, créé dans la console (Users, puis Role mapping `admin`) :
```bash
curl -I https://auth.entreprise.lan/admin/
```
👉 Explication : Vérifie l'accès à la console par son adresse publique HTTPS avant de travailler dans l'interface. Après création et test du nouvel administrateur dans la console, supprimer `admin_lab` : le compte de démonstration ne doit pas subsister.

2. Restriction des droits sur la distribution et sur la configuration :
```bash
sudo chown -R root:keycloak /opt/keycloak-26.0.7
sudo chmod -R o-rwx /opt/keycloak-26.0.7
ls -ld /opt/keycloak-26.0.7
```
👉 Explication : Seul root modifie les fichiers, le compte `keycloak` les lit et les exécute. Les autres utilisateurs n'ont aucun accès.

3. Restriction de l'exposition réseau au seul reverse proxy :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow from <adresse_ip_reverse_proxy> to any port 8080 proto tcp
sudo ufw allow from <adresse_ip_reverse_proxy> to any port 9000 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port HTTP 8080 et le port de santé 9000 ne sont accessibles que depuis le reverse proxy. Le port de santé ne doit jamais être publié sur Internet.

4. Sauvegarde de la base avant toute mise à jour :
```bash
sudo -u postgres pg_dump keycloak > /root/keycloak-db-$(date +%F).sql
sudo ls -l /root/keycloak-db-*.sql
```
👉 Explication : Exporte la base Keycloak dans un fichier daté. Il contient les comptes et les secrets clients : le stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

---