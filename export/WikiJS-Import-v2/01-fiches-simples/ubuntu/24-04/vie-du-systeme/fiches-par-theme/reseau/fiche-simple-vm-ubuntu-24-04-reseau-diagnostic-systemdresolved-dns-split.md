---
title: "Fiche Simple - VM Ubuntu 24.04 Reseau Diagnostic SystemdResolved DNS Split"
description: "Diagnostiquer et configurer la résolution DNS par interface sur Ubuntu Server, notamment pour séparer les noms internes d'entreprise des noms publics."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[netplan]", "[systemd-resolved]", "[dns]", "[diagnostic]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Reseau_Diagnostic_SystemdResolved_DNS_Split.md

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS avec Netplan et `systemd-resolved`
- **Catégorie** : Réseau / DNS
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[netplan]`, `[systemd-resolved]`, `[dns]`, `[diagnostic]`

## 🎯 Problème précis à résoudre
Diagnostiquer et configurer la résolution DNS par interface sur Ubuntu Server, notamment pour séparer les noms internes d'entreprise des noms publics.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever le service DNS, les DNS par lien et les routes DNS :
   ```bash
   resolvectl status
   resolvectl dns
   resolvectl domain
   ```
2. Comparer les résultats d'une résolution ciblée :
   ```bash
   resolvectl query serveur.corp.example
   resolvectl query example.com
   ```
   👉 *Explication : `resolvectl` montre quel lien et quels serveurs DNS sont utilisés; ne pas déduire la configuration réelle du seul contenu de `/etc/resolv.conf`.*

## ⚡ 2. Production — Façon Simplifiée
1. Identifier l'interface et le fichier Netplan qui la gère; vérifier si cloud-init possède cette configuration.
2. Dans le fichier Netplan approprié, déclarer le DNS interne et le domaine de recherche/routage selon le plan DNS :
   ```yaml
   network:
     version: 2
     ethernets:
       enp0s3:
         dhcp4: true
         nameservers:
           addresses: [192.0.2.53]
           search: [corp.example]
   ```
3. Tester avant de confirmer puis vérifier le résultat :
   ```bash
   sudo netplan try
   resolvectl status
   resolvectl query serveur.corp.example
   ```
   👉 *Explication : remplacer interface et résolveur par ceux de l'organisation; pour un routage DNS conditionnel, confirmer le support des domaines de routage par le backend Netplan et `systemd-resolved` utilisés.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas ajouter de résolveur public en secondaire sur une machine qui dépend du DNS interne; les requêtes internes pourraient être envoyées au mauvais serveur.
2. Ne pas éditer directement `/etc/resolv.conf` s'il s'agit d'un lien géré par `systemd-resolved`.
3. Garder une console ou un accès hyperviseur pendant un changement Netplan; ne pas appliquer à distance sans retour arrière.

## ✅ Validation et retour arrière
- Confirmer les DNS attachés au lien, le domaine de routage et la résolution de noms internes et externes attendue.
- En cas d'échec, laisser `netplan try` annuler ou restaurer le fichier Netplan sauvegardé depuis la console.
- Vérifier les journaux avec `journalctl -u systemd-resolved` et `journalctl -u systemd-networkd`.