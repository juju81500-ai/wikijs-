---
title: "MongoDB"
description: "Installer MongoDB 7.0 sur Debian 12 depuis le dépôt officiel, vérifier qu'il répond et qu'il enregistre un document, puis le préparer pour la production : authentification obligatoire, écoute limitée, compte applicatif restreint, sauvegarde testée. Les tests ne se font que sur votre propre serveur."
published: true
date: 2026-10-29T12:27:07Z
tags: ["[debian-12]", "[mongodb]", "[base-de-donnees]", "[sauvegarde]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:27:07Z
dateModified: 2026-10-29T12:27:07Z
---

# 📄 MongoDB

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : MongoDB 7.0.x (dépôt officiel MongoDB, Debian 12 ne fournit pas MongoDB dans ses dépôts ; version à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[mongodb]`, `[base-de-donnees]`, `[sauvegarde]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer MongoDB 7.0 sur Debian 12 depuis le dépôt officiel, vérifier qu'il répond et qu'il enregistre un document, puis le préparer pour la production : authentification obligatoire, écoute limitée, compte applicatif restreint, sauvegarde testée. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Ajout du dépôt officiel et installation du serveur :
```bash
curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-7.0.gpg --dearmor
echo "deb [ signed-by=/usr/share/keyrings/mongodb-server-7.0.gpg ] https://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-7.0.list
sudo apt update
sudo apt install -y mongodb-org
mongod --version
systemctl status mongod --no-pager
```
👉 Explication : Ajoute la clé et le dépôt MongoDB 7.0 pour Debian 12 (`bookworm`), puis installe `mongodb-org`. Le service `mongod` doit être `active (running)`. Le nom du dépôt et de la clé suit la documentation publique de MongoDB : à vérifier sur la version déployée.

2. Test de réponse et d'écriture :
```bash
sudo apt install -y mongodb-mongosh
mongosh --eval "db.runCommand({ ping: 1 })"
mongosh --eval 'db.getSiblingDB("essai_lab").test.insertOne({ message: "ok" })'
```
👉 Explication : `mongodb-mongosh` installe le client `mongosh` (paquet séparé à vérifier sur la version déployée). `ping` doit renvoyer `{ ok: 1 }`. L'insertion crée la base `essai_lab` et renvoie un `acknowledged: true`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Écoute réseau limitée et authentification activée :
```bash
sudo nano /etc/mongod.conf
```
Dans le fichier, régler la section réseau :
```
net:
  port: 27017
  bindIp: 127.0.0.1,192.168.10.50
```
👉 Explication : `bindIp` limite l'écoute à `localhost` et à l'adresse du serveur `192.168.10.50` (à adapter). L'authentification sera activée à l'étape 3, une fois les comptes créés.

2. Création des comptes, avant d'activer l'authentification :
```bash
mongosh --eval 'db.getSiblingDB("admin").createUser({ user: "admin_mongo", pwd: passwordPrompt(), roles: [{ role: "root", db: "admin" }] })'
mongosh --eval 'db.getSiblingDB("base_appli").createUser({ user: "appli", pwd: passwordPrompt(), roles: [{ role: "readWrite", db: "base_appli" }] })'
```
👉 Explication : `passwordPrompt()` demande le mot de passe sans l'afficher ni le laisser dans l'historique. Le compte `admin_mongo` est l'administrateur, le compte `appli` n'a que l'écriture sur `base_appli`. Enregistrer les deux mots de passe dans le coffre-fort du pack. Cette commande ne fonctionne que si l'authentification n'est pas encore activée.

3. Activation de l'authentification, application de la configuration et ouverture du pare-feu :
```bash
sudo nano /etc/mongod.conf
sudo systemctl restart mongod
sudo ss -ltnp | grep 27017
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow from 192.168.10.21 to any port 27017 proto tcp
sudo ufw enable
sudo ufw status verbose
```
Ajouter dans `/etc/mongod.conf` :
```
security:
  authorization: enabled
```
👉 Explication : `authorization: enabled` oblige à s'identifier pour toute opération, à ajouter seulement après la création des comptes de l'étape 2. Le port 27017 n'est accessible qu'au serveur applicatif `192.168.10.21` (à adapter). `ss` confirme l'adresse d'écoute. SSH est ouvert avant l'activation du pare-feu.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur le fichier de configuration :
```bash
sudo chown root:mongodb /etc/mongod.conf
sudo chmod 640 /etc/mongod.conf
ls -l /etc/mongod.conf
```
👉 Explication : Seul `root` peut modifier la configuration, et le groupe `mongodb` peut la lire. Le compte du service n'a pas besoin d'écrire dans ce fichier.

2. Contrôle des comptes et des rôles :
```bash
mongosh -u admin_mongo -p --authenticationDatabase admin --eval 'db.getSiblingDB("admin").system.users.find({}, { user: 1, db: 1, "roles.role": 1 })'
```
👉 Explication : `-p` demande le mot de passe. La requête liste les comptes et leurs rôles. Tout rôle `root` ou `dbAdminAnyDatabase` doit être justifié, et les comptes applicatifs ne doivent pas avoir de rôle sur d'autres bases.

3. Sauvegarde logique de la base applicative :
```bash
sudo install -d -m 700 /root/sauvegardes
sudo mongodump --host 127.0.0.1 --username admin_mongo --authenticationDatabase admin -p --db base_appli --gzip --archive=/root/sauvegardes/base_appli-$(date +%F).archive.gz
sudo ls -l /root/sauvegardes
```
👉 Explication : `mongodump` écrit une archive compressée. `-p` demande le mot de passe de `admin_mongo` au moment de l'exécution. Le fichier doit être copié hors du serveur et protégé en lecture.

4. Restauration de contrôle sur une machine de test, jamais sur la production :
```bash
mongorestore --host 127.0.0.1 --username admin_mongo --authenticationDatabase admin -p --gzip --archive=/root/sauvegardes/base_appli-$(date +%F).archive.gz --nsFrom "base_appli.*" --nsTo "base_test.*"
```
👉 Explication : Restaure la sauvegarde dans une base de test renommée `base_test`, sans toucher à `base_appli`. Une sauvegarde non restaurée n'est pas validée.

5. Contrôle des journaux du service :
```bash
sudo tail -n 50 /var/log/mongodb/mongod.log
```
👉 Explication : Les échecs d'authentification (`Authentication failed`) et les connexions depuis des adresses inconnues doivent être remontés au responsable sécurité. Le chemin du journal correspond à la configuration par défaut du paquet, à vérifier sur la version déployée.

---