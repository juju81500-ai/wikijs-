---
title: "Fiche Simple - VM Debian 13 Securite Certbot TLS"
description: "Obtenir et renouveler automatiquement un certificat TLS Let's Encrypt pour un site Nginx sur Debian 13, à partir des paquets Debian, avec un renouvellement vérifié par systemd."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[debian13]", "[debian]", "[certbot]", "[tls]", "[letsencrypt]", "[nginx]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Securite_Certbot_TLS

- **Environnement** : VM ou serveur Debian 13 avec Nginx et nom de domaine public
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sécurité / Chiffrement TLS (Let's Encrypt)
- **Tags** : `[debian13]`, `[debian]`, `[certbot]`, `[tls]`, `[letsencrypt]`, `[nginx]`

## 🎯 Problème précis à résoudre
Obtenir et renouveler automatiquement un certificat TLS Let's Encrypt pour un site Nginx sur Debian 13, à partir des paquets Debian, avec un renouvellement vérifié par `systemd`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Certbot et son greffon Nginx :
   ```bash
   sudo apt-get update
   sudo apt-get install -y certbot python3-certbot-nginx
   certbot --version
   ```
   👉 Explication : Le paquet `certbot` est fourni par Debian 13. Le greffon `python3-certbot-nginx` modifie automatiquement la configuration Nginx pour le certificat.

2. Tester l'obtention d'un certificat sur l'environnement de préproduction de Let's Encrypt :
   ```bash
   sudo certbot --nginx --staging -d <domaine_test> -m <email_admin> --agree-tos --no-eff-email
   ```
   👉 Explication : L'option `--staging` évite d'atteindre les limites de débit de la production. Le certificat obtenu n'est pas reconnu par les navigateurs, ce qui est normal en lab.

3. Vérifier le certificat et la configuration Nginx :
   ```bash
   sudo certbot certificates
   sudo nginx -t
   ```
   👉 Explication : `certificates` liste le domaine, la date d'expiration et le chemin du fichier. `nginx -t` valide la syntaxe après modification automatique.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier les prérequis réseau : le DNS public doit pointer vers le serveur, et les ports 80 et 443 doivent être ouverts :
   ```bash
   dig +short <domaine_public>
   sudo ss -tlnp | grep -E ":(80|443) "
   ```
   👉 Explication : Let's Encrypt contacte le serveur sur le port 80 pour valider le domaine. Une adresse DNS différente de l'IP du serveur fait échouer la demande.

2. Demander le certificat de production :
   ```bash
   sudo certbot --nginx -d <domaine_public> -m <email_admin> --agree-tos --no-eff-email
   ```
   👉 Explication : Certbot crée le certificat dans `/etc/letsencrypt/live/<domaine_public>/` et ajoute la configuration HTTPS au bloc Nginx.

3. Vérifier la date d'expiration et la chaîne servie :
   ```bash
   echo | openssl s_client -connect <domaine_public>:443 -servername <domaine_public> 2>/dev/null | openssl x509 -noout -subject -enddate
   ```
   👉 Explication : Confirme que le serveur présente le certificat attendu. L'expiration est habituellement de 90 jours.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Contrôler le timer de renouvellement fourni par le paquet Debian :
   ```bash
   systemctl list-timers certbot.timer --no-pager
   sudo systemctl status certbot.timer --no-pager
   ```
   👉 Explication : Le timer `certbot.timer` lance `certbot renew` deux fois par jour. Le paquet Debian 13 l'installe ; il ne doit pas être remplacé par une tâche cron en double.

2. Tester le renouvellement avec un hook de rechargement Nginx, sans émettre de certificat réel :
   ```bash
   sudo certbot renew --dry-run --deploy-hook "systemctl reload nginx"
   ```
   👉 Explication : `--dry-run` simule le renouvellement sans modifier le certificat. Le hook `--deploy-hook` recharge Nginx uniquement lorsqu'un renouvellement réel a lieu.

3. Vérifier les droits des clés privées, qui ne doivent pas être lisibles par tous :
   ```bash
   sudo ls -l /etc/letsencrypt/archive/<domaine_public>/
   ```
   👉 Explication : Les fichiers `privkey*.pem` doivent appartenir à `root` et être en `0600` ou `0640`. Une clé privée lisible par un compte non privilégié compromet le certificat.