# 📄 VM_WinSrv_2022_Stockage_Partage-SMB-Permissions-NTFS.md

- **Environnement** : VM (Windows Server 2022 Serveur de Fichiers)
- **OS / Version** : Windows Server 2022 - Famille Windows
- **Catégorie** : Stockage / Partages & Sécurité

## 🎯 Problème précis à résoudre
Créer un répertoire sur un volume de données, configurer un partage SMB réseau, cumuler et ajuster les autorisations de partage SMB et les autorisations de sécurité NTFS (ACL), et activer l'Abe (Access-Based Enumeration) pour masquer les dossiers non autorisés.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création d'un dossier de test sur le lecteur C: :
   `New-Item -Path "C:\PartageTest" -ItemType Directory`
   👉 Explication : Crée le répertoire physique C:\PartageTest.

2. Partage rapide du dossier sur le réseau avec accès total :
   `New-SmbShare -Name "PartageTest" -Path "C:\PartageTest" -FullAccess "Everyone"`
   👉 Explication : Rend le dossier accessible à tous sur le réseau `\\serveur\PartageTest` sans restriction initiale.

3. Test d'accès local SMB :
   `Get-SmbShare -Name "PartageTest"`
   👉 Explication : Affiche le statut et le chemin d'accès du partage réseau.

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Services de fichiers et de stockage > Partages > Tâches > Nouveau partage...**, choisir le dossier, régler les autorisations (éviter `Everyone`) et valider.
  👉 Explication : équivalent de `New-SmbShare`; ou `fsmgmt.msc` pour la console Dossiers partagés.

## ⚡ 2. Production — Façon Simplifiée
1. Création du dossier de données sur un volume dédié (D:) :
   `New-Item -Path "D:\Donnees_Entreprise" -ItemType Directory`
   👉 Explication : Stocke les données sur un disque secondaire D: pour isoler le système d'exploitation C:.

2. Configuration du partage SMB avec autorisation "Everyone / Tout le monde = Modification" :
   `New-SmbShare -Name "Donnees_Entreprise" -Path "D:\Donnees_Entreprise" -ChangeAccess "Tout le monde"`
   👉 Explication : Applique la règle recommandée : accorder la modification au niveau SMB et gérer le verrouillage fin via les permissions NTFS.

3. Attribution des autorisations NTFS pour le groupe d'administration et les utilisateurs :
   `$acl = Get-Acl "D:\Donnees_Entreprise"; $ruleAdmin = New-Object System.Security.AccessControl.FileSystemAccessRule("LAB\GRP_TSSR_Admins","FullControl","ContainerInherit,ObjectInherit","None","Allow"); $acl.AddAccessRule($ruleAdmin); Set-Acl "D:\Donnees_Entreprise" $acl`
   👉 Explication : Accorde le contrôle total NTFS au groupe d'administration avec héritage automatique sur les sous-dossiers et fichiers.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activation de l'Énumération Basée sur l'Accès (Access-Based Enumeration - ABE) :
   `Set-SmbShare -Name "Donnees_Entreprise" -FolderEnumerationMode AccessBased`
   👉 Explication : Masque automatiquement les dossiers et fichiers auxquels l'utilisateur connecté n'a pas le droit d'accéder en lecture.

2. Force du chiffrement des flux réseau SMB3 (SMB Encryption) :
   `Set-SmbShare -Name "Donnees_Entreprise" -EncryptData $true`
   👉 Explication : Chiffre l'intégralité des échanges de fichiers sur le réseau entre le client et le serveur pour empêcher l'interception de données (Eavesdropping).

3. Suppression de l'héritage NTFS et purge des accès implicites "Utilisateurs Authentifiés" :
   `$acl = Get-Acl "D:\Donnees_Entreprise"; $acl.SetAccessRuleProtection($true, $false); Set-Acl "D:\Donnees_Entreprise" $acl`
   👉 Explication : Casse l'héritage du disque parent D: et supprime toutes les permissions résiduelles non définies explicitement.

4. Verrouillage strict des permissions NTFS selon le modèle AGDLP (Account -> Global Group -> Domain Local Group -> Permission) :
   `$ruleSec = New-Object System.Security.AccessControl.FileSystemAccessRule("LAB\DL_Donnees_Lecteurs","ReadAndExecute","ContainerInherit,ObjectInherit","None","Allow"); $acl.AddAccessRule($ruleSec); Set-Acl "D:\Donnees_Entreprise" $acl`
   👉 Explication : Accorde uniquement la lecture/exécution aux membres du groupe local de domaine DL_Donnees_Lecteurs.