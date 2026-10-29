---
title: "Fiche Simple - VM Ubuntu 26.04 Securite Certbot TLS"
description: "Obtenir un certificat TLS Let's Encrypt valide pour un nom de domaine public avec Certbot, et s'assurer que le renouvellement automatique fonctionne avant l'expiration."
published: true
date: 2026-10-29T18:57:19Z
tags: ["ubuntu2604", "certbot", "letsencrypt", "tls", "nginx", "renouvellement"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_26.04_Securite_Certbot_TLS

- **Environnement** : VM Ubuntu publique avec nom de domaine pointant vers le serveur
- **OS / Version** : Ubuntu Server 26.04 LTS
- **Catégorie** : Sécurité / Certificats TLS
- **Tags** : `ubuntu2604`, `certbot`, `letsencrypt`, `tls`, `nginx`, `renouvellement`

---

## 🎯 Problème précis à résoudre

Obtenir un certificat TLS Let's Encrypt valide pour un nom de domaine public avec Certbot, et s'assurer que le renouvellement automatique fonctionne avant l'expiration.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Vérifier que le nom pointe vers le serveur et que le port 80 est joignable :
```bash
dig +short <nom_de_domaine>
```
👉 Explication : L'adresse retournée doit correspondre à l'IP publique du serveur. Let's Encrypt contrôle le domaine en joignant le port 80 (HTTP-01) ou un enregistrement DNS (DNS-01).

2. Installer Certbot et le plugin Nginx :
```bash
sudo apt update
sudo apt install -y certbot python3-certbot-nginx
```
👉 Explication : Le paquet `certbot` de la distribution fournit la commande, le timer de renouvellement systemd et le plugin pour modifier automatiquement la configuration Nginx. Ce plugin n'est nécessaire que si Nginx sert le site.

3. Tester avec l'autorité de staging (certificat non reconnu, aucune limite de débit stricte) :
```bash
sudo certbot --nginx --staging -d <nom_de_domaine>
```
👉 Explication : Valide la chaîne complète (DNS, port 80, écriture Nginx) sans consommer le quota de certificats de production.

## ⚡ 2. Production — Façon Simplifiée

1. Obtenir le certificat de production :
```bash
sudo certbot --nginx -d <nom_de_domaine> -m <adresse_contact> --agree-tos --no-eff-email
```
👉 Explication : Demande le certificat, le fixe dans `/etc/letsencrypt/live/<nom_de_domaine>/` et active la redirection HTTPS dans Nginx. `--agree-tos` accepte les conditions d'utilisation de Let's Encrypt ; à utiliser en connaissance de cause.

2. Vérifier le renouvellement automatique :
```bash
sudo certbot renew --dry-run
systemctl list-timers certbot.timer --no-pager
```
👉 Explication : `--dry-run` simule un renouvellement sans modifier le certificat. Le timer systemd doit apparaître avec sa prochaine exécution.

## 🔒 3. Production — Façon Sécurisée

1. Contrôler l'expiration et la chaîne servie :
```bash
echo | openssl s_client -connect <nom_de_domaine>:443 -servername <nom_de_domaine> 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```
👉 Explication : Confirme le sujet, l'émetteur et la date d'expiration du certificat réellement présenté aux clients, et non celui présent sur le disque.

2. Ajouter une alerte d'expiration à la supervision. Lister les certificats gérés et leur date d'expiration :
```bash
sudo certbot certificates
```
👉 Explication : Liste les certificats gérés et leur date d'expiration. À intégrer dans un contrôle périodique ; un certificat à moins de 14 jours doit déclencher une alerte.

3. Ajouter un hook de rechargement pour que Nginx prenne le nouveau certificat :
```bash
sudo certbot reconfigure --cert-name <nom_de_domaine> --deploy-hook "systemctl reload nginx"
```
👉 Explication : Sans rechargement, Nginx continue à servir l'ancien certificat jusqu'au prochain redémarrage. Le hook s'exécute après chaque renouvellement réussi.

## ✅ Validation et retour arrière

- **Précontrôles** : DNS pointant vers le serveur, port 80 ouvert (`sudo ufw status`), sauvegarde de `/etc/nginx/`.
- **Validation** : `sudo certbot renew --dry-run` sans erreur ; `openssl` affiche le bon nom et une date d'expiration future.
- **Retour arrière** : `sudo certbot delete --cert-name <nom_de_domaine>` supprime le certificat ; restaurer la configuration Nginx depuis la sauvegarde puis `sudo systemctl reload nginx`.