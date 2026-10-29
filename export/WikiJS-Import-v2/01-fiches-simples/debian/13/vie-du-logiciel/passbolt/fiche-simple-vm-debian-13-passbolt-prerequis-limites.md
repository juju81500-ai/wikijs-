---
title: "Fiche Simple - VM Debian 13 Passbolt Prerequis Limites"
description: "Préparer DNS, base, SMTP, TLS et récupération des clés avant l’installation Passbolt CE."
published: true
date: 2026-10-29T20:47:59Z
tags: ["debian13", "passbolt", "secrets", "tls", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:47:59Z
dateModified: 2026-10-29T20:47:59Z
---

# Fiche_Simple_-_VM_Debian_13_Passbolt_Prerequis_Limites

- **Environnement** : VM Debian 13 dédiée avec domaine, base et SMTP définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : gestionnaire de secrets / serveur
- **Tags** : `debian13`, `passbolt`, `secrets`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Préparer DNS, base, SMTP, TLS et récupération des clés avant l’installation Passbolt CE.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier Debian, temps, stockage et DNS
   ```bash
   cat /etc/os-release
   timedatectl status
   df -h
   getent hosts passbolt.example.com
   ```
   👉 Explication : remplacer le FQDN par le nom à remplacer; horloge correcte.

2. Définir base, SMTP et propriétaire
   ```text
   Navigateur > ouvrir la documentation officielle : https://www.passbolt.com/docs/hosting/install/ce/debian/
   ```
   👉 Explication : confirmer versions supportées dans guide CE. Détail à confirmer dans la documentation officielle avant application : Documenter base supportée, relais mail, stockage, responsable, rétention et RPO/RTO.

3. Vérifier les ports exposés
   ```bash
   sudo ss -lntp | grep -E ":(80|443|3306)\b" || true
   ```
   👉 Explication : base ne doit pas être joignable depuis les clients.

## 2. Production — Contrôles

Confirmer support Debian 13, base, DNS, SMTP, TLS et procédure de reprise des clés serveur.

## 3. Production — Sécurité

- Isoler le serveur, limiter les administrateurs et protéger la clé privée.
- Ne jamais inclure phrase secrète ou mot de passe réel dans les documents.
- Planifier sauvegarde cohérente des clés, config et données.

## Validation et retour arrière

- **Validation** : Architecture et restauration clés sont validées avant installation.
- **Retour arrière** : Reporter si clés et plan de reprise ne sont pas établis.

## Si le problème n'est pas résolu

- [Passbolt — installation Debian 13 CE](https://www.passbolt.com/docs/hosting/install/ce/debian/)
- [Passbolt — configuration serveur](https://www.passbolt.com/docs/hosting/configure/)
- [Passbolt — sauvegarde](https://www.passbolt.com/docs/hosting/backup/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/passbolt/fiche-simple-vm-debian-13-passbolt-installer>)