---
title: "Gestion du réseau (vSphere et VLAN)"
description: "Un VLAN (Virtual LAN) est un réseau local logique, isolé virtuellement sur un réseau physique."
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Gestion du réseau (vSphere et VLAN)

## 🧱 Concepts fondamentaux : les VLAN

### Qu’est-ce qu’un VLAN ?

Un **VLAN (Virtual LAN)** est un réseau local logique, isolé virtuellement sur un réseau physique.

### Intérêts

- Isolation des flux → sécurité
- Réduction des domaines de broadcast → performance
- Priorisation de flux → qualité de service (QoS)
- Optimisation matérielle

### Requiert :

- Matériel compatible VLAN (switchs, cartes réseau)
- Support de la norme **802.1Q** (tag des trames VLAN)

---

## 🌐 Types de VLAN (en fonction de l’OSI)

- **VLAN niveau 1** : basé sur le **port physique** (port-based)
- **VLAN niveau 2** : basé sur l’**adresse MAC**
- **VLAN niveau 3** : basé sur l’**adresse IP**

> Chaque trame étiquetée contient un tag VLAN (12 bits pour l’ID, 3 bits pour la priorité, 1 bit CFI)

### Configuration sur les switchs

- **Port Access** : un seul VLAN
- **Port Trunk** : plusieurs VLAN autorisés
- **Marquage actif** : le tag est propagé
- **Marquage inactif** : le tag est supprimé avant transmission

---

## 🧩 Réseau dans vSphere – Composants clés

### vSwitch Standard (VSS)

- Créé par défaut (`vSwitch0`)
- Gestion locale à chaque hôte ESXi
- Utilisable pour les machines virtuelles et la gestion

### vSwitch Distribué (VDS)

- Partagé entre plusieurs hôtes ESXi
- Configuration centralisée via **vCenter**
- **Nécessite une licence Enterprise Plus**
- Avantage : aucun impact réseau lors de migration de VM

---

## 🎛️ Groupements de ports (Port Groups)

### Deux types :

|Type|Usage principal|
|---|---|
|VM Network|Réseau pour les machines virtuelles|
|VMkernel|Réseau pour les fonctions d’infrastructure (gestion, vMotion, stockage)|

> La **segmentation VLAN peut être définie dans un port group** via un ID VLAN spécifique

---

## 🖧 Interfaces réseau dans ESXi

### pNIC / VMNIC

- **Cartes physiques** installées sur l’hôte ESXi
- Associées à un **vSwitch** unique (mais un vSwitch peut regrouper plusieurs pNIC)

### vNIC

- **Cartes réseau virtuelles** présentées aux VMs
- Connectées à un port group (VM Network)
- Peuvent aussi être taguées VLAN via 802.1Q (si OS invité compatible)

---

## 🔁 Regroupement (Teaming) et tolérance de pannes

### Objectifs du Teaming

- Tolérance de panne (actif/passif)
- Agrégation de bande passante (actif/actif)

### Méthodes de répartition :

- Par VM (chaque VM utilise une carte)
- Par adresse MAC source
- Par trame (hash source/destination)
- Par ordonnancement simple (failover seulement)

---

## 📡 Cas d’usage : affectation des VMNICs

- VMNIC1 : réseau VM (production)
- VMNIC2 : gestion de l’infrastructure (VMkernel)
- VMNIC3 : vMotion
- VMNIC4 : stockage (iSCSI)

> Le **design réseau** doit respecter l’isolement logique des flux critiques

---

## ✅ À retenir pour les révisions

- **802.1Q** est le standard de tagging VLAN reconnu sur tous les équipements
- Le **vSwitch standard** est propre à chaque hôte ; le **vSwitch distribué** est géré globalement
- Les **groupes de ports** définissent les fonctions réseau : VM, gestion, stockage…
- Les **VMNICs physiques** doivent être soigneusement affectées pour assurer performance et résilience

---

## 📌 Bonnes pratiques professionnelles

- Isoler les réseaux critiques (vMotion, stockage) sur des ports dédiés
- Utiliser des VLAN distincts pour les flux de VM, de gestion, de sauvegarde…
- Prévoir des **trunks configurés côté switch physique** si plusieurs VLAN traversent un même lien
- Toujours vérifier la **compatibilité 802.1Q** des équipements terminaux et switchs
- Enregistrer l’architecture réseau et le plan d’adressage de chaque hôte

---

## 🔗 Outils et notions clés

- vSwitch Standard, vSwitch Distribué (VDS)
- VMNIC / vNIC
- Port Group VMkernel / VM Network
- VLAN, 802.1Q, Port Trunk, Access
- Teaming, Load Balancing, Failover