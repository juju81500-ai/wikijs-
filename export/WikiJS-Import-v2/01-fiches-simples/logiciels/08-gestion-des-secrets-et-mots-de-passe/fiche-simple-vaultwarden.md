---
title: "Vaultwarden"
description: "Déployer Vaultwarden, serveur compatible avec les clients Bitwarden, sur une VM Debian 13 avec Docker, vérifier qu'il répond, puis le publier en HTTPS avec inscription fermée, page d'administration protégée et sauvegardes testées. Les coffres chiffrés sont côté client, mais la perte de la base et de"
published: true
date: 2026-10-29T11:49:36Z
tags: ["[debian-13]", "[docker]", "[vaultwarden]", "[bitwarden-compatible]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T11:49:36Z
dateModified: 2026-10-29T11:49:36Z
---

# 📄 Vaultwarden

- **Environnement** : VM (Debian 13) avec Docker
- **OS / Version** : Debian 13 (trixie)
- **Version** : Vaultwarden `<version_vaultwarden>` (image Docker `vaultwarden/server`, à vérifier sur la version déployée)
- **Catégorie** : Gestion des secrets et mots de passe
- **Tags** : `[debian-13]`, `[docker]`, `[vaultwarden]`, `[bitwarden-compatible]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer Vaultwarden, serveur compatible avec les clients Bitwarden, sur une VM Debian 13 avec Docker, vérifier qu'il répond, puis le publier en HTTPS avec inscription fermée, page d'administration protégée et sauvegardes testées. Les coffres chiffrés sont côté client, mais la perte de la base et de la clé serveur reste une perte de données.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Docker, Compose et de l'outil SQLite :
```bash
sudo apt update
sudo apt install -y docker.io docker-compose sqlite3
sudo systemctl enable docker
sudo systemctl start docker
sudo docker compose version
```
👉 Explication : Installe Docker, Compose et `sqlite3` (utile aux sauvegardes). Le nom du paquet Compose varie selon les dépôts Debian 13 (à vérifier sur la version déployée).

2. Création du dossier de travail :
```bash
mkdir -p ~/vaultwarden
cd ~/vaultwarden
```
👉 Explication : Crée le dossier qui contiendra le fichier Compose et les données persistantes.

3. Création du fichier `docker-compose.yml` :
```bash
nano ~/vaultwarden/docker-compose.yml
```
Contenu :
```yaml
services:
  vaultwarden:
    image: vaultwarden/server:<version_vaultwarden>
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      DOMAIN: http://localhost:8080
      SIGNUPS_ALLOWED: "true"
    volumes:
      - ./vw-data:/data
    ports:
      - "8080:80"
```
👉 Explication : `<version_vaultwarden>` est un tag de version publié (à vérifier sur Docker Hub). `DOMAIN` est l'adresse complète par laquelle les utilisateurs accèdent au service : en lab, `http://localhost:8080`. `SIGNUPS_ALLOWED: "true"` autorise la création de comptes de test, à désactiver ensuite. Les données persistent dans `./vw-data`.

4. Démarrage du conteneur et contrôle des journaux :
```bash
cd ~/vaultwarden
sudo docker compose up -d
sudo docker compose ps
sudo docker compose logs --tail 30 vaultwarden
```
👉 Explication : Lance Vaultwarden en arrière-plan, affiche son état (`running`) et ses 30 dernières lignes de journal. Aucune erreur ne doit apparaître au démarrage.

5. Test du service en local :
```bash
curl -I http://localhost:8080
```
👉 Explication : Demande uniquement les en-têtes HTTP. Un code `HTTP/1.1 200 OK` confirme que l'interface web répond.

6. Création d'un compte de test dans le navigateur :
Ouvrir `http://localhost:8080` depuis la VM, puis créer un compte de test avec une adresse fictive et un mot de passe maître robuste.
👉 Explication : Le coffre web n'est utilisable qu'en contexte sécurisé : `localhost` convient en lab, mais une connexion par adresse IP en HTTP sera refusée par le navigateur. Le mot de passe maître ne se récupère pas : le noter dans un endroit sûr.

---

## ⚡ 2. Production — Façon Simplifiée
1. Génération du hash Argon2 du jeton d'administration (ne jamais stocker le jeton en clair) :
```bash
sudo docker run --rm -it vaultwarden/server:<version_vaultwarden> /vaultwarden hash --preset owasp
```
👉 Explication : Demande un jeton d'administration puis affiche son empreinte Argon2. Noter le jeton dans un coffre externe ; seule l'empreinte va dans le fichier Compose. La sous-commande `hash` et l'option `--preset` sont à vérifier sur la version déployée.

2. Mise à jour du fichier Compose pour la production :
```yaml
services:
  vaultwarden:
    image: vaultwarden/server:<version_vaultwarden>
    container_name: vaultwarden
    restart: unless-stopped
    environment:
      DOMAIN: https://<domaine_vaultwarden>
      SIGNUPS_ALLOWED: "false"
      ADMIN_TOKEN: '<empreinte_argon2_doublee>'
    volumes:
      - ./vw-data:/data
    ports:
      - "127.0.0.1:8080:80"
```
👉 Explication : `<domaine_vaultwarden>` est le nom DNS public du service. `SIGNUPS_ALLOWED: "false"` interdit l'inscription libre. Dans `<empreinte_argon2_doublee>`, chaque caractère `$` de l'empreinte doit être doublé en `$$` (Compose interprète sinon `$` comme une variable). Le port n'écoute que sur `127.0.0.1` : seul le proxy y accède.

3. Relance et contrôle :
```bash
cd ~/vaultwarden
sudo docker compose up -d
sudo docker compose logs --tail 30 vaultwarden
```
👉 Explication : Applique la nouvelle configuration et vérifie l'absence d'erreur au démarrage.

4. Proxy Nginx et certificat TLS :
```bash
sudo apt install -y nginx certbot python3-certbot-nginx
sudo nano /etc/nginx/sites-available/vaultwarden
```
Contenu du fichier, à adapter :
```nginx
server {
    server_name <domaine_vaultwarden>;
    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```
Puis :
```bash
sudo ln -s /etc/nginx/sites-available/vaultwarden /etc/nginx/sites-enabled/vaultwarden
sudo nginx -t
sudo certbot --nginx -d <domaine_vaultwarden>
```
👉 Explication : Nginx transmet le trafic HTTPS public au conteneur. `nginx -t` valide la configuration avant rechargement. Certbot obtient un certificat Let's Encrypt pour `<domaine_vaultwarden>`. Le domaine doit pointer vers ce serveur et le port 80 doit être joignable pour la validation.

5. Pare-feu : seuls SSH (depuis l'administration) et HTTPS sont ouverts :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Autorise HTTP (redirection et validation TLS) et HTTPS pour tous, SSH seulement depuis `<adresse_ip_admin>`. Le port 8080 reste interne.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction de la page d'administration à un poste d'administration. Ajouter dans le bloc `server` de Nginx, avant `location / {` :
```nginx
    location /admin {
        allow <adresse_ip_admin>;
        deny all;
        proxy_pass http://127.0.0.1:8080;
    }
```
Puis :
```bash
sudo nginx -t
sudo systemctl reload nginx
```
👉 Explication : Seul `<adresse_ip_admin>` peut atteindre `/admin`, les autres reçoivent une erreur 403. Cela évite qu'un attaquant n'interroge la page d'administration depuis Internet.

2. Sauvegarde cohérente de la base SQLite, planifiée :
```bash
sudo mkdir -p /var/backups/vaultwarden
sudo sqlite3 ~/vaultwarden/vw-data/db.sqlite3 ".backup '/var/backups/vaultwarden/db-$(date +%F).sqlite3'"
sudo tar czf /var/backups/vaultwarden/vw-data-$(date +%F).tgz ~/vaultwarden/vw-data
```
👉 Explication : `.backup` produit une copie cohérente même si la base est en cours d'utilisation, à la différence d'une simple copie de fichier. L'archive du dossier `vw-data` contient aussi les clés et les pièces jointes. Ces fichiers contiennent des données sensibles : les copier ensuite hors du serveur, chiffrés. Planifier l'opération (cron ou timer systemd) selon la politique de sauvegarde de l'entreprise.

3. Restriction des droits sur les données et le fichier Compose :
```bash
sudo chmod 700 ~/vaultwarden/vw-data
sudo chmod 600 ~/vaultwarden/docker-compose.yml
sudo chmod 600 /var/backups/vaultwarden/*
```
👉 Explication : Le dossier de données et les sauvegardes ne sont lisibles que par `root`. Le fichier Compose contient l'empreinte du jeton d'administration : il reste privé.

4. Authentification à deux facteurs pour tous les comptes :
Dans l'interface web, chaque utilisateur active l'authentification à deux facteurs (Paramètres du compte, Sécurité).
👉 Explication : Un mot de passe maître seul ne suffit pas en production. Imposer l'activation et vérifier la liste des comptes depuis la page d'administration (les menus exacts dépendent de la version, à vérifier sur la version déployée).

5. Mise à jour contrôlée avec version figée :
```bash
cd ~/vaultwarden
sudo docker compose pull
sudo docker compose up -d
sudo docker compose logs --tail 30 vaultwarden
```
👉 Explication : Remplacer le tag `<version_vaultwarden>` par la version validée en lab avant de relancer. Lire les notes de version, car les correctifs de sécurité sont publiés régulièrement (à vérifier sur la version déployée).

6. Test de restauration sur une VM distincte :
```bash
sudo mkdir -p /tmp/vw-test
sudo cp /var/backups/vaultwarden/db-<date_sauvegarde>.sqlite3 /tmp/vw-test/db.sqlite3
sudo sqlite3 /tmp/vw-test/db.sqlite3 "PRAGMA integrity_check;"
```
👉 Explication : Copie la sauvegarde dans un dossier de test, puis vérifie son intégrité : la réponse attendue est `ok`. `<date_sauvegarde>` est la date du fichier sauvegardé (format AAAA-MM-JJ). Sur une VM de test, répéter aussi la restauration complète du dossier `vw-data` au moins une fois par trimestre, car une base saine ne suffit pas sans sa clé RSA.

---