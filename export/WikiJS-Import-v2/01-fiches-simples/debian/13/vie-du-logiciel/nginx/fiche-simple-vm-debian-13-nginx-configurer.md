---
title: "Fiche Simple - VM Debian 13 Nginx Configurer"
description: "Publier un site statique et un reverse proxy minimal avec un server block dédié, sans toucher à la configuration par défaut."
published: true
date: 2026-10-29T20:32:41Z
tags: ["debian13", "nginx", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:32:41Z
dateModified: 2026-10-29T20:32:41Z
---

# Fiche_Simple_-_VM_Debian_13_Nginx_Configurer

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Configurer un site
- **Tags** : `debian13`, `nginx`, `configuration`

---

## Problème précis à résoudre

Publier un site statique et un reverse proxy minimal avec un server block dédié, sans toucher à la configuration par défaut.

## 1. Hors-Production (Lab / Test / POC)

1. Créer la racine du site :
   ```bash
   sudo install -d -o root -g www-data -m 0755 /var/www/SITE/public
   echo 'Site Nginx OK' | sudo tee /var/www/SITE/public/index.html >/dev/null
   ```
   👉 Explication : remplacer `SITE` par le nom du site ; contenu neutre, en lecture seule pour `www-data`.

2. Créer le server block :
   ```bash
   sudo tee /etc/nginx/sites-available/SITE >/dev/null <<'EOF'
   server {
       listen 80;
       listen [::]:80;
       server_name SITE.example.net;
       root /var/www/SITE/public;
       index index.html;
       access_log /var/log/nginx/SITE.access.log;
       error_log  /var/log/nginx/SITE.error.log;
       location / { try_files $uri $uri/ =404; }
   }
   EOF
   ```
   👉 Explication : remplacer `SITE` et `SITE.example.net` (à remplacer par le nom DNS réel).

3. Ajouter, si besoin, un reverse proxy vers une application locale :
   ```bash
   sudo tee /etc/nginx/snippets/proxy-APP.conf >/dev/null <<'EOF'
   proxy_pass http://127.0.0.1:PORT_APP;
   proxy_set_header Host $host;
   proxy_set_header X-Real-IP $remote_addr;
   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
   proxy_set_header X-Forwarded-Proto $scheme;
   EOF
   ```
   👉 Explication : remplacer `APP` et `PORT_APP` (port d'écoute de l'application) ; à inclure avec `include snippets/proxy-APP.conf;` dans un `location`.

4. Activer, tester et recharger :
   ```bash
   sudo ln -s /etc/nginx/sites-available/SITE /etc/nginx/sites-enabled/SITE
   sudo nginx -t && sudo systemctl reload nginx
   ```
   👉 Explication : ne recharger que si le test de syntaxe réussit.

## 2. Production — Contrôles

Un server block par site, nommé explicitement ; journaux séparés ; configuration versionnée (dépôt Git d'infrastructure) et revue avant déploiement.

## 3. Production — Sécurité

- Ne jamais éditer directement `nginx.conf` pour un site : utiliser `sites-available` et `sites-enabled`.
- Toujours lancer `nginx -t` avant `reload`.
- Ne pas laisser de `autoindex on` ni de racine pointant sur `/`.

## Validation et retour arrière

- **Validation** : `curl -H 'Host: SITE.example.net' http://127.0.0.1/` renvoie le contenu du site.
- **Retour arrière** : supprimer le lien `sites-enabled/SITE`, lancer `sudo nginx -t` puis `sudo systemctl reload nginx`.

## Si le problème n'est pas résolu

- [Nginx — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-prerequis-limites)
- [Nginx — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-installer)
- [Nginx — Sécuriser (TLS, en-têtes, pare-feu)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-securiser)
- [Nginx — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-valider)
- [Nginx — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-sauvegarder-restaurer)
- [Nginx — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-mettre-a-jour)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)