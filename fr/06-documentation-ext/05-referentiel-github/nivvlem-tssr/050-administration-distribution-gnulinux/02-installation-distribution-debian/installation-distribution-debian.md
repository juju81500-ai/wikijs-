---
title: "Installation d’une distribution Debian GNU/Linux"
description: "- Permet de tester Debian sans installation (exécution depuis le média)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Installation d’une distribution Debian GNU/Linux

## 💽 Les modes d’installation

### 🔸 Live-CD

- Permet de tester Debian sans installation (exécution depuis le média)
- Propose l’installation depuis l’environnement live
- Plusieurs variantes selon l’environnement de bureau (Gnome, KDE…)

### 🔸 DVD-ROM

- Image complète (offline), ne nécessite pas Internet
- Ne contient pas les dernières mises à jour

### 🔸 CD Netinstall

- Image minimale
- Téléchargement des paquets via un miroir en ligne
- Accès aux paquets les plus récents

### 🔸 Clé USB ou disque USB

- Alternatives modernes aux lecteurs optiques
- Outils recommandés :
    - **Ventoy** (Windows/Linux)
    - **Balena Etcher**
    - **Rufus** (Windows uniquement)
    - **Unetbootin**

### 🔸 Installation par le réseau (PXE)

- Utilisé dans les environnements professionnels
- Le BIOS télécharge automatiquement le programme d’installation

### 🔸 Automatisation/déploiement massif

- FAI (Fully Automatic Installation)
- CD personnalisés préconfigurés
- Outils de clonage : FOG, Clonezilla, Ghost, Acronis

---

## 🧱 Étapes d’installation Debian

### 🧭 Lancement de l’installeur

- Choix entre **mode graphique** ou **semi-graphique** (texte)
- Ce choix n’influence **pas** l’environnement du système installé

### 🗣️ Langue et disposition clavier

- Il est possible d’installer un système **en anglais** avec un **clavier français** (souvent utilisé en production)

### 🖥️ Nom d’hôte et domaine

- Nom de la machine (hostname)
- Domaine DNS (optionnel)

### 🔐 Choix du superutilisateur : root ou sudo

|Mode|Description|
|---|---|
|**Root activé**|Mot de passe demandé à l’installation, seul root peut administrer|
|**Root désactivé**|L’utilisateur créé peut utiliser `sudo`|

➡️ On peut activer root plus tard avec :

```bash
sudo passwd root
```

### 💾 Partitionnement du disque

- Minimum requis :
    - `/` (racine)
    - `swap`

### Recommandation pour le swap :

|RAM|Taille SWAP recommandée|
|---|---|
|< 1 Go|RAM x 1.5|
|≤ 2 Go|= RAM|
|> 2 Go|2 Go ou plus (si hibernation souhaitée)|

### 🎛️ Sélection des dépôts

- Dépôt Debian officiel par défaut (ex : ftp.fr.debian.org)
- Possibilité d’utiliser un **miroir** ou un **proxy**

### 📦 Choix des paquets à installer

- Interface Gnome / KDE / XFCE (pour postes clients)
- Serveur sans interface graphique (usage pro recommandé)

### 🔃 GRUB

- Installation de GRUB (programme de démarrage) en fin de processus

---

## ✅ À retenir pour les révisions

- Plusieurs modes d’installation sont disponibles selon les cas (Live, DVD, Netinstall, PXE)
- Partitionnement minimal requis : `/` et `swap`
- Choix du mode administrateur : `root` ou `sudo`
- Il est recommandé en entreprise d’avoir un système installé **en anglais** avec **clavier français**
- `GRUB` est le chargeur de démarrage par défaut

---

## 📌 Bonnes pratiques professionnelles

- Toujours tester un système via Live-CD ou VM avant installation réelle
- Séparer `/home` sur une autre partition si possible (sécurité, facilité de réinstallation)
- Utiliser la **Netinstall** pour bénéficier de paquets à jour
- Garder l’environnement minimal sur les serveurs (sans interface graphique)
- Documenter le schéma de partitionnement et les choix réseau

---

## 🔗 Liens utiles

- [Images Debian officielles](https://www.debian.org/CD/http-ftp/#stable)
- [Ventoy – clé multiboot](https://www.ventoy.net/)
- [iPXE – Boot réseau](http://ipxe.org/)