# 📄 Passbolt

- **Environnement** : VM (Debian 13) avec Docker
- **OS / Version** : Debian 13 (trixie)
- **Version** : Passbolt CE `<version_passbolt>` (image Docker `passbolt/passbolt`, à vérifier sur la version déployée)
- **Catégorie** : Gestion des secrets et mots de passe

## 🎯 Problème précis à résoudre
Déployer Passbolt CE (gestionnaire de mots de passe partagés) sur une VM Debian 13 avec Docker, créer le premier compte administrateur, vérifier que l'interface répond, puis le publier derrière HTTPS avec des sauvegardes et des secrets protégés. Passbolt repose sur une clé GPG serveur : sa perte rend les secrets inaccessibles, d'où les étapes de sauvegarde.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Docker et du plugin Compose :
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo systemctl start docker
sudo docker compose version
```
👉 Explication : Installe le moteur Docker et Compose, puis vérifie la version de Compose. Le nom du paquet Compose varie selon les dépôts Debian 13 (à vérifier sur la version déployée) ; si `docker compose` n'est pas reconnu, installer le paquet de plugin Compose correspondant.

2. Création du dossier de travail et des sous-dossiers de clés :
```bash
mkdir -p ~/passbolt/gpg ~/passbolt/jwt ~/passbolt/db
cd ~/passbolt
```
👉 Explication : Crée l'arborescence du projet : `gpg` pour la clé serveur, `jwt` pour les clés d'authentification API, `db` pour les données MariaDB.

3. Génération de la clé GPG du serveur (sans phrase de passe, requise par le conteneur) :
```bash
gpg --batch --passphrase '' --quick-gen-key "Passbolt <adresse_email_passbolt>" rsa3072 default never
gpg --list-keys --fingerprint <adresse_email_passbolt>
```
👉 Explication : Crée une clé RSA 3072 sans expiration pour le serveur. `<adresse_email_passbolt>` est l'adresse de service de Passbolt. La seconde commande affiche l'empreinte (fingerprint) de la clé : la noter, elle est nécessaire à l'étape suivante. Les options exactes de `gpg` peuvent varier selon la version (à vérifier sur la version déployée).

4. Export de la clé publique et de la clé privée serveur :
```bash
gpg --armor --export <empreinte_cle> > ~/passbolt/gpg/serverkey.asc
gpg --armor --export-secret-keys <empreinte_cle> > ~/passbolt/gpg/serverkey_private.asc
chmod 600 ~/passbolt/gpg/serverkey_private.asc
```
👉 Explication : `<empreinte_cle>` est l'empreinte relevée à l'étape 3. Le conteneur attend ces deux noms de fichiers dans `/etc/passbolt/gpg` (à vérifier sur la version déployée). La clé privée n'est lisible que par son propriétaire.

5. Génération des clés JWT (authentification de l'API) :
```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out ~/passbolt/jwt/jwt.key
openssl rsa -in ~/passbolt/jwt/jwt.key -pubout -out ~/passbolt/jwt/jwt.pem
```
👉 Explication : Crée une paire de clés RSA 2048 bits utilisée pour signer les jetons d'authentification. Le nom des fichiers et la prise en charge automatique par l'image sont à vérifier sur la version déployée.

6. Création du fichier `docker-compose.yml` (valeurs à remplacer entre chevrons) :
```bash
nano ~/passbolt/docker-compose.yml
```
Contenu :
```yaml
services:
  db:
    image: mariadb:10.11
    environment:
      MARIADB_DATABASE: passbolt
      MARIADB_USER: passbolt
      MARIADB_PASSWORD: <mot_de_passe_base>
      MARIADB_ROOT_PASSWORD: <mot_de_passe_root_base>
    volumes:
      - ./db:/var/lib/mysql
  passbolt:
    image: passbolt/passbolt:latest-ce
    depends_on:
      - db
    environment:
      APP_FULL_BASE_URL: https://<domaine_passbolt>
      DATASOURCES_DEFAULT_HOST: db
      DATASOURCES_DEFAULT_USERNAME: passbolt
      DATASOURCES_DEFAULT_PASSWORD: <mot_de_passe_base>
      DATASOURCES_DEFAULT_DATABASE: passbolt
    volumes:
      - ./gpg:/etc/passbolt/gpg
      - ./jwt:/etc/passbolt/jwt
    ports:
      - "443:443"
```
👉 Explication : `<domaine_passbolt>` est le nom DNS du service (en lab, l'adresse IP de la VM convient). `<mot_de_passe_base>` et `<mot_de_passe_root_base>` sont des mots de passe forts différents, à saisir identiques pour les deux champs `DATASOURCES_DEFAULT_PASSWORD` et `MARIADB_PASSWORD`. La base n'expose aucun port vers l'extérieur. `latest-ce` est acceptable en lab seulement.

7. Démarrage des conteneurs et contrôle de leur état :
```bash
cd ~/passbolt
sudo docker compose up -d
sudo docker compose ps
```
👉 Explication : Lance la base et Passbolt en arrière-plan, puis affiche leur état. Les deux services doivent être `running`.

8. Création du premier compte administrateur :
```bash
sudo docker compose exec passbolt su -m -c "/usr/share/php/passbolt/bin/cake passbolt register_user -u <adresse_email_admin> -f <prenom_admin> -l <nom_admin> -r admin" -s /bin/sh www-data
```
👉 Explication : Crée l'utilisateur administrateur de Passbolt. `<adresse_email_admin>`, `<prenom_admin>` et `<nom_admin>` sont les informations de ce compte. La commande affiche un lien d'activation à ouvrir dans le navigateur (à vérifier sur la version déployée).

9. Test de l'interface :
```bash
curl -k -I https://<adresse_ip_serveur>
```
👉 Explication : Vérifie que le service répond en HTTPS. `-k` accepte le certificat auto-signé du lab ; `<adresse_ip_serveur>` est l'IP de la VM. Un code `HTTP/2 200` ou une redirection est attendu. Terminer l'activation du compte administrateur dans le navigateur.

---

## ⚡ 2. Production — Façon Simplifiée
1. Publication locale uniquement, derrière un reverse proxy HTTPS. Dans `~/passbolt/docker-compose.yml`, remplacer la ligne de ports par :
```yaml
    ports:
      - "127.0.0.1:8080:80"
```
puis relancer :
```bash
cd ~/passbolt
sudo docker compose up -d
```
👉 Explication : Le conteneur n'écoute plus que sur `127.0.0.1` du serveur : seul le proxy y accède. Le port 80 interne du conteneur est exposé sur le port 8080 de l'hôte (à vérifier sur la version déployée).

2. Installation de Nginx et de Certbot, puis création du proxy :
```bash
sudo apt install -y nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/passbolt
```
Contenu du fichier, à adapter :
```nginx
server {
    server_name <domaine_passbolt>;
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
👉 Explication : Nginx reçoit le trafic public et le transmet au conteneur. `<domaine_passbolt>` doit correspondre à `APP_FULL_BASE_URL` dans le fichier Compose et pointer en DNS vers ce serveur.

3. Activation du site, contrôle de la configuration et certificat TLS :
```bash
sudo ln -s /etc/nginx/sites-available/passbolt /etc/nginx/sites-enabled/passbolt
sudo nginx -t
sudo certbot --nginx -d <domaine_passbolt>
```
👉 Explication : `nginx -t` valide la syntaxe avant tout rechargement. Certbot obtient un certificat Let's Encrypt pour `<domaine_passbolt>` et configure HTTPS. Le domaine doit être joignable depuis Internet sur le port 80 pour la validation.

4. Pare-feu : seuls SSH (depuis l'administration) et HTTP/HTTPS sont ouverts :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre HTTP/HTTPS pour les utilisateurs et SSH uniquement depuis `<adresse_ip_admin>`. Le port 8080 n'est pas ouvert : il reste interne au serveur.

5. Sauvegarde de la base et des clés :
```bash
cd ~/passbolt
sudo docker compose exec -T db sh -c 'mariadb-dump -u root -p"$MARIADB_ROOT_PASSWORD" passbolt' > ~/passbolt-base-$(date +%F).sql
sudo tar czf ~/passbolt-cles-$(date +%F).tgz ~/passbolt/gpg ~/passbolt/jwt
```
👉 Explication : Exporte la base Passbolt (les secrets chiffrés) et archive les clés GPG et JWT. Sans la clé GPG serveur, les secrets sont irrécupérables : ces archives doivent être copiées hors du serveur. Les noms de commandes (`mariadb-dump`) sont à vérifier sur la version déployée.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Déplacement des mots de passe hors du fichier Compose, dans un fichier `.env` protégé :
```bash
nano ~/passbolt/.env
chmod 600 ~/passbolt/.env
```
Contenu du fichier `.env` :
```
MARIADB_PASSWORD=<mot_de_passe_base>
MARIADB_ROOT_PASSWORD=<mot_de_passe_root_base>
```
Dans `docker-compose.yml`, remplacer chaque mot de passe en clair par `${MARIADB_PASSWORD}` ou `${MARIADB_ROOT_PASSWORD}`.
👉 Explication : Les secrets ne figurent plus dans le fichier Compose, qui peut être relu ou versionné. `chmod 600` limite la lecture au seul propriétaire. Le fichier `.env` ne doit jamais être copié dans un dépôt Git.

2. Restriction des droits sur les clés :
```bash
chmod 700 ~/passbolt/gpg ~/passbolt/jwt
chmod 600 ~/passbolt/gpg/serverkey_private.asc ~/passbolt/jwt/jwt.key
ls -l ~/passbolt/gpg ~/passbolt/jwt
```
👉 Explication : Seul le propriétaire accède aux dossiers et à la clé privée serveur. Le conteneur doit pouvoir lire ces fichiers : si le démarrage échoue, vérifier l'UID du conteneur (à vérifier sur la version déployée) avant d'élargir les droits.

3. Vérification qu'aucun port de la base n'est publié :
```bash
sudo docker compose ps
sudo ss -tlnp
```
👉 Explication : La colonne `PORTS` de `db` doit être vide. `ss -tlnp` liste les ports en écoute : seuls `127.0.0.1:8080`, `22` et `443` doivent apparaître.

4. Procédure de mise à jour contrôlée, avec version figée :
```bash
cd ~/passbolt
sudo docker compose pull
sudo docker compose up -d
sudo docker compose logs --tail 50 passbolt
```
👉 Explication : Dans `docker-compose.yml`, remplacer `latest-ce` par la version figée `<version_passbolt>` validée en lab. Lire les notes de version avant chaque mise à jour, puis vérifier les journaux après redémarrage (à vérifier sur la version déployée).

5. Test de restauration sur une VM distincte, au moins une fois par trimestre :
```bash
sudo docker compose exec -T db sh -c 'mariadb -u root -p"$MARIADB_ROOT_PASSWORD" passbolt' < ~/passbolt-base-<date_sauvegarde>.sql
```
👉 Explication : Restaure la base sauvegardée à l'étape 5 de la façon simplifiée. Une sauvegarde non testée n'est pas une sauvegarde : répéter la restauration complète, clés comprises, sur une machine de test. `<date_sauvegarde>` est la date du fichier sauvegardé (format AAAA-MM-JJ).

---