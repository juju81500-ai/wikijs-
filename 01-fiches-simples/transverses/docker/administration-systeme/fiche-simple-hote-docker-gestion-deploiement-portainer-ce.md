# 📄 Docker_Conteneur_Gestion_Deploiement-Portainer-CE.md

- **Environnement** : Docker (Hôte Docker)
- **OS / Version** : Tout OS avec Docker Engine - Famille Multi-OS
- **Catégorie** : Supervision & Administration Web
- **Tags** : `[docker]`, `[portainer]`, `[conteneurs]`, `[webui]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer l'interface Web d'administration Portainer CE (Community Edition) via un conteneur Docker isolé avec persistance des données et sécurisation TLS.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. En lab isolé, lancer une version validée avec l'interface HTTPS limitée à loopback :
   `docker run -d -p 127.0.0.1:9443:9443 --name portainer-lab --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock -v portainer_lab_data:/data portainer/portainer-ce:<VERSION_VALIDEE>`
   👉 Explication : Le socket Docker donne à Portainer des privilèges équivalents à root sur l'hôte. Ne déployer que sur un hôte d'administration isolé et ne pas publier l'interface sans VPN/proxy authentifié.
2. Vérification de l'état du conteneur :
   `docker ps`
   👉 Explication : Vérifie que le conteneur tourne correctement.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un volume Docker dédié pour la persistance des données :
   `docker volume create portainer_data`
   👉 Explication : Garantit que les utilisateurs, paramètres et configurations Portainer survivent aux mises à jour du conteneur.
2. Déploiement propre avec port HTTPS sécurisé (9443) :
   `docker run -d -p 127.0.0.1:9443:9443 --name portainer --restart=unless-stopped -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:<VERSION_VALIDEE>`
   👉 Explication : Remplacer le tag par une version supportée et testée. Le port 8000 n'est nécessaire que pour l'agent Edge ; ne pas l'ouvrir par défaut.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Socket Protection)
1. Créer une pile Compose avec version épinglée, volume de données et publication limitée à loopback. Garder l'accès au socket Docker uniquement sur un hôte dédié :
   `docker compose config`
   👉 Explication : `docker compose config` valide la pile. Un montage `:ro` du socket n'est pas une barrière d'autorisation à l'API Docker.
2. Lancement de la pile sécurisée avec montage restreint :
   `docker compose up -d`
   👉 Explication : Lance le service Portainer en arrière-plan avec isolation et redémarrage automatique en cas de panne.
3. Vérification de la réponse HTTPS, activation du MFA et suppression de l'accès initial non nécessaire :
   `docker logs portainer`
   👉 Explication : Inspecte les journaux d'initialisation pour valider la première connexion administrateur HTTPS.