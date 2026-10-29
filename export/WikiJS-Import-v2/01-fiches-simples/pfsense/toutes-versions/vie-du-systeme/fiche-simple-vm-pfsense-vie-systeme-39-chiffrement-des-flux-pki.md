---
title: "Fiche Simple - VM pfSense Vie Systeme 39 Chiffrement Des Flux Pki"
description: "Remplacer le certificat auto-signé du GUI."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-39"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

---

## Problème précis à résoudre

Remplacer le certificat auto-signé du GUI.

## 1. Hors-Production (Lab / Test / POC)

1. Créer ou importer une autorité : System > Certificate Manager > CAs > Add, puis Certificates > Add/Sign (Common Name `fw01.exemple.lan`).
   👉 Explication : génère un certificat serveur signé par votre autorité.

2. Appliquer le certificat : System > Advanced > Admin Access > SSL/TLS Certificate, puis Save.
   👉 Explication : le GUI présente le certificat reconnu par les postes.

3. Contrôler en shell :
   ```sh
   echo | openssl s_client -connect IP_LAN:443 2>/dev/null | openssl x509 -noout -subject -dates
   ```
   👉 Explication : affiche le sujet et les dates de validité du certificat servi.

## 2. Production — Contrôles

Surveiller les dates d'expiration; utiliser le paquet `acme` si le nom est public.

## 3. Production — Sécurité

Clé d'au moins 2048 bits (RSA) ou ECDSA; TLS 1.2 minimum.

## Validation et retour arrière

- **Validation** : Le navigateur accepte le certificat sans alerte.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)