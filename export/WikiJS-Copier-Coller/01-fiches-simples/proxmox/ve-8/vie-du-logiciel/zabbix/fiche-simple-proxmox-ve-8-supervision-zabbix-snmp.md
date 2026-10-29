# 📄 Fiche_Simple_-_Proxmox_VE_8_Supervision_Zabbix_Snmp.md

- **Environnement** : Hyperviseur Proxmox VE 8 supervisé par un serveur Zabbix (agent) ou par un poller SNMP
- **OS / Version** : Proxmox VE 8.x - Debian 12 Bookworm
- **Catégorie** : Supervision / Métriques et inventaire

---

## 🎯 Problème précis à résoudre
Superviser l'état de l'hyperviseur Proxmox VE 8 (charge, mémoire, disques, services) depuis un serveur Zabbix, avec l'agent Zabbix en premier choix et SNMPv3 en alternative sécurisée.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer l'agent Zabbix depuis les dépôts Debian :
```bash
apt update && apt install -y zabbix-agent
```
👉 Explication : installe l'agent classique fourni par Debian 12 ; `zabbix_agentd -V` affiche la version installée.

2. Renseigner le serveur Zabbix et le nom d'hôte de l'agent :
```bash
sed -i -e 's/^Server=.*/Server=<ip_serveur_zabbix>/' -e 's/^ServerActive=.*/ServerActive=<ip_serveur_zabbix>/' -e 's/^Hostname=.*/Hostname=<nom_de_l_hote>/' /etc/zabbix/zabbix_agentd.conf
grep -E '^(Server|ServerActive|Hostname)=' /etc/zabbix/zabbix_agentd.conf
```
👉 Explication : `Server` autorise le serveur Zabbix à interroger l'agent, `ServerActive` définit le serveur des contrôles actifs, `Hostname` doit être identique au nom de l'hôte déclaré dans l'interface Zabbix. Si `Hostname` n'apparaît pas dans le résultat, décommenter la ligne correspondante dans le fichier.

3. Activer et démarrer l'agent :
```bash
systemctl enable zabbix-agent
systemctl restart zabbix-agent
```
👉 Explication : `enable` active le démarrage automatique au boot ; `restart` applique la nouvelle configuration immédiatement.

4. Tester une clé de supervision localement :
```bash
zabbix_agentd -t system.cpu.load[all,avg1]
```
👉 Explication : exécute la clé `system.cpu.load` sans passer par le serveur et affiche la valeur de charge moyenne sur 1 minute, ce qui valide le fonctionnement de l'agent.

---

## ⚡ 2. Production — Façon Simplifiée
1. Autoriser le port 10050 uniquement depuis le serveur Zabbix :
```bash
pvesh create /cluster/firewall/rules --type in --action ACCEPT --proto tcp --dport 10050 --source <ip_serveur_zabbix> --enable 1 --comment "Zabbix agent"
```
👉 Explication : ouvre l'agent Zabbix (TCP/10050) au seul serveur de supervision, en complément du pare-feu datacenter.

2. Déclarer l'hôte dans l'interface Zabbix avec le modèle « Linux by Zabbix agent » (action dans l'interface web Zabbix, nom d'hôte identique à `Hostname`), puis valider depuis le serveur Zabbix :
```bash
zabbix_get -s <nom_de_l_hote> -k agent.ping
```
👉 Explication : `zabbix_get` (paquet `zabbix-get` sur le serveur) interroge l'agent distant ; la réponse `1` confirme la communication.

3. Contrôler les journaux de l'agent :
```bash
journalctl -u zabbix-agent -n 50 --no-pager
```
👉 Explication : affiche les 50 dernières lignes du service ; aucune erreur de connexion au serveur ni de paramètre invalide ne doit apparaître.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Installer le démon SNMP et créer un utilisateur SNMPv3 en lecture seule :
```bash
apt install -y snmpd
net-snmp-create-v3-user -ro -A <mot_de_passe_auth> -a SHA -X <mot_de_passe_priv> -x AES <utilisateur_snmp>
```
👉 Explication : SNMPv3 avec authentification SHA et chiffrement AES remplace la communauté SNMPv2c en clair ; l'utilisateur n'a qu'un droit de lecture. Utiliser des mots de passe distincts et de plus de 12 caractères.

2. Restreindre le port SNMP au serveur de supervision :
```bash
pvesh create /cluster/firewall/rules --type in --action ACCEPT --proto udp --dport 161 --source <ip_serveur_zabbix> --enable 1 --comment "SNMP lecture supervision"
```
👉 Explication : seul le serveur de supervision peut interroger le port UDP/161 de l'hôte ; toute autre source reste bloquée par la politique du pare-feu.

3. Redémarrer snmpd puis tester une requête SNMPv3 :
```bash
systemctl restart snmpd
snmpwalk -v3 -l authPriv -u <utilisateur_snmp> -a SHA -A <mot_de_passe_auth> -x AES -X <mot_de_passe_priv> <ip_hote> sysName.0
```
👉 Explication : relance le démon avec le nouvel utilisateur ; `snmpwalk` depuis le serveur de supervision doit renvoyer le nom d'hôte, ce qui confirme l'authentification et le chiffrement.