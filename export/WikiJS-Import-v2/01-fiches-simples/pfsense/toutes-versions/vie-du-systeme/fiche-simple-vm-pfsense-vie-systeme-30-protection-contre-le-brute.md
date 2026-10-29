---
title: "Fiche Simple - VM pfSense Vie Systeme 30 Protection Contre Le Brute"
description: "Bloquer les tentatives répétées de connexion."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-30"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_30_Protection_Contre_Le_Brute

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 30 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-30`

---

## Problème précis à résoudre

Bloquer les tentatives répétées de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier dans System > Advanced > Admin Access que la protection contre le brute-force (« Login Protection ») est active pour le GUI et SSH.
   👉 Explication : les adresses fautives sont placées dans une table de blocage.

2. Lister et débloquer les adresses (Diagnostics > Tables > `sshguard`) ou en shell :
   ```sh
   pfctl -t sshguard -T show
   pfctl -t sshguard -T delete IP_BLOQUEE
   ```
   👉 Explication : `IP_BLOQUEE` est l'adresse à débloquer après vérification.

3. Compléter par le paquet Suricata ou Snort si le débit le permet.
   👉 Explication : détecte les attaques connues en plus du blocage.

## 2. Production — Contrôles

Surveiller les adresses bloquées dans les journaux d'authentification.

## 3. Production — Sécurité

Ne pas bloquer son propre poste : l'ajouter à la liste de confiance.

## Validation et retour arrière

- **Validation** : Une série d'échecs de test aboutit à un blocage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)