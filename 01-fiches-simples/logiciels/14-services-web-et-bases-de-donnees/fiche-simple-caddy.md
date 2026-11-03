# 📄 Caddy

- **Environnement** : VM (Debian 12)
- **OS / Version** : Debian 12 (bookworm)
- **Version** : Caddy 2.x (paquet du dépôt officiel Cloudsmith, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données
- **Tags** : `[debian-12]`, `[caddy]`, `[reverse-proxy]`, `[https]`, `[hardening]`

## 🎯 Objectif
Installer le serveur web et reverse proxy Caddy 2 sur Debian 12, vérifier sur ce même serveur qu'une réponse de test est servie, puis le durcir (HTTPS automatique, masquage de l'en-tête `Server`, en-têtes de sécurité) avant de le publier. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Caddy depuis le dépôt officiel :
```bash
sudo apt update
sudo apt install -y debian-keyring debian-archive-keyring apt-transport-https curl
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | sudo gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | sudo tee /etc/apt/sources.list.d/caddy-stable.list
sudo apt update
sudo apt install -y caddy
```
👉 Explication : Ajoute le dépôt officiel Caddy (clé GPG puis source APT) et installe le paquet. La procédure d'ajout du dépôt est celle publiée par le projet, à vérifier sur la version déployée.

2. Vérification de la version et de la syntaxe :
```bash
caddy version
sudo caddy validate --config /etc/caddy/Caddyfile
```
👉 Explication : `caddy version` affiche la version installée. `caddy validate` contrôle le fichier `Caddyfile` et affiche `Valid configuration` si la syntaxe est correcte.

3. Démarrage du service et contrôle de son état :
```bash
sudo systemctl enable caddy
sudo systemctl start caddy
systemctl status caddy --no-pager
```
👉 Explication : Active le démarrage automatique, lance le service puis affiche son état. La ligne `Active: active (running)` est attendue.

4. Définition d'une réponse de test sur le port 80 :
```bash
sudo nano /etc/caddy/Caddyfile
```
Remplacer le contenu par :
```
:80 {
    respond "Test Caddy lab" 200
}
```
Puis :
```bash
sudo caddy reload --config /etc/caddy/Caddyfile
curl -I http://127.0.0.1/
```
👉 Explication : Le `Caddyfile` répond `Test Caddy lab` à toute requête sur le port 80. `caddy reload` applique la configuration sans couper le service. La ligne `HTTP/1.1 200 OK` est attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Déclaration du site et du reverse proxy :
```bash
sudo nano /etc/caddy/Caddyfile
```
Ajouter ce bloc, en remplaçant les valeurs entre chevrons :
```
<nom_site_fqdn> {
    reverse_proxy <adresse_ip_backend>:<port_backend>
    log {
        output file /var/log/caddy/<nom_site>.log
    }
}
```
👉 Explication : Caddy obtient et renouvelle automatiquement le certificat HTTPS pour `<nom_site_fqdn>` (le nom doit résoudre vers ce serveur et les ports 80 et 443 doivent être joignables). Le trafic est transmis à `<adresse_ip_backend>:<port_backend>`, l'application interne.

2. Contrôle de la syntaxe puis rechargement :
```bash
sudo caddy validate --config /etc/caddy/Caddyfile
sudo caddy reload --config /etc/caddy/Caddyfile
systemctl status caddy --no-pager
```
👉 Explication : Valide le fichier avant de le recharger, puis confirme que le service est actif.

3. Ouverture du pare-feu pour HTTP, HTTPS et administration :
```bash
sudo apt install -y ufw
sudo ufw allow from <adresse_ip_admin> to any port 22 proto tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
sudo ufw status verbose
```
👉 Explication : Ouvre SSH seulement pour `<adresse_ip_admin>` avant d'activer le pare-feu. Le port 80 sert à la validation du certificat et à la redirection, le port 443 au trafic HTTPS.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Suppression de l'en-tête `Server` et ajout des en-têtes de sécurité :
```bash
sudo nano /etc/caddy/Caddyfile
```
Dans le bloc du site, ajouter :
```
header {
    -Server
    Strict-Transport-Security "max-age=31536000"
    X-Content-Type-Options "nosniff"
    X-Frame-Options "SAMEORIGIN"
}
```
👉 Explication : `-Server` supprime l'en-tête qui révèle le logiciel. Les autres lignes ajoutent les en-têtes de sécurité habituels. Puis `sudo caddy reload --config /etc/caddy/Caddyfile`.

2. Formatage et contrôle du fichier de configuration :
```bash
sudo caddy fmt --overwrite /etc/caddy/Caddyfile
sudo caddy validate --config /etc/caddy/Caddyfile
```
👉 Explication : Met le fichier au format standard, puis valide la syntaxe. Le résultat `Valid configuration` est attendu.

3. Vérification du certificat et des en-têtes :
```bash
curl -I https://<nom_site_fqdn>/
echo | openssl s_client -connect <nom_site_fqdn>:443 -servername <nom_site_fqdn> 2>/dev/null | openssl x509 -noout -issuer -dates
```
👉 Explication : Vérifie que la réponse HTTPS contient les en-têtes attendus et que le certificat est bien émis par l'autorité prévue, avec ses dates de validité.

4. Contrôle des journaux :
```bash
sudo tail -n 50 /var/log/caddy/<nom_site>.log
journalctl -u caddy --no-pager -n 50
```
👉 Explication : Affiche les dernières requêtes du site et les messages du service. Les erreurs de certificat ou les réponses 502 répétées sont à remonter au responsable sécurité.

5. Sauvegarde de la configuration avant toute évolution :
```bash
sudo tar czf /root/caddy-conf-$(date +%F).tgz /etc/caddy
sudo ls -l /root/caddy-conf-*.tgz
```
👉 Explication : Crée une archive datée du `Caddyfile`, à stocker hors du serveur et à protéger en lecture. Les certificats gérés par Caddy se trouvent dans `/var/lib/caddy/` et ne sont pas inclus.

---
