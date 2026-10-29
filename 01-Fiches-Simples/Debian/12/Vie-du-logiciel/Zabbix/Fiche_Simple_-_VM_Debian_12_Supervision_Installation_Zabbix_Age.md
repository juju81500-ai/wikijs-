# 📄 VM_Debian_12_Supervision_Installation-Zabbix-Agent.md

- **Environnement** : VM (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Supervision / Zabbix Agent 2
- **Tags** : `[debian12]`, `[zabbix]`, `[zabbix-agent2]`, `[supervision]`, `[monitoring]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer l'agent de supervision Zabbix Agent 2 sur Debian 12 à partir des dépôts officiels Zabbix, le connecter au serveur de supervision central et restreindre la communication via chiffrement PSK.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet zabbix-agent standard depuis les dépôts Debian :
   `apt-get update && apt-get install -y zabbix-agent`
   👉 Explication : Installe la version de base de l'agent Zabbix.

2. Configuration rapide du serveur Zabbix autorisé dans `/etc/zabbix/zabbix_agentd.conf` :
   `sed -i 's/Server=127.0.0.1/Server=192.168.1.100/' /etc/zabbix/zabbix_agentd.conf && systemctl restart zabbix-agent`
   👉 Explication : Déclare l'adresse IP du serveur Zabbix central pour autoriser la collecte de métriques.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajout du dépôt officiel Zabbix pour Debian 12 :
   `dpkg -i zabbix-release.deb && apt-get update`
   👉 Explication : Configure les canaux officiels de l'éditeur Zabbix pour bénéficier des fonctionnalités récentes.

2. Installation de Zabbix Agent 2 :
   `apt-get install -y zabbix-agent2`
   👉 Explication : Installe le nouvel agent moderne capable de superviser nativement les conteneurs et bases de données.

3. Configuration des paramètres hôte dans `/etc/zabbix/zabbix_agent2.conf` :
   `sed -i 's/Server=127.0.0.1/Server=192.168.1.100/' /etc/zabbix/zabbix_agent2.conf && systemctl enable --now zabbix-agent2`
   👉 Explication : Définit l'IP du serveur central et active le service au boot.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Générer une clé aléatoire avec un outil approuvé, la déposer dans un fichier protégé lisible uniquement par le compte de service et la conserver dans un coffre sécurisé. Ne jamais coller la clé dans une commande enregistrée ou dans la fiche.

2. Configurer dans `/etc/zabbix/zabbix_agent2.conf` les paramètres nécessaires au mode choisi (passif, actif ou les deux) : `TLSAccept=psk`, `TLSConnect=psk`, `TLSPSKIdentity=<IDENTITE>` et `TLSPSKFile=/etc/zabbix/zabbix_agent2.psk`. Sauvegarder le fichier et vérifier la syntaxe selon la version installée avant redémarrage.
   👉 Explication : L'identité et la clé doivent aussi être configurées côté hôte Zabbix. PSK chiffre le transport, mais la distribution/rotation de la clé reste à gérer.

3. Interdiction de l'exécution de commandes système à distance :
   `echo "DenyKey=system.run[*]" >> /etc/zabbix/zabbix_agent2.conf`
   👉 Explication : Interdit au serveur Zabbix d'exécuter des commandes Shell arbitraires sur la machine cliente.

4. Si l'agent accepte des connexions passives, autoriser TCP/10050 uniquement depuis le serveur Zabbix dans le pare-feu persistant géré par l'hôte. Pour un agent actif uniquement, ne pas ouvrir de port entrant inutile. Ne pas utiliser `nft add rule` seul comme règle permanente.