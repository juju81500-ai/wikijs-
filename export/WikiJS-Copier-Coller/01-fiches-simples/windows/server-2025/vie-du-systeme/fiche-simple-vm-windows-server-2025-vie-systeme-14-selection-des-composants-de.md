# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Choisir l'édition et le mode d'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l'assistant d'installation, choisir **Windows Server 2025 Standard (Server Core)** ou **Standard (Expérience utilisateur)**, ou l'édition **Datacenter** si la licence l'exige. Contrôler après installation :
   ```powershell
   Get-ComputerInfo -Property WindowsProductName, WindowsEditionId, WindowsInstallationType, OsVersion, OsBuildNumber
   ```
   👉 Explication : indique l'édition, le type (`Server` pour Core ou `Server` avec interface) et la build.

2. Lister les images disponibles dans l'ISO (D: étant l'ISO montée) :
   ```powershell
   Get-WindowsImage -ImagePath D:\sources\install.wim | Select-Object ImageIndex, ImageName
   ```
   👉 Explication : affiche l'index de chaque édition proposée à l'installation.

3. Consulter le journal d'installation en cas de doute :
   ```powershell
   Get-Content C:\Windows\Panther\setupact.log -Tail 30
   ```
   👉 Explication : montre les dernières étapes de l'installation.

## 2. Production — Contrôles

Privilégier Server Core pour réduire la surface d'attaque et les correctifs; l'interface graphique reste utile pour les rôles qui l'exigent.

## 3. Production — Sécurité

Server Core expose moins de composants et de vulnérabilités.

## Validation et retour arrière

- **Validation** : Édition et build conformes au besoin.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)