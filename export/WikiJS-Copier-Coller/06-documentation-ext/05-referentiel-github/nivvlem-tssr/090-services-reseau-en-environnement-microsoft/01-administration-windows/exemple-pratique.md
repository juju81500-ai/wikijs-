# TP 1 & 2 – Installation, configuration initiale et gestion du stockage

## ✅ TP 1

### 🔹 Création des modèles

- Créer deux VM :
    - `VM_Modele_2019` avec Windows Server 2019, 2 Go RAM, 32 Go HDD
    - `VM_Modele_W10` avec Windows 10, 2 Go RAM, 32 Go HDD
- Réseau configuré en **mode bridge**

### 🔹 Installation et configuration initiale

- Installer Windows + mises à jour
- Installer **VMware Tools**
- Exécuter `sysprep /oobe /generalize /shutdown` dans `C:\Windows\System32\Sysprep`
- Éteindre les VM et créer un **groupe de modèles** dans VMware

### 🔹 Clonage des VM

- Cloner en VM complète :
    - `W19-CD1` et `W19-SRV1` à partir de `VM_Modele_2019`
    - `W10-CLI1` à partir de `VM_Modele_W10`

### 🔹 Plan d’adressage IP statique :

```plaintext
W19-CD1    → 172.28.10.1
W19-SRV1   → 172.28.10.2
W10-CLI1   → 172.28.10.11
Masque     → 255.255.0.0
Passerelle → (facultative dans ce cas)
DNS        → 127.0.0.1 (ou adresse AD si déployé ultérieurement)
```

### 🔹 Installation des rôles (graphiquement ou PowerShell)

```powershell
Install-WindowsFeature -Name Web-Server, Windows-Server-Backup -IncludeManagementTools
```

- Tester IIS dans un navigateur local (`http://localhost`) ou distant (`http://172.28.10.2`)

### 🔹 Activer le Bureau à distance (graphique ou PowerShell)

```powershell
Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -Name "fDenyTSConnections" -Value 0
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"
```

- Connexion : `mstsc /v:172.28.10.2`

---

## ✅ TP 2

### 🔹 Préparation

- Ajouter 3 disques SCSI de 10 Go à `W19-SRV1` dans VMware

### 🔹 Créer les volumes via **Gestion des disques**

#### 1. Volume RAID-5 – lecteur D:

- Convertir les 3 disques en **disques dynamiques**
- Créer un **volume RAID-5** sur les 3 disques → Lettre `D:`
- Nom : "Données"

#### 2. Volume miroir – montage C:\INFO-TOOLS

- Choisir 2 disques
- Créer un **volume en miroir (RAID-1)**
- Monter dans le dossier `C:\INFO-TOOLS` (créez le dossier au préalable)

#### 3. Volume optimisé RAID-0 – lecteur E:

- Sélectionner 2 autres disques non utilisés précédemment
- Créer un volume **RAID-0** (agrégation de bandes) → Lettre `E:`

### 🔹 Vérification en PowerShell :

```powershell
Get-Volume | Select DriveLetter, FileSystemLabel, SizeRemaining, HealthStatus
```

### 🔹 Simulation de panne

- Supprimer un disque dans VMware
- Observer le comportement des volumes dans la gestion des disques :
    - RAID-5 → toujours lisible ✅
    - RAID-1 → lisible ✅
    - RAID-0 → inaccessible ❌

### 🔹 Réparation du RAID-5

- Ajouter un nouveau disque de 10 Go
- Convertir en dynamique
- Étendre le volume RAID-5 pour inclure le nouveau disque via GUI

---

## 🧠 À retenir pour les révisions

- Clonage depuis un modèle sysprepé = gain de temps, homogénéité
- Toujours tester les rôles installés immédiatement (ex : IIS via navigateur)
- Préférer les disques dynamiques pour RAID logiciel
- RAID-5 tolère 1 panne, RAID-1 aussi, RAID-0 **aucune**

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Cloner à partir de modèles Sysprepés|Gain de temps, cohérence, flexibilité|
|Affecter des IPs statiques documentées|Meilleure lisibilité réseau, pas de conflit DHCP|
|Toujours tester le service post-install|Valider la configuration avant intégration dans un SI|
|Utiliser la GUI pour RAID complexe|Moins d’erreurs pour des manipulations critiques|
|Utiliser PowerShell pour l’automatisation|Permet l’industrialisation du déploiement|