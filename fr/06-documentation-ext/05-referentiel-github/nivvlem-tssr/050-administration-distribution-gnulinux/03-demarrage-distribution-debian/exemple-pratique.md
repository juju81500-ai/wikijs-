---
title: "TP – Démarrage et gestion des services Debian"
description: "systemctl get-default  # ➜ graphical.target"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Démarrage et gestion des services Debian 

# 🧱 TP1 – Démarrer et arrêter Debian via SystemD

### 🔎 Identifier la cible par défaut

```bash
systemctl get-default  # ➜ graphical.target
```

### 📖 Consulter les cibles disponibles

```bash
man systemd  # /graphical.target ➜ multi-user.target
```

### ⚙️ Changer la cible par défaut (mode console)

```bash
sudo systemctl set-default multi-user.target
```

### 🔃 Redémarrer et tester

```bash
sudo shutdown -r now
# Pas d’environnement graphique (comportement attendu)
```

### 🚀 Lancer manuellement l’environnement graphique

```bash
sudo systemctl isolate graphical.target
```

---

# 🧱 TP2 – Gérer les services `cron` et `sshd`

## 🔒 Partie 1 – SSHD

### 🔍 Trouver les fichiers associés à `sshd`

```bash
# Fichier unit systemd
systemctl status ssh

# Binaire
which sshd

# Fichier de configuration
sudo find /etc -type f -name '*sshd*conf*'
```

## ⏰ Partie 2 – CRON

### 🔎 Le service est-il activé au démarrage ?

```bash
systemctl status cron.service  # ➜ active (enabled)
```

### 🛑 Arrêter temporairement le service

```bash
sudo systemctl stop cron.service
```

### 🔄 Redémarrer la machine et vérifier l’état

```bash
sudo shutdown -r now
systemctl status cron.service  # ➜ actif à nouveau
```

### ❌ Désactiver le lancement automatique au démarrage

```bash
sudo systemctl disable cron.service
```

### ✅ Restaurer les paramètres par défaut

```bash
sudo systemctl enable cron.service
sudo systemctl start cron.service
```

---

## ✅ À retenir pour les révisions

- `systemctl set-default` modifie le **mode de démarrage** (graphique ou console)
- Les **cibles SystemD** remplacent les runlevels SysV (ex : 3 → multi-user)
- `systemctl status` permet de **vérifier les services** actifs
- `enable` et `disable` contrôlent la **persistance** au redémarrage

---

## 📌 Bonnes pratiques professionnelles

- Ne jamais supprimer ou modifier directement les fichiers de `/boot` ou `/etc/systemd`
- Toujours tester les modifications de cible avec `isolate` avant `set-default`
- Documenter les changements sur un poste serveur (journalisation)
- Utiliser `systemctl list-units` pour surveiller les services en temps réel

---

## 🔗 Ressources utiles

- [SystemD Targets – Arch Wiki](https://wiki.archlinux.org/title/systemd#Targets)
- [Debian SystemD documentation](https://wiki.debian.org/systemd)