---
title: "Nginx"
description: "Installer le serveur web Nginx sur Debian 12, vérifier sur ce même serveur qu'une page de test répond, puis le durcir (HTTPS obligatoire, masquage de la version, en-têtes de sécurité) avant de le publier. Les tests ne se font que sur votre propre serveur."
published: true
date: 2026-10-29T12:25:24Z
tags: ["[debian-12]", "[nginx]", "[serveur-web]", "[reverse-proxy]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:24Z
dateModified: 2026-10-29T12:25:24Z
---

# 📄 Nginx

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Nginx 1.22.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[nginx]`, `[serveur-web]`, `[reverse-proxy]`, `[hardening]`

## 🎯 Objectif
Installer le serveur web Nginx sur Debian 12, vérifier sur ce même serveur qu'une page de test répond, puis le durcir (HTTPS obligatoire, masquage de la version, en-têtes de sécurité) avant de le publier. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Nginx :
```bash
sudo apt update
sudo apt install -y nginx
```
👉 Explication : Installe Nginx et ses fichiers de configuration dans `/etc/nginx/`. Les paquets proviennent des dépôts Debian 12.

2. Vérification de la version et de la syntaxe :
```bash
nginx -v
sudo nginx -t
```
👉 Explication : `nginx -v` affiche la version installée. `nginx -t` relit toute la configuration et affiche `syntax is ok` puis `test is successful` si elle est valide.

3. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable nginx
sudo systemctl start nginx
systemctl status nginx --no-pager
```
👉 Explication : Active le démarrage automatique, lance le service puis affiche son état. La ligne `Active: active (running)` est attendue.

4. Création d'une page de test et contrôle de la réponse :
```bash
echo "<h1>Test Nginx lab</h1>" | sudo tee /var/www/html/index.html
curl -I http://127.0.0.1/
```
👉 Explication : Remplace la page d'accueil par défaut par une page de test. La ligne `HTTP/1.1 200 OK` est attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un bloc serveur dédié :
```bash
sudo nano /etc/nginx/sites-available/<nom_site>
```
Ajouter ce bloc, en remplaçant les valeurs entre chevrons :
```
server {
    listen 80;
    server_name <nom_site_fqdn>;
    root /var/www/<nom_site>;
    index index.html;
    access_log /var/log/nginx/<nom_site>.access.log;
    error_log /var/log/nginx/<nom_site>.error.log;
}
```
👉 Explication : Définit un site servi pour le nom `<nom_site_fqdn>`, avec ses propres journaux. `<nom_site>` est un identifiant court, sans espaces.

2. Activation du site et désactivation du site par défaut :
```bash
sudo mkdir -p /var/www/<nom_site>
sudo ln -s /etc/nginx/sites-available/<nom_site> /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx
```
👉 Explication : Le lien symbolique active le site ; sa suppression désactive le site par défaut. `nginx -t` valide la syntaxe avant le rechargement.

3. Ouverture du pare-feu pour HTTP, HTTPS et administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre SSH seulement pour `<adresse_ip_admin>` avant d'activer le pare-feu. Le profil `Nginx Full` ouvre les ports 80 et 443. Vérifier la présence du profil avec `sudo ufw app list`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Masquage de la version dans les en-têtes et les pages d'erreur :
```bash
sudo nano /etc/nginx/nginx.conf
```
Dans le bloc `http { }`, ajouter :
```
server_tokens off;
```
👉 Explication : Empêche Nginx d'afficher son numéro de version. Puis `sudo nginx -t` et `sudo systemctl reload nginx`.

2. Passage en HTTPS et redirection depuis HTTP :
```bash
sudo nano /etc/nginx/sites-available/<nom_site>
```
Ajouter un bloc `server` sur le port 443 avec `ssl_certificate /etc/ssl/certs/<certificat_web>.crt;`, `ssl_certificate_key /etc/ssl/private/<certificat_web>.key;` et `ssl_protocols TLSv1.2 TLSv1.3;`. Dans le bloc port 80, ajouter `return 301 https://$host$request_uri;`.
👉 Explication : Force le chiffrement et refuse les anciens protocoles TLS. `<certificat_web>` est le nom du certificat émis pour le site, à vérifier sur la version déployée.

3. Ajout des en-têtes de sécurité :
```bash
sudo nano /etc/nginx/snippets/securite-headers.conf
```
Ajouter :
```
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Strict-Transport-Security "max-age=31536000" always;
```
👉 Explication : Ces en-têtes limitent l'affichage dans des cadres, le typage MIME et imposent HTTPS au navigateur. Inclure le fichier dans le bloc `server` avec `include snippets/securite-headers.conf;`.

4. Contrôle de la configuration et des journaux :
```bash
sudo nginx -t
sudo systemctl reload nginx
sudo tail -n 50 /var/log/nginx/error.log
```
👉 Explication : Valide la syntaxe, recharge le service puis affiche les dernières erreurs. Une série d'erreurs 403 ou 502 est à remonter au responsable sécurité.

5. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/nginx-conf-$(date +%F).tgz /etc/nginx
sudo ls -l /root/nginx-conf-*.tgz
```
👉 Explication : Crée une archive datée de toute la configuration Nginx, à stocker hors du serveur et à protéger en lecture.

---