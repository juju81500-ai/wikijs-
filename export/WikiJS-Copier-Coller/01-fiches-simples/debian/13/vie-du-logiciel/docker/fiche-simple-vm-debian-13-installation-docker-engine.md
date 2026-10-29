# 📄 VM_Debian_13_Services_Installation-Docker-Engine.md

- **Environnement** : VM (Debian 13 Trixie / Kernel 6.x)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Conteneurs & Virtualisation / Docker Engine

## 🎯 Problème précis à résoudre
Installer le moteur Docker Engine officiel, le plugin Docker Compose v2 et containerd sur Debian 13 (Trixie), configurer le démarrage automatique et sécuriser le socket Unix.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide de Docker depuis les dépôts Debian natifs :
   `apt-get update && apt-get install -y docker.io docker-compose-v2`
   👉 Explication : Télécharge et installe les paquets de conteneurisation du projet Debian.

2. Vérification de l'exécution du moteur :
   `docker run --rm alpine echo "Docker fonctionnel"`
   👉 Explication : Exécute un conteneur temporaire Alpine pour valider le fonctionnement du démon.

---

## ⚡ 2. Production — Façon Simplifiée
1. Installation des dépendances et préparation des clés de sécurité :
   `apt-get update && apt-get install -y ca-certificates gnupg`
   👉 Explication : Installe les outils nécessaires à la validation des certificats et des signatures GPG.

2. Configuration de la clé GPG et du dépôt officiel Docker pour Debian 13 :
   `install -m 0755 -d /etc/apt/keyrings && apt-get update`
   👉 Explication : Prépare l'arborescence des clés APT sécurisées pour le dépôt Docker officiel Trixie.

3. Installation de la suite Docker Engine complète :
   `apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin`
   👉 Explication : Installe le moteur complet Docker Engine et ses composants officiels.

4. Activation et démarrage des services au boot :
   `systemctl enable --now docker containerd`
   👉 Explication : S'assure que les démons Docker et containerd démarrent automatiquement au boot.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création du groupe restreint docker et ajout d'un utilisateur nommé :
   `groupadd -f docker && usermod -aG docker user_tssr`
   👉 Explication : Permet à l'administrateur d'exécuter des commandes Docker sans privilèges root directs.

2. Hardening du démon Docker via `/etc/docker/daemon.json` :
   {
     "icc": false,
     "no-new-privileges": true,
     "userland-proxy": false,
     "live-restore": true
   }
   👉 Explication : Interdit l'élévation de privilèges, désactive le proxy utilisateur et sécurise les échanges réseau inter-conteneurs.

3. Rechargement du démon Docker :
   `systemctl reload docker`
   👉 Explication : Applique la configuration de sécurité sur le démon actif sans couper les conteneurs.

4. Verrouillage des permissions du fichier de configuration :
   `chmod 600 /etc/docker/daemon.json && chown root:root /etc/docker/daemon.json`
   👉 Explication : Empêche la modification du fichier de sécurité par d'autres utilisateurs du système.