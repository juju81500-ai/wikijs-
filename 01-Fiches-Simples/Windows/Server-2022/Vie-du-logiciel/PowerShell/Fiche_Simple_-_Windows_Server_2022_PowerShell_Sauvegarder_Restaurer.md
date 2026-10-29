# Fiche_Simple_-_Windows_Server_2022_PowerShell_Sauvegarder_Restaurer

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting
- **Tags** : `windows-server-2022`, `powershell`, `pwsh`, `scripting`, `remoting`

---

## Problème précis à résoudre

Sauvegarder et restaurer profils, inventaire de modules et configuration SSH de PowerShell sur Windows Server 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un dossier de sauvegarde et exporter l'inventaire des modules :
   ```powershell
   New-Item -ItemType Directory -Path C:\Sauvegarde\PowerShell -Force
   Get-Module -ListAvailable | Select-Object Name,Version | Export-Csv C:\Sauvegarde\PowerShell\modules.csv -NoTypeInformation
   ```
   👉 Explication : permet de réinstaller des versions identiques.

2. Copier profils et configuration SSH :
   ```powershell
   Copy-Item $PROFILE.CurrentUserAllHosts C:\Sauvegarde\PowerShell\ -ErrorAction SilentlyContinue
   Copy-Item $env:ProgramData\ssh\sshd_config C:\Sauvegarde\PowerShell\
   Get-FileHash C:\Sauvegarde\PowerShell\* -Algorithm SHA256
   ```
   👉 Explication : les clés privées d'hôte (`ssh_host_*_key`) ne doivent pas être copiées dans une sauvegarde non chiffrée.

3. Restaurer sshd_config puis redémarrer le service :
   ```powershell
   Copy-Item C:\Sauvegarde\PowerShell\sshd_config $env:ProgramData\ssh\sshd_config -Force
   Restart-Service sshd
   ```
   👉 Explication : remet la configuration SSH d'origine.

## 2. Production — Contrôles

Intégrer ces fichiers à la sauvegarde habituelle du serveur et la chiffrer. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Protéger l'accès au dossier (ACL restreintes).
- Ne pas sauvegarder de clés privées en clair.

## Validation et retour arrière

- **Validation** : fichiers présents, empreintes consignées, restauration testée en lab.
- **Retour arrière** : rejouer la restauration depuis la sauvegarde précédente.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Windows](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-windows)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_Windows_Server_2022_PowerShell_Prerequis_Limites.md)
