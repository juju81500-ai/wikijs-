# 📄 VM_Debian_12_ReverseProxy_Installation-Nginx-Proxy-Manager.md

- **Environnement** : VM / Docker (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Réseau & Reverse Proxy / Nginx Proxy Manager
- **Tags** : `[debian12]`, `[nginx-proxy-manager]`, `[docker]`, `[reverse-proxy]`, `[ssl]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer Nginx Proxy Manager (NPM) sous Docker pour centraliser la redirection des flux HTTP/HTTPS, automatiser la gestion des certificats Let's Encrypt et protéger les applications Web internes.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création du répertoire de travail :
   `mkdir -p /opt/npm && cd /opt/npm`
   👉 Explication : Définit l'emplacement racine pour la pile Nginx Proxy Manager.
2. Démarrage rapide en conteneur autonome :
   `docker run -d --name npm -p 80:80 -p 127.0.0.1:81:81 -p 443:443 jc21/nginx-proxy-manager:<VERSION_VALIDEE>`
   👉 Explication : Remplacer le tag par une version testée. L'interface d'administration n'écoute que sur loopback ; l'accès distant passe par VPN/tunnel.

---

## ⚡ 2. Production — Façon Simplifiée
1. Rédaction du fichier `docker-compose.yml` avec volumes de persistance :
   ```yaml
   version: '3.8'
   services:
     app:
      image: 'jc21/nginx-proxy-manager:<VERSION_VALIDEE>'
       container_name: nginx-proxy-manager
       restart: unless-stopped
       ports:
         - '80:80'
         - '127.0.0.1:81:81'
         - '443:443'
       volumes:
         - ./data:/data
         - ./letsencrypt:/etc/letsencrypt
   ```
   👉 Explication : Structure le conteneur applicatif avec stockage persistant des certificats et réglages.
2. Lancement du service Compose :
   `docker compose up -d`
   👉 Explication : Instancie et connecte le conteneur du Reverse Proxy en arrière-plan.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Dans le fichier Compose, lier le port d'administration uniquement à loopback :
   ```yaml
   ports:
     - '80:80'
     - '127.0.0.1:81:81'
     - '443:443'
   ```
   Puis contrôler et appliquer depuis `/opt/npm` :
   `docker compose config --quiet && docker compose up -d`
   👉 Explication : Bloque l'exposition publique du panneau de contrôle NPM (accès réservé au tunnel SSH ou VPN).
2. Restreindre l'accès au répertoire persistant des certificats selon l'UID/GID utilisé par l'image et sauvegarder les clés hors hôte. Vérifier les permissions après déploiement ; ne pas appliquer un `chmod` qui empêcherait le conteneur de lire ses certificats.
3. Configurer les en-têtes de sécurité et les options TLS par hôte proxy dans l'interface NPM après validation avec l'application concernée. Ne pas injecter une directive Nginx globale dans un shell : elle doit être placée dans le contexte de configuration approprié et testée avant rechargement.