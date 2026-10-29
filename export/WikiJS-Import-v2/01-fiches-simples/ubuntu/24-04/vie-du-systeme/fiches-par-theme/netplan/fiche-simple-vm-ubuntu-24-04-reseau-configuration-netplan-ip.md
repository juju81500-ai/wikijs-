---
title: "Diagnostic et dépannage Netplan sur Ubuntu 24.04"
description: "Diagnostiquer une configuration Netplan qui ne s'applique pas ou qui est écrasée au redémarrage, sans perdre l'accès à la VM."
published: true
date: 2026-10-29T20:22:42Z
tags: ["ubuntu24.04", "netplan", "diagnostic", "cloud-init", "reseau"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Diagnostic et dépannage Netplan sur Ubuntu 24.04

- **Environnement** : VM Ubuntu Server 24.04 LTS
- **Catégorie** : Réseau / Netplan
- **Tags** : `ubuntu24.04`, `netplan`, `diagnostic`, `cloud-init`, `reseau`

## 🎯 Problème précis à résoudre

Diagnostiquer une configuration Netplan qui ne s'applique pas ou qui est écrasée au redémarrage, sans perdre l'accès à la VM.

## 🧪 1. Collecte non destructive

```bash
ls -l /etc/netplan/
cloud-init status --long
sudo netplan get
ip -br addr
ip route
resolvectl status
```
   👉 Explication : relève les fichiers Netplan, l'état cloud-init, la configuration et le réseau actuels.

Repérer quel fichier et quel outil sont propriétaires de la configuration. Si cloud-init gère le réseau, corriger la source cloud-init appropriée ou désactiver son contrôle réseau selon la procédure de l'image ; ne pas éditer un fichier généré en supposant qu'il persistera.

## ⚡ 2. Valider sans appliquer

Après sauvegarde du fichier réellement géré, contrôler le YAML et la génération backend :

```bash
sudo netplan generate
```
   👉 Explication : génère la configuration pour détecter les erreurs de syntaxe sans l'appliquer.

Corriger les erreurs de syntaxe et vérifier interface, adresse, route, DNS, renderer et conflits avec d'autres fichiers sous `/etc/netplan/`.

## 🔒 3. Appliquer avec accès de secours

Depuis la console de l'hyperviseur ou avec un accès hors bande :

```bash
sudo netplan try
```
   👉 Explication : applique avec retour arrière automatique si vous ne confirmez pas dans le délai.

Confirmer seulement après test de la nouvelle adresse et de la passerelle. Si l'accès est perdu ou si le test échoue, laisser Netplan annuler puis restaurer la sauvegarde. Ne pas enchaîner `netplan apply` après un test échoué.