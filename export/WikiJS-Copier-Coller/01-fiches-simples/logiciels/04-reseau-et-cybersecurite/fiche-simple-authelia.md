# 📄 Authelia

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Authelia 4.38.x (binaire officiel GitHub, à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité

## 🎯 Objectif
Installer Authelia sur Debian 12 comme portail d'authentification et de double facteur devant une application web, vérifier l'ouverture de session sur ce même serveur, puis le durcir (secrets forts, règles d'accès par domaine, TLS). Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création d'un compte de service et des dossiers :
```bash
sudo apt update
sudo apt install -y curl ca-certificates
sudo useradd --system --home /var/lib/authelia --shell /usr/sbin/nologin authelia
sudo mkdir -p /etc/authelia /var/lib/authelia
```
👉 Explication : Installe curl, crée un compte système sans shell pour exécuter Authelia, puis crée le dossier de configuration `/etc/authelia` et le dossier de données `/var/lib/authelia`.

2. Installation du binaire officiel :
```bash
cd /tmp
curl -LO https://github.com/authelia/authelia/releases/download/v4.38.17/authelia-linux-amd64.tar.gz
tar -xzf authelia-linux-amd64.tar.gz
sudo install -m 0755 authelia-linux-amd64 /usr/local/bin/authelia
authelia --version
```
👉 Explication : Télécharge la version 4.38.17 (numéro à vérifier, la dernière version publiée peut différer), installe le binaire dans `/usr/local/bin` et affiche sa version.

3. Génération des secrets et du hash du mot de passe de test :
```bash
authelia crypto rand --length 64 --charset alphanumeric
authelia crypto hash generate argon2 --password 'MotDePasseDeLab-2026'
```
👉 Explication : La première commande produit une valeur aléatoire à utiliser comme secret de session et clé de chiffrement. La seconde produit un hash argon2 à copier dans le fichier d'utilisateurs. Le mot de passe en clair ne doit exister qu'en laboratoire.

4. Fichier de configuration minimal :
```bash
sudo nano /etc/authelia/configuration.yml
```
```yaml
server:
  address: 'tcp://0.0.0.0:9091'
log:
  level: info
authentication_backend:
  file:
    path: /etc/authelia/users_database.yml
access_control:
  default_policy: deny
  rules:
    - domain: app.lab.local
      policy: two_factor
session:
  secret: <secret_session_genere>
  cookies:
    - domain: lab.local
      authelia_url: https://auth.lab.local
storage:
  encryption_key: <cle_chiffrement_generee>
  local:
    path: /var/lib/authelia/db.sqlite3
notifier:
  filesystem:
    filename: /var/lib/authelia/notification.txt
```
👉 Explication : Définit le port d'écoute, la base d'utilisateurs fichier, la politique par défaut `deny` et une règle d'exemple pour `app.lab.local`. `<secret_session_genere>` et `<cle_chiffrement_generee>` reçoivent les valeurs de l'étape 3. Les options exactes peuvent évoluer selon la version, à vérifier avec `authelia validate-config`.

5. Fichier d'utilisateurs de test puis validation de la configuration :
```bash
sudo nano /etc/authelia/users_database.yml
sudo authelia validate-config --config /etc/authelia/configuration.yml
```
```yaml
users:
  utilisateur_lab:
    displayname: 'Utilisateur de lab'
    password: '<hash_argon2_genere>'
    email: utilisateur@lab.local
    groups:
      - admins
```
👉 Explication : Le fichier déclare un compte `utilisateur_lab` dont le mot de passe est le hash produit à l'étape 3. `validate-config` contrôle la syntaxe sans démarrer le service.

6. Démarrage du service et contrôle :
```bash
sudo chown -R authelia:authelia /etc/authelia /var/lib/authelia
sudo tee /etc/systemd/system/authelia.service > /dev/null <<'EOF'
[Unit]
Description=Authelia
After=network-online.target

[Service]
User=authelia
ExecStart=/usr/local/bin/authelia --config /etc/authelia/configuration.yml
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now authelia
systemctl status authelia --no-pager
```
👉 Explication : Crée l'unité systemd, active le démarrage automatique et lance Authelia. La ligne `Active: active (running)` est attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du port d'écoute uniquement au reverse proxy :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_reverse_proxy> to any port 9091 proto tcp
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 9091 n'est accessible que depuis le reverse proxy. SSH reste limité à l'administration. Autoriser SSH avant `ufw enable` évite de perdre l'accès.

2. Règle d'accès en production (deux facteurs pour le domaine applicatif) dans `configuration.yml` :
```yaml
access_control:
  default_policy: deny
  rules:
    - domain: app.entreprise.lan
      policy: two_factor
```
👉 Explication : Toute application non déclarée est refusée par défaut. Le domaine `app.entreprise.lan` impose le mot de passe et le second facteur.

3. Validation puis redémarrage :
```bash
sudo authelia validate-config --config /etc/authelia/configuration.yml
sudo systemctl restart authelia
systemctl status authelia --no-pager
```
👉 Explication : Contrôle la configuration avant de relancer le service, puis confirme qu'il est actif.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur les fichiers contenant les secrets :
```bash
sudo chown root:authelia /etc/authelia/configuration.yml /etc/authelia/users_database.yml
sudo chmod 640 /etc/authelia/configuration.yml /etc/authelia/users_database.yml
ls -l /etc/authelia/
```
👉 Explication : Seul root modifie les fichiers, seul le compte `authelia` les lit. Les secrets ne doivent jamais être lisibles par tous les utilisateurs.

2. Remplacement du stockage local par une base dédiée et contrôle de la cohérence : à vérifier selon l'architecture retenue (PostgreSQL ou MariaDB), la configuration `storage` change alors complètement.

3. Journal et détection des échecs :
```bash
sudo journalctl -u authelia --since "1 hour ago" | grep -i "authentication failed"
```
👉 Explication : Liste les échecs d'authentification de la dernière heure. Une série d'échecs sur un même compte doit être remontée au responsable sécurité.

4. Sauvegarde de la configuration et de la base avant toute évolution :
```bash
sudo tar czf /root/authelia-conf-$(date +%F).tgz /etc/authelia /var/lib/authelia
sudo ls -l /root/authelia-conf-*.tgz
```
👉 Explication : L'archive contient les secrets et la base : la stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack), avec une lecture restreinte.

---