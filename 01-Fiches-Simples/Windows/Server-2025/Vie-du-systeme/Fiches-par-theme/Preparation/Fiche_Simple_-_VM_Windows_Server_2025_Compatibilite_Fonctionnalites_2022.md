# 📄 Fiche_Simple_-_VM_Windows_Server_2025_Compatibilite_Fonctionnalites_2022.md

- **Environnement** : Migration ou coexistence de serveurs Windows Server 2022 et 2025
- **OS / Version** : Windows Server 2022 / Windows Server 2025
- **Catégorie** : Compatibilité / Sécurité / Migration
- **Tags** : `[windows-server-2022]`, `[windows-server-2025]`, `[compatibilite]`, `[smb]`, `[openssh]`, `[active-directory]`

## 🎯 Problème précis à résoudre
Vérifier les différences de prérequis et de valeurs par défaut avant d'installer Windows Server 2025, d'ajouter un rôle, de migrer un serveur 2022 ou de connecter des clients SMB/LDAP anciens.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier édition, build, options Core/Desktop Experience et ressources VM :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores
   Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize
   ```
2. Vérifier les valeurs SMB locales avant de connecter un NAS ou client tiers :
   ```powershell
   Get-SmbClientConfiguration | Select-Object RequireSecuritySignature, RequireEncryption
   Get-SmbServerConfiguration | Select-Object RequireSecuritySignature, EncryptData, RejectUnencryptedAccess
   ```
3. Vérifier OpenSSH et les rôles réellement installés :
   ```powershell
   Get-Service sshd -ErrorAction SilentlyContinue
   Get-WindowsFeature | Where-Object Installed
   ```
   👉 *Explication : Server 2025 ajoute SSE4.2 et POPCNT aux prérequis CPU; OpenSSH Server est installé par défaut mais son service et son exposition restent à valider.*

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Résultats** : rôles et fonctionnalités installés; `winver` pour la version.
  👉 Explication : équivalent graphique de `Get-WindowsFeature` et du contrôle de version.

## ⚡ 2. Production — Façon Simplifiée
1. **Avant installation ou mise à niveau :** vérifier CPU/firmware, licences, éditeur d'application, sauvegarde restaurable, option Core/Desktop et retour arrière.
2. **SMB :** tester signature et chiffrement avec tous les clients et NAS. Server 2025 exige la signature SMB sortante par défaut et renforce le chiffrement client; ne pas désactiver ces protections pour masquer une incompatibilité.
3. **OpenSSH :** contrôler service, règle pare-feu, groupe `OpenSSH Users` et clés avant de l'exposer; ne pas supposer que le service est démarré parce que le composant est présent.
4. **AD DS :** vérifier les applications LDAP non signées, les clients anciens, le niveau fonctionnel et la réplication avant d'ajouter un DC 2025. Les nouvelles options de niveau fonctionnel et de pages AD 32K ne doivent pas être activées globalement sans étude forêt-wide.
5. Tester chaque rôle sur un environnement pilote et vérifier événements, authentification, partages, imprimantes, sauvegardes et agents de supervision.

## 🔒 3. Production — Façon Sécurisée
1. Ne pas modifier par défaut la signature SMB, LDAP, Kerberos ou Credential Guard sur un domaine pour rétablir un ancien client.
2. Maintenir Server Core/Desktop Experience cohérent avec l'application : il n'existe pas de conversion sur place entre ces options.
3. Séparer installation/mise à niveau du système et migration de rôle; un nouveau serveur membre/DC doit suivre le runbook AD DS approprié.

## ✅ Validation et retour arrière
- Documenter les valeurs SMB, les clients testés, l'état OpenSSH, les niveaux AD et les versions avant/après.
- Tester une restauration dans une VM isolée et valider les données avant toute bascule.
- Si l'interopérabilité échoue, interrompre la migration et revenir au serveur/version précédente selon le plan, sans abaisser globalement la sécurité.

## 🔗 Sources officielles
- [Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Exigences matérielles Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements)