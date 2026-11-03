---
title: "Installation du système d’exploitation Windows"
description: "- Installation \"propre\" sur matériel neuf"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Installation du système d’exploitation Windows

## ⚙️ Prérequis matériels Windows

|Composant|Windows 10|Windows 11|
|---|---|---|
|Processeur|1 GHz|1 GHz, 2 cœurs, compatible 64 bits et TPM 2.0|
|RAM|1 Go (32 bits) / 2 Go (64 bits)|4 Go minimum|
|Espace disque|16 Go (32 bits) / 32 Go (64 bits)|64 Go minimum|
|Affichage|DirectX 9 avec pilote WDDM 1.0|DirectX 12, WDDM 2.0|

> 📌 Windows 11 impose **des critères de sécurité matériels** (Secure Boot, TPM 2.0, processeur récent).

---

## 🛠️ Supports d’installation disponibles

- **DVD**
- **Clé USB bootable**
- **Image ISO**
- **Partage réseau** (déploiement via serveur)
- **WDS / SCCM** (solutions d’entreprise)

### 🔹 Fichiers importants

- **install.wim** : contient l’image de Windows à déployer
- **boot.wim** : mini-OS permettant d'amorcer l'installation

> 📌 Tout support d'installation doit contenir ces fichiers.

---

## 🖥️ Modes d’installation Windows

### 🔹 Nouvelle installation

- Installation "propre" sur matériel neuf
- Remplacement d’un système existant
- Permet un **partitionnement complet** du disque

### 🔹 Mise à niveau

- Installation "par-dessus" un Windows existant (Windows 10 → Windows 11 par ex)
- **Conserve** applications, paramètres et données
- Réservée à des usages spécifiques (peu recommandée pour de gros changements de version)

> 📌 La mise à niveau vers **Windows 11** n'est possible que depuis Windows 10.

---

## 🔄 Transfert de données et paramètres

|Objectif|Outils utilisés|
|---|---|
|Sauvegarder/restaurer fichiers personnels|Outil de sauvegarde intégré|
|Migrer comptes et paramètres utilisateurs|**USMT** (User State Migration Tool) en CLI|

> 📌 USMT est utilisé surtout dans les déploiements massifs d’entreprise (via MDT, SCCM...)

---

## ✅ À retenir pour les révisions

- Vérifier **les prérequis matériels** avant toute tentative d’installation
- Utiliser un **support bootable** contenant `boot.wim` et `install.wim`
- Privilégier une **installation propre** sur nouveau matériel
- Utiliser **USMT** pour la migration de profils dans un contexte pro
- Pour Windows 11, attention aux **exigences de sécurité renforcées** (TPM 2.0, Secure Boot)

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Toujours tester la compatibilité matérielle (PC Health Check)|Éviter des échecs d’installation|
|Choisir l'édition de Windows adaptée aux besoins|Optimiser les coûts et les fonctionnalités disponibles|
|Effectuer une sauvegarde complète avant migration|Prévenir toute perte de données lors de l'installation|
|Utiliser des outils certifiés (Media Creation Tool, Rufus)|Fiabiliser le processus d'installation|
|Documenter la version, édition et clé produit utilisée|Assurer la traçabilité et la conformité légale|