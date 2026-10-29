---
title: "Apache Guacamole"
description: "Déployer Apache Guacamole en Docker Compose sur Debian 13 avec ses trois conteneurs (guacd, PostgreSQL, interface web), vérifier l'accès au portail, remplacer le compte administrateur par défaut, puis restreindre l'exposition réseau et la sauvegarde de la base."
published: true
date: 2026-10-29T11:49:54Z
tags: ["[debian13]", "[debian-family]", "[guacamole]", "[docker]", "[docker-compose]", "[rdp]", "[ssh]", "[vnc]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T11:49:54Z
dateModified: 2026-10-29T11:49:54Z
---

# 📄 Apache Guacamole

- **Environnement** : VM Debian 13 avec Docker Compose (passerelle d'accès distant RDP, SSH et VNC depuis un navigateur)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian / Apache Guacamole (version fixée par le tag d'image Docker `<version_guacamole>`, à vérifier sur la version déployée)
- **Catégorie** : Poste de travail et VDI
- **Tags** : `[debian13]`, `[debian-family]`, `[guacamole]`, `[docker]`, `[docker-compose]`, `[rdp]`, `[ssh]`, `[vnc]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer Apache Guacamole en Docker Compose sur Debian 13 avec ses trois conteneurs (`guacd`, PostgreSQL, interface web), vérifier l'accès au portail, remplacer le compte administrateur par défaut, puis restreindre l'exposition réseau et la sauvegarde de la base.

Valeurs à personnaliser dans les fichiers et commandes : `<version_guacamole>` (tag d'image Guacamole, identique pour `guacd` et `guacamole`), `<version_postgresql>` (version PostgreSQL compatible avec Guacamole), `<mot_de_passe_bdd>` (mot de passe fort de la base), `<adresse_ip_serveur>` (adresse IP de la VM), `<reseau_admin>` (sous-réseau d'administration au format CIDR).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Docker et de Docker Compose :
   ```bash
   sudo apt update && sudo apt install -y docker.io docker-compose
   ```
   👉 Explication : Installe le moteur Docker et l'outil Compose depuis les dépôts Debian 13. Paquets à vérifier sur la version déployée (la commande `docker-compose version` doit répondre).

2. Démarrage et activation automatique de Docker au démarrage de la VM :
   ```bash
   sudo systemctl enable --now docker
   ```
   👉 Explication : Lance le service Docker maintenant et à chaque redémarrage de la VM.

3. Création du répertoire de travail et du dossier d'initialisation de la base :
   ```bash
   mkdir -p ~/guacamole/initdb
   ```
   👉 Explication : Regroupe le fichier Compose, le script SQL et les données PostgreSQL dans un seul dossier.

4. Génération du script SQL d'initialisation de la base Guacamole :
   ```bash
   docker run --rm guacamole/guacamole:<version_guacamole> /opt/guacamole/bin/initdb.sh --postgresql > ~/guacamole/initdb/01-initdb.sql
   ```
   👉 Explication : Demande à l'image Guacamole de produire le schéma PostgreSQL. Le script `01-initdb.sql` est lu une seule fois, à la première création de la base. Option `--postgresql` à vérifier sur la version déployée.

5. Création du fichier `~/guacamole/docker-compose.yml` :
   ```yaml
   services:
     guacd:
       image: guacamole/guacd:<version_guacamole>
       restart: unless-stopped

     postgres:
       image: postgres:<version_postgresql>
       restart: unless-stopped
       environment:
         POSTGRES_DB: guacamole_db
         POSTGRES_USER: guacamole_user
         POSTGRES_PASSWORD: <mot_de_passe_bdd>
       volumes:
         - ./initdb:/docker-entrypoint-initdb.d:ro
         - ./pgdata:/var/lib/postgresql/data

     guacamole:
       image: guacamole/guacamole:<version_guacamole>
       restart: unless-stopped
       depends_on:
         - guacd
         - postgres
       environment:
         GUACD_HOSTNAME: guacd
         POSTGRESQL_HOSTNAME: postgres
         POSTGRESQL_DATABASE: guacamole_db
         POSTGRESQL_USER: guacamole_user
         POSTGRESQL_PASSWORD: <mot_de_passe_bdd>
       ports:
         - "8080:8080"
   ```
   👉 Explication : `guacd` traite les protocoles distants, `postgres` stocke les comptes et connexions, `guacamole` fournit le portail web sur le port 8080. Remplacer `<version_guacamole>`, `<version_postgresql>` et `<mot_de_passe_bdd>` (le même mot de passe dans les deux services). Noms de variables d'environnement à vérifier sur la version déployée.

6. Démarrage de la pile :
   ```bash
   cd ~/guacamole && docker-compose up -d
   ```
   👉 Explication : Télécharge les images si nécessaire et lance les trois conteneurs en arrière-plan.

7. Contrôle de l'état des conteneurs :
   ```bash
   docker-compose ps
   ```
   👉 Explication : Les services `guacd`, `postgres` et `guacamole` doivent être à l'état `Up`. Un redémarrage en boucle indique souvent un mot de passe ou un script SQL incorrect.

8. Test d'accès au portail :
   ```bash
   curl -I http://localhost:8080/guacamole/
   ```
   👉 Explication : Doit renvoyer `HTTP/1.1 200` ou une redirection `302`. Ensuite, ouvrir `http://<adresse_ip_serveur>:8080/guacamole/` depuis un poste de test.

---

## ⚡ 2. Production — Façon Simplifiée
1. Connexion initiale avec le compte par défaut, puis changement immédiat du mot de passe :
   ```text
   http://<adresse_ip_serveur>:8080/guacamole/
   ```
   Identifiant par défaut : `guacadmin` ; mot de passe par défaut : `guacadmin`.
   👉 Explication : Le compte `guacadmin` est connu de tous les installateurs. Dans **Paramètres** > **Utilisateurs**, modifier son mot de passe immédiatement, puis créer un compte administrateur nominatif.

2. Création d'une première connexion de test (RDP ou SSH) depuis l'interface : **Paramètres** > **Connexions** > **Nouvelle connexion**.
   👉 Explication : Valide la chaîne complète `navigateur` > `guacamole` > `guacd` > cible. Renseigner le nom de la connexion, le protocole, `<adresse_ip_serveur_cible>` (adresse de la machine à atteindre) et les identifiants du compte cible.

3. Sauvegarde de la base PostgreSQL :
   ```bash
   cd ~/guacamole && docker-compose exec -T postgres pg_dump -U guacamole_user guacamole_db > ~/guacamole/sauvegarde-guacamole.sql
   ```
   👉 Explication : Exporte la base (comptes, connexions, droits) dans un fichier SQL. Ce fichier contient des données sensibles : le protéger comme un secret.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Limitation de la publication du port au poste local, l'accès externe passant par un reverse proxy HTTPS :
   ```yaml
       ports:
         - "127.0.0.1:8080:8080"
   ```
   Appliquer ensuite la modification du fichier `~/guacamole/docker-compose.yml` puis :
   ```bash
   cd ~/guacamole && docker-compose up -d
   ```
   👉 Explication : Le portail n'écoute plus sur toutes les interfaces. Le reverse proxy HTTPS (nginx, Apache ou équivalent, hors périmètre de cette fiche) doit être configuré pour exposer le service en TLS.

2. Pare-feu local : n'autoriser que le réseau d'administration sur SSH et HTTPS, puis activer le pare-feu. Garder une console ouverte avant ces commandes :
   ```bash
   sudo apt install -y ufw && sudo ufw allow from <reseau_admin> to any port 22 proto tcp && sudo ufw allow from <reseau_admin> to any port 443 proto tcp && sudo ufw default deny incoming && sudo ufw enable
   ```
   👉 Explication : La règle SSH est posée avant l'activation pour éviter de se couper l'accès. `<reseau_admin>` est le sous-réseau d'administration au format CIDR (exemple : `192.168.10.0/24`). Vérifier l'interaction entre UFW et Docker sur la version déployée.

3. Vérification de la liste des règles appliquées :
   ```bash
   sudo ufw status verbose
   ```
   👉 Explication : Contrôle en lecture seule que seuls les ports prévus sont autorisés et que la politique par défaut est `deny (incoming)`.

4. Sauvegarde : restriction des droits sur le fichier exporté :
   ```bash
   chmod 600 ~/guacamole/sauvegarde-guacamole.sql
   ```
   👉 Explication : Restreint la lecture du fichier de sauvegarde au seul propriétaire. Le transférer ensuite vers un stockage approuvé et chiffré, jamais dans un dépôt de code.