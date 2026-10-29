---
title: "TP Découverte d’Hyper-V"
description: "- Ouvrir VMware Workstation"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP Découverte d’Hyper-V

## 📝 Étapes

### 1. Préparation de l’environnement

- Ouvrir VMware Workstation
- Augmenter la **RAM** de la VM `SRV_2K19` à **8 Go**
- Ajouter un **deuxième disque dur SCSI** de **100 Go**
- Démarrer la VM `SRV_2K19`

### 2. Configuration dans `SRV_2K19`

- Initialiser et formater le nouveau disque en volume nommé `DATA`
- Créer deux dossiers sur le volume `DATA` :
    - `DATA\VMs` (emplacement des VMs)
    - `DATA\VHDs` (emplacement des disques virtuels)

### 3. Installation du rôle Hyper-V

- Ajouter le rôle **Hyper-V** via le Gestionnaire de serveur
- Utiliser la carte réseau `ethernet0` comme **switch virtuel** externe
- Ne pas activer la **migration à chaud** (Live Migration)
- Redémarrer la VM si demandé

### 4. Création d’une VM Hyper-V : `SRV_2K19-HV1`

- Placer l’ISO Windows Server 2019 sur le bureau
- Depuis Hyper-V Manager :
    - Créer une nouvelle VM : `SRV_2K19-HV1`
    - **Génération** : 2
    - **RAM** : 2 Go (statique)
    - **Réseau** : connecter à la carte Intel (via le switch Hyper-V)
    - **Disque VHDX** : 32 Go (stocké dans `DATA\VHDs`)
    - Associer l’ISO comme lecteur DVD

### 5. Installation système et préparation du clonage

- Démarrer la VM `SRV_2K19-HV1`
- Lancer l’installation de Windows Server 2019
- Une fois installée, exécuter :
    ```
    C:\Windows\System32\Sysprep\Sysprep.exe
    ```
    - Cocher **Generalize**
    - Sélectionner **Shutdown**

### 6. Exportation et importation d’une nouvelle VM

- Exporter `SRV_2K19-HV1` vers `DATA\VMs\EXPORT\Machines virtuelles`
- Depuis Hyper-V, importer la VM à partir du chemin précédent
    - Choisir **Copy the virtual machine**
    - Stocker la copie dans `VMs\SRV_2K19-HV2` et `VHDs\SRV_2K19-HV2`
- Renommer la VM importée : `SRV_2K19-HV2`

### 7. Vérification et test réseau

- Démarrer les deux VMs Hyper-V : `SRV_2K19-HV1` et `SRV_2K19-HV2`
- Relever leurs **adresses IPs**
- Tester le **ping entre les deux VMs**
    - Si échec, vérifier le **pare-feu Windows**

### 8. Finalisation

- Revenir dans VMware Workstation
- Réaliser un **snapshot** de la VM `SRV_2K19` et le nommer **Fin atelier 2**

---

## ✅ À retenir pour les révisions

- Hyper-V peut être utilisé **dans une VM**, mais uniquement à des fins de test (nested virtualization)
- La **généralisation Sysprep** permet de cloner une VM proprement
- Une **exportation préalable est obligatoire** pour pouvoir importer une VM ailleurs
- Les **types de réseaux Hyper-V** influencent directement les communications entre VM

---

## 📌 Bonnes pratiques professionnelles

- Prévoir un **répertoire de stockage clair et structuré** pour les VMs et disques
- Toujours effectuer une **sauvegarde snapshot avant modifications majeures**
- Désactiver les pare-feux pour les tests **uniquement en environnement contrôlé**
- Documenter systématiquement les **adresses IPs et configurations réseau** des VMs
- S’assurer que le rôle Hyper-V est bien configuré sans fonctionnalité inutile (Live Migration désactivée ici)

---

## 🔗 Composants / actions à connaître

- Hyper-V Manager (MMC)
- `Sysprep.exe` pour généraliser une VM
- Réseaux virtuels Hyper-V : privé, interne, externe
- Snapshots dans VMware Workstation : `VM > Snapshot > Take Snapshot`
- `Export-VM`, `Import-VM`, `Get-VM` (PowerShell)