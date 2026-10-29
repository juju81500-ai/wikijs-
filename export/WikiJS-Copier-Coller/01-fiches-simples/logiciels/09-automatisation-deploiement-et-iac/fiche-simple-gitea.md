# 📄 Gitea

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Gitea 1.22.x (binaire officiel, version exacte à vérifier sur la version déployée)
- **Catégorie** : Automatisation, déploiement et IaC

## 🎯 Problème précis à résoudre
Installer la forge Git Gitea sur Debian 12 avec son binaire officiel, SQLite en lab, la créer comme service systemd, vérifier l'accès web, puis la durcir (inscriptions fermées, pare-feu restreint, sauvegarde `gitea dump`) avant mise à disposition des équipes.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des prérequis et création de l'utilisateur de service :
```bash
sudo apt update
sudo apt install -y git sqlite3 wget
sudo adduser --system --group --shell /bin/bash --home /var/lib/gitea --disabled-password git
sudo mkdir -p /var/lib/gitea/custom /var/lib/gitea/data /var/log/gitea /etc/gitea
sudo chown -R git:git /var/lib/gitea /var/log/gitea
sudo chmod 750 /etc/gitea
```
👉 Explication : Installe Git et l'outil `sqlite3`, crée un compte système `git` sans mot de passe et prépare les dossiers de données, de journaux et de configuration.

2. Téléchargement et installation du binaire :
```bash
sudo wget -O /usr/local/bin/gitea "https://dl.gitea.com/gitea/1.22.6/gitea-1.22.6-linux-amd64"
sudo chmod 755 /usr/local/bin/gitea
gitea --version
```
👉 Explication : Télécharge le binaire officiel depuis le serveur Gitea. La version `1.22.6` est à vérifier sur https://dl.gitea.com avant installation. `gitea --version` confirme la version.

3. Création du service systemd :
```bash
sudo nano /etc/systemd/system/gitea.service
```
Contenu :
```
[Unit]
Description=Gitea
After=network.target

[Service]
User=git
Group=git
WorkingDirectory=/var/lib/gitea
ExecStart=/usr/local/bin/gitea web --config /etc/gitea/app.ini
Restart=always

[Install]
WantedBy=multi-user.target
```
```bash
sudo systemctl daemon-reload
sudo systemctl enable gitea
sudo systemctl start gitea
systemctl status gitea --no-pager
```
👉 Explication : Le service tourne sous l'utilisateur `git`, redémarre automatiquement, et sa configuration est lue dans `/etc/gitea/app.ini`, créé par l'assistant web à l'étape suivante. La ligne `Active: active (running)` est attendue.

4. Assistant d'installation web :
```bash
curl -I http://localhost:3000
```
👉 Explication : Une réponse `HTTP/1.1 200 OK` confirme que Gitea écoute sur le port 3000. Dans un navigateur, ouvrir `http://<adresse_serveur>:3000`, renseigner SQLite comme base, le dossier `/var/lib/gitea` pour les données et `/etc/gitea/app.ini` comme fichier de configuration, puis créer le compte administrateur.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du pare-feu pour l'accès web, SSH Git et l'administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 3000/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH n'est autorisé que depuis `<adresse_ip_admin>`. Le port 3000 correspond au port par défaut de Gitea, à remplacer par un reverse proxy HTTPS si l'entreprise en impose un.

2. Contrôle de la configuration :
```bash
sudo -u git /usr/local/bin/gitea doctor check --config /etc/gitea/app.ini
```
👉 Explication : Vérifie la configuration, les dossiers et la base. Les lignes en erreur sont à corriger avant mise en service.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Fermeture des inscriptions et verrouillage de l'installation dans `app.ini` :
```bash
sudo nano /etc/gitea/app.ini
sudo systemctl restart gitea
```
Dans les sections correspondantes :
```
[service]
DISABLE_REGISTRATION = true

[security]
INSTALL_LOCK = true
```
👉 Explication : `DISABLE_REGISTRATION` empêche toute création de compte libre. `INSTALL_LOCK` bloque l'assistant web après installation. Ces noms de clés sont à vérifier dans la documentation de la version déployée.

2. Restriction des droits sur la configuration, qui contient les secrets :
```bash
sudo chown root:git /etc/gitea/app.ini
sudo chmod 640 /etc/gitea/app.ini
ls -l /etc/gitea/app.ini
```
👉 Explication : Seul `root` modifie le fichier, et seul le groupe `git` peut le lire. La sortie doit commencer par `-rw-r----- 1 root git`.

3. Sauvegarde applicative avec `gitea dump` :
```bash
sudo mkdir -p /var/backups/gitea
sudo chown git:git /var/backups/gitea
sudo -u git sh -c 'cd /var/backups/gitea && /usr/local/bin/gitea dump --config /etc/gitea/app.ini'
sudo ls -l /var/backups/gitea
```
👉 Explication : `gitea dump` crée une archive ZIP avec la base, les dépôts et les données. Elle est écrite dans le dossier courant, d'où le `cd`. L'archive, comme `/etc/gitea/app.ini` qui contient le secret interne, est à copier hors du serveur et à protéger.

4. Contrôle des connexions et des erreurs :
```bash
sudo journalctl -u gitea --since "24 hours ago" | grep -i "failed" | tail -n 50
```
👉 Explication : Affiche les tentatives de connexion échouées des dernières 24 heures. Un nombre anormal est à remonter au responsable sécurité.

---