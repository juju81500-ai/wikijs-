---
title: "TP - Windows Deployment Services (WDS)"
description: "✅ Serveur DEPLOY intégré au domaine nivvlem.tssr.eni"
published: true
date: 2026-10-27T20:13:54Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:13:54Z
dateModified: 2026-10-27T20:13:54Z
---

# TP - Windows Deployment Services (WDS)  
## 🏗️ Pré-requis

✅ Serveur `DEPLOY` intégré au domaine `nivvlem.tssr.eni`  
✅ Image ISO de **Windows 10** disponible  
✅ VM `CliNvx` prête (sans OS)  

---

## ⚙️ Étapes de mise en œuvre
### 1️⃣ Ajout du rôle WDS + disque de stockage

#### Sur `DEPLOY` :

##### Ajout du rôle :

```powershell
Install-WindowsFeature WDS -IncludeManagementTools
```

##### Ajout d’un disque de 100 Go :

1. Ajouter un disque de 100 Go à la VM via **VMware Workstation**  
2. Initialiser le disque dans **Gestion des disques**  
3. Le partitionner, formater en **NTFS**, lettre **F:**  
4. Créer le dossier : `F:\WDS`

---

### 2️⃣ Configuration initiale de WDS

#### Lancer la configuration du service :

- Chemin du dossier de travail → `F:\WDS`  
- Paramétrage : le serveur doit répondre à **tous les clients**

#### Monter l’ISO Windows 10 :

- Monter l’ISO dans le lecteur CD de `DEPLOY` (ex : D:)

---

### 3️⃣ Ajout des images au service WDS

#### Image de démarrage :

- Source → `D:\sourcesoot.wim`  
- Ajouter dans **Images de démarrage**

#### Image d’installation :

- Source → `D:\sources\install.wim`  
- Ajouter dans **Images d’installation**  
- Choisir : `Windows 10 Pro N`

---

### 4️⃣ Déploiement d’un client (CliNvx)

#### Configuration VM `CliNvx` :

- **Démarrage en PXE** (réseau Host-Only)  
- Lancer le boot PXE → WDS → **WinPE** → Suivre l’assistant

#### Vérifier :

- Le déploiement s’effectue correctement  
- Windows 10 Pro N est installé sur `CliNvx`

---

### 5️⃣ Snapshot de l’infrastructure

| VM     | Action |
|--------|--------|
| INFRA  | Snapshot "Atelier 4 OK" |
| DEPLOY | Snapshot "Atelier 4 OK" |
| CliNvx | Snapshot "Atelier 4 OK" |

---

## 🚀 BONUS

### Suppression de l’écran "WDS Boot Manager"

#### Méthode :

Modifier les paramètres de réponse PXE → **ne pas afficher** le menu WDS Boot Manager.  
Exemple : dans les propriétés du serveur WDS → onglet **Boot**.

---

### Compte de service `deploy` dans AD

#### Création du compte :

```powershell
New-ADUser -Name "deploy" -SamAccountName "deploy" -AccountPassword (ConvertTo-SecureString "P@ssw0rd!" -AsPlainText -Force) -PasswordNeverExpires $true -CannotChangePassword $true -Enabled $true
```

#### Vérifier que le déploiement peut être réalisé avec ce compte.

---

## 📌 Bonnes pratiques

✅ Utiliser un disque **dédié** pour le stockage des images  
✅ Nommer clairement les **images de boot** et **images d’installation**  
✅ Garder les images **à jour** (MAJ Windows)  
✅ Toujours **tester le PXE** sur un poste vierge (CliNvx)  
✅ Automatiser la suppression de l’écran WDS Boot Manager pour fluidifier le déploiement

---

## ⚠️ Pièges à éviter

- Ne pas monter l’image ISO → pas d’images disponibles  
- Chemin incorrect pour `F:\WDS` → erreurs de service  
- PXE non autorisé / DHCP mal configuré → pas de boot réseau  
- Mauvais choix d’image (`Windows 10 Home` par erreur)  
- Snapshot oublié → pas de rollback possible !