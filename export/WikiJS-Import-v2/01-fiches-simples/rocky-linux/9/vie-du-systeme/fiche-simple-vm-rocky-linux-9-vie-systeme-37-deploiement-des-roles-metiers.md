---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 37 Deploiement Des Roles Metiers"
description: "Installer le rôle attendu."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-37"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-37`

---

## Problème précis à résoudre

Installer le rôle attendu.

## 1. Hors-Production (Lab / Test / POC)

1. Installer le paquet du rôle (exemple web) :
   ```bash
   sudo dnf install -y nginx
   sudo systemctl enable --now nginx
   ```
   👉 Explication : installe et démarre le service.

2. Ouvrir le flux dans firewalld :
   ```bash
   sudo firewall-cmd --permanent --add-service=https
   sudo firewall-cmd --reload
   ```
   👉 Explication : autorise uniquement HTTPS.

3. Autoriser le rôle dans SELinux si nécessaire :
   ```bash
   sudo setsebool -P httpd_can_network_connect on
   ```
   👉 Explication : booléen permanent pour un proxy inverse.

## 2. Production — Contrôles

Déployer avec un outil de configuration (Ansible) pour la reproductibilité.

## 3. Production — Sécurité

Un rôle par machine quand c'est possible.

## Validation et retour arrière

- **Validation** : Le service répond sur le port prévu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Rocky 9 Pile Web Configurer Nginx PHP FPM](</01-fiches-simples/rocky-linux/9/vie-du-logiciel/pile-web/fiche-simple-vm-rocky-9-pile-web-configurer-nginx-php-fpm>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)