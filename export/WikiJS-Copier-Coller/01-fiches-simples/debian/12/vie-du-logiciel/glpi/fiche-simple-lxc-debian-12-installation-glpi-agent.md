# 📄 LXC_Debian_12_Services_Installation-GLPI-Agent.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Services & Automatisation

## 🎯 Problème précis à résoudre
Installer, configurer et sécuriser l'agent officiel GLPI (`glpi-agent`) sur un conteneur LXC Debian 12 pour remonter l'inventaire matériel et logiciel vers le serveur GLPI central.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Téléchargement et exécution du script d'inventaire ponctuel :
   `apt-get update && apt-get install -y glpi-agent`
   👉 Explication : Installe le paquet officiel glpi-agent directement depuis les dépôts Debian.
2. Lancement d'un inventaire immédiat en mode verbeux imprimé sur la console :
   `glpi-agent --stdout`
   👉 Explication : Exécute l'inventaire complet du conteneur sans envoyer de données au serveur pour vérifier la détection des composants.

---

## ⚡ 2. Production — Façon Simplifiée
1. Configuration de l'URL du serveur GLPI central dans le fichier officiel :
   `sed -i 's|^#server =.*|server = http://glpi.lab.local/market/front/inventory.php|' /etc/glpi-agent/agent.cfg`
   👉 Explication : Spécifie l'adresse de l'endpoint d'inventaire GLPI auquel l'agent doit transmettre son rapport JSON/XML.
2. Déclenchement manuel de la première remontée d'inventaire :
   `glpi-agent --force`
   👉 Explication : Force l'envoi immédiat de la fiche d'inventaire au serveur GLPI sans attendre le délai planifié.
3. Activation et démarrage du service d'arrière-plan :
   `systemctl enable --now glpi-agent`
   👉 Explication : Garantit que l'agent s'exécute en démon et remonte périodiquement les modifications d'état.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Configuration du canal chiffré HTTPS et vérification du certificat SSL/TLS :
   `sed -i 's|^#server =.*|server = https://glpi.lab.local/market/front/inventory.php|' /etc/glpi-agent/agent.cfg && sed -i 's|^#no-ssl-check =.*|no-ssl-check = 0|' /etc/glpi-agent/agent.cfg && sed -i 's|^#ssl-cert-file =.*|ssl-cert-file = /etc/ssl/certs/ca-certificates.crt|' /etc/glpi-agent/agent.cfg`
   👉 Explication : Impose l'authentification SSL/TLS stricte du serveur GLPI et rejette les certificats auto-signés non approuvés.
2. Restriction des permissions du fichier de configuration aux seuls utilisateurs privilégiés :
   `chmod 600 /etc/glpi-agent/agent.cfg && chown root:root /etc/glpi-agent/agent.cfg`
   👉 Explication : Empêche la lecture des identifiants et jetons d'authentification GLPI par des utilisateurs non autorisés.
3. Confinement du service via un override systemd (NoNewPrivileges & PrivateTmp) :
   `mkdir -p /etc/systemd/system/glpi-agent.service.d/ && echo -e "[Service]\nNoNewPrivileges=true\nPrivateTmp=true" > /etc/systemd/system/glpi-agent.service.d/override.conf && systemctl daemon-reload`
   👉 Explication : Restreint les capacités du démon systemd pour empêcher toute élévation de privilèges en cas de vulnérabilité.