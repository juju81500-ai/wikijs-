# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Securite_Certbot_TLS.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Sécurité / Chiffrement des flux TLS

## 🎯 Problème précis à résoudre
Obtenir et renouveler automatiquement un certificat TLS Let's Encrypt sur un conteneur Alpine Linux avec le paquet `certbot` (dépôt `community`) et le démon `crond` d'OpenRC, sans systemd timer.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production. Le paquet `acme.sh`, également dans `community`, est une alternative à `certbot`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Activer le dépôt `community` et installer `certbot` :
   ```sh
   grep community /etc/apk/repositories
   apk update
   apk add certbot
   certbot --version
   ```
   👉 Explication : `certbot` n'est pas dans le dépôt principal. Si la ligne `community` est commentée, la décommenter dans `/etc/apk/repositories` puis relancer `apk update`.

2. Tester le flux HTTP-01 en mode `--staging` (certificats de test, sans limite de délivrance) :
   ```sh
   mkdir -p /var/www/localhost/htdocs/.well-known/acme-challenge
   certbot certonly --staging --webroot -w /var/www/localhost/htdocs -d <fqdn_du_service> -m <adresse_email> --agree-tos --non-interactive
   ```
   👉 Explication : Let's Encrypt doit joindre `http://<fqdn_du_service>/.well-known/` sur le port 80. Sans DNS public pointant vers le conteneur, cette étape échoue : le lab doit alors utiliser une CA interne.

---

## ⚡ 2. Production — Façon Simplifiée
1. Demander le certificat de production :
   ```sh
   certbot certonly --webroot -w /var/www/localhost/htdocs -d <fqdn_du_service> -m <adresse_email> --agree-tos --non-interactive
   ```
   👉 Explication : Les fichiers sont écrits dans `/etc/letsencrypt/live/<fqdn_du_service>/`. Le serveur web doit pointer vers ces fichiers, et non vers une copie manuelle.

2. Activer `crond` au démarrage et planifier le renouvellement une seule fois :
   ```sh
   rc-update add crond default
   rc-service crond start
   echo '0 3 * * * certbot renew --quiet --deploy-hook "rc-service <service_web> reload"' >> /etc/crontabs/root
   crontab -l
   ```
   👉 Explication : `/etc/crontabs/root` est la crontab de `root` sous Alpine. Le hook `--deploy-hook` recharge le serveur web uniquement après un renouvellement réussi. Ne pas relancer la commande `echo` : elle dupliquerait la tâche.

3. Contrôler le renouvellement sans modifier le certificat :
   ```sh
   certbot certificates
   certbot renew --dry-run
   ```
   👉 Explication : `certbot certificates` affiche la date d'expiration. `--dry-run` simule le renouvellement complet.

---

## 🔒 3. Production — Façon Sécurisée
1. Vérifier les droits des clés privées générées par certbot :
   ```sh
   ls -l /etc/letsencrypt/archive/<fqdn_du_service>/privkey*.pem
   ```
   👉 Explication : Les clés privées doivent appartenir à `root` avec des droits restreints. Ne jamais placer une copie de la clé dans un répertoire servi par le serveur web.

2. Surveiller l'expiration du certificat depuis une sonde externe (étape 44 du cycle de vie) et conserver la procédure de renouvellement manuel dans la fiche serveur.