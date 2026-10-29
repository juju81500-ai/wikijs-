---
title: "Postman"
description: "Installer Postman Desktop et Newman (exécution en ligne de commande) sur Debian 12, tester une API de lab avec une collection et un environnement, puis lancer les mêmes tests en production sans secret en clair ni synchronisation non maîtrisée. Les tests ne ciblent que vos propres API."
published: true
date: 2026-10-29T12:26:04Z
tags: ["[debian-12]", "[postman]", "[newman]", "[api]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:26:04Z
dateModified: 2026-10-29T12:26:04Z
---

# 📄 Postman

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Postman Desktop (dernière version publique, archive Linux 64 bits) et Newman 6.x (npm, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration
- **Tags** : `[debian-12]`, `[postman]`, `[newman]`, `[api]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Postman Desktop et Newman (exécution en ligne de commande) sur Debian 12, tester une API de lab avec une collection et un environnement, puis lancer les mêmes tests en production sans secret en clair ni synchronisation non maîtrisée. Les tests ne ciblent que vos propres API.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Téléchargement et extraction de Postman Desktop dans `/opt` :
```bash
wget -O /tmp/postman-linux-x64.tar.gz https://dl.pstmn.io/download/latest/linux64
sudo tar -xzf /tmp/postman-linux-x64.tar.gz -C /opt
ls /opt/Postman
```
👉 Explication : Télécharge l'archive officielle Linux 64 bits et l'extrait dans `/opt/Postman`. Le dossier contient l'exécutable `Postman`. Pas de paquet Debian officiel : l'archive est la méthode standard.

2. Lancement de l'application et création d'une requête de test :
```bash
/opt/Postman/Postman
```
Dans l'interface : `New > HTTP Request`, méthode `GET`, URL `https://wiki.lab.local/api/health`, puis `Send`.
👉 Explication : Ouvre Postman et envoie une requête de test. Un statut `200 OK` est attendu. Un avertissement de certificat signale une autorité interne non importée (Settings > Certificates).

3. Installation de Node.js et de Newman, l'exécuteur de collections en ligne de commande :
```bash
sudo apt update
sudo apt install -y nodejs npm
sudo npm install -g newman
newman --version
```
👉 Explication : Newman exécute les collections Postman sans interface graphique, ce qui permet de les lancer dans un script. `newman --version` confirme l'installation.

4. Exécution d'une collection de lab exportée depuis Postman :
```bash
mkdir -p ~/postman
newman run ~/postman/lab-api.postman_collection.json --env-var "base_url=https://wiki.lab.local"
```
👉 Explication : Exécute toutes les requêtes de la collection `lab-api.postman_collection.json` (exportée via `Export` dans Postman) en remplaçant la variable `base_url`. Un résumé des assertions réussies ou échouées s'affiche.

---

## ⚡ 2. Production — Façon Simplifiée
1. Environnement de production séparé, exporté sans valeurs sensibles :
```
Environments > New > prod-api
Variable base_url : https://api.entreprise.lab
Variable token : laisser vide, type Secret
Export > prod-api.postman_environment.json
```
👉 Explication : L'environnement de production ne doit contenir aucun jeton. Le type `Secret` évite que la valeur soit exportée en clair. Le jeton sera fourni à l'exécution.

2. Exécution en production de la collection avec l'environnement :
```bash
newman run ~/postman/lab-api.postman_collection.json -e ~/postman/prod-api.postman_environment.json --env-var "token=$(cat /home/svc_postman/.postman-token)" --timeout-request 10000
```
👉 Explication : Lance la collection avec l'environnement de production. Le jeton est lu depuis un fichier, sans l'écrire dans la commande. `--timeout-request 10000` arrête une requête qui dépasse 10 secondes.

3. Contrôle du code de retour :
```bash
newman run ~/postman/lab-api.postman_collection.json -e ~/postman/prod-api.postman_environment.json --env-var "token=$(cat /home/svc_postman/.postman-token)" --reporters cli
echo "Code : $?"
```
👉 Explication : Newman renvoie `0` si toutes les assertions passent et un code différent de `0` en cas d'échec. Le code affiché par `echo` doit être lu par le script appelant, qui déclenche une alerte si la valeur n'est pas `0`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Jeton dans un fichier réservé au compte de service :
```bash
sudo install -o svc_postman -g svc_postman -m 600 /dev/null /home/svc_postman/.postman-token
sudo ls -l /home/svc_postman/.postman-token
```
👉 Explication : Crée un fichier vide, lisible et modifiable par le seul compte de service `svc_postman`. Le jeton est saisi ensuite dans ce fichier, à partir du coffre-fort de l'entreprise.

2. Droits des collections et environnements :
```bash
chmod 600 ~/postman/prod-api.postman_environment.json
ls -l ~/postman/
```
👉 Explication : Les fichiers d'environnement de production ne doivent être lisibles que par leur propriétaire.

3. Désactivation de la synchronisation cloud pour les environnements de production :
```
Settings > General > Sync : désactivé pour ce poste
```
👉 Explication : La synchronisation envoie les collections et environnements vers le compte Postman. Pour des environnements de production, elle doit être désactivée ou validée par la politique de sécurité. Libellé du réglage à confirmer sur la version déployée.

4. Journal d'exécution sans secret :
```bash
newman run ~/postman/lab-api.postman_collection.json -e ~/postman/prod-api.postman_environment.json --env-var "token=$(cat /home/svc_postman/.postman-token)" --reporters cli | sudo tee -a /var/log/newman_prod.log
sudo chown root:adm /var/log/newman_prod.log && sudo chmod 640 /var/log/newman_prod.log
```
👉 Explication : Enregistre le rapport d'exécution dans un journal réservé à root et au groupe `adm`. Le journal ne contient pas le jeton, mais peut révéler des noms de points d'API : à protéger.

---

**Point à vérifier** : le lien de téléchargement `dl.pstmn.io` et le libellé du réglage de synchronisation peuvent évoluer ; la version de Node.js fournie par Debian 12 (18.x) doit rester compatible avec la version de Newman installée.