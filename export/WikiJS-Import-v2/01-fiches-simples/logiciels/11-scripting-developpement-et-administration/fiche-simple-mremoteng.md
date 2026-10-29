---
title: "mRemoteNG"
description: "Installer mRemoteNG sur Windows Server 2022, créer un jeu de connexions de test (RDP et SSH) dans un fichier de connexions chiffré, puis le protéger et le sauvegarder pour l'exploitation en production. Les connexions ne ciblent que vos propres machines."
published: true
date: 2026-10-29T12:25:05Z
tags: ["[windows-server-2022]", "[mremoteng]", "[rdp]", "[ssh]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:25:05Z
dateModified: 2026-10-29T12:25:05Z
---

# 📄 mRemoteNG

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Desktop Experience), PowerShell 5.1
- **Version** : mRemoteNG 1.77.x (paquet winget `mRemoteNG.mRemoteNG`, à vérifier sur la version déployée)
- **Catégorie** : Scripting, développement et administration
- **Tags** : `[windows-server-2022]`, `[mremoteng]`, `[rdp]`, `[ssh]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer mRemoteNG sur Windows Server 2022, créer un jeu de connexions de test (RDP et SSH) dans un fichier de connexions chiffré, puis le protéger et le sauvegarder pour l'exploitation en production. Les connexions ne ciblent que vos propres machines.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation de mRemoteNG et contrôle du dossier de configuration :
```powershell
winget install -e --id mRemoteNG.mRemoteNG
Get-ChildItem "$env:APPDATA\mRemoteNG"
```
👉 Explication : Installe mRemoteNG via winget. Le dossier `%APPDATA%\mRemoteNG` contient le fichier de connexions `confCons.xml` et le fichier de réglages `mRemoteNG.xml`.

2. Création d'une connexion de test dans l'interface :
```
Clic droit sur le dossier racine > Ajouter une connexion
Nom : Lab-SRV-RDP-01   Protocole : RDP   Hôte : 192.168.10.30
Nom : Lab-SRV-SSH-01   Protocole : SSH2  Hôte : 192.168.10.20   Port : 22
```
👉 Explication : Crée deux connexions de lab, une RDP vers un serveur Windows et une SSH vers un serveur Linux. Les identifiants saisis doivent être des comptes de test.

3. Test de connexion RDP depuis mRemoteNG puis contrôle du fichier de connexions :
```powershell
Test-NetConnection 192.168.10.30 -Port 3389
Get-Item "$env:APPDATA\mRemoteNG\confCons.xml" | Select-Object Name, Length, LastWriteTime
```
👉 Explication : `Test-NetConnection` vérifie que le port RDP 3389 répond avant d'ouvrir la connexion. La seconde commande confirme que `confCons.xml` a bien été écrit après enregistrement.

---

## ⚡ 2. Production — Façon Simplifiée
1. Définition d'un mot de passe maître dans les options de sécurité :
```
Outils > Options > Sécurité
Mot de passe de chiffrement : saisir une phrase longue et stockée dans le coffre-fort de l'entreprise
Algorithme de chiffrement : AES-256 (GCM si proposé par la version)
```
👉 Explication : Le fichier `confCons.xml` contient les mots de passe des connexions. Ce réglage le chiffre : sans la phrase, le fichier ne peut pas être relu. La phrase ne doit pas être notée à côté du fichier.

2. Séparation des connexions de production et de lab :
```
Dossier racine > Ajouter un dossier : PROD
Déplacer les connexions de production dans PROD (glisser-déposer)
```
👉 Explication : Un dossier dédié évite de se connecter à un serveur de production depuis une liste de lab. Les identifiants sont liés à chaque connexion.

3. Vérification de la sauvegarde automatique du fichier :
```
Outils > Options > Sauvegarde
Sauvegarder automatiquement la configuration : coché
```
Dans le même menu, vérifier aussi l'emplacement de sauvegarde indiqué.
👉 Explication : mRemoteNG écrit `confCons.xml` à chaque modification. Les versions récentes conservent aussi des copies de sauvegarde : à confirmer sur la version déployée.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restriction des droits sur le dossier de configuration :
```powershell
icacls "$env:APPDATA\mRemoteNG" /inheritance:r /grant:r "$env:USERNAME:(OI)(CI)F" "SYSTEM:(OI)(CI)F"
icacls "$env:APPDATA\mRemoteNG"
```
👉 Explication : Supprime l'héritage des droits et ne laisse l'accès qu'à l'utilisateur qui administre et à `SYSTEM`. La seconde commande affiche les droits obtenus.

2. Sauvegarde chiffrée du fichier de connexions :
```powershell
Copy-Item "$env:APPDATA\mRemoteNG\confCons.xml" "C:\Admin\Sauvegardes\confCons_$(Get-Date -Format yyyy-MM-dd).xml"
Get-FileHash "C:\Admin\Sauvegardes\confCons_$(Get-Date -Format yyyy-MM-dd).xml" -Algorithm SHA256
```
👉 Explication : Copie le fichier daté dans un dossier réservé aux administrateurs et en calcule l'empreinte SHA-256. La copie reste chiffrée par la phrase maître : la phrase doit être conservée séparément, dans le coffre-fort.

3. Contrôle qu'aucune connexion n'utilise un compte ou un mot de passe en clair :
```powershell
Select-String -Path "$env:APPDATA\mRemoteNG\confCons.xml" -Pattern 'Protected="false"'
```
👉 Explication : Le fichier de connexions indique l'état du chiffrement de chaque mot de passe. La commande ne doit rien afficher. Une ligne trouvée signale une connexion à corriger.

4. Verrouillage de la session et de l'accès à l'application :
```
Outils > Options > Sécurité
Décocher le stockage des identifiants dans le fichier si la politique le demande
```
👉 Explication : Quand les identifiants ne sont pas enregistrés, chaque administrateur les saisit à la connexion. Réduit le risque de fuite du fichier de connexions.

---

**Point à vérifier** : le libellé exact des menus (`Outils > Options > Sécurité`), l'identifiant winget et la présence de la sauvegarde automatique varient selon la version. Vérifier aussi l'attribut `Protected` dans `confCons.xml` sur la version déployée.