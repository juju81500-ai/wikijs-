---
title: "Fiche Simple - VM Ubuntu 24.04 Securite Certbot TLS"
description: "Obtenir, installer et renouveler automatiquement un certificat TLS Let's Encrypt pour un nom de domaine public servi par Nginx sur Ubuntu Server 24.04 LTS, et vérifier que le renouvellement fonctionne avant l'échéance."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[certbot]", "[letsencrypt]", "[tls]", "[nginx]", "[renouvellement]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Certbot_TLS

- **Environnement** : VM Ubuntu Server exposant un service HTTPS public
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - certbot 2.9.x depuis le dépôt Noble (la documentation amont recommande le paquet snap)
- **Catégorie** : Sécurité / Chiffrement des flux (TLS)
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[certbot]`, `[letsencrypt]`, `[tls]`, `[nginx]`, `[renouvellement]`

## 🎯 Problème précis à résoudre
Obtenir, installer et renouveler automatiquement un certificat TLS Let's Encrypt pour un nom de domaine public servi par Nginx sur Ubuntu Server 24.04 LTS, et vérifier que le renouvellement fonctionne avant l'échéance.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Utiliser l'environnement de test de Let's Encrypt (staging), qui ne publie aucun certificat de confiance :
   ```bash
   sudo apt update
   sudo apt install -y certbot python3-certbot-nginx
   sudo certbot --nginx --staging -d <domaine_de_test> --non-interactive --agree-tos -m <email_admin>
   ```
   👉 *Explication : Le mode `--staging` évite d'atteindre les limites de requêtes de la production. Le certificat obtenu n'est pas reconnu par les navigateurs.*
2. Vérifier la configuration du certificat de test :
   ```bash
   sudo certbot certificates
   ```
   👉 *Explication : Affiche le domaine, le chemin du certificat et la date d'expiration.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier que le domaine pointe déjà vers le serveur et que les ports 80 et 443 sont ouverts :
   ```bash
   dig +short <domaine>
   sudo ufw status verbose
   ```
   👉 *Explication : Let's Encrypt valide le domaine en accédant au port 80 ; un DNS ou un pare-feu incorrect fait échouer l'émission.*
2. Émettre le certificat de production et configurer Nginx :
   ```bash
   sudo certbot --nginx -d <domaine> --non-interactive --agree-tos --redirect -m <email_admin>
   sudo nginx -t
   sudo systemctl reload nginx
   ```
   👉 *Explication : L'option `--redirect` force la redirection HTTP vers HTTPS. Le plugin Nginx modifie le fichier du site ; `nginx -t` doit valider la syntaxe avant rechargement.*

## 🔒 3. Production — Façon Sécurisée
1. Tester le renouvellement sans modifier le certificat réel :
   ```bash
   sudo certbot renew --dry-run
   ```
   👉 *Explication : Simule le renouvellement complet, y compris le rechargement du service ; toute erreur apparaît avant l'échéance.*
2. Contrôler le minuteur de renouvellement fourni par le paquet Ubuntu :
   ```bash
   systemctl list-timers certbot.timer --no-pager
   systemctl status certbot.timer --no-pager
   ```
   👉 *Explication : Le paquet `certbot` fournit `certbot.timer`, qui lance deux fois par jour la vérification de renouvellement. Si le minuteur n'est pas actif, le certificat expirera sans alerte.*
3. Vérifier le certificat présenté et sa date de fin :
   ```bash
   echo | openssl s_client -connect <domaine>:443 -servername <domaine> 2>/dev/null | openssl x509 -noout -subject -enddate
   ```
   👉 *Explication : Confirme le certificat réellement servi par le port 443, et non seulement le fichier présent sur le disque.*

## ✅ Validation et retour arrière
- Ouvrir `https://<domaine>` depuis un poste externe et vérifier le cadenas sans avertissement.
- Lister les certificats avec `sudo certbot certificates` ; la date d'expiration doit être supérieure à 30 jours.
- Retour arrière : `sudo certbot delete --cert-name <domaine>` puis restaurer la sauvegarde du site Nginx et exécuter `sudo nginx -t` avant rechargement.