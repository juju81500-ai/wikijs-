---
title: "Fiche Simple - VM Debian 13 Traefik Securiser"
description: "Activer HTTPS (certificat ACME ou fichier), rediriger HTTP vers HTTPS et limiter l'exposition."
published: true
date: 2026-10-29T20:33:54Z
tags: ["debian13", "traefik", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:33:54Z
dateModified: 2026-10-29T20:33:54Z
---

# Fiche_Simple_-_VM_Debian_13_Traefik_Securiser

- **Environnement** : VM Debian 13 Trixie
- **OS / Version** : Debian 13 Trixie; Traefik v3 (binaire officiel)
- **Catégorie** : reverse proxy / Traefik / Sécuriser (TLS, redirection, pare-feu)
- **Tags** : `debian13`, `traefik`, `securite`

---

## Problème précis à résoudre

Activer HTTPS (certificat ACME ou fichier), rediriger HTTP vers HTTPS et limiter l'exposition.

## 1. Hors-Production (Lab / Test / POC)

1. Option ACME : ajouter un résolveur de certificats :
   ```bash
   sudo tee -a /etc/traefik/traefik.yml >/dev/null <<'EOF'
   certificatesResolvers:
     le:
       acme:
         email: ADMIN@example.net
         storage: /var/lib/traefik/acme.json
         httpChallenge:
           entryPoint: web
   EOF
   sudo install -o traefik -g traefik -m 0600 /dev/null /var/lib/traefik/acme.json
   ```
   👉 Explication : remplacer `ADMIN@example.net` (à remplacer) ; utiliser d'abord le serveur de préproduction Let's Encrypt (`caServer`) en lab ; nécessite un nom DNS public et le port 80.

2. Passer le routeur en HTTPS :
   ```bash
   sudo tee /etc/traefik/dynamic/app.yml >/dev/null <<'EOF'
   http:
     routers:
       app-http:
         rule: "Host(`APP.example.net`)"
         entryPoints: [web]
         middlewares: [to-https]
         service: app
       app:
         rule: "Host(`APP.example.net`)"
         entryPoints: [websecure]
         tls:
           certResolver: le
         service: app
     middlewares:
       to-https:
         redirectScheme:
           scheme: https
           permanent: true
     services:
       app:
         loadBalancer:
           servers:
             - url: "http://127.0.0.1:PORT_APP"
   EOF
   ```
   👉 Explication : la redirection permanente envoie tout le trafic HTTP vers HTTPS.

3. Option certificat fourni : limiter les versions TLS :
   ```bash
   sudo tee /etc/traefik/dynamic/tls.yml >/dev/null <<'EOF'
   tls:
     options:
       default:
         minVersion: VersionTLS12
     certificates:
       - certFile: /etc/traefik/certs/APP.crt
         keyFile: /etc/traefik/certs/APP.key
   EOF
   ```
   👉 Explication : uniquement si le certificat est fourni (ex. AC interne) ; remplacer les chemins (à remplacer) ; clés en `0600` propriétaire `traefik`.

4. Filtrer le réseau :
   ```bash
   sudo nft list ruleset | head -20
   # si ufw est utilisé :
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   ```
   👉 Explication : ne pas ouvrir d'autre port.

## 2. Production — Contrôles

Certificats supervisés (échéance), sauvegarde de `acme.json`, journaux centralisés, revue des routeurs exposés.

## 3. Production — Sécurité

- `acme.json` en `0600`, jamais versionné.
- Ne jamais écrire de jeton API DNS dans les fichiers ; utiliser un fichier d'environnement en `0600` pour l'unité.
- Aucun tableau de bord public.

## Validation et retour arrière

- **Validation** : `curl -I https://APP.example.net/` répond avec un certificat valide et HTTP redirige.
- **Retour arrière** : retirer le résolveur et revenir au routeur HTTP, ou restaurer la sauvegarde de `/etc/traefik`.

## Si le problème n'est pas résolu

- [Traefik — Prérequis et limites](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-prerequis-limites)
- [Traefik — Installer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-installer)
- [Traefik — Configurer (statique, dynamique, premier service)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-configurer)
- [Traefik — Valider (recette)](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-valider)
- [Traefik — Sauvegarder et restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-sauvegarder-restaurer)
- [Traefik — Mise à jour et retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/traefik/fiche-simple-vm-debian-13-traefik-mettre-a-jour)
- [Guide complet Traefik v3.1 et Let's Encrypt (variante Docker)](/02-fiches-completes/transverses/docker/installation-deploiement/06-reverse-proxy-traefik-v31-letsencrypt-docker)
- [Traefik — documentation officielle](https://doc.traefik.io/traefik/)
- [Série Traefik sous Docker](/01-fiches-simples/transverses/docker/traefik/fiche-simple-docker-conteneur-traefik-configuration-statique)