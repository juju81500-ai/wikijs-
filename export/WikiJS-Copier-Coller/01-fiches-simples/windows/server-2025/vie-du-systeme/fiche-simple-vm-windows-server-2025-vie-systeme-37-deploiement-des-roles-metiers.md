# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_37_Deploiement_Des_Roles_Metiers

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 37 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Installer les rôles et fonctionnalités nécessaires.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités**.
   ```powershell
   Get-WindowsFeature | Where-Object Installed
   ```
   👉 Explication : dresse la liste de l'existant.

2. Installer un rôle par commande (exemple : IIS ; remplacer par le rôle voulu) :
   ```powershell
   Install-WindowsFeature -Name Web-Server -IncludeManagementTools
   ```
   👉 Explication : installe le rôle avec ses outils; le nom des rôles s'obtient par `Get-WindowsFeature`.

3. Contrôler et consulter les journaux d'installation :
   ```powershell
   Get-WindowsFeature Web-Server
   Get-Content C:\Windows\Logs\CBS\CBS.log -Tail 20
   ```
   👉 Explication : confirme l'état `Installed`.

## 2. Production — Contrôles

Un rôle par serveur quand c'est possible; documenter les ports ouverts.

## 3. Production — Sécurité

N'installer que les fonctionnalités nécessaires.

## Validation et retour arrière

- **Validation** : Le rôle apparaît `Installed` et le service répond.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)