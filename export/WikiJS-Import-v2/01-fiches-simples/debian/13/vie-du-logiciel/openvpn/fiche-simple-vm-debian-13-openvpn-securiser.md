---
title: "Fiche Simple - VM Debian 13 OpenVPN Securiser"
description: "Limiter les accès, protéger les clés et n’ouvrir que le flux VPN approuvé."
published: true
date: 2026-10-29T20:39:42Z
tags: ["openvpn", "debian13", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T20:39:42Z
dateModified: 2026-10-29T20:39:42Z
---

# Fiche_Simple_-_VM_Debian_13_OpenVPN_Securiser

- **Environnement** : VM Debian 13 dédiée à OpenVPN Community Edition
- **OS / Version** : Debian 13 Trixie; version des dépôts à vérifier sur l’hôte
- **Catégorie** : OpenVPN Community Edition / sécuriser
- **Tags** : `openvpn`, `debian13`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Limiter les accès, protéger les clés et n’ouvrir que le flux VPN approuvé.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les permissions des fichiers :
   ```bash
   sudo find /etc/openvpn/server -maxdepth 1 -type f -printf "%M %u:%g %p\n"
   ```
   👉 Explication : Vérifier que les clés privées et la configuration ne sont pas lisibles par des comptes ordinaires.

2. Examiner le pare-feu existant avant toute règle :
   ```bash
   sudo nft list ruleset
   ```
   👉 Explication : Commande en lecture seule. Définir la règle dans le gestionnaire déjà utilisé, limitée au port et aux sources prévus; ne pas superposer les gestionnaires.

3. Si UFW est déjà le pare-feu actif et que l’équipe réseau a approuvé ce flux, limiter l’ouverture :
   ```bash
   sudo ufw allow from VPN_SOURCE_CIDR to any port 1194 proto udp
   sudo ufw status numbered
   ```
   👉 Explication : remplacer VPN_SOURCE_CIDR par la plage approuvée; ne pas activer UFW ni superposer un pare-feu si un autre gestionnaire est utilisé.

4. Si une CRL est prévue, installer la CRL validée et configurer son chemin dans server.conf.
   👉 Explication : Contrôler la directive et le rechargement selon la version installée.

## 2. Production — Contrôles

Limiter l’écoute à l’interface prévue, vérifier les journaux d’authentification et tester révocation/expiration avec un client pilote.

## 3. Production — Sécurité

- TLS 1.2 minimum et suites AEAD supportées; appliquer le moindre privilège seulement après vérification de compatibilité.

## Validation et retour arrière

- **Validation** : Clés privées en mode 600, flux limité au port approuvé, révocation vérifiable.
- **Retour arrière** : restaurer la configuration antérieure vérifiée et arrêter le service ou la capture si la recette échoue; consigner le changement.

## Si le problème n’est pas résolu

- [OpenVPN Community Edition — documentation officielle](https://openvpn.net/community-resources/)
- [Étape suivante du guide](/01-fiches-simples/debian/13/vie-du-logiciel/openvpn/fiche-simple-vm-debian-13-openvpn-valider)