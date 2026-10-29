# 📄 Bitwarden

- **Environnement** : VM (Debian 12) avec Docker
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Bitwarden self-hosted, script `bitwarden.sh` officiel (version à vérifier sur la version déployée)
- **Catégorie** : Gestion des secrets et mots de passe

## 🎯 Problème précis à résoudre
Installer Bitwarden auto-hébergé sur Debian 12 avec Docker, vérifier qu'il répond en HTTPS, puis le durcir (inscriptions fermées, pare-feu restreint, sauvegarde chiffrée du dossier de données) avant de confier à l'équipe les mots de passe de l'entreprise. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Docker et des outils de base :
```bash
sudo apt update
sudo apt install -y docker.io docker-compose curl
sudo systemctl enable docker
sudo systemctl start docker
```
👉 Explication : Installe le moteur Docker et `docker-compose` depuis les dépôts Debian 12. Les versions exactes de `docker-compose` (v1 ou plugin v2) sont à vérifier sur la machine déployée, le script Bitwarden le détecte.

2. Téléchargement du script d'installation officiel :
```bash
sudo mkdir -p /opt/bitwarden
cd /opt/bitwarden
sudo curl -L -o /opt/bitwarden/bitwarden.sh "https://func.bitwarden.com/api/dl/?app=self-host&platform=linux"
sudo chmod +x /opt/bitwarden/bitwarden.sh
```
👉 Explication : Récupère le script `bitwarden.sh` depuis le site Bitwarden et le rend exécutable. L'URL de téléchargement est à vérifier dans la documentation Bitwarden à la date de l'installation.

3. Installation de la pile Bitwarden :
```bash
sudo /opt/bitwarden/bitwarden.sh install
```
👉 Explication : Le script pose des questions : domaine (en lab, `<domaine_lab>`, par exemple `bitwarden.lab.local` ajouté dans `/etc/hosts`), adresse courriel de l'administrateur, puis génération d'un certificat auto-signé pour le lab. Les fichiers de configuration sont créés dans `/opt/bitwarden/bwdata`.

4. Démarrage et contrôle des conteneurs :
```bash
sudo /opt/bitwarden/bitwarden.sh start
sudo docker ps --format "table {{.Names}}\t{{.Status}}"
```
👉 Explication : Lance les conteneurs Bitwarden. Les conteneurs doivent afficher `Up` (ou `healthy`) dans la colonne `Status`.

5. Test d'accès depuis le serveur :
```bash
curl -k -I https://<domaine_lab>
```
👉 Explication : `-k` accepte le certificat auto-signé du lab. La réponse attendue est `HTTP/2 200` (ou une redirection `302` vers la page de connexion). Le compte administrateur se crée ensuite dans l'interface web si l'inscription est ouverte.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du pare-feu uniquement pour HTTPS et l'administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Autorise SSH seulement depuis `<adresse_ip_admin>` avant d'activer le pare-feu, pour ne pas se couper l'accès. Le port 443 TCP sert au coffre web et aux clients. `ufw status verbose` liste les règles actives.

2. Certificat HTTPS signé par une autorité de confiance, à placer dans le dossier de données puis à relancer la pile :
```bash
sudo /opt/bitwarden/bitwarden.sh rebuild
sudo /opt/bitwarden/bitwarden.sh restart
```
👉 Explication : Le certificat et sa clé sont à copier dans `/opt/bitwarden/bwdata/ssl/` selon les noms attendus par le script (à vérifier dans la documentation de la version déployée). `rebuild` et `restart` appliquent la nouvelle configuration.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Fermeture des inscriptions publiques après création du compte administrateur :
```bash
sudo nano /opt/bitwarden/bwdata/env/global.override.env
sudo /opt/bitwarden/bitwarden.sh restart
```
👉 Explication : Ajouter la variable `globalSettings__disableUserRegistration=true` dans ce fichier, puis redémarrer. Empêche toute création de compte depuis Internet. Le nom exact de la variable est à vérifier dans la documentation de la version déployée.

2. Restriction des droits sur le dossier de données, qui contient la base et les secrets :
```bash
sudo chown -R root:root /opt/bitwarden/bwdata
sudo chmod -R go-rwx /opt/bitwarden/bwdata
ls -ld /opt/bitwarden/bwdata
```
👉 Explication : Seul `root` peut lire ou modifier le dossier `bwdata`. La sortie de `ls -ld` doit montrer `drwx------`.

3. Sauvegarde chiffrée du dossier de données, stockée hors du serveur :
```bash
sudo /opt/bitwarden/bitwarden.sh stop
sudo tar czf /root/bwdata-$(date +%F).tgz /opt/bitwarden/bwdata
sudo /opt/bitwarden/bitwarden.sh start
sudo ls -l /root/bwdata-*.tgz
```
👉 Explication : Arrête la pile pour une copie cohérente, crée une archive datée, puis relance le service. L'archive contient la base chiffrée et la configuration : la transférer hors du serveur et la protéger (chiffrement GPG ou coffre distinct). La commande `stop` est à vérifier dans la version déployée.

4. Contrôle des journaux et des tentatives de connexion :
```bash
sudo docker logs --since 24h bitwarden-api 2>&1 | grep -i "fail" | tail -n 50
```
👉 Explication : Affiche les échecs de connexion récents. Un pic d'échecs doit être remonté au responsable sécurité. Le nom du conteneur `bitwarden-api` est à vérifier avec `sudo docker ps`.

---