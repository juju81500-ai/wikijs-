---
title: "Docker_Hote_Installation_Docker-Et-Compose"
description: "Installer le moteur officiel Docker Engine et le plugin Docker Compose v2 depuis les dépôts de l'éditeur, et sécuriser l'accès au socket local."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[docker]", "[docker-compose]", "[debian-family]", "[conteneurs]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Docker_Hote_Installation_Docker-Et-Compose.md

- **Environnement** : VM / Hôte Physique
- **OS / Version** : Debian 12 / Ubuntu 24.04 - Famille Debian
- **Catégorie** : Virtualisation & Conteneurs
- **Tags** : `[docker]`, `[docker-compose]`, `[debian-family]`, `[conteneurs]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le moteur officiel Docker Engine et le plugin Docker Compose v2 depuis les dépôts de l'éditeur, et sécuriser l'accès au socket local.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide depuis les dépôts par défaut de la distribution :
   `apt-get update && apt-get install -y docker.io docker-compose-v2`
   👉 Explication : Télécharge et installe la version pré-paquetée par la distribution pour un test immédiat.
2. Lancement d'un conteneur de test :
   `docker run --rm hello-world`
   👉 Explication : Télécharge l'image de test, l'exécute et détruit le conteneur à la fin.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation des dépendances et certificats :
   `apt-get update && apt-get install -y ca-certificates curl gnupg`
   👉 Explication : Prépare le système pour le téléchargement et la vérification des paquets sécurisés.
2. Déclaration de la source officielle du dépôt Docker :
   `apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
   👉 Explication : Installe l'ensemble de la suite officielle Docker CE et Docker Compose.
3. Activation du service système :
   `systemctl enable --now docker`
   👉 Explication : Active et démarre le moteur Docker au lancement du serveur.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Daemon Protection)
1. Restriction d'accès au groupe docker dédié :
   `groupadd -f docker && usermod -aG docker sysadmin`
   👉 Explication : Délègue l'exécution des conteneurs à l'administrateur sans recourir au compte root.
2. Hardening du démon via le fichier de configuration `/etc/docker/daemon.json` :
   `echo '{"no-new-privileges": true, "userland-proxy": false, "live-restore": true}' > /etc/docker/daemon.json`
   👉 Explication : Interdit l'élévation de privilèges dans les conteneurs, désactive le proxy utilisateur redondant et maintient les conteneurs en vie si le démon redémarre.
3. Rechargement et sécurisation du service systemd :
   `systemctl restart docker`
   👉 Explication : Applique les règles du fichier de configuration sécurisé.