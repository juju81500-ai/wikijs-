---
title: "Gestion du stockage (Sauvegarde & Restauration)"
description: "- Connecté directement au serveur (disque, bande, USB)"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion du stockage (Sauvegarde & Restauration)

## 🧱 Infrastructure de sauvegarde

### Composants matériels

- **Supports de sauvegarde** : disques, bandes, RDX, cloud…
- **Lecteurs/robots** : pour automatiser les sauvegardes (bande notamment)

### Composants logiciels

- **Logiciel de sauvegarde** (ex : Backup Exec, Veeam)
- **Ordonnanceur** : planifie et déclenche les sauvegardes automatiquement

---

## 📦 Critères de choix des supports

|Critère|Pourquoi c’est important|
|---|---|
|Capacité|Gérer le volume des données à sauvegarder|
|Fiabilité|Résistance aux défaillances matérielles|
|Temps d’accès|Performance de lecture/écriture (sauvegarde/restauration)|
|Consommation|Optimisation énergétique (surtout en datacenter)|
|Sécurité|Protection contre perte, vol, ou corruption|

---

## 💾 Supports de sauvegarde – comparatif

|Support|Atouts|Limites|
|---|---|---|
|CD / DVD|Peu coûteux, compact|Faible capacité, durabilité limitée|
|Blu-Ray||Durée de vie limitée|
|Disque dur (HDD)|Économique, simple|Fragile, sensible aux chocs|
|Disque SSD|Résistant, performant|Plus cher que HDD|
|Clé USB|Résistante, portable|Capacité limitée, peu sécurisée|
|Bande magnétique|Longévité, robotisation|Manipulation délicate, lenteur|
|RDX|Facile à transporter|Fragilité physique|
|NAS|Facilité de mise en œuvre, RAID|Charge le réseau, encombrement|
|SAN|Haute disponibilité, gestion centralisée|Complexe, coûteux|
|Cloud|Accès distant, sécurité intégrée|Débit dépendant, dépendance à un tiers|

---

## 🔌 Technologies de stockage

### DAS (Direct Attached Storage)

- Connecté directement au serveur (disque, bande, USB)
- Avantages : simplicité, performance locale
- Inconvénients : pas de mutualisation, difficile à centraliser

### NAS (Network Attached Storage)

- Stockage en mode fichier via réseau (CIFS, NFS)
- Gère lui-même son système de fichiers
- Simplicité de déploiement

### SAN (Storage Area Network)

- Accès en mode bloc via réseau dédié (iSCSI, Fibre Channel)
- L’hôte gère le système de fichiers
- Très utilisé pour virtualisation et serveurs critiques

---

## 📊 Comparatif NAS vs SAN

|Critère|NAS|SAN|
|---|---|---|
|Protocole|CIFS, NFS, SMB|SCSI, Fibre Channel, iSCSI|
|Mode d’accès|Fichier|Bloc|
|Système de fichier|Intégré au NAS|Géré par le serveur hôte|
|Coût / complexité|Abordable, facile|Coûteux, administration experte|
|Performances|Correctes, suffisant pour fichiers|Élevées, adapté aux bases, VM, backups critiques|

---

## 🌍 Local vs distant

### Sauvegarde locale

- Directement sur le site (disque, bande, NAS)
- Rapide à restaurer mais vulnérable en cas de sinistre

### Sauvegarde externalisée

- Vers site distant (NAS distant, cloud)
- Sécurise contre sinistres physiques mais nécessite bande passante

---

## 🧪 Exécution des sauvegardes

- Nécessite combinaison **logiciel + ordonnanceur + support**
- À planifier : fréquence, type, rétention, volume estimé

> Rappel de la règle **3–2–1** : 3 copies, 2 supports différents, 1 hors site

---

## ✅ À retenir pour les révisions

- Les supports doivent être choisis selon **la volumétrie, la criticité, et la fréquence des sauvegardes**
- Le **DAS** est simple, **NAS** est accessible, **SAN** est robuste et complexe
- La **bande magnétique** reste très utilisée en archivage longue durée
- Le cloud ajoute de la **résilience** mais dépend du débit et des coûts

---

## 📌 Bonnes pratiques professionnelles

- Ne jamais centraliser les sauvegardes **sur un seul site ou support**
- **Documenter les choix techniques** (type, protocole, fréquence, volume)
- Prévoir des tests réguliers **de restauration** pour chaque solution retenue
- Conserver une trace écrite de la **cartographie de stockage**
- Choisir la **solution la moins complexe possible** pour le périmètre ciblé

---

## 🔗 Technologies et notions clés à connaître

- **DAS, NAS, SAN**
- **Protocole CIFS, NFS, SCSI, iSCSI**
- **Disque dur, bande, RDX, cloud**
- Règle **3–2–1**
- Logiciels : Veeam, Veritas, Atempo, Backup Exec