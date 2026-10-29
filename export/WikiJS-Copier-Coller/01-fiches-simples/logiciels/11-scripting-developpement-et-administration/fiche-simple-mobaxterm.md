# 📄 MobaXterm

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Desktop Experience), PowerShell 5.1
- **Version** : MobaXterm 24.x (paquet winget `Mobatek.MobaXterm`, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration

## 🎯 Problème précis à résoudre
Installer MobaXterm sur Windows Server 2022, ouvrir une session SSH de test vers un serveur Linux et contrôler l'empreinte de la clé d'hôte, puis activer un mot de passe maître et restreindre les sessions enregistrées pour l'administration en production. Les connexions ne ciblent que vos propres machines.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de MobaXterm et contrôle du paquet :
```powershell
winget install -e --id Mobatek.MobaXterm
winget list --id Mobatek.MobaXterm
```
👉 Explication : Installe MobaXterm depuis les dépôts winget. `winget list` confirme l'identifiant et la version installée.

2. Session SSH de test vers le serveur Linux du lab :
```
Session > SSH
Remote host : 192.168.10.20   Specify username : admin   Port : 22
```
👉 Explication : Ouvre une session SSH vers `admin@192.168.10.20` (Debian 12 ou Rocky Linux 9). Au premier contact, MobaXterm affiche l'empreinte de la clé d'hôte : la noter pour l'étape suivante.

3. Contrôle de l'empreinte de la clé d'hôte côté serveur :
```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```
👉 Explication : Exécutée sur le serveur Linux, cette commande affiche l'empreinte SHA-256 de la clé ED25519. Elle doit correspondre à celle affichée par MobaXterm.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un mot de passe maître :
```
Settings > Configuration > General > Master password
Définir une phrase longue, stockée dans le coffre-fort de l'entreprise
```
👉 Explication : Le mot de passe maître chiffre les mots de passe enregistrés dans les sessions. Sans cette phrase, les identifiants enregistrés ne peuvent pas être relus.

2. Utilisation de clés SSH au lieu des mots de passe :
```
Éditer la session SSH > onglet Advanced SSH settings > Use private key
Chemin : C:\Users\admin\.ssh\lab_admin.ppk
```
👉 Explication : Associe une clé privée à la session pour que la connexion se fasse par clé. La clé elle-même doit être protégée par une phrase de passe. Libellé de l'option à confirmer sur la version déployée.

3. Organisation des sessions de production dans un dossier dédié :
```
Sessions > Clic droit > New folder : PROD
```
👉 Explication : Sépare les sessions de production des sessions de lab pour éviter une erreur de cible.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Localisation du fichier de configuration et de ses droits :
```powershell
Get-ChildItem "$env:USERPROFILE\Documents\MobaXterm" -Filter *.ini -ErrorAction SilentlyContinue
icacls "$env:USERPROFILE\Documents\MobaXterm"
```
👉 Explication : Liste les fichiers `.ini` de configuration (sessions et réglages) et affiche leurs droits. Le dossier doit être réservé à l'utilisateur administrateur. Chemin à confirmer sur la version déployée : MobaXterm peut aussi utiliser son dossier d'installation en mode portable.

2. Restriction des droits sur le dossier de configuration :
```powershell
icacls "$env:USERPROFILE\Documents\MobaXterm" /inheritance:r /grant:r "$env:USERNAME:(OI)(CI)F" "SYSTEM:(OI)(CI)F"
```
👉 Explication : Supprime l'héritage des droits et limite l'accès au compte administrateur et à `SYSTEM`.

3. Sauvegarde datée du fichier de sessions :
```powershell
Copy-Item "$env:USERPROFILE\Documents\MobaXterm\MobaXterm.ini" "C:\Admin\Sauvegardes\MobaXterm_$(Get-Date -Format yyyy-MM-dd).ini"
Get-FileHash "C:\Admin\Sauvegardes\MobaXterm_$(Get-Date -Format yyyy-MM-dd).ini" -Algorithm SHA256
```
👉 Explication : Copie la configuration dans un dossier d'administration daté et calcule son empreinte. Le fichier peut contenir des informations de connexion : son stockage doit suivre la politique de sauvegarde.

4. Contrôle des identifiants enregistrés :
```powershell
Select-String -Path "$env:USERPROFILE\Documents\MobaXterm\MobaXterm.ini" -Pattern "password" -SimpleMatch
```
👉 Explication : Recherche les mots de passe enregistrés en clair. Une ligne trouvée doit être corrigée : supprimer le mot de passe et passer à une clé SSH.

---

**Point à vérifier** : le chemin exact de `MobaXterm.ini` (dossier `Documents\MobaXterm` ou dossier d'installation en mode portable), le libellé des menus `Settings > Configuration` et le fait que les mots de passe soient chiffrés par le mot de passe maître sont à confirmer sur la version déployée.