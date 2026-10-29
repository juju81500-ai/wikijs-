# 📄 Fiche_Simple_-_VM_Rocky_9_Securite_Certbot_TLS.md

- **Environnement** : VM ou serveur Rocky Linux exposant un service web
- **OS / Version** : Rocky Linux 9 / RHEL 9 (certbot fourni par EPEL)
- **Catégorie** : Sécurité / Certificats TLS
- **Tags** : `[rocky9]`, `[rhel9]`, `[certbot]`, `[tls]`, `[letsencrypt]`, `[epel]`

## 🎯 Problème précis à résoudre
Obtenir un certificat TLS Let's Encrypt avec Certbot sur Rocky Linux 9, vérifier le renouvellement automatique et protéger la clé privée.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer EPEL puis Certbot :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf install -y certbot
   certbot --version
   ```
   👉 Explication : Certbot n'est pas dans les dépôts de base de Rocky Linux 9. La commande `--version` confirme l'installation.

2. Tester l'obtention d'un certificat sur l'environnement de test Let's Encrypt :
   ```bash
   sudo firewall-cmd --add-service=http
   sudo certbot certonly --standalone --staging -d <nom_du_domaine>
   sudo firewall-cmd --remove-service=http
   ```
   👉 Explication : Le défi HTTP-01 exige que le port 80 soit joignable depuis Internet. L'option `--staging` évite d'atteindre les limites de délivrance de Let's Encrypt. L'ouverture firewalld est temporaire, sans `--permanent`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Obtenir le certificat de production :
   ```bash
   sudo firewall-cmd --add-service=http
   sudo certbot certonly --standalone -d <nom_du_domaine> --agree-tos -m <email_administrateur>
   sudo firewall-cmd --remove-service=http
   ```
   👉 Explication : Les fichiers sont créés dans `/etc/letsencrypt/live/<nom_du_domaine>/`. `fullchain.pem` et `privkey.pem` sont les deux fichiers à référencer dans le serveur web.

2. Vérifier les dates et tester le renouvellement sans modifier le certificat :
   ```bash
   sudo certbot certificates
   sudo certbot renew --dry-run
   ```
   👉 Explication : `certificates` affiche la date d'expiration. `renew --dry-run` simule le renouvellement et signale tout problème de défi ou de chemin.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier les droits de la clé privée :
   ```bash
   sudo ls -l /etc/letsencrypt/archive/<nom_du_domaine>/privkey*.pem
   ```
   👉 Explication : La clé doit être en `-rw-------` et appartenir à `root`. Une clé lisible par d'autres comptes compromet le TLS du service.

2. Recharger le service web automatiquement après chaque renouvellement, en adaptant le nom du service au serveur web utilisé :
   ```bash
   sudo certbot renew --deploy-hook "systemctl reload nginx"
   ```
   👉 Explication : Le hook n'est exécuté que si un certificat a effectivement été renouvelé. Remplacer `nginx` par `httpd` si le serveur web est Apache.

3. Vérifier le certificat réellement servi, en local :
   ```bash
   sudo openssl x509 -in /etc/letsencrypt/live/<nom_du_domaine>/fullchain.pem -noout -subject -dates
   ```
   👉 Explication : Affiche le sujet et les dates de validité. Confirmer aussi que le domaine correspond bien à celui de la configuration du service web.

---

## ✅ Contrôle
```bash
sudo systemctl list-timers --all | grep -i certbot
```
👉 Explication : Vérifie qu'un timer de renouvellement est actif. S'il n'existe pas, planifier `sudo certbot renew` par une tâche cron ou un timer systemd dédié.
