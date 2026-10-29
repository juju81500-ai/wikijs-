---
title: "Mise en situation professionnelle : Systèmes clients"
description: "Configurer et optimiser les systèmes Debian et Windows pour une meilleure performance, sécurité et accessibilité : gestion avancée du GRUB, extension du swap, activation du bureau à distance sécurisé avec vérification croisée depuis la machine du binôme."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Mise en situation professionnelle : Systèmes clients

## Configuration avancée des systèmes

## 🧱 Objectif

Configurer et optimiser les systèmes Debian et Windows pour une meilleure performance, sécurité et accessibilité : gestion avancée du GRUB, extension du swap, activation du bureau à distance sécurisé avec vérification croisée depuis la machine du binôme.

---

## 🐧 Debian 10 – Optimisations système

### ⏱ Réduction du temps d'affichage du GRUB

> Objectif : limiter le temps d'attente inutile au démarrage

### 🔧 Étapes

```bash
sudo nano /etc/default/grub
```

Modifier :

```bash
GRUB_TIMEOUT=2
```

Puis :

```bash
sudo update-grub
```

### ✅ Vérification

Redémarrer et observer le compte à rebours réduit.

---

### 🔄 Extension du SWAP à 1 Go

> Objectif : remplacer le swap initial de 256 Mo par un espace de 1 Go

#### 📌 Pré-requis

Utiliser l’espace **libre restant sur le disque principal (`/dev/sda`)**

### 🔧 Étapes

1. Créer une nouvelle partition avec `fdisk` :

```bash
sudo fdisk /dev/sda
```

- Créer une nouvelle partition Linux (type `82`) d’environ 1024 Mo

2. Formater en swap :

```bash
sudo mkswap /dev/sda1
```

3. Activer :

```bash
sudo swapon /dev/sda1
```

4. Modifier `/etc/fstab` pour montage permanent :

```bash
echo "/dev/sda1 none swap sw 0 0" | sudo tee -a /etc/fstab
```

5. Désactiver l’ancien swap :

```bash
sudo swapoff /dev/sda3
```

6. Mettre à jour l’entrée active :

```bash
sudo swapon --show
```

---

### 📦 Mise à jour complète du système Debian

```bash
sudo apt update && sudo apt full-upgrade -y
```

> ✅ Prendre un snapshot après la mise à jour complète.

---

## 🪟 Windows 10 – Configuration du bureau à distance sécurisé (RDP)

### 🎯 Objectif

Permettre une connexion distante RDP **sécurisée via NLA** pour ton binôme

### 🔧 Étapes

1. Ouvrir **Paramètres > Système > Bureau à distance**
2. Activer le bureau à distance
3. Vérifier que l’option **“Exiger l’authentification au niveau du réseau (NLA)”** est activée
4. Ajouter le binôme dans la liste des utilisateurs autorisés

#### PowerShell alternatif :

```powershell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

---

### 🔍 Vérification du port RDP

```powershell
netstat -an | findstr :3389
```

- Vérifier l’écoute sur `0.0.0.0:3389`
- Optionnel : utiliser `nmap` depuis Debian pour tester la connectivité

---

## 🔁 Test croisé avec le binôme

### 🧪 Étapes

1. Demander au binôme de se connecter à ton poste avec `mstsc` (adresse IP)
2. Valider la connexion : ouverture de session OK, droits restreints OK
3. Inversement, tester la connexion vers le poste Windows du binôme

---

## ✅ Résumé des validations

|Élément|Action/Vérification|
|---|---|
|GRUB réduit à 2s|Redémarrage plus rapide|
|SWAP Debian = 1 Go|swapon --show valide|
|Debian à jour|`apt update && upgrade` terminé|
|RDP activé avec NLA|Connexion distante sécurisée disponible|
|Binôme autorisé en RDP|Présent dans la liste des utilisateurs|
|Port RDP écouté (TCP 3389)|Visible via `netstat`|
|Connexion croisée fonctionnelle|RDP depuis et vers le poste du binôme|