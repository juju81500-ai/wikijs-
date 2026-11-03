---
title: "Mise en situation professionnelle : Systèmes clients"
description: "Réaliser l’installation initiale complète et méthodique des deux systèmes clients (Windows 10 et Debian 10), effectuer un partitionnement adapté avec gestion des contraintes pédagogiques, désactiver Windows Update, puis vérifier la connectivité réseau bilatérale avec les machines du binôme."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Mise en situation professionnelle : Systèmes clients

## Installation des systèmes

## 🧱 Objectif

Réaliser l’installation initiale complète et méthodique des deux systèmes clients (Windows 10 et Debian 10), effectuer un partitionnement adapté avec gestion des contraintes pédagogiques, désactiver Windows Update, puis vérifier la **connectivité réseau bilatérale** avec les machines du binôme.

---

## 🖥️ Création des machines virtuelles

Les VMs doivent être créées sous **VMware Workstation**. On utilise ici une carte réseau **en mode Bridged** afin que chaque machine dispose d'une **adresse IP réelle** sur le réseau local, condition indispensable pour la communication avec le poste du binôme.

### 📌 VM Windows 10 Professionnel

- **Nom de la VM** : `W10-MD`
- **Système d’exploitation** : Windows 10 Professionnel (x64)
- **ISO** : `\\10.0.0.6\Distrib\iso\os\windows\10`
- **Configuration matérielle** :
    - **CPU** : 2 vCPU (selon recommandations Microsoft)
    - **RAM** : 4 Go
    - **Disques** :
        - Disque principal : 32 Go (pour le système)
        - Disque secondaire : 40 Go (pour les données – à préparer pour la suite de la MSP)
    - **Carte réseau** : 1 carte en mode **Bridged**

### 📌 VM Debian 10 (interface graphique)

- **Nom de la VM** : `DEB10-MD`
- **Système** : Debian 10.x (Buster) – ISO version DVD avec interface graphique
- **ISO** : `\\10.0.0.6\Distrib\iso\os\unix-linux\linux\Debian\debian10Buster`
- **Configuration matérielle** :
    - **CPU** : 1 vCPU
    - **RAM** : 2 Go
    - **Disques** :
        - Disque principal : 20 Go (installation système)
        - Disque secondaire : 40 Go (données, stockage – utilisé dans les étapes suivantes)
    - **Carte réseau** : 1 carte en mode **Bridged**

> 🔁 Le disque supplémentaire de 40 Go est à **laisser vide** à ce stade : il sera utilisé dans les étapes ultérieures (DATA, LVM, /var/log, etc.).

---

## 🧭 Partitionnement personnalisé de Debian (20 Go)

La création des partitions est **manuelle** et doit respecter les contraintes suivantes :

|Point de montage|Taille|Type système de fichiers|Remarques|
|---|---|---|---|
|`/boot`|512 Mo|ext4|Nécessaire au démarrage|
|`swap`|256 Mo|swap|Minimum initial demandé|
|`/home`|1 Go|ext4|Pour tests → volontairement sous-estimé|
|`/`|17 Go|ext4|Système de base|

- **Ne pas allouer tout l’espace du disque** : laisser un peu d’espace libre si LVM ou extensions ultérieures prévues.
- **Sélectionner ftp.fr.debian.org** comme source de paquets.
- Conserver uniquement la **sélection par défaut des paquets**.

---

## ⚙️ Paramétrage initial de Windows 10

### 🔧 Étapes

1. Lors de l'installation, définir un nom d’ordinateur `W10-MD`.
2. Une fois l’installation terminée :
    - Ouvrir `services.msc`
    - Rechercher le service **Windows Update**
    - Clic droit > Propriétés > Type de démarrage : **Désactivé** > Appliquer
    - Arrêter le service si actif

> ❌ Cette étape est essentielle pour empêcher les connexions non souhaitées au WAN ENI.

---

## 🌐 Vérification de la connectivité réseau

### 🧪 Objectif : s’assurer que chaque machine peut joindre celles du binôme

#### ✅ À tester :

- Depuis `W10-MD` → `DEB10-Binôme`
- Depuis `DEB10-MD` → `W10-Binôme`

### 🛠️ Outils à utiliser :

- Sous Windows :
    - `ping`, `ipconfig`, `tracert`, `netstat -r`
- Sous Debian :
    - `ip a`, `ping`, `traceroute`, `arp`, `ip route`

> 📌 Vérifier que chaque VM est bien en **mode Bridged** et dispose d'une IP sur le même sous-réseau que celle du binôme.

---

## 🧰 Bonnes pratiques à retenir

- Toujours **nommer clairement les machines** (`W10-MD`, `DEB10-MD`, etc.)
- Prendre des **captures d’écran de chaque étape importante** (partitionnement, test réseau, désactivation Windows Update)
- Documenter les IP, nom, OS, CPU/RAM/Disque dans un **tableau synthétique `.md`**
- **Créer un snapshot post-installation** de chaque VM pour rollback facile

---

## ✅ Résumé des validations

|Étape|Action réalisée|Vérification|
|---|---|---|
|Création VM Windows 10|Nom, disques, ISO, Bridged|VM démarrée|
|Création VM Debian|Nom, disques, ISO, Bridged|Interface graphique OK|
|Partitionnement Debian manuel|`/`, `/boot`, `/home`, swap|Table de partition visible|
|Désactivation Windows Update|Service désactivé|Plus de MAJ actives|
|Tests réseau croisés binôme|ping entre toutes les VMs|Réponses ping correctes|
|Snapshots post-installation|Snapshots nommés et datés|Restauration possible|