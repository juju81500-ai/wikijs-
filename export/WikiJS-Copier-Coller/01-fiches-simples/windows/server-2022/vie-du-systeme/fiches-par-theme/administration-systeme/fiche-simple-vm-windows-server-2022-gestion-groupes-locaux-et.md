# 📄 VM_WinSrv_2022_Utilisateurs_Gestion-Groupes-Locaux-Et-AD.md

- **Environnement** : VM / Contrôleur de Domaine (Windows Server 2022)
- **OS / Version** : Windows Server 2022 Standard / Datacenter
- **Catégorie** : Utilisateurs & Droits / Groupes Active Directory & Locaux

---

## 🎯 Problème précis à résoudre
Créer des groupes de sécurité locaux et Active Directory (Global / Local de Domaine), ajouter et retirer des membres, et implémenter la stratégie d'attribution des droits selon le modèle AGDLP.

---

## 🖥️ Méthode Interface Graphique (GUI Pas-à-Pas)

### Créer un groupe Active Directory
1. Sur un serveur avec les outils AD DS/RSAT, ouvrir **Gestionnaire de serveur** > **Outils** > **Utilisateurs et ordinateurs Active Directory** (`dsa.msc`).
2. Dans l'OU prévue pour les groupes, clic droit > **Nouveau** > **Groupe**. Saisir un nom explicite (ex. `GRP_TSSR_Techniciens`), choisir **Global** comme étendue et **Sécurité** comme type, puis valider.
3. Ouvrir les propriétés du groupe > **Membres** > **Ajouter**, saisir le compte (ex. `jdupont`), choisir **Vérifier les noms**, puis **OK**. Confirmer le membre dans la liste.
4. Pour attribuer un accès à une ressource selon AGDLP, créer le groupe de ressource **Domain Local** (ex. `DL_Donnees_Modification`), y ajouter le groupe Global métier, puis attribuer les permissions de la ressource au groupe Domain Local. Ne pas attribuer directement des ACL aux personnes.

### Gérer un groupe local sur un serveur membre
1. Sur un serveur autonome ou membre du domaine (pas sur un contrôleur de domaine), ouvrir **Gestion de l'ordinateur** (`compmgmt.msc`) > **Utilisateurs et groupes locaux** > **Groupes**.
2. Clic droit > **Nouveau groupe**, saisir le nom et la description, puis **Ajouter** pour sélectionner les comptes ou groupes autorisés. Confirmer la liste avant de cliquer **Créer**.
3. Pour modifier un groupe, ouvrir ses propriétés et utiliser **Ajouter** ou **Supprimer**. Vérifier les membres et les accès effectifs après modification.

Sur un contrôleur de domaine, **Utilisateurs et groupes locaux** n'est pas disponible pour administrer les comptes de domaine ; utiliser ADUC. Une console locale ne doit pas servir à modifier l'appartenance des groupes intégrés du domaine.

---

## ⚡ Méthode Ligne de commande PowerShell

1. Créer un groupe AD :
   ```powershell
   New-ADGroup -Name "GRP_TSSR_Techniciens" -GroupScope Global -GroupCategory Security -Path "OU=TSSR_Groupes,DC=lab,DC=local"
   ```
   👉 Explication : remplacer nom et OU; groupe Global de sécurité (A dans AGDLP).
2. Ajouter un membre :
   ```powershell
   Add-ADGroupMember -Identity "GRP_TSSR_Techniciens" -Members "jdupont"
   ```
   👉 Explication : ajoute le compte au groupe.
3. Retirer un membre :
   ```powershell
   Remove-ADGroupMember -Identity "GRP_TSSR_Techniciens" -Members "jdupont"
   ```
   👉 Explication : demande confirmation avant retrait.
4. Lister les membres :
   ```powershell
   Get-ADGroupMember -Identity "GRP_TSSR_Techniciens"
   ```
   👉 Explication : vérifie le résultat.
5. Groupe local sur un serveur membre (équivalent de la méthode GUI) :
   ```powershell
   New-LocalGroup -Name "GRP_Local_Support" -Description "Support"
   Add-LocalGroupMember -Group "GRP_Local_Support" -Member "LAB\jdupont"
   Get-LocalGroupMember -Group "GRP_Local_Support"
   ```
   👉 Explication : ne pas l'utiliser sur un contrôleur de domaine.