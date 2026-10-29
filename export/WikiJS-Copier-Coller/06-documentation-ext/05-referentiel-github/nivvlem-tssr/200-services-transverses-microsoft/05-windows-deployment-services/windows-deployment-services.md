# Windows Deployment Services (WDS)
## 🧩 Présentation du service WDS

- **Windows Deployment Services** (WDS) est un rôle Windows Server qui permet de :
    - Déployer des systèmes d’exploitation par le réseau (PXE boot)
    - Gérer des images **WIM** de manière centralisée
    - Automatiser l’installation de Windows sur des postes clients

### Fonctionnement général

```text
Client PXE → Serveur DHCP → Serveur WDS → Image de démarrage → Image d'installation
```

### Avantages

- Évite de préparer des **clés USB** pour chaque machine
- Gain de temps pour le déploiement en masse
- Compatible avec **MDT** pour automatisation avancée

---

## ⚙️ Prérequis de mise en œuvre

### Prérequis techniques

- Serveur **membre du domaine** (recommandé)
- Rôle **DHCP** présent et configuré correctement
- Accès aux **images ISO Windows** (sources des WIM)

### Compatibilité

- BIOS Legacy ou UEFI
- WDS supporte les deux mais la configuration PXE doit être adaptée

---

## 🔄 WDS et DHCP

- WDS et DHCP doivent coexister sur le réseau :

### Si DHCP sur le même serveur que WDS

- Activer les options PXE dans les propriétés de WDS

### Si DHCP sur un autre serveur

- Ajouter les options DHCP :
    - **Option 66** : nom ou IP du serveur WDS
    - **Option 67** : nom du fichier de boot (ex : `boot\\x64\\wdsnbp.com`)

### Commandes utiles

```powershell
# Installer le rôle WDS
Install-WindowsFeature -Name WDS -IncludeManagementTools
```

---

## 🛠️ Installation du service WDS

### Via l’assistant (Server Manager)

1️⃣ Ajouter le rôle **Windows Deployment Services**  
2️⃣ Installer les services suivants :

- Déploiement de transport
- Serveur de déploiement

### Configuration initiale

- Dossier de stockage des images (ex: `D:\\RemoteInstall`)
- Intégration dans AD DS (mode recommandé)

---

## 🛠️ Configuration initiale du service WDS

- Dossier de stockage : `RemoteInstall`
- Mode : intégré à **Active Directory** (permet un suivi des machines)
- Autoriser le démarrage PXE pour :
    - Tous les ordinateurs (pour phase de test)
    - Puis affiner (uniquement ordinateurs connus)

---

## 🎬 Démonstration - Déploiement de WDS

### Processus PXE

1️⃣ Client démarre en PXE (F12)  
2️⃣ Téléchargement de l’image de démarrage (WinPE → `boot.wim`)  
3️⃣ Lancement de l’installation Windows

### Étapes observées

- Découverte DHCP → serveur WDS
- Téléchargement de l’image de boot
- Installation de l’image Windows

---

## 🛠️ Configuration globale du service WDS

### Options clés

- **Réponses PXE automatiques** :
    - Tous les clients
    - Clients connus uniquement
- **Filtrage PXE** :
    - Contrôle par AD (par OU, par groupe)
- **Multicast** :
    - Permet de déployer plusieurs machines simultanément → gain de bande passante

---

## 📦 Images de démarrage et d’installation

### Image de démarrage

- Image **boot.wim** issue du média Windows
- Permet de lancer l’environnement **WinPE**

### Image d’installation

- Image **install.wim** issue du média Windows
- Contient les versions de Windows disponibles

---

## ➕ Ajout d’image de démarrage

### Processus

1️⃣ Copier le fichier `boot.wim` depuis le dossier `sources` du DVD ISO  
2️⃣ Ajouter dans la console WDS → Images de démarrage

---

## ➕ Ajout d’image d’installation

### Processus

1️⃣ Copier le fichier `install.wim` depuis le DVD ISO  
2️⃣ Ajouter dans la console WDS → Images d’installation  
3️⃣ Organiser par **groupe d’images** (ex: Windows 10 Pro, Windows 11 Enterprise)

---

## 🔍 Suite ou fin ?

- WDS seul = bien pour **déploiement simple**
- WDS + MDT = recommandé pour scénarios avancés (avec séquences de tâches)
- WDS + MDT + SCCM = pour **grandes infrastructures**

---

## 🚀 Pour aller plus loin

- Intégration des **drivers spécifiques**
- Création de **séquences de tâches** (via MDT)
- Automatisation avec **fichiers de réponse**
- Gestion avancée de **captation d’images** (custom WIM)

---

## 🎥 Images de capture

### Objectif

- Créer une image personnalisée à partir d’un poste de référence

### Processus

1️⃣ Ajouter une image de capture via WDS  
2️⃣ Démarrer le poste en PXE sur cette image  
3️⃣ Capturer l’image du disque en WIM  
4️⃣ Réinjecter cette image dans WDS pour déploiement ultérieur

---

## 📝 Fichiers de réponse

### Objectif

- Automatiser l’installation de Windows
- Réduire les interactions manuelles (unattended.xml)

### Outil de création

- **Windows System Image Manager** (SIM, fourni avec ADK)

### Exemples d’automatisation

- Acceptation de la licence
- Clé produit
- Nom du PC
- Joindre au domaine

---

## 🎯 Spécificités du déploiement de Windows 11 avec WDS

|Élément|Particularité / impact sur le déploiement|
|---|---|
|**TPM 2.0** obligatoire|TPM 2.0 doit être activé dans le BIOS/UEFI, sinon l'installation sera bloquée|
|**Secure Boot**|Obligatoire également (doit être activé)|
|**UEFI uniquement**|Le support de BIOS Legacy est officiellement abandonné pour Windows 11 (WDS doit être configuré en mode UEFI PXE !)|
|**Drivers**|Certains matériels plus anciens ne sont plus compatibles|
|**Compatibilité MDT/WDS**|MDT doit être en version >= 8456 + ADK Windows 11 compatible|
|**Images**|L’`install.wim` de Windows 11 est en général plus lourd (> 5 Go), nécessite parfois de configurer IIS ou TFTP en conséquence si utilisé avec PXE|

### Impact sur la configuration WDS

✅ **DHCP / PXE**

- Il faut prévoir un PXE UEFI (bootx64.efi), pas seulement du **BIOS Legacy**.
- Fichier de boot typique pour UEFI : `boot\\x64\\wdsmgfw.efi`

✅ **Images de démarrage**

- Bien utiliser une **image de boot** issue de l’ADK Windows 11 (WinPE adaptée).

✅ **TPM 2.0**

- Le contrôle du TPM se fait au moment de la vérification des prérequis Windows 11 :
    - Si TPM non présent ou désactivé → installation bloquée.
- Possible de contourner le contrôle TPM **dans un contexte de test / lab** via modification de `unattend.xml` ou registre, mais **non supporté en prod**.

✅ **Secure Boot**

- Il doit être activé sur les machines cible.
- Vérifier que le serveur WDS accepte les clients Secure Boot.

### Commandes utiles pour vérifier le support matériel Windows 11

```powershell
# Vérification de la compatibilité TPM
Get-WmiObject -Namespace root\\cimv2\\security\\microsofttpm -Class Win32_Tpm

# Vérification de l’état du Secure Boot
Confirm-SecureBootUEFI
```

---

## ✅ À retenir pour les révisions

- WDS = service de **déploiement PXE**
- Permet de déployer des **images WIM**
- Le service s’appuie sur **DHCP** pour le boot PXE
- La combinaison **WDS + MDT** est très puissante
- Les **images de capture** permettent de standardiser les postes
- Les **fichiers de réponse** automatisent l’installation
- **Windows 11** apporte des spécificités : TPM 2.0, Secure Boot, UEFI obligatoire

---

## 📌 Bonnes pratiques professionnelles

- Documenter la **structure des images** (versions, date de build)
- Garder les images **à jour** (Windows + drivers)
- **Sécuriser le PXE** (éviter d’ouvrir à tout le réseau)
- Utiliser des **collections ciblées** pour le multicast
- Contrôler l’accès aux **images de capture**
- Tester systématiquement les **fichiers de réponse** avant production
- Prévoir des **snapshots** ou backups avant déploiements massifs
- Intégrer WDS avec MDT pour une meilleure flexibilité
- Anticiper les contraintes **UEFI / Secure Boot / TPM 2.0** pour les parcs Windows 11