# TP 1 à 4 – Active Directory : Domaine, Objets, Accès et Impression

## ✅ TP 1 : Mise en place du domaine Active Directory

### 🔹 Installation du rôle AD DS

```powershell
Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools
```

### 🔹 Promotion en contrôleur de domaine

```powershell
Install-ADDSForest -DomainName "nivvlem.local"
```

- Suivre les étapes de l’assistant ou passer les bons paramètres en PowerShell
- Après redémarrage, le domaine est opérationnel, le serveur devient contrôleur de domaine (DC)

### 🔹 Intégration au domaine

```powershell
Add-Computer -DomainName "nivvlem.local" -Restart
```

- À exécuter sur les serveurs membres et postes clients (SRV1 et CLI1)

---

## ✅ TP 2 : Utilisateurs et groupes AD

### 🔹 Création d’OU

```powershell
New-ADOrganizationalUnit -Name "Agences"
New-ADOrganizationalUnit -Name "Services"
```

### 🔹 Création de modèles utilisateurs et duplication

```powershell
New-ADUser -Name "_mod_production" -SamAccountName "mod_production" -Enabled $false
```

- Duplication : soit manuelle dans l’interface, soit scriptée en PowerShell

### 🔹 Création des utilisateurs à partir des modèles

```powershell
$users = @("patrick", "isabelle", "guillaume")
foreach ($u in $users) {
  New-ADUser -Name $u -SamAccountName $u -AccountPassword (ConvertTo-SecureString "P@ssw0rd" -AsPlainText -Force) -Enabled $true -Path "OU=Production,OU=Services,DC=nivvlem,DC=local"
}
```

### 🔹 Création des groupes globaux par service

```powershell
New-ADGroup -Name "GG_Production" -GroupScope Global -GroupCategory Security
```

### 🔹 Ajout des utilisateurs dans les groupes

```powershell
Add-ADGroupMember -Identity "GG_Production" -Members patrick, isabelle
```

---

## ✅ TP 3 : Accès aux ressources (AGDLP)

### 🔹 Création de groupes domaine local

```powershell
New-ADGroup -Name "DL_Prod_Access" -GroupScope DomainLocal -GroupCategory Security
```

### 🔹 Affectation des groupes globaux aux DL

```powershell
Add-ADGroupMember -Identity "DL_Prod_Access" -Members "GG_Production"
```

### 🔹 Création d’un dossier partagé

```powershell
New-Item -Path "D:\DATA\Production" -ItemType Directory
New-SmbShare -Name "Production" -Path "D:\DATA\Production" -FullAccess "DL_Prod_Access"
```

### 🔹 Configuration NTFS

```powershell
$acl = Get-Acl "D:\DATA\Production"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("DL_Prod_Access","Modify","ContainerInherit,ObjectInherit","None","Allow")
$acl.AddAccessRule($rule)
Set-Acl -Path "D:\DATA\Production" -AclObject $acl
```

---

## ✅ TP 4 : Gestion des impressions

### 🔹 Installation du service d’impression

```powershell
Install-WindowsFeature Print-Services -IncludeManagementTools
```

### 🔹 Ajout du port TCP/IP et driver

```powershell
Add-PrinterPort -Name "172.28.10.10" -PrinterHostAddress "172.28.10.10"
Add-PrinterDriver -Name "HP Universal Printing PCL 6"
```

### 🔹 Création d’imprimantes partagées

```powershell
Add-Printer -Name "Imprimante1" -DriverName "HP Universal Printing PCL 6" -PortName "172.28.10.10" -ShareName "Imprimante1" -Published $true
```

### 🔹 Affectation à des utilisateurs

- Manuellement via `\\NomServeur` ou via GPO :

```plaintext
GPO → Config Utilisateur → Paramètres Windows → Imprimantes
```

---

## 🧠 À retenir pour les révisions

- `Install-ADDSForest` initie un domaine complet
- Les scripts PowerShell permettent de déployer massivement et proprement comptes, groupes et accès
- AGDLP est une méthode d’**attribution propre des permissions** : Utilisateurs → GG → DL → Ressource
- L’impression centralisée est pilotable via `PrintManagement.msc` ou PowerShell

---

## 📌 Bonnes pratiques professionnelles

|Pratique|Pourquoi ?|
|---|---|
|Ne jamais attribuer des droits directs|Utiliser groupes AD pour évolutivité|
|Créer des modèles pour standardiser|Gain de temps et cohérence|
|Documenter chaque étape de structure|Auditabilité, transfert de compétences|
|Tester avec des comptes non-admin|Reproduire les usages réels utilisateurs|
|Isoler objets et profils par OU|Application ciblée des GPO et meilleure gestion|