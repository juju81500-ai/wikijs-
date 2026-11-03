# 📄 HAProxy

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : HAProxy 2.6.x (paquet des dépôts Debian 12, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[haproxy]`, `[reverse-proxy]`, `[load-balancer]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer HAProxy sur Debian 12 comme répartiteur de charge HTTP devant deux serveurs web, vérifier qu'il redistribue les requêtes, puis le durcir (statistiques protégées, pare-feu restreint, certificat TLS) avant de le mettre devant un service de l'entreprise. Les tests ne se font que sur votre propre serveur et vos propres machines.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de HAProxy et de l'outil de test de socket :
```bash
sudo apt update
sudo apt install -y haproxy socat
haproxy -v
```
👉 Explication : Installe HAProxy et `socat`, utilisé pour interroger le socket d'administration. `haproxy -v` affiche la version installée.

2. Sauvegarde de la configuration par défaut puis écriture d'un frontal et d'un backend de test :
```bash
sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.orig
sudo nano /etc/haproxy/haproxy.cfg
```
Ajouter à la fin du fichier, en adaptant les adresses au lab :
```
frontend ft_web_lab
    bind *:80
    default_backend bk_web_lab

backend bk_web_lab
    balance roundrobin
    option httpchk GET /
    server web01 192.168.10.11:80 check
    server web02 192.168.10.12:80 check
```
👉 Explication : Le frontal écoute sur le port 80 et envoie les requêtes au backend `bk_web_lab`, réparti en round-robin entre `web01` et `web02`. `check` active la vérification de santé des serveurs. Les adresses `192.168.10.11` et `192.168.10.12` sont celles du lab, à remplacer par celles de vos machines de test.

3. Contrôle de la syntaxe puis démarrage du service :
```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
sudo systemctl enable haproxy
sudo systemctl restart haproxy
systemctl status haproxy --no-pager
```
👉 Explication : `haproxy -c` vérifie la configuration sans démarrer le service. La ligne `Active: active (running)` est attendue.

4. Test de répartition et lecture de l'état des serveurs :
```bash
curl -I http://127.0.0.1/
echo "show servers state" | sudo socat stdio /run/haproxy/admin.sock
```
👉 Explication : `curl -I` récupère les en-têtes de la réponse servie par un des deux serveurs. `show servers state` liste l'état de chaque serveur du backend (valeur `2` pour un serveur en service à vérifier sur la version déployée).

---

## ⚡ 2. Production — Façon Simplifiée
1. Ouverture du pare-feu uniquement pour le web et l'administration SSH :
```bash
sudo apt install -y ufw
sudo ufw allow from 192.168.10.0/24 to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : SSH n'est autorisé que depuis le sous-réseau d'administration `192.168.10.0/24` (à adapter), avant l'activation du pare-feu pour éviter de se couper l'accès. Les ports 80 et 443 sont ouverts pour le trafic web. `ufw status verbose` liste les règles actives.

2. Contrôle de la syntaxe puis rechargement sans coupure :
```bash
sudo haproxy -c -f /etc/haproxy/haproxy.cfg
sudo systemctl reload haproxy
systemctl status haproxy --no-pager
```
👉 Explication : Le rechargement applique la nouvelle configuration sans interrompre les connexions déjà établies.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Génération du mot de passe de la page de statistiques, à stocker dans le coffre-fort du pack :
```bash
openssl rand -base64 24
sudo grep -n "stats" /etc/haproxy/haproxy.cfg
sudo nano /etc/haproxy/haproxy.cfg
```
Ajouter dans le fichier, en collant le mot de passe généré à la place de `MotDePasseGenere` :
```
listen stats
    bind 192.168.10.5:8404
    stats enable
    stats uri /stats
    stats auth supervision:MotDePasseGenere
    acl net_admin src 192.168.10.0/24
    http-request deny unless net_admin
```
👉 Explication : `openssl rand -base64 24` produit un mot de passe aléatoire. La page `/stats` n'est accessible qu'au sous-réseau d'administration et demande l'identifiant `supervision`. Le mot de passe en clair reste dans le fichier de configuration : d'où la restriction de droits de l'étape 2. Un mot de passe haché est possible avec la directive `stats auth` côté `userlist` (à vérifier sur la version déployée).

2. Restriction des droits sur le fichier de configuration :
```bash
sudo chown root:haproxy /etc/haproxy/haproxy.cfg
sudo chmod 640 /etc/haproxy/haproxy.cfg
ls -l /etc/haproxy/haproxy.cfg
```
👉 Explication : Seul `root` peut modifier le fichier, et le groupe `haproxy` peut le lire. Le fichier contient des mots de passe : il ne doit pas être lisible par tous.

3. Chiffrement HTTPS sur le frontal :
```bash
sudo mkdir -p /etc/haproxy/certs
sudo install -m 600 -o root -g root /etc/ssl/private/site-entreprise.pem /etc/haproxy/certs/site-entreprise.pem
sudo ls -l /etc/haproxy/certs/site-entreprise.pem
```
👉 Explication : HAProxy lit le certificat et sa clé dans un seul fichier PEM. Le fichier `/etc/ssl/private/site-entreprise.pem` est un exemple à remplacer par le certificat réellement émis. Dans le frontal, la ligne `bind *:443 ssl crt /etc/haproxy/certs/site-entreprise.pem` remplace le `bind *:80` pour le trafic chiffré.

4. Contrôle des journaux :
```bash
sudo journalctl -u haproxy -n 50 --no-pager
```
👉 Explication : Affiche les 50 dernières lignes du journal du service. Les serveurs marqués `DOWN` et les réponses `503` doivent être surveillés. La journalisation détaillée des requêtes exige la directive `log` (à vérifier sur la version déployée).

5. Sauvegarde de la configuration avant toute évolution :
```bash
sudo cp /etc/haproxy/haproxy.cfg /root/haproxy-$(date +%F).cfg
sudo ls -l /root/haproxy-*.cfg
```
👉 Explication : Conserve une copie datée de la configuration avant chaque modification. Le fichier contient des secrets de statistiques : le stocker hors du serveur, dans le coffre-fort de mots de passe du pack, et le protéger en lecture.

---
