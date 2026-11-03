---
title: "Applications de virtualisation sur poste de travail"
description: "- Console de gestion centralisée des VM"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Applications de virtualisation sur poste de travail

## 🛠️ Outils de virtualisation utilisés

### VMware Workstation (v17)

- Console de gestion centralisée des VM
- Création, importation, modification, suppression de VMs
- Interface graphique riche et intuitive

> ⚠️ Attention à la **compatibilité entre versions** : une VM créée dans une version récente peut ne pas être compatible avec une version plus ancienne.

---

## 💻 Prérequis système

- Processeur **Intel VT-x** ou **AMD-V** (activé dans le BIOS/UEFI)
- Quantité de **RAM et stockage suffisante** selon les VMs utilisées

---

## 📦 Étapes de création d'une machine virtuelle

### Paramètres à définir :

- Nom de la VM et **emplacement personnalisé** (éviter le dossier par défaut « Mes documents »)
- Mode d'installation : **"I will install the OS later"** recommandé pour garder la main
- Choix du système invité (Windows, Linux…)
- Taille du disque (ex : 40 Go) et mode de stockage :
    - **Dynamic** : allocation progressive (par défaut)
    - **Fixed (single file)** : recommandé pour de meilleures performances
- Personnalisation du matériel : CPU, RAM, support ISO, carte réseau, USB, etc.

---

## 🧩 Gestion du matériel et interactions VM ↔ hôte

- Capture clavier/souris automatique par la VM
    - `Ctrl + Alt` pour libérer la souris
    - `Ctrl + Alt + Inser` pour simuler `Ctrl + Alt + Suppr`
- Support des **périphériques USB, CD/DVD, disquettes**
- Fonction **Shared Folder** : partage de dossiers entre l’hôte et la VM

---

## 🌐 Modes réseau disponibles

|Mode|Description|
|---|---|
|Bridged|Connexion directe au réseau physique|
|NAT|La VM passe par l’interface réseau de l’hôte|
|Host-only|Réseau interne entre VM et hôte uniquement|
|LAN Segment|Réseau privé entre VM, nécessite déclaration manuelle|

> Des **services VMware** (NAT & DHCP) assurent l’adressage dans les modes NAT et Host-only.

---

## ⚠️ Problèmes courants & solutions

|Problème|Solution|
|---|---|
|Clavier non capturé|`Ctrl + Alt` puis redémarrer avec focus sur la VM|
|Réseau non fonctionnel|Désactiver / réactiver les cartes réseau physiques de l’hôte|
|Espace disque hôte insuffisant|Vérifier le dossier de la VM / déplacer ou libérer de l’espace|
|Espace disque VM insuffisant|Ajouter un disque virtuel ou redimensionner manuellement|

---

## ✅ À retenir pour les révisions

- VMware Workstation est un **hyperviseur de type 2**, idéal pour le test et l’apprentissage.
- Toujours utiliser un **mode de création manuel** pour un contrôle total.
- Les **modes réseau** influencent les capacités de communication de la VM.
- Certains paramètres sont modifiables **à chaud**, d’autres nécessitent arrêt ou redémarrage.

---

## 📌 Bonnes pratiques professionnelles

- Prévoir une **arborescence claire** pour stocker ses VMs
- Affecter des **noms explicites** aux VMs pour éviter les confusions
- Définir des tailles de disque cohérentes et éviter le surprovisionnement
- **Documenter les paramètres réseaux** de chaque VM si complexes (ex : LAN segment)
- Faire des **snapshots réguliers** lors des phases de test

---

## 🔗 Outils / commandes utiles

- VMware Workstation UI : onglet `Edit > Virtual Network Editor`
- `Ctrl + Alt` : libération du curseur
- `Ctrl + Alt + Insert` : équivalent `Ctrl + Alt + Suppr`
- Virtual Machine Settings (clic droit sur la VM)
- ISO boot : modifier l’ordre de démarrage dans le BIOS VM