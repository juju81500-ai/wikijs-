---
title: "TP – Découverte de vSphere (VMware ESXi)"
description: "- Éteindre la VM SRV2K19 (non utilisée ici)."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Découverte de vSphere (VMware ESXi)

## 📝 Étapes

### 1. Préparation dans VMware Workstation

- Éteindre la VM `SRV_2K19` (non utilisée ici).
- Créer une VM nommée `ESXi1`, type **ESXi 7**, avec stockage dans `D:\Machines virtuelles\ESXi1`

#### Configuration matérielle :

- 2 CPU / 1 cœur
- 6 Go RAM
- 1 carte réseau bridgée
- 1 disque dur de 40 Go (SCSI)
- 1 disque dur supplémentaire de 200 Go (SCSI)
- Utiliser l’ISO : `VMware-VMvisor-Installer-7.0U3-18644231.x86_64` (depuis `\\distrib\iso\virtualisation`)

### 2. Installation de `ESXi1`

- Installer ESXi sur le disque de 40 Go
- Choisir la langue **française**
- Définir le mot de passe de `root` (respecter les critères de complexité)
- Relever l’**adresse IP** attribuée à `ESXi1` à la fin de l’installation

### 3. Création de `ESXi2`

- Créer une seconde VM `ESXi2` avec la **même configuration** matérielle
- Stocker la VM dans `D:\Machines virtuelles\ESXi2`

---

## 🔧 Configuration via vSphere Web Client

Depuis l’hôte Windows :

1. Ouvrir un navigateur (Chrome, Firefox, Edge)
2. Accéder à l’adresse IP d’`ESXi1`
3. Se connecter avec le compte `root`
4. Accepter le certificat de sécurité non valide

### 4. Création du stockage local

- Aller dans **Stockage** > Créer une banque de données VMFS
- Nom : `DS-Local`
- Utiliser le disque de **200 Go** ajouté précédemment

### 5. Chargement de l’image ISO

- Naviguer dans `DS-Local`
- Charger l’ISO de **Windows Server 2019** dans le répertoire souhaité

### 6. Création d’une VM `SRV-1`

- Depuis `Machines virtuelles` > Nouvelle machine virtuelle
- Nom : `SRV-1`
- Paramètres :
    - 1 CPU / 1 cœur
    - 2 Go RAM
    - Disque dur : 32 Go
    - Image ISO : celle précédemment uploadée

### 7. Installation de l’OS invité

- Démarrer `SRV-1`
- Prendre la main via la **console Web**
- Suivre l’installation de Windows Server 2019
- Installer les **VMware Tools** une fois l’installation terminée

---

## ✅ À retenir pour les révisions

- Une **infrastructure vSphere** peut être simulée sous VMware Workstation à des fins pédagogiques
- ESXi est un hyperviseur de type 1, géré via **vSphere Web Client**
- La **banque de données (datastore)** est essentielle pour le stockage VM
- L’ajout d’un ISO au datastore permet de déployer facilement des OS dans les VMs

---

## 📌 Bonnes pratiques professionnelles

- Affecter des **noms clairs et explicites** aux VMs et datastores
- Créer un **stockage dédié** pour les VMs (second disque virtuel)
- Vérifier l’**adéquation entre ressources VM et hôte** pour assurer de bonnes performances
- Installer systématiquement les **VMware Tools** pour une meilleure intégration
- Utiliser une **architecture en miroir** (ESXi1 / ESXi2) pour les tests de montée en charge ou de résilience

---

## 🔗 Outils et manipulations clés

- ESXi 7 ISO : `VMware-VMvisor-Installer-7.0U3...`
- vSphere Web Client (navigateur)
- `DS-Local` (datastore)
- Console Web VMware pour démarrage et installation des VMs
- VMware Tools