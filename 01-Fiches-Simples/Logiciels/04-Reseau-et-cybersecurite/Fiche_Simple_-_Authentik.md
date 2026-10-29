# 📄 Authentik

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Authentik 2024.x (conteneurs officiels via Docker Compose, tag à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité
- **Tags** : `[debian-12]`, `[authentik]`, `[sso]`, `[mfa]`, `[docker]`, `[hardening]`

## 🎯 Objectif
Déployer Authentik sur Debian 12 avec Docker Compose comme fournisseur d'identité (SSO, double facteur), vérifier l'assistant de première configuration sur ce même serveur, puis le durcir (secrets forts, accès d'administration restreint, sauvegarde). Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Docker et de Docker Compose :
```bash
sudo apt update
sudo apt install -y docker.io docker-compose-plugin curl openssl
sudo systemctl enable --now docker
docker compose version
```
👉 Explication : Installe Docker et le plugin Compose, active le démarrage du moteur Docker, puis affiche la version de Compose. Le paquet `docker-compose-plugin` n'est pas garanti dans les dépôts Debian 12 : si `apt` ne le trouve pas, utiliser le dépôt officiel Docker, à vérifier.

2. Création du dossier de déploiement et téléchargement du fichier Compose officiel :
```bash
sudo mkdir -p /opt/authentik
cd /opt/authentik
sudo curl -L -o /opt/authentik/docker-compose.yml https://goauthentik.io/docker-compose.yml
```
👉 Explication : Crée `/opt/authentik` et récupère le fichier Compose publié par le projet. Le fichier désigne les images et les volumes à utiliser, à vérifier sur la version déployée.

3. Génération des secrets dans le fichier `.env` :
```bash
cd /opt/authentik
echo "PG_PASS=$(openssl rand -base64 36 | tr -d '\n')" | sudo tee .env
echo "AUTHENTIK_SECRET_KEY=$(openssl rand -base64 60 | tr -d '\n')" | sudo tee -a .env
echo "AUTHENTIK_ERROR_REPORTING__ENABLED=false" | sudo tee -a .env
sudo chmod 600 .env
```
👉 Explication : Crée un mot de passe pour PostgreSQL, une clé secrète d'application et désactive l'envoi des erreurs. `chmod 600` limite la lecture à root.

4. Démarrage des conteneurs et contrôle de leur état :
```bash
cd /opt/authentik
sudo docker compose pull
sudo docker compose up -d
sudo docker compose ps
```
👉 Explication : Télécharge les images, lance la base PostgreSQL, Redis et le serveur Authentik, puis affiche l'état des conteneurs. Les services `server` et `worker` doivent être à l'état `running`.

5. Première configuration du compte administrateur :
```bash
curl -I http://127.0.0.1:9000/if/flow/initial-setup/
```
👉 Explication : Vérifie que l'interface répond (`HTTP/1.1 200 OK` attendu). Ouvrir ensuite `http://<adresse_ip_serveur>:9000/if/flow/initial-setup/` dans un navigateur pour créer le compte `akadmin`. Le lien d'initialisation n'est valide que peu de temps après le premier démarrage.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du port d'administration uniquement pour le poste d'administration et le reverse proxy :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow from <adresse_ip_reverse_proxy> to any port 9000 proto tcp
sudo ufw allow from <adresse_ip_reverse_proxy> to any port 9443 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH est limité au poste d'administration. Les ports 9000 et 9443 ne sont accessibles que depuis le reverse proxy qui publie Authentik en HTTPS. Autoriser SSH avant `ufw enable` évite de perdre l'accès.

2. Redémarrage propre après modification du `.env` :
```bash
cd /opt/authentik
sudo docker compose up -d
sudo docker compose ps
```
👉 Explication : Recrée les conteneurs avec les nouvelles variables, puis confirme leur état.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur le fichier de secrets :
```bash
sudo chown root:root /opt/authentik/.env
sudo chmod 600 /opt/authentik/.env
ls -l /opt/authentik/.env
```
👉 Explication : Seul root lit le fichier qui contient la clé secrète et le mot de passe de base.

2. Sauvegarde de la base PostgreSQL avant toute mise à jour :
```bash
cd /opt/authentik
sudo docker compose exec postgresql pg_dump -U authentik authentik > /root/authentik-db-$(date +%F).sql
sudo ls -l /root/authentik-db-*.sql
```
👉 Explication : Exporte la base `authentik` dans un fichier daté. Le fichier contient les comptes et secrets : le stocker hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

3. Contrôle des journaux d'authentification :
```bash
cd /opt/authentik
sudo docker compose logs --since 1h server | grep -i "failed"
```
👉 Explication : Liste les échecs de connexion de la dernière heure. Une série d'échecs sur un même compte doit être remontée au responsable sécurité.

---
