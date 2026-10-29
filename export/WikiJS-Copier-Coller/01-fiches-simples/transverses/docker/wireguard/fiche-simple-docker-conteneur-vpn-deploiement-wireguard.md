# 📄 Docker_Conteneur_VPN_Deploiement-Wireguard.md

- **Environnement** : Docker (Hôte Debian / Ubuntu)
- **OS / Version** : Docker Engine 24+ / Compose v2
- **Catégorie** : Sécurité & VPN / WireGuard

## 🎯 Problème précis à résoudre
Déployer un serveur VPN moderne et haute performance WireGuard dans un conteneur Docker avec l'interface d'administration Web `wg-easy`, configurer la persistance des clés et sécuriser l'accès au port UDP.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lancement rapide d'un conteneur WireGuard en une ligne de commande :
   `docker run -d --name=wireguard --cap-add=NET_ADMIN --cap-add=SYS_MODULE -p 51820:51820/udp -p 127.0.0.1:51821:51821/tcp -e WG_HOST=vpn.example.net -e PASSWORD_HASH=<HASH_BCRYPT> -v wireguard_data:/etc/wireguard ghcr.io/wg-easy/wg-easy:<VERSION_VALIDEE>`
   👉 Explication : Démarrage immédiat du serveur WireGuard avec les capacités réseau Linux requises.

2. Vérification de l'état du conteneur :
   `docker ps -f name=wireguard`
   👉 Explication : Contrôle le statut de démarrage du conteneur et le mappage du port UDP 51820.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du répertoire de travail et du fichier `docker-compose.yml` :
   `mkdir -p /opt/wireguard && cd /opt/wireguard`
   👉 Explication : Prépare l'emplacement persistant pour la configuration et les clés WireGuard.

2. Fichier `docker-compose.yml` complet :
   ```yaml
   version: "3.8"
   services:
     wg-easy:
      image: ghcr.io/wg-easy/wg-easy:<VERSION_VALIDEE>
       container_name: wg-easy
       environment:
         - WG_HOST=vpn.example.net
         - PASSWORD_HASH=${WG_PASSWORD_HASH:?Définir un hash bcrypt dans l’environnement}
         - WG_PORT=51820
         - WG_DEFAULT_DNS=192.0.2.53
       volumes:
         - ./data:/etc/wireguard
       ports:
         - "51820:51820/udp"
         - "127.0.0.1:51821:51821/tcp"
       cap_add:
         - NET_ADMIN
         - SYS_MODULE
       sysctls:
         - net.ipv4.conf.all.src_valid_mark=1
         - net.ipv4.ip_forward=1
       restart: unless-stopped
   ```
   👉 Explication : Remplacer la version, le nom DNS et le DNS interne. Générer le hash bcrypt selon la documentation wg-easy, le fournir hors du dépôt et ne publier l'interface qu'à travers un accès d'administration protégé.

3. Démarrage de la stack Docker Compose :
   `docker compose up -d`
   👉 Explication : Lance le conteneur WireGuard en arrière-plan.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier que le port d'administration est lié à `127.0.0.1` dans Compose, puis valider et appliquer :
   `docker compose config --quiet && docker compose up -d`
   👉 Explication : Empêche l'exposition de la console Web d'administration sur Internet (accessible uniquement via tunnel SSH ou Reverse Proxy local).

2. Activation du transfert d'IP sécurisé (IP Forwarding) sur l'hôte Linux :
   `sysctl -w net.ipv4.ip_forward=1 && echo "net.ipv4.ip_forward=1" >> /etc/sysctl.d/99-wireguard.conf`
   👉 Explication : Permet au noyau hôte de router le trafic chiffré des clients VPN vers le réseau local.

3. Filtrage strict du port VPN UDP 51820 sur l'hôte via nftables/ufw :
   `ufw allow 51820/udp comment 'WireGuard VPN Port'`
   👉 Explication : Autorise le trafic VPN UDP tout en maintenant le pare-feu actif sur tous les autres ports.

4. Protéger le volume contenant les clés selon l'UID/GID de l'image. Sauvegarder la configuration hors hôte avec chiffrement ; ne pas appliquer `chmod -R` sans vérifier les permissions attendues par le conteneur.