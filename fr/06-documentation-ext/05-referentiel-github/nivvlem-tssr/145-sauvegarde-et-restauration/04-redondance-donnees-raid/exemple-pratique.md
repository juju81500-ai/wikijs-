---
title: "TP – Utilisation du RAID"
description: "- TP précédent réalisé"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Utilisation du RAID

## 🛠️ Prérequis

- TP précédent réalisé
- Supprimer les serveurs précédents pour libérer des ressources

---

## 🖥️ Déploiement de la VM SRV-FIC2

- Créer une nouvelle VM nommée `SRV-FIC2`
- Paramètres :
    - OS : Windows Server 2019
    - Disque système : 40 Go
    - RAM : 2048 Mo

---

## Partie 1 – Mise en œuvre d’un volume miroir (RAID 1)

### 1. Ajouter deux disques à la VM

- 1 disque de 5 Go
- 1 disque de 10 Go

### 2. Gestionnaire de disques

- Initialiser les deux disques avec une **partition GPT**
- Créer un **volume miroir** (RAID 1 logiciel)
    - Taille de la partition miroir : 5 Go (limité par le plus petit disque)
- Créer un **volume simple** avec l’espace restant (5 Go sur le disque de 10 Go)
- Formater les volumes et ajouter des **fichiers et dossiers de test**

### 3. Simulation de panne disque

- Supprimer **à chaud** le disque de 5 Go
- Observer l’état du miroir depuis le Gestionnaire de disques
- Supprimer le disque miroir manquant
- Vérifier si les **données restent accessibles** depuis l’explorateur

### 4. Remplacement du disque et reconstruction

- Ajouter un **nouveau disque de 5 Go** à la VM
- Réintégrer ce disque dans le miroir pour le **reconstruire**

---

## Partie 2 – Mise en œuvre d’un RAID 5 logiciel

### 1. Ajouter cinq disques de 5 Go à la VM

- Initialiser les disques en GPT via le **Gestionnaire de disques**
- Créer un **RAID 5 logiciel** avec les 5 disques
- Taille utile de la partition : 20 Go (RAID 5 = n - 1 disques)
- Formater et **ajouter des données de test**

### 2. Simulation de panne

- Supprimer **à chaud** un des 5 disques
- Observer l’état du RAID dans le Gestionnaire de disques
- Supprimer le disque manquant
- Vérifier la **disponibilité des données** dans l’explorateur
- Ajouter un **nouveau disque de 5 Go** et le réintégrer au RAID pour **reconstruction**

---

## Bonus – Mise en œuvre via le Gestionnaire de serveur

### 1. Initialisation des disques

- Utiliser le **Gestionnaire de disques** pour initialiser les nouveaux disques en GPT

### 2. Créer un pool de stockage

- Dans le **Gestionnaire de serveur > Services de fichiers et de stockage** :
    - Accéder à l’onglet **Pools de stockage**
    - Créer un **nouveau pool** avec les disques ajoutés
    - Créer un **disque virtuel** en mode **RAID 1**, puis un autre en **RAID 5**

### 3. Vérification

- Vérifier si les disques apparaissent toujours dans le Gestionnaire de disques
- Formater, assigner une lettre et tester **l’accès aux données**

---

## ✅ À retenir pour les révisions

- Le **RAID logiciel** sous Windows permet de simuler RAID 1 et RAID 5 sans contrôleur dédié
- La **capacité du miroir RAID 1** est limitée par le plus petit disque
- En RAID 5, la perte d’un disque n’entraîne pas de perte immédiate de données
- Le **Gestionnaire de serveur** offre une interface plus moderne pour gérer les pools

---

## 📌 Bonnes pratiques professionnelles

- Toujours utiliser des **disques de capacité équivalente** pour éviter le gaspillage d’espace
- Nommer les volumes et lettres de lecteur de façon explicite (`RAID1_VOL`, `RAID5_VOL`…)
- Sauvegarder les **données critiques hors RAID**, celui-ci ne remplace pas une vraie sauvegarde
- Tester les scénarios de **reconstruction après panne** régulièrement en environnement de test

---

## 🔗 Outils et composants utilisés

- Windows Server 2019
- Gestionnaire de disques (`diskmgmt.msc`)
- Gestionnaire de serveur > Services de fichiers et de stockage
- RAID logiciel (RAID 1 et RAID 5)