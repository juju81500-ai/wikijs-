---
title: "Leçon — Serveur web et reverse proxy (Apache, Nginx)"
description: "À l'issue de cette leçon, vous saurez :"
published: true
date: 2026-11-03T09:36:13Z
tags: ["transverse", "tout-en-un", "lecon", "services-infrastructure", "serveur-web", "nginx", "apache", "reverse-proxy", "tls", "equilibrage"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Leçon — Serveur web et reverse proxy (Apache, Nginx)

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `services-infrastructure`, `serveur-web`, `nginx`, `apache`, `reverse-proxy`, `tls`, `equilibrage`
- **Niveau** : intermédiaire (administrateur système débutant à confirmé)
- **Durée estimée** : 4 à 5 heures (cours 1 h 30, laboratoire 2 h, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À l'issue de cette leçon, vous saurez :

1. distinguer serveur web, proxy direct et **proxy inverse** ;
2. installer Apache ou Nginx et repérer configuration, journaux et service `systemd` ;
3. publier **plusieurs sites sur une seule [[Glossary:IP]]** avec des hôtes virtuels ;
4. activer HTTPS, choisir des versions de [[Glossary:TLS]] raisonnables et rediriger [[Glossary:HTTP]] vers HTTPS ;
5. ajouter des **en-têtes de sécurité** de base sans casser l'application ;
6. lire les journaux pour diagnostiquer un incident ;
7. placer un proxy inverse devant une application et répartir la charge ;
8. valider une configuration **avant** de la recharger.

## Prérequis et durée

- Savoir utiliser un terminal Linux, un éditeur, `systemctl` et `journalctl` ; notions d'IP, de port, de [[Glossary:DNS]] et de HTTP/HTTPS.
- Une **machine virtuelle jetable** (Debian 12 ou Ubuntu 22-04/24-04) sans donnée réelle, avec `sudo`. Durée : 4 à 5 heures.

Les adresses de documentation (`192.0.2.0/24`, `203.0.113.0/24`) et les noms `example.com` / `example.test` remplacent vos vraies valeurs.

## L'essentiel en bref

- Un **serveur web** répond aux requêtes HTTP(S) ; Apache et Nginx sont les plus répandus.
- Un **hôte virtuel** héberge plusieurs noms sur une IP : le choix se fait par l'en-tête `Host` ou le SNI de TLS.
- Un **proxy inverse** se place devant les applications : il termine TLS, journalise et relaie.
- Un **équilibrage simple** répartit les requêtes et écarte les serveurs en panne.
- Règle d'or : **valider (`nginx -t`, `apachectl configtest`) avant de recharger**, et préférer `reload` à `restart`.
- Les en-têtes de sécurité et TLS réduisent le risque ; ils ne remplacent ni les mises à jour ni le filtrage réseau.

---

## 1. Comprendre les rôles : serveur web, proxy, reverse proxy

### 1.1 Le serveur web : le guichetier

Imaginez un guichet de mairie : le visiteur (le navigateur) présente une demande, le guichetier (le serveur web) cherche le document sur le disque ou demande à une application de le fabriquer.

```text
GET /index.html HTTP/1.1
Host: www.example.com
```

La ligne contient méthode, chemin et version ; l'en-tête `Host` est **capital** : il dit de quel site on parle (section 3).

La réponse porte un **code d'état** : `200` réussi, `301`/`302` redirection, `403` interdit, `404` introuvable, `502` le proxy n'a pas obtenu de réponse valide de l'application, `503` indisponible, `504` délai dépassé.

### 1.2 Proxy direct et proxy inverse

Un proxy direct sert les **clients** (filtrage de navigation) ; un proxy inverse sert les **serveurs**. Analogie : le **réceptionniste d'un hôtel** : on ne frappe pas à la porte du cuisinier, la réception transmet, contrôle et répond. Le proxy inverse offre :

- **un seul point d'entrée** exposé, les applications restant en réseau privé ;
- une **terminaison TLS** centralisée ;
- une **journalisation** et des en-têtes uniformes ;
- la **répartition de charge**, voire le cache.

![Schéma d'un proxy inverse Nginx à l'adresse 203.0.113.10 relayant les requêtes HTTPS d'un navigateur vers deux applications internes 192.0.2.11 et 192.0.2.12 en HTTP](images/serveur-web-reverse-proxy-2.svg)

*Figure 1 — Le proxy inverse est le seul point exposé ; les applications restent dans la zone privée. Création originale du projet Pack Master (CC0).*

### 1.3 Apache ou Nginx ?

**Apache** est modulaire et accepte les `.htaccess` ; **Nginx** est économe en mémoire et excellent en proxy inverse. Souvent Nginx fait face à Internet et Apache travaille derrière. Les exemples couvrent les deux.

---

## 2. Installer et s'orienter dans l'arborescence

### 2.1 Installation sous Debian/Ubuntu

```bash
sudo apt update
sudo apt install nginx
nginx -v
```

👉 Explication : met à jour l'index, installe Nginx depuis les dépôts de la distribution et affiche sa version ; le service démarre automatiquement.

Pour Apache :

```bash
sudo apt install apache2
apache2 -v
```

👉 Explication : installe Apache ; ne laissez pas deux serveurs écouter sur les mêmes ports 80/443.

### 2.2 Vérifier que le service tourne et écoute

```bash
systemctl status nginx --no-pager
sudo ss -lntp | grep -E ':(80|443)\b'
curl -I http://127.0.0.1/
```

👉 Explication : `systemctl status` donne l'état du service ; `ss -lntp` liste les sockets [[Glossary:TCP]] en écoute avec le processus propriétaire ; `curl -I` demande uniquement les en-têtes de la page d'accueil locale. Un `200 OK` prouve que le serveur répond **localement**, pas qu'il est joignable depuis un autre poste.

### 2.3 Où se trouve quoi ?

| Élément | Nginx (Debian) | Apache (Debian) |
|---|---|---|
| Fichier principal | `/etc/nginx/nginx.conf` | `/etc/apache2/apache2.conf` |
| Sites disponibles | `/etc/nginx/sites-available/` | `/etc/apache2/sites-available/` |
| Sites activés (liens) | `/etc/nginx/sites-enabled/` | `/etc/apache2/sites-enabled/` |
| Modules / extraits | `/etc/nginx/conf.d/`, `snippets/` | `mods-available/`, `conf-available/` |
| Journal d'accès | `/var/log/nginx/access.log` | `/var/log/apache2/access.log` |
| Journal d'erreurs | `/var/log/nginx/error.log` | `/var/log/apache2/error.log` |
| Racine web par défaut | `/var/www/html` | `/var/www/html` |
| Valider la syntaxe | `sudo nginx -t` | `sudo apachectl configtest` |
| Recharger sans coupure | `sudo systemctl reload nginx` | `sudo systemctl reload apache2` |

Les distributions Red Hat utilisent d'autres chemins (`/etc/httpd/`) : consultez la documentation de **votre** version. Principe « disponible / activé » : on écrit dans `sites-available`, puis on lie dans `sites-enabled` (`a2ensite` sous Apache).

### 2.4 Le réflexe de validation

```bash
sudo nginx -t
sudo systemctl reload nginx
```

👉 Explication : `-t` analyse sans appliquer et signale la ligne fautive ; `reload` relit la configuration sans couper les connexions, contrairement à `restart`. Si `-t` échoue, **ne rechargez pas**.

---

## 3. Hôtes virtuels : plusieurs sites, une seule adresse

### 3.1 Le principe

Une adresse IP, `203.0.113.10`, peut servir `www.example.com` et `api.example.test`. Lorsque le navigateur se connecte, il indique le nom voulu :

1. en HTTP clair, dans l'en-tête `Host` ;
2. en HTTPS, dans l'extension **SNI** (Server Name Indication) de la poignée de main TLS, avant même l'envoi de la requête, pour que le serveur choisisse le bon certificat.

Analogie : un immeuble à un seul numéro de rue mais plusieurs boîtes aux lettres : on lit le nom sur l'enveloppe.

![Schéma montrant deux requêtes, l'une pour www.example.com et l'autre pour api.example.test, reçues par un même serveur web à l'adresse 203.0.113.10 qui choisit le bloc server correspondant, avec un site par défaut qui refuse les noms inconnus](images/serveur-web-reverse-proxy-3.svg)

*Figure 2 — Sélection de l'hôte virtuel : SNI, puis en-tête Host, puis site par défaut. Création originale du projet Pack Master (CC0).*

### 3.2 Exemple Nginx

```nginx
# /etc/nginx/sites-available/www.example.com
server {
    listen 80;
    listen [::]:80;
    server_name www.example.com example.com;

    root /var/www/www.example.com/public;
    index index.html;

    access_log /var/log/nginx/www.example.com.access.log;
    error_log  /var/log/nginx/www.example.com.error.log;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

👉 Explication : un bloc `server` décrit un site ; `server_name` liste ses noms ; `root` désigne le dossier publié ; `try_files` cherche le fichier puis le dossier, sinon 404 ; des journaux par site facilitent le diagnostic.

Activation :

```bash
sudo mkdir -p /var/www/www.example.com/public
echo '<h1>Bienvenue sur www.example.com (lab)</h1>' | sudo tee /var/www/www.example.com/public/index.html
sudo ln -s /etc/nginx/sites-available/www.example.com /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

👉 Explication : crée la racine et une page de test, active le site par lien symbolique, puis ne recharge que si la syntaxe est valide (`&&` empêche le rechargement en cas d'échec).

### 3.3 Le site par défaut : fermer la porte aux inconnus

Si aucun `server_name` ne correspond, Nginx utilise `default_server` (à défaut le premier bloc). Un bloc de capture évite d'exposer un vrai site à n'importe quel nom :

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    return 444;
}
```

👉 Explication : `return 444` (propre à Nginx) ferme la connexion sans réponse ; en HTTPS, ce bloc exige un certificat ou `ssl_reject_handshake on;` (Nginx récent).

### 3.4 Exemple Apache

```apache
# /etc/apache2/sites-available/www.example.com.conf
<VirtualHost *:80>
    ServerName www.example.com
    ServerAlias example.com
    DocumentRoot /var/www/www.example.com/public

    ErrorLog  ${APACHE_LOG_DIR}/www.example.com.error.log
    CustomLog ${APACHE_LOG_DIR}/www.example.com.access.log combined

    <Directory /var/www/www.example.com/public>
        Options -Indexes
        AllowOverride None
        Require all granted
    </Directory>
</VirtualHost>
```

👉 Explication : `ServerName`/`ServerAlias` jouent le rôle de `server_name` ; `Options -Indexes` interdit la liste des fichiers ; `AllowOverride None` désactive les `.htaccess` ; `Require all granted` autorise l'accès (Apache 2.4).

```bash
sudo a2ensite www.example.com.conf
sudo apachectl configtest && sudo systemctl reload apache2
```

👉 Explication : `a2ensite` crée le lien dans `sites-enabled` ; on teste puis on recharge.

---

## 4. TLS : chiffrer et authentifier

### 4.1 Ce que fait TLS

TLS apporte **confidentialité**, **intégrité** et **authentification du serveur** : le certificat prouve que l'on parle bien à `www.example.com`. Le serveur présente un certificat signé par une autorité (voir la leçon [Temps et certificats](/fr/00-cours-theoriques/tout-en-un/03-services-d-infrastructure/lecons/lecon-temps-et-certificats)). Il lui faut la **clé privée** (secrète, jamais exportée) et un fichier de **chaîne complète** : certificat du site puis intermédiaire(s).

### 4.2 Certificat auto-signé pour le laboratoire

```bash
sudo mkdir -p /etc/ssl/lab
sudo openssl req -x509 -newkey ec -pkeyopt ec_paramgen_curve:P-256 -nodes \
  -keyout /etc/ssl/lab/www.example.test.key -out /etc/ssl/lab/www.example.test.crt \
  -days 30 -subj "/CN=www.example.test" -addext "subjectAltName=DNS:www.example.test"
sudo chmod 600 /etc/ssl/lab/www.example.test.key
```

👉 Explication : génère une clé EC P-256 et un certificat auto-signé de 30 jours avec un [[Glossary:SAN]] ; `-nodes` = sans phrase de passe (laboratoire seulement) ; `chmod 600` protège la clé. Un navigateur avertira : aucune autorité n'a signé.

### 4.3 Bloc HTTPS Nginx

```nginx
server {
    listen 443 ssl;
    listen [::]:443 ssl;
    http2 on;
    server_name www.example.test;

    ssl_certificate     /etc/ssl/lab/www.example.test.crt;
    ssl_certificate_key /etc/ssl/lab/www.example.test.key;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_timeout 1d;
    ssl_session_cache shared:SSL:10m;
    ssl_session_tickets off;

    root /var/www/www.example.test/public;
}

server {
    listen 80;
    listen [::]:80;
    server_name www.example.test;
    return 301 https://$host$request_uri;
}
```

👉 Explication : le premier bloc n'autorise que TLS 1.2 et 1.3 ; le second redirige HTTP vers HTTPS en gardant le chemin. `http2 on;` existe depuis Nginx 1.25.1 (avant : `listen 443 ssl http2;`). Évitez de copier de longues listes de chiffrements : les valeurs par défaut récentes sont raisonnables.

### 4.4 Équivalent Apache

```bash
sudo a2enmod ssl headers rewrite
```

👉 Explication : active TLS, en-têtes et réécriture.

```apache
<VirtualHost *:443>
    ServerName www.example.test
    DocumentRoot /var/www/www.example.test/public

    SSLEngine on
    SSLCertificateFile    /etc/ssl/lab/www.example.test.crt
    SSLCertificateKeyFile /etc/ssl/lab/www.example.test.key
    SSLProtocol -all +TLSv1.2 +TLSv1.3
</VirtualHost>

<VirtualHost *:80>
    ServerName www.example.test
    Redirect permanent / https://www.example.test/
</VirtualHost>
```

👉 Explication : `SSLProtocol -all +TLSv1.2 +TLSv1.3` n'autorise que les versions modernes ; depuis Apache 2.4.8, `SSLCertificateFile` accepte la chaîne complète ; `Redirect permanent` renvoie vers HTTPS.

### 4.5 Vérifier le résultat

```bash
openssl s_client -connect 127.0.0.1:443 -servername www.example.test </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

👉 Explication : ouvre une connexion TLS avec SNI et affiche sujet, émetteur et dates du certificat présenté ; `</dev/null` clôt la session. Auto-signé : sujet et émetteur sont identiques.

---

## 5. En-têtes de sécurité de base

Les en-têtes de réponse sont des **consignes** au navigateur : ils réduisent la surface d'attaque sans remplacer la sécurité de l'application.

| En-tête | Rôle | Valeur prudente |
|---|---|---|
| `Strict-Transport-Security` | Impose HTTPS pour ce nom | `max-age=300`, augmenté après validation |
| `X-Content-Type-Options` | Interdit de « deviner » les types | `nosniff` |
| `X-Frame-Options` | Interdit l'affichage dans le cadre d'un autre site | `SAMEORIGIN` |
| `Referrer-Policy` | Limite les informations d'origine envoyées | `strict-origin-when-cross-origin` |
| `Content-Security-Policy` | Liste les sources autorisées | À bâtir **avec les développeurs** |

Deux précautions : **[[Glossary:HSTS]] est difficile à annuler** (le navigateur refuse HTTP pendant toute la durée), donc commencez court et n'ajoutez ni `includeSubDomains` ni `preload` sans audit ; une **CSP trop stricte casse le site**, commencez par `Content-Security-Policy-Report-Only`.

Nginx :

```nginx
server_tokens off;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Strict-Transport-Security "max-age=300" always;
```

👉 Explication : `server_tokens off` masque la version ; `always` ajoute l'en-tête même aux erreurs. Attention : un `location` qui définit ses propres `add_header` **n'hérite plus** de ceux du niveau supérieur.

Apache :

```apache
ServerTokens Prod
ServerSignature Off
Header always set X-Content-Type-Options "nosniff"
Header always set X-Frame-Options "SAMEORIGIN"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Strict-Transport-Security "max-age=300"
```

👉 Explication : `ServerTokens Prod` réduit la signature ; `ServerSignature Off` retire le pied de page des erreurs ; `Header always set` (module `headers`) ajoute les en-têtes à toutes les réponses.

Contrôle :

```bash
curl -skI --resolve www.example.test:443:127.0.0.1 https://www.example.test/
```

👉 Explication : `-k` accepte le certificat de laboratoire (jamais pour valider un vrai certificat) ; `-I` n'affiche que les en-têtes à contrôler.

---

## 6. Journaux : savoir lire avant de chercher

### 6.1 Deux journaux, deux usages

Le **journal d'accès** (une ligne par requête) répond à « que s'est-il passé ? » ; le **journal d'erreurs** répond à « pourquoi ça casse ? ». Format « combined » :

```text
198.51.100.23 - - [01/Nov/2026:10:15:42 +0100] "GET /index.html HTTP/1.1" 200 612 "-" "Mozilla/5.0"
```

On y lit IP du client, date, requête, **code 200**, taille et agent utilisateur.

### 6.2 Commandes utiles

```bash
sudo tail -n 50 /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
sudo awk '{print $9}' /var/log/nginx/access.log | sort | uniq -c | sort -rn
```

👉 Explication : dernières requêtes ; suivi en direct des erreurs (Ctrl+C pour quitter) ; décompte des codes (champ 9 du format « combined ») .

### 6.3 Rotation, confidentialité, proxy

`logrotate` fait tourner les journaux (`/etc/logrotate.d/nginx`). IP et URL sont des **données personnelles** : limitez conservation et droits de lecture, anonymisez avant de joindre un journal à un ticket. Derrière un proxy, le serveur d'arrière-plan ne voit que l'IP du proxy : n'accordez confiance à `X-Forwarded-For` que s'il vient **d'un proxy que vous contrôlez**, un visiteur pouvant le forger.

---

## 7. Le proxy inverse en pratique

### 7.1 Configuration minimale Nginx

Supposons une application qui écoute en HTTP sur `192.0.2.11:8080`.

```nginx
server {
    listen 443 ssl;
    server_name app.example.test;
    ssl_certificate     /etc/ssl/lab/www.example.test.crt;
    ssl_certificate_key /etc/ssl/lab/www.example.test.key;

    location / {
        proxy_pass http://192.0.2.11:8080;
        proxy_set_header Host              $host;
        proxy_set_header X-Real-IP         $remote_addr;
        proxy_set_header X-Forwarded-For   $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 5s;
        proxy_read_timeout    60s;
    }
}
```

👉 Explication : `proxy_pass` désigne l'application ; les `proxy_set_header` transmettent nom demandé, IP réelle, chaîne d'IP et protocole d'origine (pour générer des liens `https://`) ; les délais évitent qu'une application bloquée accapare les connexions.

Piège de la **barre oblique finale** : `proxy_pass http://192.0.2.11:8080;` conserve le chemin, `…:8080/;` remplace la partie correspondant au `location`.

### 7.2 Équivalent Apache

```bash
sudo a2enmod proxy proxy_http headers
```

👉 Explication : active le module de proxy générique et sa prise en charge HTTP.

```apache
<VirtualHost *:443>
    ServerName app.example.test
    SSLEngine on
    SSLCertificateFile    /etc/ssl/lab/www.example.test.crt
    SSLCertificateKeyFile /etc/ssl/lab/www.example.test.key

    ProxyPreserveHost On
    RequestHeader set X-Forwarded-Proto "https"
    ProxyPass        / http://192.0.2.11:8080/
    ProxyPassReverse / http://192.0.2.11:8080/
</VirtualHost>
```

👉 Explication : `ProxyPreserveHost On` garde l'en-tête `Host` ; `ProxyPass` relaie ; `ProxyPassReverse` réécrit les redirections de l'application ; Apache ajoute lui-même `X-Forwarded-For`.

### 7.3 Sécurité du proxy inverse

- N'exposez **jamais** le port interne (8080) : filtrez-le pour que seul le proxy l'atteigne.
- Gardez `ProxyRequests Off` sur Apache : activer le proxy direct sans contrôle d'accès crée un proxy ouvert.
- Limitez la taille des requêtes (`client_max_body_size`, `LimitRequestBody`).

---

## 8. Équilibrage de charge simple

### 8.1 Pourquoi répartir ?

Deux serveurs identiques valent mieux qu'un : plus de capacité, et la panne de l'un n'arrête plus le service. Analogie : les **caisses d'un supermarché**, où l'on n'envoie personne vers une caisse fermée.

![Schéma d'un répartiteur de charge placé entre un commutateur relié à plusieurs postes clients et deux serveurs situés sur un réseau privé](images/serveur-web-reverse-proxy-1.svg)

*Figure 3 — Principe d'un répartiteur de charge entre plusieurs clients et deux serveurs (légendes en anglais : Terminal = poste client, Switch = commutateur, Loading Balancer = répartiteur de charge, Server = serveur). Image « Load Balancing Cluster ([[Glossary:NAT]]).svg » par HFWMan, Wikimedia Commons, licence CC BY-SA 4.0 ; voir les crédits en fin de leçon.*

### 8.2 Configuration Nginx

```nginx
upstream app_pool {
    least_conn;
    server 192.0.2.11:8080 max_fails=3 fail_timeout=30s;
    server 192.0.2.12:8080 max_fails=3 fail_timeout=30s;
    server 192.0.2.13:8080 backup;
}

server {
    listen 80;
    server_name app.example.test;
    location / {
        proxy_pass http://app_pool;
        proxy_set_header Host $host;
        proxy_next_upstream error timeout http_502 http_503;
    }
}
```

👉 Explication : `upstream` regroupe les serveurs (tourniquet par défaut, `least_conn` = le moins de connexions) ; après 3 échecs en 30 s, un serveur est écarté 30 s ; `backup` n'intervient que si tous les autres sont indisponibles ; `proxy_next_upstream` rejoue la requête ailleurs. Le contrôle de santé de Nginx libre est **passif** : il détecte la panne à la première requête échouée.

### 8.3 Configuration Apache

```bash
sudo a2enmod proxy_balancer lbmethod_byrequests
```

👉 Explication : active le module de répartition et l'algorithme par nombre de requêtes.

```apache
<Proxy "balancer://app_pool">
    BalancerMember "http://192.0.2.11:8080" retry=30
    BalancerMember "http://192.0.2.12:8080" retry=30
    ProxySet lbmethod=byrequests
</Proxy>
ProxyPass        "/" "balancer://app_pool/"
ProxyPassReverse "/" "balancer://app_pool/"
```

👉 Explication : `BalancerMember` déclare un serveur ; `retry=30` attend 30 s avant de le retenter ; `byrequests` répartit à tour de rôle.

### 8.4 Les sessions

Si la session est en mémoire locale, un visiteur renvoyé vers l'autre serveur la perd. Solutions : magasin de sessions partagé, **affinage** (`ip_hash`, cookie sticky) ou application sans état.

---

## Mise en pratique guidée

**Objectif** : Nginx en HTTPS relaie une « application » factice vers deux serveurs locaux. **Contexte** : [[Glossary:VM]] Debian 12 jetable ; toutes les connexions restent sur `127.0.0.1`.

### Étape 1 — Installer Nginx et Python (pour les applications factices)

```bash
sudo apt update
sudo apt install nginx python3 curl openssl
```

👉 Explication : installe le serveur et les outils de test.

### Étape 2 — Lancer deux applications factices

```bash
mkdir -p ~/lab-web/app1 ~/lab-web/app2
echo 'réponse de app1' > ~/lab-web/app1/index.html
echo 'réponse de app2' > ~/lab-web/app2/index.html
(cd ~/lab-web/app1 && python3 -m http.server 8081 --bind 127.0.0.1 >/dev/null 2>&1 &)
(cd ~/lab-web/app2 && python3 -m http.server 8082 --bind 127.0.0.1 >/dev/null 2>&1 &)
curl -s http://127.0.0.1:8081/ ; curl -s http://127.0.0.1:8082/
```

👉 Explication : crée deux pages identifiables, démarre deux mini-serveurs liés à l'adresse locale uniquement et vérifie qu'ils répondent.

### Étape 3 — Certificat de laboratoire

Reprenez la commande de la section 4.2.

### Étape 4 — Écrire la configuration Nginx

Créez `/etc/nginx/sites-available/lab.conf` avec ce contenu :

```nginx
upstream lab_pool {
    server 127.0.0.1:8081 max_fails=2 fail_timeout=10s;
    server 127.0.0.1:8082 max_fails=2 fail_timeout=10s;
}

server {
    listen 80 default_server;
    server_name _;
    return 444;
}

server {
    listen 80;
    server_name www.example.test;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name www.example.test;
    ssl_certificate     /etc/ssl/lab/www.example.test.crt;
    ssl_certificate_key /etc/ssl/lab/www.example.test.key;
    ssl_protocols TLSv1.2 TLSv1.3;

    server_tokens off;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;

    access_log /var/log/nginx/lab.access.log;
    error_log  /var/log/nginx/lab.error.log;

    location / {
        proxy_pass http://lab_pool;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

👉 Explication : site de capture, redirection HTTP→HTTPS et proxy inverse répartissant sur les deux applications.

### Étape 5 — Activer et valider

```bash
sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /etc/nginx/sites-available/lab.conf /etc/nginx/sites-enabled/lab.conf
sudo nginx -t && sudo systemctl reload nginx
```

👉 Explication : retire le site par défaut de Debian, active le laboratoire, recharge si la syntaxe est valide.

### Étape 6 — Vérifier

```bash
curl -sI --resolve www.example.test:80:127.0.0.1 http://www.example.test/ | head -n 3
for i in 1 2 3 4; do curl -sk --resolve www.example.test:443:127.0.0.1 https://www.example.test/; done
curl -skI --resolve www.example.test:443:127.0.0.1 https://www.example.test/ | grep -iE 'server|x-content|x-frame'
```

👉 Explication : `--resolve` force `127.0.0.1` pour le nom sans toucher au DNS (l'en-tête `Host` reste correct) ; attendu : un `301`, l'alternance `app1`/`app2`, puis les en-têtes de sécurité sans numéro de version.

### Étape 7 — Simuler une panne

```bash
pkill -f "http.server 8081"
for i in 1 2 3 4; do curl -sk --resolve www.example.test:443:127.0.0.1 https://www.example.test/; done
sudo tail -n 5 /var/log/nginx/lab.error.log
```

👉 Explication : arrête le serveur du port 8081 ; toutes les réponses doivent venir de `app2`, le journal d'erreurs montre les échecs.

### Étape 8 — Nettoyage

```bash
pkill -f "http.server 8082"
sudo rm -f /etc/nginx/sites-enabled/lab.conf
sudo nginx -t && sudo systemctl reload nginx
rm -rf ~/lab-web
```

👉 Explication : arrête le second mini-serveur, désactive le laboratoire et supprime les fichiers de test.

---

## Exercices

1. **(Facile)** Citez deux différences entre proxy direct et proxy inverse.
2. **(Facile)** Quelle commande valide la configuration de Nginx ? celle d'Apache ?
3. **(Facile)** Un site derrière Nginx renvoie 502 : que consultez-vous d'abord ?
4. **(Moyen)** Écrivez un bloc Nginx pour `blog.example.com` servant `/var/www/blog` avec journaux dédiés.
5. **(Moyen)** Pourquoi HSTS d'un an est-il risqué dès le premier jour ?
6. **(Moyen)** Que change la barre finale dans `proxy_pass http://app:8080/;` pour un `location /api/` ?
7. **(Avancé)** Les sessions se perdent depuis l'ajout d'un second serveur : proposez deux corrections.
8. **(Avancé)** Écrivez un contrôle affichant le code HTTP, l'expiration du certificat et trois en-têtes de sécurité.

## Corrigés des exercices

1. Le proxy direct sert les clients (ils le configurent) ; le proxy inverse sert les serveurs et reste invisible du client, il termine souvent TLS et répartit la charge.
2. `sudo nginx -t` ; `sudo apachectl configtest`.
3. Le journal d'erreurs du proxy : `connect() failed` ou `upstream timed out` indique une application arrêtée, mal adressée ou lente. Vérifiez ensuite `ss -lntp`, le journal de l'application, le pare-feu et SELinux.
4. Bloc :
   ```nginx
   server {
       listen 80;
       server_name blog.example.com;
       root /var/www/blog;
       access_log /var/log/nginx/blog.example.com.access.log;
       error_log  /var/log/nginx/blog.example.com.error.log;
       location / { try_files $uri $uri/ =404; }
   }
   ```
   👉 Explication : même structure que la section 3.2 avec les noms demandés.
5. Le navigateur mémorise HSTS : si le certificat expire ou si HTTPS est mal configuré, l'utilisateur ne peut plus contourner. On commence par `max-age=300`.
6. Sans barre, `/api/users` est transmis tel quel ; avec barre, `/api/` est remplacé par `/` et l'application reçoit `/users`.
7. Stockage de sessions partagé (base, cache) ; affinage `ip_hash` ou cookie ; application sans état.
8. ```bash
   H=www.example.test
   curl -skI "https://$H/" | grep -iE '^HTTP|strict-transport|x-content-type|x-frame'
   echo | openssl s_client -connect "$H:443" -servername "$H" 2>/dev/null | openssl x509 -noout -enddate
   ```
   👉 Explication : affiche code et en-têtes, puis la date d'expiration ; retirez `-k` sur un vrai site.

## Quiz

**1.** Quel en-tête choisit l'hôte virtuel en HTTP clair ? A. `Accept` — B. `Host` — C. `Referer` — D. `Cookie`. **Réponse : B** ; `Host` porte le nom du site demandé.

**2.** Quelle commande applique la configuration sans couper les connexions ? A. `stop` — B. `restart` — C. `reload` — D. `nginx -t`. **Réponse : C** ; `restart` coupe, `-t` ne fait que valider.

**3.** Quel code signale un échec entre proxy et application ? A. 301 — B. 403 — C. 404 — D. 502. **Réponse : D** (*Bad Gateway*).

**4.** À quoi sert le SNI ? A. Chiffrer les cookies — B. Indiquer le nom du site avant le choix du certificat — C. Compresser — D. Limiter le débit. **Réponse : B** ; il permet de présenter le bon certificat sur une IP partagée.

**5.** Pourquoi `always` dans `add_header` ? A. Accélérer — B. Inclure aussi les réponses d'erreur — C. Activer HTTP/2 — D. Chiffrer. **Réponse : B**.

**6.** Que fait `X-Forwarded-Proto $scheme` ? A. Choisit TLS — B. Informe l'application du protocole du visiteur — C. Change le port — D. Bloque HTTP. **Réponse : B** ; l'application sait que le visiteur est en HTTPS.

**7.** Risque de `X-Forwarded-For` non maîtrisé ? A. Aucun — B. Un client peut le forger — C. Il ralentit TLS — D. Il casse le DNS. **Réponse : B**.

**8.** Que signifie `backup` dans un `upstream` ? A. Sauvegarde les données — B. Reçoit du trafic seulement si les autres sont indisponibles — C. Reçoit les écritures — D. Désactivé. **Réponse : B**.

**9.** Bonne pratique pour le port 8080 de l'application ? A. L'ouvrir à Internet — B. Le restreindre au proxy — C. Le changer chaque jour — D. Le remplacer par 22. **Réponse : B** ; le proxy doit rester le seul point d'entrée.

**10.** Pourquoi une CSP en mode « Report-Only » d'abord ? A. Plus rapide — B. Observer les violations sans bloquer le site — C. Désactiver TLS — D. Masquer la version. **Réponse : B** ; une politique trop stricte casse les scripts.

---

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Vérification / correction |
|---|---|---|
| `Address already in use` | Autre serveur sur le port 80 | `sudo ss -lntp \| grep :80` ; arrêter ou déplacer l'un des deux |
| Mauvais site affiché | `server_name` erroné, lien non créé | `nginx -T \| grep server_name`, `apachectl -S` |
| Erreur de syntaxe au test | `;` manquant, accolade non fermée | Lire la ligne indiquée |
| 403 Forbidden | Droits, absence d'`index`, `Require` refusé | `namei -l /var/www/…` |
| 502 / `connect() failed` | Application arrêtée, mauvais port | `ss -lntp`, journal applicatif, SELinux |
| Avertissement de certificat | Auto-signé, nom absent du SAN, expiré, chaîne incomplète | `openssl s_client … -servername …` ; servir la chaîne complète |
| Boucle de redirections | L'application redirige vers HTTPS alors que le proxy lui parle en HTTP | Transmettre `X-Forwarded-Proto` |
| En-têtes absents | `add_header` écrasé dans un `location`, module `headers` absent | Redéfinir ; `a2enmod headers` |

Méthode : reproduire avec `curl -v`, lire le journal d'erreurs, isoler le maillon (client → proxy → application), ne changer qu'un paramètre à la fois.

## À retenir

- Le serveur web sert ; le proxy inverse protège et distribue.
- Hôtes virtuels : un nom par site (`Host`, SNI) et un site par défaut qui refuse les inconnus.
- **Valider puis recharger**, jamais l'inverse.
- TLS 1.2/1.3, clé privée protégée, chaîne complète, redirection HTTPS, HSTS prudent.
- En-têtes de sécurité utiles ; CSP avec les développeurs, d'abord en rapport seul.
- Journaux = premiers outils de diagnostic, et données personnelles.
- Équilibrage : serveurs de secours, délais courts, sessions partagées.
- Ne jamais exposer l'application directement ni croire un `X-Forwarded-For` non maîtrisé.

## Pour aller plus loin

- Documentation de Nginx : <https://nginx.org/en/docs/>
- Documentation d'Apache HTTP Server 2.4 : <https://httpd.apache.org/docs/2.4/>
- Module `mod_proxy` d'Apache : <https://httpd.apache.org/docs/2.4/mod/mod_proxy.html>
- Module `ngx_http_proxy_module` : <https://nginx.org/en/docs/http/ngx_http_proxy_module.html>
- Module `ngx_http_upstream_module` : <https://nginx.org/en/docs/http/ngx_http_upstream_module.html>
- RFC 9110, HTTP Semantics : <https://www.rfc-editor.org/rfc/rfc9110>
- RFC 8446, TLS 1.3 : <https://www.rfc-editor.org/rfc/rfc8446>
- RFC 6797, HTTP Strict Transport Security : <https://www.rfc-editor.org/rfc/rfc6797>
- Leçon suivante du même dossier, sur les certificats : [Temps et certificats](lecon-temps-et-certificats.md)

## Crédits des images

| Fichier | Source (URL de la page Commons) | Auteur | Licence (nom + URL) | Modifications |
|---|---|---|---|---|
| `images/serveur-web-reverse-proxy-1.svg` | <https://commons.wikimedia.org/wiki/File:Load_Balancing_Cluster_(NAT).svg> | HFWMan | CC BY-SA 4.0 — <https://creativecommons.org/licenses/by-sa/4.0/> | Aucune (fichier d'origine, légendes en anglais). Cette image reste sous CC BY-SA 4.0. |
| `images/serveur-web-reverse-proxy-2.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |
| `images/serveur-web-reverse-proxy-3.svg` | Création originale du projet Pack Master | Projet Pack Master | Dédiée au domaine public (CC0) — <https://creativecommons.org/publicdomain/zero/1.0/> | Sans objet |

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Debian 12 / Nginx / Apache 2.4 | Rédaction assistée (Copilot) | Non testé sur plateforme cible |