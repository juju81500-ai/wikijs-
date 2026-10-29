# WDS (Windows Deployment Services)

## 📌 Présentation

**WDS (Windows Deployment Services)** est un rôle serveur Windows permettant de **déployer automatiquement des images d’installation Windows** (client ou serveur) sur des postes via le réseau (PXE).

Il est très utilisé en entreprise et en établissement scolaire pour :
- Déployer rapidement un parc de machines homogène
- Automatiser l’installation de Windows + drivers + logiciels

WDS utilise le protocole **PXE** (Preboot eXecution Environment) pour démarrer des machines sur le réseau et leur pousser une image d’installation.

---

## 🔧 Prérequis

- Contrôleur de domaine (AD recommandé)
- Serveur DHCP (peut être intégré ou externe)
- Serveur WDS (rôle installé sur Windows Server)
- Image de démarrage (boot.wim) et image d’installation (install.wim)

---

## 🏗️ Architecture typique

```
[DHCP] <--> [WDS Server] <--> [Clients PXE Boot]
```

- Le serveur WDS répond aux requêtes PXE.
- Les clients reçoivent une image de démarrage (WinPE).
- L’image de Windows est ensuite installée.

---

## ⚙️ Installation du rôle WDS
### Sur Windows Server (via PowerShell)

```powershell
Install-WindowsFeature -Name WDS -IncludeManagementTools
```

### Via Server Manager

1. Gérer > Ajouter des rôles
2. Rôle **Services de déploiement Windows**
3. Valider et installer

---

## 🗂️ Dossiers importants

| Dossier | Rôle |
|---------|------|
| `RemoteInstall` | Dossier racine des images WDS |
| `Boot Images` | Images de démarrage (WinPE) |
| `Install Images` | Images d’installation (Windows .wim) |

---

## 🧰 Cas d’usage courant

- Déploiement **massif de postes Windows** (salles, entreprise)
- **Réinstallation rapide** après panne
- Environnement de test pour différentes versions de Windows

---

## ⚠️ Erreurs fréquentes

- DHCP et WDS sur des serveurs différents → config PXE option 66/67 manquante
- Image boot.wim non modifiée (WinPE générique peu personnalisée)
- Mauvais pilotes réseau → poste PXE boot mais pas d’installation
- Mauvaise configuration du pare-feu (ports UDP 67, 68, 69, 4011…)

---

## ✅ Bonnes pratiques

- Créer une **image de référence personnalisée** (sysprep)
- Intégrer les pilotes réseau et stockage dans l’image de boot
- Tester le boot PXE sur plusieurs modèles de machines
- Coupler WDS avec MDT pour un déploiement plus automatisé (voir fiche MDT)
- Sauvegarder le dossier RemoteInstall régulièrement

---

## 📚 Ressource complémentaire

- [WDS Deployment Guide](https://learn.microsoft.com/en-us/iis/web-hosting/installing-infrastructure-components/deploying-images-with-wds)