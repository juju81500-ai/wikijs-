# 📄 InfluxDB

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : InfluxDB 2.x (dépôt officiel InfluxData, Debian 12 ne fournit pas InfluxDB dans ses dépôts ; version à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données

## 🎯 Problème précis à résoudre
Installer InfluxDB 2.x sur Debian 12 depuis le dépôt officiel, écrire une mesure de test, puis le préparer pour la production : écoute limitée, jeton d'accès restreint à un seul bucket, sauvegarde testée. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ajout du dépôt officiel et installation :
```bash
curl -fsSL https://repos.influxdata.com/influxdata-archive.key | gpg --dearmor | sudo tee /usr/share/keyrings/influxdata-archive.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/influxdata-archive.gpg] https://repos.influxdata.com/debian stable main" | sudo tee /etc/apt/sources.list.d/influxdata.list
sudo apt update
sudo apt install -y influxdb2 influxdb2-cli
influx version
systemctl status influxdb --no-pager
```
👉 Explication : Ajoute la clé et le dépôt InfluxData, puis installe le serveur `influxdb2` et le client `influx`. Le nom du paquet et de la clé suit la documentation publique d'InfluxData : à vérifier sur la version déployée. Le service doit être `active (running)`.

2. Initialisation de l'instance (organisation, bucket, administrateur de lab) :
```bash
influx setup --username admin_lab --org lab_org --bucket essai_lab --retention 0 --force
```
👉 Explication : Crée l'administrateur `admin_lab`, l'organisation `lab_org` et le bucket `essai_lab`. `--retention 0` conserve les données sans limite de durée. Le mot de passe est demandé de façon masquée : le noter dans le coffre-fort du pack. Cette commande ne s'exécute qu'une fois sur une instance neuve.

3. Écriture et lecture d'une mesure de test :
```bash
influx write --bucket essai_lab --precision s "mesure_lab,hote=lab valeur=1"
influx query 'from(bucket: "essai_lab") |> range(start: -1h)'
```
👉 Explication : `write` envoie une ligne au format ligne d'InfluxDB : la mesure `mesure_lab`, le tag `hote`, le champ `valeur`. `query` relit les données de la dernière heure, en langage Flux. La mesure doit apparaître dans la réponse.

---

## ⚡ 2. Production — Façon Simplifiée
1. Écoute réseau limitée à l'adresse du serveur :
```bash
sudo systemctl edit influxdb
sudo systemctl restart influxdb
sudo ss -ltnp | grep 8086
```
Dans l'éditeur, ajouter :
```
[Service]
Environment="INFLUXD_HTTP_BIND_ADDRESS=192.168.10.60:8086"
```
👉 Explication : Limite l'écoute HTTP à l'adresse `192.168.10.60` (à adapter). La variable d'environnement de l'écoute est à vérifier sur la version déployée. `ss` confirme le port 8086 et l'adresse d'écoute.

2. Création d'un jeton limité à un seul bucket pour l'application :
```bash
BID=$(influx bucket find --name essai_lab --hide-headers | cut -f1)
influx auth create --org lab_org --description appli_mesures --read-bucket $BID --write-bucket $BID
```
👉 Explication : Le jeton affiché une seule fois est à copier dans le coffre-fort du pack. Il ne donne accès qu'au bucket `essai_lab` (à remplacer par le bucket de production). Le nom du sous-commande `bucket find` est à vérifier sur la version déployée.

3. Ouverture du pare-feu pour l'application et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.21 to any port 8086 proto tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Le port 8086 n'est accessible qu'au serveur applicatif `192.168.10.21` (à adapter). SSH est ouvert avant l'activation du pare-feu.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Inventaire des jetons et révocation des jetons inutiles :
```bash
influx auth list
influx auth inactivate --id $(influx auth list --hide-headers | grep appli_test | cut -f1)
```
👉 Explication : `auth list` affiche les jetons, leurs droits et leur statut. Un jeton `all-access` ou un jeton non nommé doit être justifié, puis désactivé. La seconde commande désactive le jeton de test `appli_test` créé en lab, à adapter au nom réel du jeton à retirer.

2. Restriction des droits sur les fichiers d'environnement :
```bash
sudo ls -l /etc/influxdb
sudo chmod 640 /etc/influxdb/*
sudo chown root:influxdb /etc/influxdb/*
```
👉 Explication : Les fichiers de configuration éventuels sont lisibles seulement par `root` et par le groupe du service. Le chemin `/etc/influxdb` est celui du paquet, à vérifier sur la version déployée.

3. Sauvegarde de l'instance :
```bash
sudo install -d -m 700 /root/sauvegardes
sudo influx backup /root/sauvegardes/influx-$(date +%F) --token "$ADMIN_TOKEN"
sudo ls -l /root/sauvegardes
```
👉 Explication : `influx backup` crée un dossier de sauvegarde complet. `$ADMIN_TOKEN` est un jeton administrateur à fournir depuis le coffre-fort : il ne doit pas être écrit dans un script. Le dossier doit être copié hors du serveur.

4. Restauration de contrôle sur une machine de test, jamais sur la production :
```bash
sudo influx restore --full /root/sauvegardes/influx-$(date +%F) --token "$ADMIN_TOKEN"
```
👉 Explication : Restaure l'instance complète sur une machine de test vide. Une sauvegarde non restaurée n'est pas validée. La commande exacte et ses options sont à vérifier sur la version déployée.

5. Contrôle des journaux du service :
```bash
sudo journalctl -u influxdb -n 50 --no-pager
```
👉 Explication : Affiche les 50 dernières lignes du journal. Les rejets d'authentification et les erreurs d'écriture doivent être remontés au responsable sécurité.

---