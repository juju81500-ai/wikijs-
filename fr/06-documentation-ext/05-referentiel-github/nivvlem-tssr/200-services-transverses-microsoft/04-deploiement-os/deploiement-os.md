---
title: "Déploiement d’un système d’exploitation"
description: "Dans une infrastructure professionnelle, il est nécessaire de :"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Déploiement d’un système d’exploitation
## 🧩 Contexte

Dans une infrastructure professionnelle, il est nécessaire de :

- Déployer rapidement des systèmes d’exploitation (Windows)
- Standardiser les postes de travail
- Gagner du temps et réduire les coûts de maintenance
- Gérer le **cycle de vie** des OS et des applications

Exemples de cas :

- **Renouvellement de parc**
- **Déploiement en masse** sur un nouveau site
- **Remise à zéro rapide** d’un poste défectueux

---

## 📦 Images de partition vs images d'installation

|Type d'image|Description|Avantages|Inconvénients|
|---|---|---|---|
|Image de partition|Clone complet d’un disque ou d’une partition (Ghost, Clonezilla)|Déploiement ultra-rapide|Lié au matériel (HAL), peu flexible|
|Image d'installation|Image type Windows (WIM), installée via WDS/MDT|Modulaire, personnalisable, compatible matériel varié|Installation plus longue qu'un clone|

### Image d'installation (WIM)

- Format **Windows Imaging Format (WIM)**
- Peut être **mise à jour** (intégration de patches, drivers...)
- Supporte **des déploiements variés** sur différents matériels

---

## 🚀 Solutions de déploiement

|Solution|Usage|
|---|---|
|Manuel (clé USB ISO)|Pour tests ou installation unique|
|Image de partition (Ghost, Clonezilla)|Clonage en masse homogène|
|WDS (Windows Deployment Services)|Déploiement PXE automatisé|
|MDT (Microsoft Deployment Toolkit)|Solution avancée, personnalisable|
|SCCM (Endpoint Configuration Manager)|Déploiement à grande échelle, gestion du cycle de vie|

---

## 🛠️ Solutions Microsoft pour le déploiement

### WDS (Windows Deployment Services)

- Permet un **démarrage PXE** (boot réseau)
- Installation automatique d’une **image WIM**
- Gestion centralisée des images

### MDT (Microsoft Deployment Toolkit)

- S’appuie sur WDS ou un support autonome (USB, DVD)
- Offre des **séquences de tâches** avancées :
    - Installation de Windows
    - Intégration de drivers
    - Installation d’applications
    - Configuration post-installation
- Supporte des scénarios **ZTI (Zero Touch Installation)** ou **LTI (Lite Touch Installation)**

### SCCM (Configuration Manager)

- Gestion complète du **cycle de vie des postes**
- Déploiement **massif** et **piloté**
- Fonctionne bien en complément d’Active Directory + GPO + Intune

---

## 🎯 Scénarios de déploiement

### Manuel

- Utilisé pour tests, VM, dépannage

### Semi-automatisé (MDT LTI)

- L’utilisateur doit valider le déploiement (ex: choix du modèle de poste)
- Adapté aux petites structures

### Automatisé (MDT ZTI + SCCM)

- Zéro intervention utilisateur
- Idéal pour **grands parcs**
- Peut être déclenché automatiquement (par collection SCCM)

### Maintenance et réinstallation

- Permet de remettre rapidement un poste en configuration standard

---

### 🚩 Spécificités du déploiement de Windows 11 avec WDS / MDT

|Élément|Particularité / impact sur le déploiement|
|---|---|
|**TPM 2.0** obligatoire|TPM 2.0 doit être activé dans le BIOS/UEFI, sinon l'installation sera bloquée|
|**Secure Boot**|Obligatoire également (doit être activé)|
|**UEFI uniquement**|Le support de BIOS Legacy est officiellement abandonné pour Windows 11 (WDS doit être configuré en mode UEFI PXE !)|
|**Drivers**|Certains matériels plus anciens ne sont plus compatibles|
|**Compatibilité MDT/WDS**|MDT doit être en version >= 8456 + ADK Windows 11 compatible|
|**Images**|L’`install.wim` de Windows 11 est en général plus lourd (> 5 Go), nécessite parfois de configurer IIS ou TFTP en conséquence si utilisé avec PXE|

---

## ✅ À retenir pour les révisions

- Une **image de partition** = clone intégral → rapide mais peu flexible
- Une **image d'installation WIM** est modulaire et maintenable
- **WDS** permet de booter sur le réseau (PXE)
- **MDT** offre un déploiement avancé et personnalisable
- **SCCM** est l’outil le plus complet pour les grandes infrastructures

---

## 📌 Bonnes pratiques professionnelles

- **Documenter** ses images (versions, contenu, date de mise à jour)
- Garder les images **à jour** (patches de sécurité, drivers)
- **Standardiser** les séquences de tâches MDT (éviter les bricolages locaux)
- Automatiser les déploiements autant que possible
- Vérifier la **compatibilité matérielle** (drivers, firmwares)
- Toujours prévoir un **plan de retour arrière** (snapshot, image disque récente)
- Former les équipes IT à l’usage de **MDT et WDS**
- Surveiller les logs de déploiement pour détecter les échecs