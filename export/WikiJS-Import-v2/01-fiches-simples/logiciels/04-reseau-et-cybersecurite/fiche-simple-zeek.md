---
title: "Zeek"
description: "Installer Zeek 8.0 LTS en capteur passif standalone sur une interface miroir autorisée, le déployer avec ZeekControl et vérifier la production de journaux (conn.log). Zeek ne bloque pas le trafic et ne remplace pas un IDS à signatures. Les tests ne se font que sur votre propre réseau de laboratoire."
published: true
date: 2026-10-29T12:23:32Z
tags: ["[debian-12]", "[zeek]", "[network-monitoring]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:23:32Z
dateModified: 2026-10-29T12:23:32Z
---

# 📄 Zeek

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Zeek 8.0 LTS depuis le dépôt OBS `security:zeek` (répertoire `Debian_12`, à vérifier : présence du paquet `zeek-8.0` pour bookworm)
- **Catégorie** : Réseau et cybersécurité
- **Tags** : `[debian-12]`, `[zeek]`, `[network-monitoring]`, `[hardening]`

## 🎯 Objectif
Installer Zeek 8.0 LTS en capteur passif standalone sur une interface miroir autorisée, le déployer avec ZeekControl et vérifier la production de journaux (`conn.log`). Zeek ne bloque pas le trafic et ne remplace pas un IDS à signatures. Les tests ne se font que sur votre propre réseau de laboratoire.

---

## 🧪 1. Hors-Production (laboratoire)
1. Ajout du dépôt officiel Zeek pour Debian 12 :
```bash
sudo apt update
sudo apt install -y ca-certificates curl gnupg libcap2-bin
sudo install -d -m 0755 /etc/apt/keyrings
curl -fsSL https://download.opensuse.org/repositories/security:/zeek/Debian_12/Release.key | sudo gpg --dearmor --yes -o /etc/apt/keyrings/zeek-obs.gpg
echo 'deb [signed-by=/etc/apt/keyrings/zeek-obs.gpg] https://download.opensuse.org/repositories/security:/zeek/Debian_12/ /' | sudo tee /etc/apt/sources.list.d/zeek-obs.list
sudo apt update
apt-cache policy zeek-8.0
```
👉 Explication : Importe la clé du dépôt OBS dans un trousseau dédié et déclare la source APT associée. `apt-cache policy` doit montrer un candidat provenant de `security:zeek`. Si le paquet n'existe pas pour `Debian_12`, le signaler : cette fiche ne prévoit pas de compilation manuelle.

2. Installation et vérification du binaire :
```bash
sudo apt install -y zeek-8.0
/opt/zeek/bin/zeek --version
/opt/zeek/bin/zeekctl --help
```
👉 Explication : Les paquets OBS installent Zeek sous `/opt/zeek` (chemin habituel, à confirmer avec `dpkg-query -L zeek-8.0`). `zeek --version` affiche la version réelle à reporter dans les métadonnées.

3. Configuration du nœud standalone sur l'interface miroir :
```bash
ip -br address
sudo cp -a /opt/zeek/etc/node.cfg /opt/zeek/etc/node.cfg.pre-lab
sudo nano /opt/zeek/etc/node.cfg
```
Dans le fichier, garder un seul nœud standalone :
```ini
[zeek]
type=standalone
host=localhost
interface=ens33
```
👉 Explication : `ens33` est un exemple, à remplacer par l'interface miroir autorisée, distincte de l'interface de gestion. Une interface reliée à un commutateur ordinaire ne voit que le trafic de la VM.

4. Vérification puis déploiement :
```bash
sudo /opt/zeek/bin/zeekctl check
sudo /opt/zeek/bin/zeekctl deploy
sudo /opt/zeek/bin/zeekctl status
```
👉 Explication : `check` valide la configuration avant tout démarrage. `deploy` installe et lance le nœud. `status` doit indiquer le nœud `zeek` en état `running`.

5. Génération de trafic et contrôle des journaux :
```bash
ping -c 3 192.168.10.20
sudo ls -lah /opt/zeek/logs/current
sudo head -n 12 /opt/zeek/logs/current/conn.log
```
👉 Explication : L'adresse `192.168.10.20` est un exemple interne. Le fichier `conn.log` doit apparaître et contenir des lignes de connexion (format TSV, en-têtes en tête de fichier).

6. Essai hors ligne sur une capture de laboratoire obtenue légalement :
```bash
sudo install -d -m 0700 /var/tmp/zeek-lab
cd /var/tmp/zeek-lab && sudo /opt/zeek/bin/zeek -C -r /var/tmp/zeek-lab/capture-lab.pcap
```
👉 Explication : Zeek lit le fichier PCAP et écrit les journaux dans le répertoire courant, sans surveiller d'interface. Le fichier `capture-lab.pcap` doit provenir d'un test autorisé. Son existence est supposée ; à créer ou copier avant l'essai.

---

## ⚡ 2. Production — Façon Simplifiée
1. Déclaration des réseaux internes suivis :
```bash
sudo nano /opt/zeek/etc/networks.cfg
```
Ajouter cette ligne :
```
192.168.10.0/24    Reseau interne autorise
```
👉 Explication : Zeek utilise ce fichier pour distinguer l'espace local. N'ajouter que les sous-réseaux du périmètre approuvé.

2. Contrôle, déploiement et supervision périodique :
```bash
sudo /opt/zeek/bin/zeekctl check
sudo /opt/zeek/bin/zeekctl deploy
sudo /opt/zeek/bin/zeekctl cron enable
sudo /opt/zeek/bin/zeekctl netstats
```
👉 Explication : `cron enable` active les contrôles périodiques de ZeekControl (état du nœud, espace disque, rotation des journaux). `netstats` affiche les paquets reçus et perdus ; une perte élevée signale un problème de miroir ou de dimensionnement.

3. Vérification de la remontée des journaux :
```bash
ping -c 3 192.168.10.20
sudo tail -n 5 /opt/zeek/logs/current/conn.log
```
👉 Explication : Confirme que de nouvelles connexions apparaissent après le déploiement.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création d'un compte de service dédié :
```bash
sudo adduser --system --group --home /opt/zeek zeek
sudo install -d -o zeek -g zeek -m 0750 /opt/zeek/logs /opt/zeek/spool
ls -ld /opt/zeek/logs /opt/zeek/spool
```
👉 Explication : Le compte `zeek` écrit les journaux et les fichiers de travail, sans pouvoir modifier les binaires. Vérifier que `/opt/zeek` n'est pas inscriptible globalement.

2. Capacités réseau minimales pour la capture :
```bash
sudo setcap cap_net_raw,cap_net_admin=+eip /opt/zeek/bin/zeek
getcap /opt/zeek/bin/zeek
```
👉 Explication : Accorde à Zeek seulement les droits de capture AF_PACKET, sans lancement complet en root. Une mise à jour du binaire peut effacer ces capacités : relancer `getcap` après chaque mise à niveau. La prise en charge exacte est à vérifier sur la version déployée.

3. Déploiement sous le compte de service :
```bash
sudo -u zeek /opt/zeek/bin/zeekctl check
sudo -u zeek /opt/zeek/bin/zeekctl deploy
sudo -u zeek /opt/zeek/bin/zeekctl status
```
👉 Explication : Les commandes de supervision tournent sous `zeek`. Si `deploy` échoue par manque de droits, lire `journalctl` et corriger les permissions plutôt que de revenir en root de façon permanente. À vérifier selon la version.

4. Protection des journaux et contrôle de l'espace :
```bash
sudo du -sh /opt/zeek/logs
sudo -u zeek /opt/zeek/bin/zeekctl cron enable
```
👉 Explication : Mesure le volume des journaux, à comparer à la politique de rétention. Le cron ZeekControl doit tourner sous le compte `zeek`.

5. Sauvegarde de la configuration avant évolution :
```bash
sudo cp -a /opt/zeek/etc /root/zeek-etc-$(date +%F)
sudo ls -ld /root/zeek-etc-*
```
👉 Explication : Copie datée de la configuration (`node.cfg`, `networks.cfg`, `zeekctl.cfg`). La conserver hors du serveur, car elle décrit le réseau interne.

---