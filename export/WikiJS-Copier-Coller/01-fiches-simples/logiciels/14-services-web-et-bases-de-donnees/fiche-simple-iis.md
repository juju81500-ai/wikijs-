# 📄 IIS

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Standard ou Datacenter, Desktop Experience non requis)
- **Version** : IIS 10.0 (rôle Serveur Web intégré à Windows Server 2022, à vérifier sur la version déployée)
- **Catégorie** : Services Web et bases de données

## 🎯 Objectif
Installer le rôle Serveur Web (IIS) sur Windows Server 2022 avec PowerShell, vérifier sur ce même serveur qu'un site de test répond, puis le durcir (HTTPS, en-tête `X-Powered-By` supprimé, site par défaut retiré) avant de le publier. Les tests ne se font que sur votre propre serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du rôle Serveur Web et des outils de gestion (PowerShell administrateur) :
```powershell
Install-WindowsFeature -Name Web-Server -IncludeManagementTools
```
👉 Explication : Installe IIS, ses modules de base et la console de gestion. Le résultat `Success` avec `Restart Needed: No` est attendu.

2. Vérification de la version et du service :
```powershell
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\InetStp | Select-Object MajorVersion, MinorVersion, VersionString
Get-Service W3SVC | Select-Object Name, Status, StartType
```
👉 Explication : La première commande affiche la version d'IIS. La seconde indique le service `W3SVC` (World Wide Web Publishing Service), attendu en `Running` et `Automatic`.

3. Création d'une page de test et contrôle de la réponse :
```powershell
Set-Content -Path C:\inetpub\wwwroot\index.html -Value "<h1>Test IIS lab</h1>"
Invoke-WebRequest -Uri http://localhost/ -UseBasicParsing | Select-Object StatusCode
```
👉 Explication : Remplace la page par défaut par une page de test. Le code `StatusCode 200` est attendu.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un site dédié et de son dossier :
```powershell
Import-Module WebAdministration
New-Item -ItemType Directory -Path C:\Sites\<nom_site> -Force
New-Website -Name "<nom_site>" -PhysicalPath "C:\Sites\<nom_site>" -HostHeader "<nom_site_fqdn>" -Port 80
```
👉 Explication : Crée le dossier du site puis le site IIS associé au nom d'hôte `<nom_site_fqdn>`. `<nom_site>` est un identifiant court, sans espaces.

2. Retrait du site par défaut :
```powershell
Stop-Website -Name "Default Web Site"
Remove-Website -Name "Default Web Site"
```
👉 Explication : Évite qu'un site d'usine réponde sur le port 80 à la place du site d'entreprise.

3. Ouverture du pare-feu Windows pour HTTP et HTTPS :
```powershell
New-NetFirewallRule -DisplayName "IIS HTTP entrant" -Direction Inbound -Protocol TCP -LocalPort 80 -Action Allow
New-NetFirewallRule -DisplayName "IIS HTTPS entrant" -Direction Inbound -Protocol TCP -LocalPort 443 -Action Allow
Get-NetFirewallRule -DisplayName "IIS*" | Select-Object DisplayName, Enabled, Action
```
👉 Explication : Ouvre uniquement les ports web. La dernière commande liste les règles créées pour les vérifier.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Installation du certificat du site et liaison HTTPS :
```powershell
Import-PfxCertificate -FilePath C:\Certificats\<certificat_web>.pfx -CertStoreLocation Cert:\LocalMachine\My -Password (Read-Host -AsSecureString "Mot de passe PFX")
New-WebBinding -Name "<nom_site>" -Protocol https -Port 443 -HostHeader "<nom_site_fqdn>" -SslFlags 1
```
👉 Explication : Importe le certificat (fichier `.pfx` fourni par l'autorité interne) et ajoute une liaison HTTPS au site. Le mot de passe est demandé à l'invite, jamais écrit dans le script. `-SslFlags 1` active le SNI ; `<certificat_web>` est le nom du fichier, à vérifier sur la version déployée.

2. Suppression de l'en-tête `X-Powered-By` :
```powershell
Remove-WebConfigurationProperty -PSPath "MACHINE/WEBROOT/APPHOST" -Filter "system.webServer/httpProtocol/customHeaders" -Name "." -AtElement @{name="X-Powered-By"} -ErrorAction SilentlyContinue
```
👉 Explication : Retire l'en-tête qui révèle la technologie utilisée. Vérifier le résultat avec un `Invoke-WebRequest` sur le site.

3. Désactivation des fonctionnalités non utilisées :
```powershell
Get-WindowsFeature -Name Web-Dir-Browsing, Web-DAV-Publishing, Web-FTP-Server | Select-Object Name, InstallState
Uninstall-WindowsFeature -Name Web-Dir-Browsing, Web-DAV-Publishing
```
👉 Explication : Liste les fonctionnalités à risque, puis retire le listing de répertoires et WebDAV si l'application ne les utilise pas. Un redémarrage peut être demandé.

4. Contrôle des journaux et des erreurs :
```powershell
Get-ChildItem C:\inetpub\logs\LogFiles\W3SVC1\ | Sort-Object LastWriteTime -Descending | Select-Object -First 1
Get-Content (Get-ChildItem C:\inetpub\logs\LogFiles\W3SVC1\*.log | Sort-Object LastWriteTime -Descending | Select-Object -First 1).FullName -Tail 50
```
👉 Explication : Repère le dernier journal W3C du site par défaut `W3SVC1`, puis affiche ses 50 dernières lignes. Les codes 401, 403 et 500 répétés sont à remonter au responsable sécurité.

5. Sauvegarde de la configuration avant toute évolution :
```powershell
Backup-WebConfiguration -Name "BackupIIS-$(Get-Date -Format yyyy-MM-dd)"
Get-WebConfigurationBackup
```
👉 Explication : Crée une sauvegarde de la configuration IIS (`applicationHost.config`) stockée localement, puis liste les sauvegardes disponibles. Copier également l'archive hors du serveur.

---