# Fiche_Simple_-_VM_Windows_11_PuTTY_Telecharger_Verifier.md

- **Environnement** : Poste Windows 11 x64 d'administration
- **OS / Version** : Windows 11 x64; PuTTY 0.85 Stable
- **Catégorie** : client SSH / intégrité

---

## Problème précis à résoudre

Obtenir le MSI officiel et prouver son intégrité.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le MSI, sa signature détachée et la clé de publication :
   ```powershell
   $download = Join-Path $HOME 'Downloads\putty-0.85'
   New-Item -ItemType Directory -Force -Path $download | Out-Null
   Set-Location $download
   Invoke-WebRequest -Uri 'https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.85-installer.msi' -OutFile '.\putty-64bit-0.85-installer.msi'
   Invoke-WebRequest -Uri 'https://the.earth.li/~sgtatham/putty/latest/w64/putty-64bit-0.85-installer.msi.gpg' -OutFile '.\putty-64bit-0.85-installer.msi.gpg'
   Invoke-WebRequest -Uri 'https://www.chiark.greenend.org.uk/~sgtatham/putty/keys/release-2026.asc' -OutFile '.\release-2026.asc'
   ```
   👉 Explication : récupère les trois fichiers depuis les URL officielles du guide.

2. Importer la clé et contrôler son empreinte, puis la signature :
   ```powershell
   gpg --import .\release-2026.asc
   gpg --fingerprint 5C67D0F88BC3E5B5
   gpg --verify .\putty-64bit-0.85-installer.msi.gpg .\putty-64bit-0.85-installer.msi
   ```
   👉 Explication : l'empreinte complète doit être `1A07 DAC0 F220 CF12 248E A719 5C67 D0F8 8BC3 E5B5` et la signature bonne; sinon refuser le fichier. Gpg4win fournit GPG sur Windows.

3. Vérifier la signature Authenticode et le SHA-256 :
   ```powershell
   $signature = Get-AuthenticodeSignature .\putty-64bit-0.85-installer.msi
   $signature.Status
   $signature.SignerCertificate.Subject
   Get-FileHash .\putty-64bit-0.85-installer.msi -Algorithm SHA256
   ```
   👉 Explication : le statut doit être `Valid`; comparer le signataire et le SHA-256 aux informations publiées.

## 2. Production — Contrôles

Ne pas installer si l'empreinte, la signature ou la provenance est douteuse.

## 3. Production — Sécurité

- Vérification GPG et Authenticode obligatoires avant installation.

## Validation et retour arrière

- **Validation** : GPG et Authenticode sont valides.
- **Retour arrière** : Supprimer le dossier de téléchargement en cas d'échec de vérification.

## Si le problème n'est pas résolu

- [PuTTY — page officielle](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
- [PuTTY — clés de signature](https://www.chiark.greenend.org.uk/~sgtatham/putty/keys.html)
- [Guide complet — 2. Télécharger et vérifier l'installateur](/02-fiches-completes/windows/client-11/installation-deploiement/84-deploiement-putty-0-85-windows-11#2-telecharger-et-verifier-linstallateur)