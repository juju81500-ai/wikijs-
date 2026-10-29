---
title: "Fiche Simple - VM Ubuntu 26.04 Supervision Zabbix Agent2"
description: "Installer l'agent Zabbix 2 sur un serveur Ubuntu 26.04, le déclarer auprès du serveur Zabbix et restreindre l'accès au port 10050 aux seules adresses de supervision."
published: true
date: 2026-10-29T18:57:19Z
tags: ["ubuntu2604", "zabbix", "zabbix-agent2", "supervision", "port-10050"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Supervision_Zabbix_Agent2

- **Environnement** : VM ou serveur Ubuntu supervisé par un serveur Zabbix existant
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Supervision / Agent Zabbix
- **Tags** : `ubuntu2604`, `zabbix`, `zabbix-agent2`, `supervision`, `port-10050`

---

## 🎯 Problème précis à résoudre

Installer l'agent Zabbix 2 sur un serveur Ubuntu 26.04, le déclarer auprès du serveur Zabbix et restreindre l'accès au port 10050 aux seules adresses de supervision.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier la disponibilité du paquet dans les dépôts actifs :
```bash
apt-cache policy zabbix-agent2
```
👉 Explication : Si le paquet affiche une version candidate, l'installation depuis la distribution est possible. Sinon, utiliser le dépôt officiel Zabbix pour Ubuntu 26.04, en suivant la documentation Zabbix (la clé de dépôt doit être référencée par `Signed-By`, sans `apt-key`). La disponibilité du dépôt officiel pour Ubuntu 26.04 doit être vérifiée sur repo.zabbix.com au moment de l'installation, car la version de la distribution peut différer de la version LTS Zabbix utilisée.

2. Installer l'agent :
```bash
sudo apt update
sudo apt install -y zabbix-agent2
```
👉 Explication : Installe l'agent 2, qui remplace l'agent historique. Il dispose de plugins natifs pour le système, les services et les journaux.

3. Renseigner le serveur Zabbix et le nom de l'hôte dans `/etc/zabbix/zabbix_agent2.conf` :
```text
Server=<IP_SERVEUR_ZABBIX>
ServerActive=<IP_SERVEUR_ZABBIX>
Hostname=<nom_de_l_hote_zabbix>
```
👉 Explication : `Server` autorise les requêtes passives du serveur ; `ServerActive` indique où l'agent envoie ses données. `Hostname` doit correspondre exactement au nom déclaré dans l'interface Zabbix.

4. Activer et démarrer l'agent :
```bash
sudo systemctl enable --now zabbix-agent2
systemctl status zabbix-agent2 --no-pager
```
👉 Explication : Lance le service au démarrage et affiche son état. Le statut doit être `active (running)`.

5. Tester une métrique localement :
```bash
zabbix_agent2 -t system.uptime
```
👉 Explication : Exécute la clé `system.uptime` sans passer par le réseau et affiche la valeur calculée par l'agent.

## ⚡ 2. Production — Façon Simplifiée

1. Ouvrir le port 10050/TCP uniquement vers le serveur Zabbix :
```bash
sudo ufw allow from <IP_SERVEUR_ZABBIX> to any port 10050 proto tcp
```
👉 Explication : Autorise le serveur Zabbix à interroger l'agent et refuse les autres sources (la politique UFW par défaut refuse déjà le trafic entrant).

2. Tester depuis le serveur Zabbix :
```bash
zabbix_get -s <IP_SERVEUR> -k agent.ping
```
👉 Explication : Doit répondre `1`. Cette commande s'exécute sur le serveur Zabbix et nécessite le paquet `zabbix-get`.

## 🔒 3. Production — Façon Sécurisée

1. Activer le chiffrement TLS entre l'agent et le serveur uniquement si la politique le demande. Vérifier d'abord les paramètres de certificats dans `/etc/zabbix/zabbix_agent2.conf` (`TLSConnect`, `TLSAccept`), puis la configuration PSK ou certificat.
👉 Explication : Sans TLS, les données de supervision transitent en clair ; le choix PSK ou certificat dépend du parc et doit être documenté.

2. Limiter les clés accessibles à distance dans `zabbix_agent2.conf` :
```text
DenyKey=system.run[*]
```
👉 Explication : `system.run` permet d'exécuter des commandes sur la machine depuis le serveur Zabbix. Le refuser évite qu'un serveur Zabbix compromis prenne le contrôle de l'hôte. Ne lever ce blocage que pour un contrôle précis, avec une clé `AllowKey` nominative placée avant la règle générique.

3. Vérifier que la configuration est valide et que le service a rechargé ses paramètres :
```bash
sudo systemctl restart zabbix-agent2
sudo ss -tlnp | grep 10050
```
👉 Explication : Le port 10050 doit écouter sur l'interface de supervision, et non sur toutes les interfaces si le serveur en possède plusieurs (paramètre `ListenIP`).

## ✅ Validation et retour arrière

- **Précontrôles** : nom d'hôte identique dans Zabbix, port 10050 autorisé depuis le serveur, version de l'agent compatible avec le serveur Zabbix.
- **Validation** : `zabbix_get -s <IP_SERVEUR> -k agent.ping` renvoie `1` ; l'hôte passe à l'état disponible dans l'interface Zabbix.
- **Retour arrière** : `sudo systemctl disable --now zabbix-agent2` ; `sudo ufw delete allow from <IP_SERVEUR_ZABBIX> to any port 10050 proto tcp`.