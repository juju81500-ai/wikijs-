# Fiche_Simple_-_VM_Windows_11_PowerShell7_Installer_Version_Stable.md

- **Environnement** : VM ou poste Windows 11 de test; compte standard puis élévation uniquement si requise
- **OS / Version** : Windows 11 x64; PowerShell 7.6.9 Stable (LTS)
- **Catégorie** : administration / PowerShell

---

## Problème précis à résoudre

Installer PowerShell 7.6.9 depuis le MSI officiel après vérification de signature et de hash.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le MSI x64 officiel :
   ```powershell
   $download = Join-Path $HOME 'Downloads\PowerShell-7.6.9'
   New-Item -ItemType Directory -Force -Path $download | Out-Null
   $msi = Join-Path $download 'PowerShell-7.6.9-win-x64.msi'
   Invoke-WebRequest -Uri 'https://github.com/PowerShell/PowerShell/releases/download/v7.6.9/PowerShell-7.6.9-win-x64.msi' -OutFile $msi
   ```
   👉 Explication : on télécharge uniquement depuis la publication officielle v7.6.9 sur GitHub.

2. Vérifier la signature Authenticode et calculer le SHA-256 :
   ```powershell
   $signature = Get-AuthenticodeSignature -FilePath $msi
   $signature.Status
   $signature.SignerCertificate.Subject
   Get-FileHash -Path $msi -Algorithm SHA256
   ```
   👉 Explication : le statut doit être `Valid`, le signataire Microsoft, et le hash identique à celui de l'asset dans les notes de version (x64 : `50D33C7494AAF82B987CFD4DE3F232D04F91FDD4C0DEECA8A669CCED3E7CF8F9`). Refuser le MSI sinon.

3. Lancer l'installateur validé :
   ```powershell
   Start-Process msiexec.exe -Wait -ArgumentList '/i', $msi
   ```
   👉 Explication : le MSI ajoute `pwsh.exe` au chemin par défaut; une approbation UAC peut être demandée. En GUI : **double-clic sur le fichier .msi** puis assistant.

4. Conserver les options de mise à jour par Microsoft Update/WSUS selon la politique du poste dans l'assistant d'installation.
   👉 Explication : on respecte la politique de mise à jour de l'organisation.

## 2. Production — Contrôles

Tester sur un poste pilote avant déploiement et conserver la preuve de vérification (signature, hash).

## 3. Production — Sécurité

- Refuser tout MSI dont la signature ou le hash diffère.
- Ne pas activer PowerShell Remoting pendant l'installation.

## Validation et retour arrière

- **Validation** : `pwsh` est installé et le MSI vérifié.
- **Retour arrière** : Désinstaller via **Paramètres > Applications > Applications installées > PowerShell > Désinstaller**.

## Si le problème n'est pas résolu

- [Microsoft Learn — Installer PowerShell 7 sur Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
- [PowerShell — publication v7.6.9](https://github.com/PowerShell/PowerShell/releases/tag/v7.6.9)
- [Guide complet PowerShell 7.6.9 Windows 11](/02-fiches-completes/windows/client-11/installation-deploiement/85-administration-powershell-7-6-9-windows-11#2-installer-la-version-stable)