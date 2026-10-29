---
title: "VM_WinSrv_2022_Stockage_Creer-Partage-SMB-Et-Droits-NTFS"
description: "Créer un dossier partagé réseau (Partage SMB), attribuer les autorisations de partage et combiner les autorisations de sécurité NTFS fines selon le modèle AGDLP."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[winsrv2022]", "[smb]", "[partage]", "[ntfs]", "[acl]", "[gui]", "[powershell]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_WinSrv_2022_Stockage_Creer-Partage-SMB-Et-Droits-NTFS.md

- **Environnement** : VM / Serveur de Fichiers Windows
- **OS / Version** : Windows Server 2022 Standard / Datacenter
- **Catégorie** : Stockage / Partage SMB & Permissions
- **Tags** : `[winsrv2022]`, `[smb]`, `[partage]`, `[ntfs]`, `[acl]`, `[gui]`, `[powershell]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer un dossier partagé réseau (Partage SMB), attribuer les autorisations de partage et combiner les autorisations de sécurité NTFS fines selon le modèle AGDLP.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Prérequis
- Ouvrir une session avec un compte autorisé à administrer le serveur de fichiers.
- Utiliser un volume de données prévu à cet effet, par exemple `D:` ; ne pas créer le partage à la racine d'un volume.
- Faire créer/valider par l'équipe AD les groupes de ressources **Domain Local** selon AGDLP, par exemple `LAB\DL_Donnees_Lecture` et `LAB\DL_Donnees_Modification`, avec les groupes globaux d'utilisateurs membres.
- Définir qui doit avoir le contrôle total du partage et du dossier ; conserver les entrées système et administrateurs nécessaires.

### Créer le partage SMB
1. Ouvrir **Gestionnaire de serveur** > **Services de fichiers et de stockage** > **Partages**.
2. Dans **TÂCHES**, choisir **Nouveau partage...**. Si le rôle Serveur de fichiers n'est pas installé, l'ajouter d'abord par **Gérer** > **Ajouter des rôles et fonctionnalités** > **Services de fichiers et de stockage** > **Serveur de fichiers**.
3. Dans l'assistant, choisir **Partage SMB - Rapide**, sélectionner le serveur et le volume de données, puis indiquer le dossier `D:\Donnees_Entreprise` et le nom de partage `Donnees_Entreprise`.
4. Dans les paramètres du partage, activer **Énumération basée sur l'accès** si les utilisateurs ne doivent pas voir les entrées auxquelles ils n'ont pas accès. Cette option masque des noms dans l'énumération ; elle ne remplace pas les autorisations.
5. Activer **Chiffrer l'accès aux données** seulement si les clients prennent en charge SMB 3.x et si les exigences de performance ont été évaluées. Les clients incompatibles risquent de ne pas accéder au partage.
6. Dans **Autorisations**, personnaliser les droits SMB : attribuer **Lecture** à `LAB\DL_Donnees_Lecture` et **Modification** à `LAB\DL_Donnees_Modification`. Éviter les accès larges comme `Tout le monde` ; ne retirer ni **Administrateurs** ni **SYSTEM** sans procédure validée.
7. Terminer l'assistant. Noter le chemin UNC, par exemple `\\FS01\Donnees_Entreprise`.

### Régler les autorisations NTFS
1. Dans l'Explorateur de fichiers, ouvrir les propriétés de `D:\Donnees_Entreprise` > **Sécurité** > **Avancé**.
2. Vérifier l'héritage et les entrées existantes avant de les modifier. Ne pas casser l'héritage sans savoir quels droits seront conservés ; préserver **SYSTEM** et les administrateurs autorisés.
3. Ajouter `LAB\DL_Donnees_Lecture` avec **Lecture et exécution**, **Afficher le contenu du dossier** et **Lecture**.
4. Ajouter `LAB\DL_Donnees_Modification` avec **Modification**. Ne pas accorder **Contrôle total** aux groupes utilisateurs.
5. Appliquer les changements au dossier, sous-dossiers et fichiers uniquement si c'est le périmètre voulu. Vérifier l'héritage sur un sous-dossier représentatif.

Les droits réellement obtenus à distance sont limités par la combinaison des autorisations de partage SMB et NTFS : l'autorisation la plus restrictive s'applique. AGDLP signifie **Accounts > Global groups > Domain Local groups > Permissions** ; les ACL du partage et du dossier sont attribuées aux groupes Domain Local, pas directement aux personnes.

### Vérifier depuis un poste client
1. Depuis un poste autorisé, ouvrir `\\FS01\Donnees_Entreprise` avec un compte membre du groupe concerné. Vérifier lecture seule pour `DL_Donnees_Lecture`, puis création/modification pour `DL_Donnees_Modification`.
2. Depuis un compte non autorisé, vérifier que l'accès est refusé. Avec ABE activé, vérifier aussi que les sous-dossiers sans droit de lecture ne sont pas énumérés.
3. En cas d'échec, contrôler séparément la résolution DNS, la connectivité SMB/pare-feu, les autorisations de partage, les ACL NTFS et l'appartenance effective aux groupes. Ne pas résoudre le problème en donnant des droits à `Tout le monde`.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Création rapide d'un partage SMB de test via PowerShell** :
   ```powershell
   New-Item -Path "C:\PartageTest" -ItemType Directory
   New-SmbShare -Name "PartageTest" -Path "C:\PartageTest" -ChangeAccess "LAB\DL_PartageTest_Modification"
   ```
   👉 *Explication : Crée un partage de test accessible en modification uniquement au groupe Domain Local prévu. Créer ce groupe et y ajouter les comptes de test avant d'exécuter la commande.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Création du dossier et partage SMB sécurisé avec droits de modification** :
   ```powershell
   New-Item -Path "D:\Donnees_Entreprise" -ItemType Directory
   New-SmbShare -Name "Donnees_Entreprise" -Path "D:\Donnees_Entreprise" -ReadAccess "LAB\DL_Donnees_Lecture" -ChangeAccess "LAB\DL_Donnees_Modification"
   ```
   👉 *Explication : Crée le partage avec des groupes Domain Local distincts pour la lecture et la modification. Les ACL NTFS doivent également être configurées pour ces groupes avant la mise en service.*

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. **Activation de l'Access-Based Enumeration (ABE) et du chiffrement SMB3** :
   ```powershell
   Set-SmbShare -Name "Donnees_Entreprise" -FolderEnumerationMode AccessBased -EncryptData $true
   ```
   👉 *Explication : ABE masque les entrées que l'utilisateur ne peut pas lire ; ce n'est pas un contrôle d'accès. Le chiffrement impose un client SMB 3.x compatible et peut avoir un coût de performance. Tester les clients avant d'activer en production.*

## Références officielles
- [Microsoft Learn — Présentation du partage de fichiers SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/file-server-smb-overview)
- [Microsoft Learn — Améliorations de sécurité SMB et chiffrement](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-security)