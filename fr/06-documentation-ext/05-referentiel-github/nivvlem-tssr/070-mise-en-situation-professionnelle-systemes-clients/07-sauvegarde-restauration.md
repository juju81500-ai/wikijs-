---
title: "Mise en situation professionnelle : Systèmes clients"
description: "Mettre en œuvre une stratégie de sauvegarde locale et distante sur les systèmes Debian 10 et Windows 10 : automatisation des sauvegardes de données, duplication sur la machine du binôme, création d’image système et configuration de la restauration."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Mise en situation professionnelle : Systèmes clients

## Sauvegarde et restauration

## 🧱 Objectif

Mettre en œuvre une stratégie de sauvegarde locale et distante sur les systèmes Debian 10 et Windows 10 : automatisation des sauvegardes de données, duplication sur la machine du binôme, création d’image système et configuration de la restauration.

---

## 🐧 Debian 10 – Sauvegarde planifiée (cron + tar)

### 📝 Objectif

Sauvegarder automatiquement :

- Les **dossiers personnels** des utilisateurs (`/home`)
- Les **dossiers partagés de service** (`/services`)

### 🔧 Script de sauvegarde `backup.sh`

```bash
#!/bin/bash
DATE=$(date +%F)
BACKUP_DIR="/var/backups"
mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/home_$DATE.tar.gz" /home
 tar -czf "$BACKUP_DIR/services_$DATE.tar.gz" /services
```

- Sauvegarde compressée au format `.tar.gz`
- Les fichiers sont nommés avec la date du jour

### 🔁 Planification avec `cron`

```bash
sudo crontab -e
```

Ajouter :

```cron
30 12 * * * /root/backup.sh
```

> Lance la sauvegarde tous les jours à 12h30

### ✅ Vérification

```bash
ls /var/backups/
```

---

## 🐧 Duplication distante avec `scp`

### 🎯 Objectif

Copier automatiquement les archives de sauvegarde vers la Debian du binôme

### 🔧 Prérequis

- Le dossier distant existe (ex : `/home/backup-md` sur le binôme)
- SSH actif sur la Debian du binôme

### 🔧 Script `scp_backup.sh`

```bash
#!/bin/bash
scp /var/backups/*.tar.gz md@10.107.200.84:/home/backup-md/
```

### ⏱ Planification :

```cron
45 12 * * * /root/scp_backup.sh
```

> 💡 Utiliser des **clés SSH** pour éviter l’interaction humaine (optionnel, mais recommandé)

### 🔍 Installation de scp si absent

```bash
sudo apt install openssh-client
```

---

## 🪟 Windows 10 – Image système

### 🎯 Objectif

Créer une image complète du système pour pouvoir le restaurer en cas de panne grave

### 🧱 Étapes

1. Ajouter un disque virtuel de **60 Go** via VMware
2. Aller dans **Panneau de configuration > Sauvegarder et restaurer (Windows 7)**
3. Cliquer sur **Créer une image système**
4. Choisir le disque de 60 Go comme destination
5. Lancer la création de l’image

### ✅ Vérification

- Vérifier la présence du dossier `WindowsImageBackup` sur le disque cible

---

## 🪟 Windows 10 – Sauvegarde planifiée des données

### 🎯 Objectif

Sauvegarder tous les jours à 12h45 le contenu de `D:\Support_Info` vers le partage `Support_Info` de ton binôme

### 🔧 Étapes

1. Ouvrir le **Planificateur de tâches**
2. Créer une tâche :
    - Horaire : tous les jours à 12h45
    - Action : lancer un script `.bat` :

```bat
@echo off
xcopy D:\Support_Info \\W10-Binome\Support_Info$\Sauvegarde_MD /E /I /Y
```

> 💡 Le dossier `Sauvegarde_MD` doit exister côté binôme

---

## 🪟 Windows 10 – Points de restauration

### 🎯 Objectif

Activer les points de restauration système pour la partition `C:`

### 🔧 Étapes

1. **Panneau de configuration > Système > Protection du système**
2. Sélectionner le lecteur `C:` > Configurer
3. Activer la protection
4. Définir l’espace disque utilisé à **8%** (~2,5 Go sur 32 Go)
5. Créer un point de restauration manuel pour vérification

---

## ✅ Résumé des validations

|Élément|Action / Résultat attendu|
|---|---|
|Script de sauvegarde Debian|Créé, planifié à 12h30, `.tar.gz` dans `/var/backups`|
|SCP Debian → Binôme|Fichiers transférés tous les jours à 12h45|
|Image système Windows|Présente sur disque 60 Go (WindowsImageBackup)|
|Sauvegarde Support_Info planifiée|Script xcopy exécuté, dossier binôme alimenté|
|Points de restauration C: activés|Historique OK, espace disque réservé|