# 📄 PingCastle

- **Environnement** : VM (Windows Server 2022, serveur membre du domaine)
- **OS / Version** : Windows Server 2022 (PowerShell 5.1)
- **Version** : PingCastle 3.x (archive officielle, numéro exact à vérifier sur la version déployée)
- **Catégorie** : Réseau et cybersécurité

## 🎯 Objectif
Installer PingCastle sur un serveur d'administration Windows Server 2022, lancer un contrôle de santé de l'Active Directory de test, puis le durcir (compte de service à droits de lecture, rapports protégés, exécution planifiée). PingCastle ne modifie pas l'annuaire : il lit et produit un rapport. Ne l'exécuter que sur un domaine autorisé par écrit, depuis un poste d'administration et jamais sur un contrôleur de domaine.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création du dossier d'installation et extraction de l'archive :
```powershell
New-Item -ItemType Directory -Path C:\Outils\PingCastle -Force
Expand-Archive -Path C:\Telechargements\PingCastle_3.3.0.0.zip -DestinationPath C:\Outils\PingCastle -Force
Get-ChildItem C:\Outils\PingCastle
```
👉 Explication : Crée `C:\Outils\PingCastle`, extrait l'archive officielle téléchargée sur le site de l'éditeur (nom de fichier à vérifier) et liste son contenu. `PingCastle.exe` doit être présent.

2. Vérification de l'exécutable et du domaine de test :
```powershell
Get-Item C:\Outils\PingCastle\PingCastle.exe | Select-Object Name, Length, LastWriteTime
Get-ADDomain | Select-Object DNSRoot, NetBIOSName
```
👉 Explication : Confirme la présence de l'exécutable et affiche le nom DNS du domaine (`Get-ADDomain` fait partie du module ActiveDirectory de RSAT, installé sur un serveur membre).

3. Lancement du contrôle de santé sur le domaine de test :
```powershell
cd C:\Outils\PingCastle
.\PingCastle.exe --healthcheck --server lab.local
```
👉 Explication : Lance l'analyse en lecture seule du domaine `lab.local`. Remplacer `lab.local` par le domaine de test réel. La durée dépend de la taille de l'annuaire.

4. Contrôle des rapports produits :
```powershell
Get-ChildItem C:\Outils\PingCastle -Filter "ad_hc_*" | Select-Object Name, Length, LastWriteTime
```
👉 Explication : Liste les rapports `ad_hc_*` (HTML pour la lecture, XML pour l'exploitation). Ouvrir le fichier `.html` dans un navigateur : la note de risque et les points d'attention y figurent. Les noms exacts des fichiers sont à vérifier sur la version déployée.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un compte de service à droits de lecture (ni administrateur ni délégation d'écriture) :
```powershell
New-ADUser -Name "SVC_PingCastle" -SamAccountName "SVC_PingCastle" -Path "OU=Services,DC=entreprise,DC=lan" -Enabled $true -AccountPassword (Read-Host -AsSecureString "Mot de passe du compte")
```
👉 Explication : Crée un compte dédié dont le mot de passe est saisi à l'invite, sans l'afficher dans l'historique. Le compte doit seulement lire l'annuaire, ce qui est le comportement par défaut d'un compte du domaine. Le chemin `OU=Services` est à adapter à l'annuaire réel.

2. Lancement avec ce compte depuis le poste d'administration :
```powershell
cd C:\Outils\PingCastle
.\PingCastle.exe --healthcheck --server entreprise.lan
```
👉 Explication : Lance le contrôle sous la session de l'administrateur qui exécute la commande. Pour utiliser `SVC_PingCastle`, lancer PowerShell avec `runas /user:ENTREPRISE\SVC_PingCastle powershell`, à vérifier selon la politique de l'entreprise.

3. Planification hebdomadaire :
```powershell
schtasks /create /tn "PingCastle-Hebdo" /tr "C:\Outils\PingCastle\PingCastle.exe --healthcheck --server entreprise.lan" /sc weekly /d MON /st 06:00 /ru "ENTREPRISE\SVC_PingCastle" /rp *
```
👉 Explication : Crée une tâche chaque lundi à 6 h. `/rp *` demande le mot de passe du compte de service à l'invite, il n'est pas stocké en clair dans la commande.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur le dossier des rapports :
```powershell
icacls C:\Outils\PingCastle /inheritance:r /grant:r "BUILTIN\Administrateurs:(OI)(CI)F" "ENTREPRISE\SVC_PingCastle:(OI)(CI)M"
icacls C:\Outils\PingCastle
```
👉 Explication : Supprime l'héritage et ne laisse l'accès qu'aux administrateurs locaux et au compte de service. Les rapports décrivent les faiblesses de l'annuaire : ils ne doivent pas être lisibles par les utilisateurs ordinaires.

2. Vérification de l'absence de droits excessifs sur le compte de service :
```powershell
Get-ADGroupMember -Identity "Admins du domaine" | Select-Object Name, SamAccountName
Get-ADUser -Identity SVC_PingCastle -Properties MemberOf | Select-Object -ExpandProperty MemberOf
```
👉 Explication : Le compte `SVC_PingCastle` ne doit figurer dans aucun groupe privilégié. Si c'est le cas, le retirer avec `Remove-ADGroupMember`.

3. Déplacement des rapports vers un stockage contrôlé et suppression des copies anciennes :
```powershell
Move-Item C:\Outils\PingCastle\ad_hc_*.html D:\Audits\PingCastle\ -Force
Get-ChildItem D:\Audits\PingCastle\ | Where-Object LastWriteTime -lt (Get-Date).AddDays(-365) | Remove-Item
```
👉 Explication : Déplace les rapports vers un partage réservé aux auditeurs (`D:\Audits\PingCastle` à adapter) et supprime ceux de plus d'un an selon la politique de conservation. Le dossier cible doit exister avant la commande.

---