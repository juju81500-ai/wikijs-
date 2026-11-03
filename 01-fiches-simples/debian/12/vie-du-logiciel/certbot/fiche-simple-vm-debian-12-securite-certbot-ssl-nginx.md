# 📄 VM_Debian_12_Securite_Certbot-SSL-Nginx.md

- **Environnement** : VM (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Sécurité & Certificats / HTTPS SSL-TLS
- **Tags** : `[debian12]`, `[certbot]`, `[letsencrypt]`, `[nginx]`, `[ssl]`, `[tls]`, `[hardening]`

## 🎯 Problème précis à résoudre
Générer et installer un certificat SSL/TLS gratuit Let's Encrypt avec Certbot pour un serveur Web Nginx sous Debian 12, automatiser le renouvellement et renforcer la suite cryptographique (TLS 1.3, HSTS).

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de Certbot et du plugin Nginx :
   `apt-get update && apt-get install -y certbot python3-certbot-nginx`
   👉 Explication : Installe l'outil officiel Certbot et son module d'interaction avec Nginx.

2. Génération rapide d'un certificat autonome de test (Standalone) :
   `certbot certonly --standalone -d lab.local --test-cert --non-interactive --agree-tos -m admin@lab.local`
   👉 Explication : Demande un certificat de test auprès des serveurs de staging Let's Encrypt pour valider la chaîne sans impacter les quotas d'émission.

---

## ⚡ 2. Production — Façon Simplifiée
1. Demande et configuration automatique du certificat SSL pour Nginx :
   `certbot --nginx -d wiki.lab.local --non-interactive --agree-tos -m admin@lab.local --redirect`
   👉 Explication : Vérifie le domaine, émet le certificat de production et configure automatiquement le VirtualHost Nginx avec une redirection HTTP vers HTTPS.

2. Test du renouvellement automatique :
   `certbot renew --dry-run`
   👉 Explication : Simule la procédure de renouvellement automatique pour s'assurer du bon fonctionnement du timer systemd.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Génération d'un groupe Diffie-Hellman fort (4096 bits) pour la confidentialité persistante (PFS) :
   `openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096`
   👉 Explication : Renforce la sécurité de l'échange de clés lors de l'établissement des connexions HTTPS.

2. Surcharge des paramètres de sécurité SSL/TLS dans `/etc/nginx/conf.d/ssl-hardening.conf` :
   `echo 'ssl_protocols TLSv1.2 TLSv1.3;\nssl_prefer_server_ciphers on;\nssl_ciphers "EECDH+AESGCM:EDH+AESGCM";\nadd_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;\nssl_dhparam /etc/ssl/certs/dhparam.pem;' > /etc/nginx/conf.d/ssl-hardening.conf`
   👉 Explication : Désactive les versions obsolètes SSLv3/TLS1.0/TLS1.1, impose TLS 1.2/1.3 et active l'en-tête de sécurité HSTS.

3. Configuration d'un hook de rechargement automatique du service Nginx lors du renouvellement :
   `echo '#!/bin/sh\nsystemctl reload nginx' > /etc/letsencrypt/renewal-hooks/post/reload-nginx.sh && chmod +x /etc/letsencrypt/renewal-hooks/post/reload-nginx.sh`
   👉 Explication : Recharge silencieusement le serveur Nginx après chaque renouvellement réussi pour appliquer le nouveau certificat sans interruption.