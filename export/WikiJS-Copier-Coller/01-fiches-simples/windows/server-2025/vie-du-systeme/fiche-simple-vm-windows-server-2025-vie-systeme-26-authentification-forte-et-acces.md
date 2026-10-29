# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_26_Authentification_Forte_Et_Acces

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 26 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Sécuriser l'accès d'administration à distance (RDP, WinRM, OpenSSH).

## 1. Hors-Production (Lab / Test / POC)

1. Activer le Bureau à distance avec authentification au niveau du réseau (**Paramètres > Système > Bureau à distance** ou **Gestionnaire de serveur > Serveur local > Bureau à distance**) :
   ```powershell
   Set-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server' fDenyTSConnections 0
   Set-ItemProperty 'HKLM:\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' UserAuthentication 1
   Enable-NetFirewallRule -DisplayGroup 'Bureau à distance'
   ```
   👉 Explication : autorise RDP avec NLA; le groupe de règles s'appelle `Remote Desktop` sur une édition anglaise.

2. Activer WinRM pour l'administration PowerShell :
   ```powershell
   Enable-PSRemoting -Force
   Get-Service WinRM
   ```
   👉 Explication : permet `Enter-PSSession` depuis le poste d'administration.

3. Option : installer OpenSSH Server (**Paramètres > Applications > Fonctionnalités facultatives**) :
   ```powershell
   Get-WindowsCapability -Online -Name OpenSSH.Server*
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   Start-Service sshd
   Set-Service sshd -StartupType Automatic
   ```
   👉 Explication : fournit un accès SSH avec clés; ne l'activer que si le besoin existe.

## 2. Production — Contrôles

Passer par un bastion ou un VPN et limiter les adresses sources autorisées.

## 3. Production — Sécurité

Jamais de RDP exposé à Internet; MFA sur le bastion; NLA obligatoire.

## Validation et retour arrière

- **Validation** : Connexion distante réussie depuis le poste d'administration uniquement.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)