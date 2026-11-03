---
title: "Les pilotes et les imprimantes"
description: "- Interface entre le matériel (carte réseau, imprimante, etc.) et le système d’exploitation"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Les pilotes et les imprimantes

## 🧩 Pilotes : rôle et gestion

### 🔹 Fonction

- Interface entre le **matériel** (carte réseau, imprimante, etc.) et le **système d’exploitation**
- Requis pour chaque architecture (32 bits ou 64 bits)

### 🔹 Types de détection

- **Plug & Play** : détection automatique à chaud (ex. USB)
- **Non Plug & Play** : nécessite souvent un redémarrage

### 🔹 Fichiers clés

| Type        | Extension                             |
| ----------- | ------------------------------------- |
| Fichier INF | `.inf` (définition du pilote)         |
| Pilote      | `.sys` (binaire)                      |
| Certificat  | `.cat` (signature Microsoft ou tiers) |
| Complément  | `.dll`, `.xml`, `.exe`…               |

### 🔹 Emplacements

- `C:\Windows\inf` → INF installés manuellement (`oemXX.inf`)
- `C:\Windows\System32\DriverStore` → Magasin de pilotes Windows

### 🔹 Outils de gestion

|Outil|Description|
|---|---|
|`devmgmt.msc`|Gestionnaire de périphériques (GUI)|
|`msinfo32`|Informations système|
|`driverquery`|Liste des pilotes en ligne de commande|
|`pnputil`|Ajouter/Supprimer/Enumérer des pilotes|

Exemples :

```powershell
pnputil /enum-drivers       # Lister les pilotes tiers
pnputil /add-driver pilote.inf /install
```

---

## 🖨️ Imprimantes : concepts clés

### 🔹 Définitions

|Terme|Description|
|---|---|
|Périphérique d’impression|Matériel réel connecté localement ou via réseau|
|Imprimante|Interface logicielle : pilote + file + port|
|File d’attente|Gérée par le service **Spouleur d’impression**|

---

## 📥 Types d’imprimantes

### 🔹 Imprimante locale

- Connectée directement à un PC (USB)
- Installée avec un pilote générique ou constructeur
- Sécurité **NTFS** configurable (onglet Sécurité)
- Gestion possible via `control printers`

### 🔹 Imprimante partagée

- Imprimante locale partagée à d’autres utilisateurs sur le réseau
- Active **seulement si le poste hôte est allumé**
- Chemin UNC : `\\nom_machine\imprimante`

### 🔹 Imprimante réseau

- Indépendante (OS intégré)
- Accessible via une **adresse IP**, interface web ou serveur d'impression
- Plus adaptée à une utilisation en entreprise

---

## 🛠️ Gestion des imprimantes

### 🔹 Panneau de configuration

```bash
control printers
```

Permet :

- Voir la file d’attente
- Modifier les propriétés générales et avancées

### 🔹 Paramètres avancés

- **Priorité** des travaux
- **Heures de disponibilité**
- Sécurité des documents imprimés

### 🔹 Pool d’impression

- Une **imprimante logicielle** gère plusieurs périphériques physiques
- Le spouleur envoie les documents à la première imprimante disponible
- Permet d’optimiser l’attente dans les environnements à fort volume

---

## ✅ À retenir pour les révisions

- Un **pilote** permet au système de communiquer avec le matériel
- Le **spouleur d’impression** convertit les documents dans un langage imprimable
- Imprimantes disponibles : **locale**, **partagée**, **réseau**
- Les pilotes doivent être **signés** et compatibles (x64/x86)
- `pnputil`, `driverquery`, `devmgmt.msc` sont des outils essentiels
- Le partage d’une imprimante s’appuie sur la sécurité NTFS et réseau (UNC)

---

## 📌 Bonnes pratiques professionnelles

|Bonnes pratiques|Pourquoi ?|
|---|---|
|Utiliser des **pilotes signés** uniquement|Assure la compatibilité et évite les écrans bleus|
|Mettre à jour les pilotes depuis le constructeur|Bénéficier des correctifs et améliorations|
|Éviter les pilotes en `.exe` non documentés|Risque de logiciels non vérifiés ou instables|
|Centraliser les imprimantes réseau|Maintenance facilitée et meilleure sécurité|
|Documenter les partages UNC|Permet un dépannage et une gestion claire des accès|