# Fiche_Simple_-_VM_Windows_Server_2022_IIS_Installer_Role_Web_Server.md

- **Environnement** : VM Windows Server 2022 pilote
- **OS / Version** : Windows Server 2022; rôle Web Server (IIS)
- **Catégorie** : serveur Web / IIS

---

## Problème précis à résoudre

Ajouter le rôle IIS et ses outils d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Rôles de serveurs > Serveur Web (IIS)**, puis cocher les outils de gestion.
   👉 Explication : équivalent graphique de la commande ci-dessous.

2. En PowerShell élevé, contrôler, installer puis recontrôler :
   ```powershell
   Get-WindowsFeature Web-Server, Web-Mgmt-Tools
   Install-WindowsFeature -Name Web-Server -IncludeManagementTools
   Get-WindowsFeature Web-Server, Web-Mgmt-Tools
   ```
   👉 Explication : l'installation modifie le système : l'effectuer sur un pilote et suivre la politique de redémarrage.

## 2. Production — Contrôles

N'installer ensuite que les composants `Web-*` requis par le runtime ou le protocole documenté.

## 3. Production — Sécurité

- Ne pas cocher les fonctionnalités optionnelles par défaut sans revue.

## Validation et retour arrière

- **Validation** : `Get-WindowsFeature Web-Server` indique `Installed`.
- **Retour arrière** : `Uninstall-WindowsFeature -Name Web-Server` seulement après évaluation des dépendances (ne pas désinstaller un rôle de production sans plan).

## Si le problème n'est pas résolu

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Microsoft Learn — Install-WindowsFeature](https://learn.microsoft.com/en-us/powershell/module/servermanager/install-windowsfeature)
- [Guide complet installation IIS Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022#2-installer-le-role-web-server)