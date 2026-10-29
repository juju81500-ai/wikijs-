---
title: "Traefik"
description: "Installer Traefik sur Debian 12 comme reverse proxy HTTP devant deux serveurs web, vérifier qu'il route une requête selon le nom d'hôte, puis le durcir (tableau de bord protégé, utilisateur de service dédié, pare-feu restreint) avant de l'exposer à un service de l'entreprise. Les tests ne se font qu"
published: true
date: 2026-10-29T12:25:12Z
tags: ["[debian-12]", "[traefik]", "[reverse-proxy]", "[load-balancer]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:12Z
dateModified: 2026-10-29T12:25:12Z
---

# 📄 Traefik

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Traefik v3.x (binaire officiel GitHub, version à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[traefik]`, `[reverse-proxy]`, `[load-balancer]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Traefik sur Debian 12 comme reverse proxy HTTP devant deux serveurs web, vérifier qu'il route une requête selon le nom d'hôte, puis le durcir (tableau de bord protégé, utilisateur de service dédié, pare-feu restreint) avant de l'exposer à un service de l'entreprise. Les tests ne se font que sur votre propre serveur et vos propres machines.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Récupération du binaire Traefik de la dernière version publiée :
```bash
sudo apt update
sudo apt install -y curl tar
TAG=$(curl -s https://api.github.com/repos/traefik/traefik/releases/latest | grep -o '"tag_name": "[^"]*' | cut -d'"' -f4)
echo $TAG
curl -LO https://github.com/traefik/traefik/releases/download/$TAG/traefik_${TAG}_linux_amd64.tar.gz
tar -xzf traefik_${TAG}_linux_amd64.tar.gz traefik
sudo install -m 755 traefik /usr/local/bin/traefik
traefik version
```
👉 Explication : Debian 12 ne fournit pas Traefik dans ses dépôts : le binaire officiel est installé. Le nom de l'archive suit le format publié par le projet, à vérifier sur la page des versions si le téléchargement échoue.

2. Création du fichier statique (points d'entrée et tableau de bord de test) :
```bash
sudo mkdir -p /etc/traefik
sudo nano /etc/traefik/traefik.yml
```
Contenu :
```
entryPoints:
  web:
    address: ":80"
providers:
  file:
    filename: /etc/traefik/dynamic.yml
api:
  dashboard: true
  insecure: true
```
👉 Explication : Le point d'entrée `web` écoute sur le port 80. Le fournisseur `file` lit les routes dans `/etc/traefik/dynamic.yml`. `insecure: true` expose le tableau de bord sans authentification : acceptable uniquement en lab.

3. Création des routes et des deux serveurs web de test :
```bash
sudo nano /etc/traefik/dynamic.yml
```
Contenu :
```
http:
  routers:
    app-lab:
      rule: "Host(`app.lab.local`)"
      entryPoints:
        - web
      service: app-lab
  services:
    app-lab:
      loadBalancer:
        servers:
          - url: "http://192.168.10.11:80"
          - url: "http://192.168.10.12:80"
```
👉 Explication : Le routeur `app-lab` envoie vers le service `app-lab` les requêtes dont l'en-tête `Host` vaut `app.lab.local`. Les adresses `192.168.10.11` et `192.168.10.12` sont celles des machines de test, à adapter.

4. Lancement en premier plan et test de routage :
```bash
sudo traefik --configFile=/etc/traefik/traefik.yml
```
Dans un second terminal :
```bash
curl -I -H "Host: app.lab.local" http://127.0.0.1/
curl -s http://127.0.0.1:8080/api/rawdata | head -n 20
```
👉 Explication : `traefik --configFile` démarre le proxy avec la configuration. La première requête doit recevoir une réponse des serveurs web. La seconde interroge l'API du tableau de bord sur le port 8080 et affiche les routeurs déclarés. Le port 8080 est le port standard de l'API Traefik (à vérifier sur la version déployée).

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un utilisateur système dédié, sans shell de connexion, et autorisation d'écouter sur le port 80 sans root :
```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin traefik
sudo setcap 'cap_net_bind_service=+ep' /usr/local/bin/traefik
getcap /usr/local/bin/traefik
```
👉 Explication : Traefik tourne sous un compte sans droits d'administration. `setcap` accorde uniquement la capacité d'ouvrir les ports inférieurs à 1024. `getcap` confirme le réglage.

2. Ouverture du pare-feu pour le web et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH n'est autorisé que depuis le sous-réseau d'administration `192.168.10.0/24` (à adapter), avant l'activation du pare-feu. `ufw status verbose` liste les règles actives.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation de l'accès anonyme au tableau de bord :
```bash
sudo sed -i 's/insecure: true/insecure: false/' /etc/traefik/traefik.yml
sudo grep -n "insecure" /etc/traefik/traefik.yml
```
👉 Explication : Remplace `insecure: true` par `insecure: false` dans le fichier statique. Le tableau de bord n'est plus exposé sans contrôle. Il reste accessible par un routeur protégé par un middleware `basicAuth`, décrit à l'étape 2. La méthode d'exposition du tableau de bord est à vérifier sur la version déployée.

2. Génération d'un identifiant et d'un mot de passe de supervision, à stocker dans le coffre-fort du pack :
```bash
sudo apt install -y apache2-utils
htpasswd -nbB supervision "$(openssl rand -base64 24)"
```
👉 Explication : La sortie est de la forme `supervision:$2y$...`. Cette valeur hachée est collée dans `/etc/traefik/dynamic.yml` sous un middleware `basicAuth` (`users:`). Le mot de passe en clair n'est pas écrit dans le fichier : il reste dans le coffre-fort.

3. Restriction des droits sur les fichiers de configuration :
```bash
sudo chown -R root:traefik /etc/traefik
sudo chmod 750 /etc/traefik
sudo chmod 640 /etc/traefik/traefik.yml /etc/traefik/dynamic.yml
ls -l /etc/traefik
```
👉 Explication : Seul `root` modifie la configuration, et le compte `traefik` peut la lire. Les hachages d'authentification ne doivent pas être lisibles par tous.

4. Préparation du journal d'accès et contrôle :
```bash
sudo mkdir -p /var/log/traefik
sudo chown traefik /var/log/traefik
sudo tail -n 50 /var/log/traefik/access.log
```
👉 Explication : Crée le dossier de journal et l'attribue au compte `traefik`. La journalisation des accès doit être activée dans `/etc/traefik/traefik.yml` (clé `accessLog`, à vérifier sur la version déployée). Les réponses `401` répétées sur le tableau de bord doivent être remontées au responsable sécurité.

5. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/traefik-conf-$(date +%F).tgz /etc/traefik
sudo ls -l /root/traefik-conf-*.tgz
```
👉 Explication : Crée une archive datée de la configuration. Elle contient des hachages d'authentification : la stocker hors du serveur, dans le coffre-fort du pack, et la protéger en lecture.

---