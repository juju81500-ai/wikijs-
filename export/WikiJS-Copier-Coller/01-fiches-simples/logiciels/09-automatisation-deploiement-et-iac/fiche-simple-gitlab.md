# 📄 GitLab

- **Environnement** : VM (Debian 12), 4 Go de RAM minimum recommandés
- **OS / Version** : Debian 12 (bookworm)
- **Version** : GitLab CE (Omnibus) via le dépôt officiel, version majeure à vérifier sur la version déployée
- **Catégorie** : Automatisation, déploiement et IaC

## 🎯 Problème précis à résoudre
Installer une forge GitLab CE sur Debian 12, vérifier l'accès web et la création d'un projet, puis la durcir (inscriptions fermées, pare-feu restreint, sauvegarde régulière) avant de la mettre à disposition des équipes d'administration.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Préparation du système et installation des prérequis :
```bash
sudo apt update
sudo apt install -y curl openssh-server ca-certificates tzdata perl
```
👉 Explication : Installe les dépendances requises par le paquet GitLab Omnibus.

2. Ajout du dépôt officiel GitLab CE et installation :
```bash
curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh -o /tmp/gitlab-repo.sh
less /tmp/gitlab-repo.sh
sudo bash /tmp/gitlab-repo.sh
sudo EXTERNAL_URL="http://<adresse_serveur_gitlab>" apt install -y gitlab-ce
```
👉 Explication : Le premier script configure le dépôt officiel. `EXTERNAL_URL` fixe l'adresse d'accès. L'installation lance une reconfiguration automatique, qui prend plusieurs minutes.

3. Contrôle de l'état des services :
```bash
sudo gitlab-ctl status
```
👉 Explication : Chaque service (`puma`, `postgresql`, `redis`, `nginx`, etc.) doit afficher `run:`.

4. Récupération du mot de passe initial de `root` :
```bash
sudo cat /etc/gitlab/initial_root_password
```
👉 Explication : Mot de passe généré à l'installation. Il est supprimé automatiquement après environ 24 heures : le changer dès la première connexion.

5. Test d'accès depuis le serveur :
```bash
curl -I http://<adresse_serveur_gitlab>
```
👉 Explication : Une réponse `HTTP/1.1 200 OK` ou une redirection `302` vers la page de connexion est attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Adresse HTTPS définie dans la configuration principale :
```bash
sudo nano /etc/gitlab/gitlab.rb
```
Modifier ou ajouter ces lignes, en remplaçant les valeurs entre chevrons :
```
external_url "https://<nom_dns_gitlab>"
letsencrypt['enable'] = false
nginx['ssl_certificate'] = "/etc/gitlab/ssl/<nom_dns_gitlab>.crt"
nginx['ssl_certificate_key'] = "/etc/gitlab/ssl/<nom_dns_gitlab>.key"
```
```bash
sudo gitlab-ctl reconfigure
```
👉 Explication : `external_url` passe en HTTPS. `letsencrypt['enable'] = false` désactive l'obtention automatique du certificat, à utiliser seulement si un certificat interne est fourni. Les fichiers du certificat doivent exister dans `/etc/gitlab/ssl/`. `reconfigure` applique la configuration.

2. Ouverture du pare-feu :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 443/tcp
sudo ufw allow 80/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH n'est autorisé que depuis `<adresse_ip_admin>`. Le port 443 sert à l'interface web et le 80 à la redirection vers HTTPS.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Fermeture des inscriptions publiques :
```bash
sudo nano /etc/gitlab/gitlab.rb
sudo gitlab-ctl reconfigure
```
Ajouter :
```
gitlab_rails['gitlab_signup_enabled'] = false
```
👉 Explication : Empêche la création de compte libre. Les comptes sont créés par l'administrateur. Le nom exact du paramètre est à vérifier dans la documentation de la version déployée.

2. Sauvegarde applicative régulière :
```bash
sudo gitlab-backup create
sudo ls -lh /var/opt/gitlab/backups/
```
👉 Explication : Crée une archive datée contenant la base, les dépôts et les pièces jointes. Les fichiers `*_gitlab_backup.tar` sont à copier hors du serveur. La configuration `/etc/gitlab/gitlab.rb` et `/etc/gitlab/gitlab-secrets.json` se sauvegardent à part, car elles ne sont pas incluses dans l'archive.

3. Sauvegarde des secrets de configuration :
```bash
sudo install -m 600 /etc/gitlab/gitlab-secrets.json /root/gitlab-secrets-$(date +%F).json
sudo install -m 600 /etc/gitlab/gitlab.rb /root/gitlab-rb-$(date +%F).rb
sudo ls -l /root/gitlab-*-*
```
👉 Explication : Sans `gitlab-secrets.json`, les sauvegardes restaurées ne peuvent pas déchiffrer les données. Ces copies sont à conserver hors du serveur, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

4. Contrôle des journaux d'authentification :
```bash
sudo tail -n 50 /var/log/gitlab/gitlab-rails/application.log
```
👉 Explication : Affiche les dernières entrées du journal applicatif. Les échecs répétés de connexion sont à remonter au responsable sécurité.

---