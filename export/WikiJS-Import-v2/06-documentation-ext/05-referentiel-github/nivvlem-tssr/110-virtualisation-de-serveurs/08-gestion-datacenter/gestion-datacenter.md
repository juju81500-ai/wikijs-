---
title: "Gestion du datacenter (vSphere)"
description: "- Il est possible d’allouer aux VMs plus de ressources que l’hôte n’en dispose physiquement."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion du datacenter (vSphere)

## 🧱 Gestion des ressources

### Réservation de ressources

- Il est possible d’allouer aux VMs **plus de ressources** que l’hôte n’en dispose physiquement.
- Pour garantir la disponibilité :
    - Réserver des ressources pour certaines VMs critiques
    - Créer des **pools de ressources** avec allocation CPU/RAM priorisée

### Pools de ressources

- Objets logiques au sein de l’hôte ou du cluster
- Permettent de :
    - Prioriser des charges critiques
    - Isoler des environnements (test, prod…)

---

## 🏢 Contexte vCenter et datacenter

### Apports de vCenter

- Regroupe des hôtes ESXi dans un **datacenter logique**
- Permet l’utilisation de **ressources partagées** (réseau, stockage)
- Active des services avancés : vMotion, HA, DRS, etc.
- Nécessite une **licence adaptée**

### vCenter : implémentation

|Variante|Nb max hôtes|Nb max VMs|Avantages|Inconvénients|
|---|---|---|---|---|
|**VCSA**|5|50|Simplicité, appliance intégrée|Capacité limitée|
|**vCenter Std**|1000|10 000|Puissant, évolutif|Mise en œuvre plus complexe|

> Accès vCenter :

- Client vSphere Web : HTTPS port 443
- Console VCSA : HTTPS port 5480

---

## 🧩 Gestion des modèles de VMs (templates)

### Types de modèles

|Format|Utilisation|Compatibilité|
|---|---|---|
|OVF|Format standard, export/import inter-plateforme|VMware, VirtualBox, Xen, Hyper-V (via conversion)|
|VMTX|Spécifique vSphere (datacenter)|vSphere uniquement|

### Avantages des modèles VMTX

- Déploiement rapide et cohérent
- Personnalisables (nom, IP, SID…)
- Utilisables avec **Sysprep** pour générer un fichier de personnalisation

### Méthodes d’utilisation

- **Convert to template** / **Convert to VM**
- **Clone to template** / **Deploy VM from this template**

> Le système de personnalisation nécessite :

- VMware Tools installés
- Intégration de **Sysprep** sur vCenter si l’OS ne le fournit pas nativement

---

## 👥 Gestion des utilisateurs et privilèges

### Où créer les comptes ?

- **Dans vCenter** : accès à tous les objets gérés
- **Dans ESXi seul** : accès uniquement aux objets locaux à l’hôte

### Gestion centralisée via SSO

- Si le vCenter est joint à un **domaine Active Directory**, il est possible d’utiliser l’authentification SSO (Single Sign-On)

### Méthodologie

1. Créer utilisateurs et groupes
2. Créer rôles et leur associer des **privilèges précis**
3. Affecter ces rôles à des objets (VM, hôte, datastore…) via des **groupes**, non des comptes individuels

### Bonnes pratiques

- Ne jamais affecter plus de droits que nécessaire
- Privilégier l’attribution de droits en **haut de l’arborescence** (héritage activé)
- Utiliser des **groupes** au lieu d’utilisateurs seuls

---

## 🔄 Migration de machines virtuelles

### Concepts

- Une VM peut migrer :
    - Entre deux **hôtes** (vMotion)
    - D’un **datastore** à un autre (Storage vMotion)

### Prérequis

- **vMotion** activé sur au moins un vSwitch source et destination
- Adressage des hôtes dans le **même domaine de broadcast**
- Datastores **accessibles simultanément** aux deux hôtes

### Risques fréquents

- ISO encore inséré dans la VM
- Port group absent sur l’hôte cible
- Problème de **compatibilité CPU** entre hôtes (instruction sets divergents)

---

## ✅ À retenir pour les révisions

- Les **pools de ressources** permettent d’allouer ou restreindre CPU/RAM
- vCenter est indispensable à la gestion centralisée de services avancés (vMotion, DRS, HA…)
- Les **modèles de VMs** facilitent le déploiement automatisé et personnalisé
- La gestion des privilèges doit être **granulaire et structurée par rôles**
- La **migration à chaud (vMotion)** nécessite une architecture réseau et stockage partagée cohérente

---

## 📌 Bonnes pratiques professionnelles

- Déployer vCenter sur une VM dédiée, sauvegardée et haute dispo
- Documenter les rôles, privilèges et affectations d’utilisateurs
- Vérifier que tous les hôtes ont accès aux mêmes ressources (datastore, port group…)
- Utiliser les **modèles VMTX** avec personnalisation pour industrialiser le déploiement
- Ne jamais migrer une VM avec ISO ou snapshot en cours (préparer la VM à la migration)

---

## 🔗 Outils / notions à connaître

- vSphere Web Client (port 443), Console VCSA (port 5480)
- Templates : OVF, VMTX, Sysprep
- Rôles, groupes, privilèges, SSO
- vMotion, Storage vMotion, Datastore, Pool de ressources