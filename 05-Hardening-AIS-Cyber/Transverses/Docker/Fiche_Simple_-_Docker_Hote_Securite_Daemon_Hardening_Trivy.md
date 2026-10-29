# 📄 Fiche Simple : Sécurisation & Hardening Hôte Docker

- **Environnement** : Hôte Docker / VM
- **OS / Version** : Debian 13 / Ubuntu 24.04 LTS
- **Catégorie** : Sécurité & Hardening
- **Tags** : `docker`, `hardening`, `trivy`, `security` 

---

## 🎯 Problème précis à résoudre
Installer le moteur Docker Engine, sécuriser la configuration du démon (/etc/docker/daemon.json), restreindre le socket Unix et auditer les conteneurs contre les vulnérabilités CVE avec Trivy.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation rapide de Docker Engine :
   apt-get update && apt-get install -y docker.io
   👉 Explication : Installe le paquet Docker de la distribution pour les tests rapides.
2. Vérification de la version :
   docker --version
   👉 Explication : Valide que le moteur Docker est fonctionnel.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajout du dépôt officiel Docker et installation :
   apt-get update && apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
   👉 Explication : Déploie les binaires officiels maintenus par Docker Inc.
2. Activation du service au démarrage :
   systemctl enable --now docker
   👉 Explication : Garantit le lancement automatique du démon Docker lors du boot.

---

## 🔒 3. Production — Façon Sécurisée (Hardening)
1. Hardening du démon via `/etc/docker/daemon.json` :
   cat << 'EOF' > /etc/docker/daemon.json
   {
     "icc": false,
     "userland-proxy": false,
   "log-driver": "local",
     "log-opts": {"max-size": "10m", "max-file": "3"}
   }
   EOF
   👉 Explication : `icc=false` peut casser certaines communications entre conteneurs ; tester les réseaux Compose avant de l'activer. Appliquer `no-new-privileges` par conteneur dans Compose, pas au niveau du démon.
2. Valider le fichier puis appliquer pendant une fenêtre de maintenance, car le redémarrage du démon peut interrompre les conteneurs :
   ```bash
   sudo dockerd --validate --config-file=/etc/docker/daemon.json
   sudo chmod 600 /etc/docker/daemon.json
   sudo systemctl restart docker
   docker ps
   ```
   👉 Explication : Vérifier la disponibilité des applications après redémarrage. `icc=false` peut casser certaines communications entre conteneurs ; tester les réseaux Compose avant de l'activer.
3. Auditer l'image avec la CLI Trivy installée depuis sa source officielle et à jour, sans monter le socket Docker dans un conteneur scanner :
   ```bash
   trivy image --severity HIGH,CRITICAL nginx:<VERSION_VALIDEE>
   ```
   👉 Explication : Remplacer le tag par la version réellement déployée. Le socket Docker accorde un contrôle privilégié sur l'hôte ; intégrer l'audit au pipeline CI et bloquer selon une politique documentée.