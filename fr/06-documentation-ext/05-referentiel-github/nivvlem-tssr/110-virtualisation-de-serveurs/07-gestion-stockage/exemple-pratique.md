---
title: "TP – Gestion du stockage dans vSphere"
description: "- VMs ESXi1 et ESXi2 fonctionnelles avec configuration réseau prête (Module 6 terminé)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP – Gestion du stockage dans vSphere

## 📝 Prérequis

- VMs `ESXi1` et `ESXi2` fonctionnelles avec configuration réseau prête (Module 6 terminé)
- VM `SRV_2K19` avec Windows Server 2019 installé (Module 1 terminé)
- Retourner à la **snapshot Fin Atelier 1** avant de commencer

---

## I – Mise en œuvre du stockage iSCSI (mode bloc)

### 1. Configuration réseau sur SRV_2K19

- Démarrer la VM
- Passer `ethernet0` en IP statique : `192.168.100.12/24`
- Vérifier la connectivité vers ESXi1 et ESXi2 via ping (`192.168.100.1`, `192.168.100.2`)

### 2. Ajout d’un disque local à SRV_2K19

- Ajouter un **2ème disque de 150 Go** dans VMware Workstation
- Le formater sous Windows et le nommer `STOCKAGE`
- Créer une arborescence `STOCKAGE\DS`

### 3. Mise en œuvre du service iSCSI sur SRV_2K19

- Ajouter le rôle **Serveur cible iSCSI** via le Gestionnaire de serveur
- Créer un **disque virtuel iSCSI de 80 Go** nommé `LUN1`
- Créer une **nouvelle cible iSCSI** : autoriser les IPs de `ESXi1` et `ESXi2`
- Lancer la création via l’assistant

### 4. Configuration sur ESXi1

- Activer et configurer l’**adaptateur iSCSI logiciel**
- Associer le port group `GRP-STORAGE-VMOTION`
- Ajouter la cible dynamique : IP `192.168.100.12`
- Lancer une **réanalyse** de l’adaptateur iSCSI
- Vérifier la détection du **périphérique MSFT iSCSI**

### 5. Création du datastore VMFS

- Créer une **banque de données nommée `DS-ISCSI`** en utilisant 100% de `LUN1`

### 6. Réplication de la configuration sur ESXi2

- Activer et configurer l’**adaptateur iSCSI logiciel**
- Ajouter la même cible dynamique
- Vérifier l’accès au **datastore `DS-ISCSI`** partagé

---

## II – Mise en œuvre du stockage NFS (mode fichier)

### 1. Préparation sur SRV_2K19

- Dans le volume `STOCKAGE`, créer un dossier `DS\NFS`
- Ajouter le rôle **Serveur pour NFS**

### 2. Création d’un partage NFS

- Créer un **partage NFS** sur `DS\NFS` avec les paramètres suivants :
    - Pas d’authentification
    - Accès des utilisateurs non mappés
    - Lecture/écriture autorisée aux IPs des `ESXi`
    - Version NFSv3

### 3. Montage sur ESXi1 et ESXi2

- Depuis le client vSphere, créer un **datastore de type NFS** nommé `DS-NFS`
- Chemin de montage : `\192.168.100.12\DS\NFS`
- Vérifier que le montage apparaît dans les banques de données

---

## ✅ À retenir pour les révisions

- Le stockage **iSCSI** est en mode bloc, nécessite un initiator + cible + VMFS
- Le stockage **NFS** est en mode fichier, plus simple à configurer mais moins performant
- Le **datastore VMFS** peut être partagé entre plusieurs ESXi via un LUN iSCSI
- Il faut un **réseau dédié** et des IP fixes pour les fonctions de stockage

---

## 📌 Bonnes pratiques professionnelles

- Toujours attribuer une IP statique aux serveurs de stockage
- Séparer les flux stockage du reste (VMNICs et VLAN dédiés)
- Vérifier que les services de rôle Windows sont installés avec les bonnes autorisations
- Sur vSphere : surveiller l’état du périphérique iSCSI ou NFS après chaque configuration
- Nommer les datastores et les LUNs de façon **explicite et homogène** (`DS-ISCSI`, `DS-NFS`…)

---

## 🔗 Composants et outils utilisés

- Windows Server 2019 : services iSCSI Target et NFS Server
- ESXi 7 : stockage VMFS via LUN + montage NFS
- VMware Workstation (disques supplémentaires)
- vSphere Web Client
- Datastore : `DS-ISCSI`, `DS-NFS`
- Réseaux : `GRP-STORAGE-VMOTION`, IP statiques `192.168.100.x`