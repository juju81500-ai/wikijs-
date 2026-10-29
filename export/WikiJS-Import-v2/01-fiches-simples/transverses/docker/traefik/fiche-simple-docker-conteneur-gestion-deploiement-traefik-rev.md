---
title: "Docker_Conteneur_Gestion_Deploiement-Traefik-Reverse-Proxy"
description: "Déployer le Reverse Proxy cloud-native Traefik v3 en conteneur Docker, configurer la découverte automatique des conteneurs via le socket Docker et sécuriser la génération des certificats Let's Encrypt SSL/TLS."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[docker]", "[traefik]", "[reverse-proxy]", "[letsencrypt]", "[docker-compose]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Docker_Conteneur_Gestion_Deploiement-Traefik-Reverse-Proxy.md

- **Environnement** : Docker (Hôte Debian / Ubuntu)
- **OS / Version** : Docker Engine 24+ / Compose v2
- **Catégorie** : Reverse Proxy & Routage / Traefik v3
- **Tags** : `[docker]`, `[traefik]`, `[reverse-proxy]`, `[letsencrypt]`, `[docker-compose]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer le Reverse Proxy cloud-native Traefik v3 en conteneur Docker, configurer la découverte automatique des conteneurs via le socket Docker et sécuriser la génération des certificats Let's Encrypt SSL/TLS.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création du répertoire de travail :
   `mkdir -p /opt/traefik && cd /opt/traefik`
   👉 Explication : Prépare l'espace pour la configuration de Traefik.
2. Lancement autonome avec tableau de bord de test :
   `docker run -d -p 80:80 -p 127.0.0.1:8080:8080 traefik:<VERSION_VALIDEE> --api.insecure=true --api.dashboard=true --entrypoints.web.address=:80`
   👉 Explication : Réservé à un lab isolé. Le dashboard est accessible uniquement depuis localhost ; remplacer le tag par une version testée et supprimer ce mode après l'essai.

---

## ⚡ 2. Production — Façon Simplifiée
1. Fichier `docker-compose.yml` complet pour Traefik v3 :
   ```yaml
   services:
     traefik:
          image: traefik:<VERSION_VALIDEE>
       container_name: traefik
          restart: unless-stopped
       command:
         - "--entrypoints.web.address=:80"
         - "--entrypoints.websecure.address=:443"
             - "--providers.file.directory=/etc/traefik/dynamic"
             - "--providers.file.watch=true"
             - "--certificatesresolvers.le.acme.email=admin@example.net"
             - "--certificatesresolvers.le.acme.storage=/letsencrypt/acme.json"
             - "--certificatesresolvers.le.acme.httpchallenge.entrypoint=web"
       ports:
         - "80:80"
         - "443:443"
       volumes:
             - ./dynamic:/etc/traefik/dynamic:ro
             - ./letsencrypt:/letsencrypt
          networks:
             - proxy
    networks:
       proxy:
          name: proxy
    ```
    Remplacer le courriel et le tag. Ce mode utilise le fournisseur fichier et ne monte pas le socket Docker.

2. Créer le stockage ACME avec des permissions privées, valider la pile puis démarrer :
    ```bash
    mkdir -p dynamic letsencrypt
    touch letsencrypt/acme.json
    chmod 600 letsencrypt/acme.json
    docker compose config --quiet
    docker compose up -d
    ```

---

## 🔒 3. Production — Façon Sécurisée
1. Créer `dynamic/app.yml` pour un service explicitement choisi et connecté au réseau Docker `proxy` :
    ```yaml
    http:
       routers:
          app:
             rule: Host(`app.example.net`)
             entryPoints: [websecure]
             service: app
             tls:
                certResolver: le
       services:
          app:
             loadBalancer:
                servers:
                   - url: http://app:8080
    ```
    Remplacer le nom DNS et le nom/port du service par les valeurs réelles. Redirection HTTP vers HTTPS et dashboard doivent être configurés explicitement ; ne pas exposer l'API insegura.
2. Le fournisseur Docker nécessite l'accès au socket, qui equivale à un privilège root. Si la découverte par labels est requise, utiliser un proxy de socket avec API minimale et réseau privé ; un montage `:ro` seul ne restreint pas les appels API.
3. Vérifier DNS, challenge ACME, certificat et renouvellement en staging avant la production. Sauvegarder `acme.json` de manière chiffrée et limitée ; ne pas publier le dashboard sur une interface publique.
4. Valider chaque modification avec `docker compose config --quiet`, consulter `docker compose logs traefik` puis tester le nom DNS en HTTPS depuis un client.