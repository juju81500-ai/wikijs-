---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 39 Chiffrement Des Flux Pki"
description: "Chiffrer les services exposés."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-39"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

---

## Problème précis à résoudre

Chiffrer les services exposés.

## 1. Hors-Production (Lab / Test / POC)

1. Installer certbot via EPEL (adapter `www.exemple.fr`) :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf install -y certbot python3-certbot-nginx
   sudo certbot --nginx -d www.exemple.fr
   ```
   👉 Explication : obtient et installe un certificat public.

2. Contrôler le renouvellement :
   ```bash
   sudo certbot renew --dry-run
   ```
   👉 Explication : simule le renouvellement.

3. Contrôler la date d'expiration :
   ```bash
   echo | openssl s_client -connect www.exemple.fr:443 2>/dev/null | openssl x509 -noout -dates
   ```
   👉 Explication : affiche les dates de validité.

## 2. Production — Contrôles

Superviser l'expiration; utiliser une PKI interne pour les noms non publics.

## 3. Production — Sécurité

Clé privée en mode `600`; TLS 1.2 minimum (politique crypto système).

## Validation et retour arrière

- **Validation** : Le certificat est valide et la chaîne complète.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Securite Certbot TLS](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/certbot/fiche-simple-vm-rocky-9-securite-certbot-tls>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)