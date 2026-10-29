# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Supervision_Zabbix_Agent.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Supervision / Métriques et inventaire

## 🎯 Problème précis à résoudre
Installer l'agent Zabbix sur un conteneur Alpine Linux, le déclarer auprès du serveur de supervision et limiter les connexions entrantes au seul serveur Zabbix.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer l'agent depuis le dépôt `community` :
   ```sh
   apk update
   apk add zabbix-agent
   ```
   👉 Explication : Le paquet installe l'agent et son service OpenRC. Vérifier que le dépôt `community` est activé dans `/etc/apk/repositories`.

2. Lister les fichiers installés pour repérer le fichier de configuration et le script de service :
   ```sh
   apk info -L zabbix-agent | grep -E 'conf|init.d|bin/'
   ls /etc/init.d | grep zabbix
   ```
   👉 Explication : Les chemins réels dépendent du paquet installé. Les utiliser à la place de chemins supposés, et reprendre le chemin du fichier `.conf` dans les étapes suivantes.

3. Tester la configuration locale sans démarrer le service :
   ```sh
   zabbix_agentd -c <fichier_conf> -t agent.ping
   ```
   👉 Explication : L'option `-t` évalue un élément de supervision localement et affiche sa valeur. `agent.ping` doit renvoyer `1`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Renseigner les directives de communication dans le fichier de configuration :
   ```text
   Server=<ip_serveur_zabbix>
   ServerActive=<ip_serveur_zabbix>
   Hostname=<nom_du_conteneur>
   ```
   👉 Explication : `Server` autorise les requêtes passives, `ServerActive` les contrôles actifs. `Hostname` doit correspondre exactement au nom de l'hôte déclaré dans l'interface Zabbix.

2. Activer et démarrer le service OpenRC :
   ```sh
   rc-update add <nom_du_service_zabbix> default
   rc-service <nom_du_service_zabbix> restart
   rc-service <nom_du_service_zabbix> status
   ```
   👉 Explication : Remplacer `<nom_du_service_zabbix>` par le nom trouvé dans `/etc/init.d/` à l'étape 2 de laboratoire.

3. Autoriser le port TCP 10050 uniquement depuis le serveur Zabbix, par le pare-feu Proxmox du conteneur ou par Awall si la VM le prend en charge :
   ```sh
   ss -lntp | grep 10050
   ```
   👉 Explication : L'agent doit écouter sur le port `10050`. Le filtrage doit ensuite n'admettre que `<ip_serveur_zabbix>`.

---

## 🔒 3. Production — Façon Sécurisée
1. Vérifier que les commandes distantes restent désactivées et que les sources sont limitées :
   ```sh
   grep -E '^(EnableRemoteCommands|Server|ServerActive|Hostname)=' <fichier_conf>
   ```
   👉 Explication : `EnableRemoteCommands=0` empêche le serveur d'exécuter des commandes shell sur le conteneur. Les valeurs `Server` et `ServerActive` ne doivent contenir que l'adresse du serveur Zabbix.

2. Ne pas exposer le port 10050 à Internet ni à des réseaux clients, et consigner le conteneur dans l'inventaire (étape 49 du cycle de vie).