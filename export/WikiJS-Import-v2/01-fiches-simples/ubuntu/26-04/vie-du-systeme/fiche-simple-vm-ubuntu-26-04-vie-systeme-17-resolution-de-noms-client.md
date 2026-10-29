---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs DNS."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : VM Ubuntu Server 26.04 LTS
- **OS / Version** : Ubuntu 26.04; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les DNS dans Netplan (section `nameservers` de l'étape 16) puis appliquer :
   ```bash
   sudoedit /etc/netplan/01-reseau.yaml
   sudo netplan try
   ```
   👉 Explication : ligne `addresses: [192.0.2.53]`; `/etc/resolv.conf` est un lien vers le résolveur local `systemd-resolved` : ne pas l'éditer à la main.

2. Tester :
   ```bash
   resolvectl status
   resolvectl query ubuntu.com
   getent hosts ubuntu.com
   ```
   👉 Explication : `resolvectl` montre les DNS par interface; `getent` vérifie la résolution par le même chemin que les applications.

## 2. Production — Contrôles

Deux serveurs DNS internes minimum.

## 3. Production — Sécurité

Éviter les DNS publics sur les machines de domaine.

## Validation et retour arrière

- **Validation** : `getent hosts` renvoie une adresse.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 26.04](/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)