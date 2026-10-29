# Fiche_Simple_-_VM_Debian_13_Nginx_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Nginx des dépôts Debian
- **Catégorie** : serveur Web / Nginx / Sécuriser (TLS, en-têtes, pare-feu)

---

## Problème précis à résoudre

Activer HTTPS, masquer la version, ajouter les en-têtes de base et limiter l'exposition réseau de Nginx.

## 1. Hors-Production (Lab / Test / POC)

1. Lab : générer un certificat auto-signé :
   ```bash
   sudo install -d -m 0750 /etc/ssl/nginx
   sudo openssl req -x509 -nodes -newkey rsa:3072 -days 90 -keyout /etc/ssl/nginx/SITE.key -out /etc/ssl/nginx/SITE.crt -subj '/CN=SITE.example.net'
   sudo chmod 0600 /etc/ssl/nginx/SITE.key
   ```
   👉 Explication : uniquement pour le lab ; en production utiliser un certificat d'une AC (voir la fiche Certbot du pack). Remplacer `SITE`.

2. Activer TLS dans le server block :
   ```bash
   sudo tee /etc/nginx/snippets/tls-durci.conf >/dev/null <<'EOF'
   ssl_protocols TLSv1.2 TLSv1.3;
   ssl_prefer_server_ciphers off;
   ssl_session_timeout 1d;
   ssl_session_cache shared:SSL:10m;
   ssl_session_tickets off;
   add_header X-Content-Type-Options nosniff always;
   add_header X-Frame-Options SAMEORIGIN always;
   add_header Referrer-Policy strict-origin-when-cross-origin always;
   EOF
   ```
   👉 Explication : les suites de chiffrement par défaut de Debian restent valides avec TLS 1.2/1.3. Inclure ce snippet dans le bloc `server { listen 443 ssl; ssl_certificate ...; ssl_certificate_key ...; include snippets/tls-durci.conf; }`.

3. Masquer la version et rediriger HTTP vers HTTPS :
   ```bash
   sudo sed -i 's/^\s*#\?\s*server_tokens.*/    server_tokens off;/' /etc/nginx/nginx.conf
   grep -n server_tokens /etc/nginx/nginx.conf
   # dans le bloc port 80 : return 301 https://$host$request_uri;
   ```
   👉 Explication : vérifier que la directive existe bien dans le bloc `http` ; ajouter la redirection 301 dans le bloc écoutant sur 80.

4. Limiter le débit des requêtes (anti-abus) :
   ```bash
   # dans le bloc http (nginx.conf) :
   #   limit_req_zone $binary_remote_addr zone=perip:10m rate=10r/s;
   # dans le location concerné :
   #   limit_req zone=perip burst=20 nodelay;
   ```
   👉 Explication : adapter `rate` et `burst` au trafic réel ; tester avant de généraliser.

5. Filtrer le réseau :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```
   👉 Explication : n'ouvrir que 80/443 ; limiter l'administration SSH au réseau d'admin.

## 2. Production — Contrôles

Certificat d'une AC reconnue avec renouvellement automatisé et supervisé, `ssl_protocols` limité à TLS 1.2/1.3, scan externe de configuration TLS dans la recette.

## 3. Production — Sécurité

- Clé privée en `0600`, jamais dans un dépôt ni dans une sauvegarde non chiffrée.
- `server_tokens off`, aucun `autoindex`, aucune page de diagnostic exposée.
- Séparer les comptes d'administration ; seul `root` écrit dans `/etc/nginx`.
- Surveiller `/var/log/nginx/error.log` et centraliser les journaux.

## Validation et retour arrière

- **Validation** : `curl -kI https://SITE.example.net/` répond, l'en-tête `Server` n'affiche plus la version, HTTP redirige vers HTTPS.
- **Retour arrière** : retirer l'include TLS et la redirection, `sudo nginx -t`, recharger, puis restaurer la sauvegarde de `/etc/nginx`.

## Si le problème n'est pas résolu

- [Nginx — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-prerequis-limites)
- [Nginx — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-installer)
- [Nginx — Configurer un site](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-configurer)
- [Nginx — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-valider)
- [Nginx — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-sauvegarder-restaurer)
- [Nginx — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/nginx/fiche-simple-vm-debian-13-nginx-mettre-a-jour)
- [Guide complet LEMP Debian 13](/02-fiches-completes/debian/13/installation-deploiement/02-pile-lemp-debian-13-nginx-php-mariadb)
- [Nginx — documentation officielle](https://nginx.org/en/docs/)