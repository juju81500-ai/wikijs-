# 📄 PowerShell

- **Environnement** : VM ou poste Windows 11 de test (compte standard, élévation uniquement si requise) ; Debian 13 pour l'étape PowerShell 7 sous Linux
- **OS / Version** : Windows 11 x64 et Debian 13 - PowerShell 7.6.9 Stable (LTS), installé côte à côte avec Windows PowerShell 5.1
- **Catégorie** : Scripting, développement et administration

## 🎯 Problème précis à résoudre
Installer et valider PowerShell 7.6.9 sur Windows 11 (et sur Debian 13 pour PowerShell 7), vérifier quel shell est actif, puis exécuter des contrôles en lecture seule sans affaiblir la stratégie d'exécution.

> **Guide complet lié** : [Administrer Windows 11 avec PowerShell 7.6.9](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11). Cette fiche ne couvre que le parcours minimal de validation ; la gestion des modules, des profils, de la journalisation et des secrets est dans le guide.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification du shell PowerShell 7 sur Windows 11 (ouvrir **PowerShell 7** depuis le menu Démarrer) :
   ```powershell
   $PSVersionTable | Select-Object PSVersion, PSEdition, Platform
   ```
   👉 Explication : Confirme la version 7.6.9 et l'édition `Core`. Windows PowerShell 5.1 apparaît avec l'édition `Desktop`.

2. Présence des deux shells et de leurs exécutables :
   ```powershell
   Get-Command pwsh, powershell -ErrorAction SilentlyContinue | Select-Object Name, Source
   ```
   👉 Explication : `pwsh` désigne PowerShell 7 ; `powershell.exe` lance toujours Windows PowerShell 5.1, qui n'est pas remplacé.

3. Installation de PowerShell 7 sur Debian 13 à partir du dépôt Microsoft :
   ```bash
   wget -q https://packages.microsoft.com/config/debian/13/packages-microsoft-prod.deb -O /tmp/packages-microsoft-prod.deb && sudo dpkg -i /tmp/packages-microsoft-prod.deb && sudo apt update && sudo apt install -y powershell
   ```
   👉 Explication : Ajoute le dépôt officiel Microsoft pour Debian 13 puis installe le paquet `powershell`. Disponibilité du dépôt pour Debian 13 à vérifier sur la version déployée.

4. Contrôle de la version sous Linux :
   ```bash
   pwsh -NoProfile -Command '$PSVersionTable.PSVersion'
   ```
   👉 Explication : Affiche le numéro de version de PowerShell 7 installé. Attendu : `7.6.9`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Contrôle de la signature du MSI téléchargé depuis la publication officielle (remplacer `<chemin_du_msi>` par le chemin complet du fichier `PowerShell-7.6.9-win-x64.msi`) :
   ```powershell
   Get-AuthenticodeSignature -FilePath "<chemin_du_msi>" | Select-Object Status, SignerCertificate
   ```
   👉 Explication : `Status` doit valoir `Valid` et le signataire doit être Microsoft. Refuser le fichier dans le cas contraire.

2. Contrôle de l'empreinte SHA-256 :
   ```powershell
   Get-FileHash -Algorithm SHA256 -Path "<chemin_du_msi>"
   ```
   👉 Explication : Compare la valeur obtenue à celle publiée dans les notes de version v7.6.9 (valeur de référence détaillée dans la section 2 du guide complet). Refuser le MSI si les valeurs diffèrent.

3. Lancement de l'installateur validé :
   ```powershell
   Start-Process -FilePath "<chemin_du_msi>" -Wait
   ```
   👉 Explication : Lance l'installation de PowerShell 7 avec l'assistant Microsoft. Conserver les options de mise à jour imposées par la politique du poste (Microsoft Update ou WSUS).

4. Validation de la version installée :
   ```powershell
   & "$env:ProgramFiles\PowerShell\7\pwsh.exe" -NoProfile -Command '$PSVersionTable.PSVersion'
   ```
   👉 Explication : Appelle directement l'exécutable installé, sans dépendre du PATH. Attendu : `7.6.9`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Lecture de la stratégie d'exécution effective, sans la modifier :
   ```powershell
   Get-ExecutionPolicy -List
   ```
   👉 Explication : Affiche la stratégie par portée (processus, utilisateur, machine). Ne jamais définir `Bypass` ou `Unrestricted`, ni affaiblir une stratégie imposée par GPO. Une stratégie d'exécution n'est pas une frontière de sécurité.

2. Inventaire des modules disponibles avant tout script :
   ```powershell
   Get-Module -ListAvailable | Sort-Object Name, Version | Select-Object Name, Version, Path
   ```
   👉 Explication : Liste les modules, leur version et leur emplacement. N'utiliser que des modules approuvés, dont l'éditeur, la version et les dépendances ont été vérifiés.

3. Contrôle en lecture seule de l'état de la machine :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   ```
   👉 Explication : Confirme la version de Windows 11 et le numéro de build avant d'exécuter un script dont le support de version est limité.

4. Vérification que le service d'administration à distance n'est pas activé par cette fiche :
   ```powershell
   Get-Service -Name WinRM | Select-Object Name, Status, StartType
   ```
   👉 Explication : Commande en lecture seule. WinRM / PowerShell Remoting n'est pas configuré par cette fiche ; son état doit rester conforme à la politique du poste.