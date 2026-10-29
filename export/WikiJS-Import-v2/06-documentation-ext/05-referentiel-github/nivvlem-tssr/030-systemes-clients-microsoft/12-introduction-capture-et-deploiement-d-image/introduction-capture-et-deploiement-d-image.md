---
title: "Introduction à la capture et au déploiement d'image"
description: "- Accélérer le déploiement des postes de travail"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# Introduction à la capture et au déploiement d'image

## 🔍 Pourquoi capturer et déployer une image ?

- Accélérer le déploiement des postes de travail
- Rendre homogène le parc informatique
- Garantir la conformité des systèmes (OS, drivers, applications)
- Disposer d'images "clé en main" pour :
    - Nouveaux collaborateurs
    - Postes à réinitialiser suite à panne ou reconfiguration

---

## 🚧 Création du poste de référence (Master)

### ✅ Etapes préliminaires

- Installer un Windows "propre"
- Configurer le système et les paramètres DSI
- Installer les logiciels validés
- Ne pas lier le poste à un domaine
- Ne pas créer d'utilisateur final

### ⚠️ Attention

- Utiliser le compte administrateur local activé (sera réinitialisé)
- Les apps Microsoft Store posent problème
- Certains pilotes tiers peuvent être supprimés automatiquement

---

## ⚖️ Sysprep (System Preparation Tool)

### 🔹 Objectif : Réinitialiser les identifiants système

### 💡 Commande typique

```powershell
C:\Windows\System32\Sysprep\Sysprep.exe /oobe /generalize /shutdown
```

- `/oobe` : lancement en mode prêt à l'emploi
- `/generalize` : suppression des identifiants uniques
- `/shutdown` : arrêt immédiat du système

### 📃 Journaux : `C:\Windows\System32\Sysprep\Panther`

> ❌ Ne jamais redémarrer le master après cette commande !

---

## 🗃️ Capture de l'image

### ✅ Méthode 1 : Automatisée via serveur WDS

- Boot PXE depuis le réseau
- Chargement d'une image WinPE
- Capture et stockage de l'image au format `.wim`

### ✅ Méthode 2 : Manuelle avec dism.exe

- Lancer WinPE (clé USB, ISO)
- Utiliser `dism` pour capturer l'image :

```powershell
dism /Capture-Image /ImageFile:D:\Win10.wim /CaptureDir:C:\ /Name:"Win10-Base"
```

---

## 🚀 Déploiement de l'image

### 🛍️ Par serveur (WDS)

- Boot PXE des machines clientes
- Choix de l'image à déployer
- Suivi automatisé

### 🚚 Par support WinPE

- Lancer `diskpart` pour préparer le disque
- Appliquer l'image avec `dism`

```powershell
dism /Apply-Image /ImageFile:D:\Win10.wim /Index:1 /ApplyDir:C:\
```

- Créer les fichiers de démarrage :

```powershell
bcdboot C:\Windows
```

---

## ⚡ Maintenance des images

- Possibilité de modification **offline** :

```powershell
dism /Mount-Image /ImageFile:Win10.wim /Index:1 /MountDir:C:\mount
```

- Modification dans le répertoire `C:\mount`
- Sauvegarde des modifications :

```powershell
dism /Unmount-Image /MountDir:C:\mount /Commit
```

---

## ✅ À retenir pour les révisions

- Sysprep est indispensable avant capture pour réinitialiser l'empreinte du poste
- La capture se fait via **dism** ou un serveur de déploiement (WDS)
- Le déploiement peut être manuel (WinPE) ou automatisé (PXE + WDS)
- Le format d'image Windows est `.wim`
- WinPE contient tous les outils nécessaires (diskpart, dism, net use, etc.)

---

## 📌 Bonnes pratiques professionnelles

|Bonne pratique|Pourquoi ?|
|---|---|
|Documenter chaque image créée (version, logiciels)|Pour faciliter les audits, migrations, dépannages|
|Tester chaque image sur différents modèles PC|Éviter les problèmes de compatibilité matérielle|
|Ne pas capturer un master non syspreppé|Risque de conflits d'ID, de noms machines, SID|
|Supprimer les apps du Microsoft Store|Elles posent problème avec sysprep|
|Mettre à jour les images régulièrement|Pour intégrer les derniers correctifs de sécurité|