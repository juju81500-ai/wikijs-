---
title: "Fiche Simple - VM Debian 13 ownCloud Configurer"
description: "Configurer ownCloud Infinite Scale derrière un reverse proxy Nginx avec TLS terminé par le proxy."
published: true
date: 2026-10-29T21:07:46Z
tags: ["debian13", "owncloud", "ocis", "cloud", "configurer"]
editor: markdown
dateCreated: 2026-10-29T21:07:46Z
dateModified: 2026-10-29T21:07:46Z
---

# Fiche_Simple_-_VM_Debian_13_ownCloud_Configurer

- **Environnement** : VM Debian 13; ownCloud Infinite Scale (oCIS), binaire officiel, Nginx
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : Messagerie et collaboratif / ownCloud — Configurer
- **Tags** : `debian13`, `owncloud`, `ocis`, `cloud`, `configurer`

---

## Problème précis à résoudre

Configurer ownCloud Infinite Scale derrière un reverse proxy Nginx avec TLS terminé par le proxy.

## 1. Hors-Production (Lab / Test / POC)

1. Adapter l'unité systemd pour n'écouter qu'en local et laisser le proxy gérer TLS :
   ```bash
   sudo systemctl edit ocis
   ```
   👉 Explication : dans l'éditeur, ajouter sous `[Service]` : `Environment=OCIS_URL=https://OCIS.EXAMPLE.NET`, `Environment=PROXY_TLS=false`, `Environment=PROXY_HTTP_ADDR=127.0.0.1:9200`. Noms de variables à confirmer dans la documentation de la version installée.

2. Installer Nginx :
   ```bash
   sudo apt install -y nginx
   ```
   👉 Explication : voir la fiche Nginx du pack pour les bases du serveur.

3. Créer le virtual host :
   ```bash
   sudo tee /etc/nginx/sites-available/ocis >/dev/null <<'EOF'
   server {
       listen 80;
       server_name OCIS.EXAMPLE.NET;
       client_max_body_size 0;
       location / {
           proxy_pass http://127.0.0.1:9200;
           proxy_set_header Host $host;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_request_buffering off;
       }
   }
   EOF
   sudo ln -s /etc/nginx/sites-available/ocis /etc/nginx/sites-enabled/ocis
   sudo nginx -t && sudo systemctl reload nginx
   ```
   👉 Explication : `OCIS.EXAMPLE.NET` à remplacer ; l'en-tête Upgrade supporte les WebSockets ; `client_max_body_size 0` autorise les gros fichiers (à encadrer par quotas).

4. Redémarrer oCIS :
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl restart ocis
   sudo journalctl -u ocis -n 20 --no-pager
   ```
   👉 Explication : aucune erreur de démarrage attendue.

5. Créer un utilisateur de test via l'interface (connexion administrateur > Utilisateurs) : chemin GUI.
   👉 Explication : les comptes se gèrent dans l'application ; les quotas aussi.

## 2. Production — Contrôles

Vérifier la cohérence `OCIS_URL`/FQDN/certificat, la limite de taille d'envoi, les journaux Nginx et oCIS, et la présence du proxy comme seul point d'entrée.

## 3. Production — Sécurité

- oCIS n'écoute que sur 127.0.0.1 : le proxy est l'unique exposition.
- Ne pas désactiver la validation TLS (`insecure`) en production.

## Validation et retour arrière

- **Validation** : `sudo nginx -t` réussit et l'URL publique répond après la fiche Sécuriser.
- **Retour arrière** : `sudo rm /etc/nginx/sites-enabled/ocis`, `sudo systemctl revert ocis` puis redémarrer les services.

## Si le problème n'est pas résolu

- [ownCloud — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-prerequis-limites)
- [ownCloud — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/owncloud/fiche-simple-vm-debian-13-owncloud-installer)
- [Nginx — LEMP Deployer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-lemp-deployer-nginx-php)
- [ownCloud Infinite Scale — documentation officielle](https://doc.owncloud.com/ocis/next/)
- [ownCloud — téléchargements](https://owncloud.com/download-server/)