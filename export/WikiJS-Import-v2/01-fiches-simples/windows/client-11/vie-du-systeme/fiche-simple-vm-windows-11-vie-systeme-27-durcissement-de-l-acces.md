---
title: "Fiche Simple - VM Windows 11 Vie Systeme 27 Durcissement De L Acces"
description: "Limiter et sécuriser Bureau à distance, WinRM et OpenSSH."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-27"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_27_Durcissement_De_L_Acces

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 27 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-27`

---

## Problème précis à résoudre

Limiter et sécuriser Bureau à distance, WinRM et OpenSSH.

## 1. Hors-Production (Lab / Test / POC)

1. Désactiver le Bureau à distance si inutile : **Paramètres > Système > Bureau à distance > Désactivé**.
   ```powershell
   Set-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server' fDenyTSConnections 1
   Disable-NetFirewallRule -DisplayGroup 'Bureau à distance'
   ```
   👉 Explication : bloque RDP et ferme la règle de pare-feu correspondante (le nom du groupe peut être `Remote Desktop` sur un système en anglais).

2. Si RDP est nécessaire : activer l'authentification au niveau du réseau (NLA) et limiter aux membres d'un groupe : **Paramètres > Système > Bureau à distance > Exiger NLA**, puis **Sélectionner les utilisateurs**.
   ```powershell
   Set-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' UserAuthentication 1
   Add-LocalGroupMember -Group 'Utilisateurs du Bureau à distance' -Member 'DOMAINE\GROUPE_SUPPORT'
   ```
   👉 Explication : n'autorise que le groupe prévu avec NLA (`GROUPE_SUPPORT`).

3. Installer OpenSSH si l'administration par clé est retenue (voir fiche détaillée) : **Paramètres > Système > Fonctionnalités facultatives > Serveur OpenSSH**.
   ```powershell
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   Set-Service sshd -StartupType Automatic
   Start-Service sshd
   ```
   👉 Explication : installe le serveur OpenSSH.

4. Désactiver l'assistance à distance non gérée.
   ```powershell
   Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Remote Assistance' fAllowToGetHelp 0
   ```
   👉 Explication : empêche les sollicitations d'assistance non contrôlées.

## 2. Production — Contrôles

Accès distant uniquement depuis le réseau d'administration (filtrage par pare-feu) et via un bastion.

## 3. Production — Sécurité

Pas de mot de passe seul, NLA obligatoire, comptes nominatifs, clés plutôt que mots de passe pour SSH.

## Validation et retour arrière

- **Validation** : `Get-NetTCPConnection -State Listen` ne montre que les ports voulus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows 11 Administration Installer OpenSSH Cle](</01-fiches-simples/windows/client-11/vie-du-logiciel/openssh/fiche-simple-vm-windows-11-administration-installer-openssh-cle>)
- [Fiche détaillée : VM Windows 11 PuTTY Valider SSH HostKey](</01-fiches-simples/windows/client-11/vie-du-logiciel/putty/fiche-simple-vm-windows-11-putty-valider-ssh-hostkey>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)