# 📄 PuTTY

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Desktop Experience), PowerShell 5.1
- **Version** : PuTTY 0.85.x (paquet winget `PuTTY.PuTTY`, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration

## 🎯 Problème précis à résoudre
Installer PuTTY sur Windows Server 2022, vérifier la connexion SSH vers une machine Linux de test, valider l'empreinte de la clé d'hôte, puis imposer une connexion par clé et une validation stricte des clés d'hôte pour l'administration en production. Les tests ne se font que sur vos propres machines.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de PuTTY depuis winget et contrôle de la version :
```powershell
winget install -e --id PuTTY.PuTTY
& "C:\Program Files\PuTTY\plink.exe" -V
```
👉 Explication : Installe PuTTY (`putty.exe`, `plink.exe`, `puttygen.exe`) dans `C:\Program Files\PuTTY`. `plink -V` affiche la version installée.

2. Première connexion SSH au serveur de test (mot de passe, lab uniquement) :
```powershell
& "C:\Program Files\PuTTY\putty.exe" -ssh admin@192.168.10.20
```
👉 Explication : Ouvre une session SSH vers `admin@192.168.10.20` (serveur Debian 12 ou Rocky Linux 9 du lab). Lors de la première connexion, PuTTY affiche l'empreinte de la clé d'hôte (`PuTTY Security Alert`) : la noter pour l'étape suivante.

3. Génération d'une paire de clés et export de la clé publique au format OpenSSH :
```powershell
& "C:\Program Files\PuTTY\puttygen.exe"
```
👉 Explication : Ouvre l'interface PuTTYgen. Choisir `EdDSA` (ou `Ed25519` selon la version), cliquer sur `Generate`, saisir une phrase de passe, enregistrer la clé privée au format `.ppk` dans `C:\Users\admin\.ssh\lab_admin.ppk`, puis copier la zone `Public key for pasting into OpenSSH authorized_keys file`.

4. Test de connexion par clé avec la commande `plink` :
```powershell
& "C:\Program Files\PuTTY\plink.exe" -ssh -i C:\Users\admin\.ssh\lab_admin.ppk admin@192.168.10.20 "uname -a"
```
👉 Explication : Se connecte avec la clé `.ppk` et exécute `uname -a` sur la machine distante. Une réponse affichant le nom du noyau confirme que l'authentification par clé fonctionne.

---

## ⚡ 2. Production — Façon Simplifiée
1. Enregistrement de la session d'administration :
```powershell
& "C:\Program Files\PuTTY\putty.exe" -load "Admin-Srv-Linux-01"
```
👉 Explication : Ouvre une session enregistrée sous le nom `Admin-Srv-Linux-01`, créée au préalable dans PuTTY (hôte, port 22, connexion SSH, clé `.ppk` renseignée dans `Connection > SSH > Auth > Credentials`).

2. Vérification de la clé d'hôte enregistrée :
```powershell
Get-ItemProperty -Path "HKCU:\Software\SimonTatham\PuTTY\SshHostKeys" | Format-List
```
👉 Explication : PuTTY stocke les empreintes des serveurs connus dans cette clé du registre. Vérifier que l'empreinte correspond à celle relevée sur le serveur (`ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub` sur la machine Linux).

3. Test non interactif qui refuse une clé d'hôte inconnue :
```powershell
& "C:\Program Files\PuTTY\plink.exe" -batch -ssh -i C:\Users\admin\.ssh\lab_admin.ppk admin@192.168.10.20 "hostname"
```
👉 Explication : `-batch` empêche toute question interactive : si l'empreinte n'est pas déjà connue, la connexion échoue au lieu d'être acceptée silencieusement. Utile pour les scripts d'exploitation.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Contrôle des sessions enregistrées et des paramètres de connexion :
```powershell
Get-ChildItem -Path "HKCU:\Software\SimonTatham\PuTTY\Sessions" | Select-Object PSChildName
```
👉 Explication : Liste les sessions PuTTY enregistrées dans le profil de l'utilisateur. Les mots de passe enregistrés ne doivent pas exister : seuls la clé `.ppk` et sa phrase de passe sont autorisés.

2. Restriction des droits du fichier de clé privée :
```powershell
icacls "C:\Users\admin\.ssh\lab_admin.ppk" /inheritance:r /grant:r "admin:(R)" "SYSTEM:(F)"
icacls "C:\Users\admin\.ssh\lab_admin.ppk"
```
👉 Explication : Supprime l'héritage des droits et ne laisse que la lecture à `admin` et le contrôle total à `SYSTEM`. La seconde commande affiche les droits obtenus.

3. Sauvegarde des empreintes de clés d'hôte validées :
```powershell
Get-ItemProperty -Path "HKCU:\Software\SimonTatham\PuTTY\SshHostKeys" | Out-File -FilePath "C:\Admin\Sauvegardes\putty_hostkeys_$(Get-Date -Format yyyy-MM-dd).txt"
```
👉 Explication : Exporte les empreintes validées dans un fichier daté, à conserver avec la documentation d'exploitation. Le dossier `C:\Admin\Sauvegardes` doit exister et être limité aux administrateurs.

4. Journalisation des sessions PuTTY (si la politique d'entreprise l'exige) :
```powershell
& "C:\Program Files\PuTTY\plink.exe" -ssh -batch -sessionlog "C:\Admin\Journaux\session_admin.log" -i C:\Users\admin\.ssh\lab_admin.ppk admin@192.168.10.20 "uptime"
```
👉 Explication : `-sessionlog` enregistre la session dans un fichier. Le journal peut contenir des données sensibles : à protéger comme les autres journaux d'administration.

---

**Point à vérifier** : la fiche de couverture renvoie vers une procédure PuTTY sur Windows 11 Client ; cette fiche est adaptée à Windows Server 2022. Le chemin d'installation `C:\Program Files\PuTTY`, la version winget et l'option `-sessionlog` sont à confirmer sur la version déployée.