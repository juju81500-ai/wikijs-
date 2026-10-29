# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer toutes les mises à jour disponibles.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Windows Update > Rechercher des mises à jour**, puis redémarrer. Par commande avec le module `PSWindowsUpdate` (depuis la Galerie PowerShell) :
   ```powershell
   Install-Module PSWindowsUpdate -Scope AllUsers
   Get-WindowsUpdate -MicrosoftUpdate
   Install-WindowsUpdate -MicrosoftUpdate -AcceptAll -AutoReboot
   ```
   👉 Explication : recherche, installe et redémarre si nécessaire; répéter jusqu'à ce qu'il n'y ait plus de mise à jour.

2. Contrôler les correctifs installés :
   ```powershell
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
   ```
   👉 Explication : liste les 10 derniers correctifs.

3. Vérifier la version de build :
   ```powershell
   (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion').UBR
   [System.Environment]::OSVersion.Version
   ```
   👉 Explication : affiche la révision de build pour la comparer à la dernière publiée.

## 2. Production — Contrôles

Réaliser la mise à jour avant d'installer les rôles; prendre un point de contrôle de VM.

## 3. Production — Sécurité

Les serveurs non corrigés sont la première cause d'intrusion.

## Validation et retour arrière

- **Validation** : Plus aucune mise à jour proposée et build à jour.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)