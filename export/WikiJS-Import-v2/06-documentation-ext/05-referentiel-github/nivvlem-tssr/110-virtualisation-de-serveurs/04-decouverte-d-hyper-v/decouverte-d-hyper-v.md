---
title: "Découverte d’Hyper-V"
description: "- Hyper-V v2 : Windows Server 2008 R2"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Découverte d’Hyper-V

## 🧱 Présentation d’Hyper-V

### Versions

- Hyper-V v2 : Windows Server 2008 R2
- Hyper-V v3 : Windows 8 / Windows Server 2012 et suivants

> Intégré en tant que **rôle serveur** (via le gestionnaire de serveur) ou **fonctionnalité client** à activer (Windows 8 Pro 64 bits et +)

---

## 🧰 Prérequis d’installation

### Matériel

- Processeur **64 bits** avec prise en charge **Intel VT-x** ou **AMD-V**
- **SLAT** requis pour l’édition client :
    - EPT (Intel)
    - NPT/RVI (AMD)
- RAM et espace disque adaptés

### Logiciel

- Windows Server 2008 (ou supérieur)
- Windows 8 Pro 64 bits minimum (client)

> ⚠️ Nécessite **2 redémarrages** à l’installation pour passer en mode natif (type 1)

---

## 🖥️ Fonctionnalités & interactions

### Interaction avec l’hôte

- Hyper-V est un **hyperviseur de type 1** : l’OS hôte devient client de l’hyperviseur
- Les **médias USB** ne sont pas pris en charge en v2

### Contrôles clavier spécifiques

- `Ctrl + Alt + Gauche` : libérer la souris
- `Ctrl + Alt + Fin` : équivalent `Ctrl + Alt + Suppr` dans la VM

### Services d’intégration

- Permettent une meilleure intégration OS invité ↔ hôte (horloge, souris, shutdown propre…)

### Fonctions avancées

- Console dédiée pour chaque VM
- Paramètres matériels poussés (BIOS, RAM dynamique, etc.)
- Snapshots, import/export

---

## 🌐 Réseaux virtuels Hyper-V

### Types de réseaux

|Type|Description|
|---|---|
|Privé|Communication uniquement entre VMs|
|Interne|Communication entre VMs et hôte uniquement|
|Externe|Connexion directe au réseau physique|
|Externe dédié|Carte réseau dédiée à Hyper-V, exclusive|

> Hyper-V **s’approprie la carte physique** : une seule carte externe par NIC physique

### Configuration

- Utilisation du **Gestionnaire de Réseau Virtuel** (console Hyper-V)
- VLAN taggés possibles

---

## 🧩 Création d’une VM Hyper-V

- Assistant : clic droit > Nouveau > Ordinateur virtuel
- Définir emplacement, nom, génération (1 ou 2)
- Le **disque de boot de génération 1** doit obligatoirement être connecté via **IDE**
- Affecter ISO, réseau, RAM, disques…

---

## 📤 Exportation / Importation de VM

### Contraintes spécifiques

- Une **VM doit être exportée** pour être réutilisable ailleurs
- Sans exportation préalable, import impossible
- Deux options lors de l’importation :
    - **Créer une copie** : pour dupliquer la VM (mais le VHD est copié dans un même emplacement)
    - **Enregistrer tel quel** : ne pas dupliquer

### Exemple de procédure

1. Exporter dans un dossier propre
2. Copier le dossier où désiré
3. Importer en **choisissant la méthode adaptée**

---

## ✅ À retenir pour les révisions

- Hyper-V est un hyperviseur **intégré à Windows**, type 1
- La configuration réseau doit être **définie manuellement**
- Les types de réseau (privé, interne, externe) sont **exclusifs**
- Les manipulations (export/import) doivent être maîtrisées pour le clonage ou la mobilité

---

## 📌 Bonnes pratiques professionnelles

- Toujours créer un **réseau externe dédié** dans les tests d’intégration
- Utiliser la **génération adaptée** à l’OS invité (UEFI = Gen 2)
- Ne jamais déplacer manuellement une VM sans exportation
- Conserver une **arborescence logique** de stockage VMs
- Documenter les réseaux et les VLAN utilisés

---

## 🔗 Commandes / outils à connaître

- `Get-VM`, `New-VM`, `Start-VM`, `Export-VM`, `Import-VM`
- Console Hyper-V (MMC)
- Gestionnaire de Réseau Virtuel