# Fiche_Simple_-_Windows_Server_2022_PowerShell_Remoting_SSH

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Activer le remoting PowerShell via SSH vers un Windows Server 2022, en complément de WinRM pour 5.1.

## 1. Hors-Production (Lab / Test / POC)

1. Installer OpenSSH Server. GUI : Paramètres > Applications > Fonctionnalités facultatives > Ajouter une fonctionnalité > Serveur OpenSSH. Ligne de commande :
   ```powershell
   Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
   Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
   ```
   👉 Explication : fonctionnalité à la demande documentée par Microsoft ; elle exige l'accès à Windows Update ou une source locale.

2. Démarrer le service et le rendre automatique. GUI : services.msc > OpenSSH SSH Server > Propriétés. Ligne de commande :
   ```powershell
   Set-Service -Name sshd -StartupType Automatic
   Start-Service sshd
   ```
   👉 Explication : rend le service disponible au redémarrage.

3. Déclarer le sous-système PowerShell : éditer `C:\ProgramData\ssh\sshd_config` (éditeur en administrateur) et ajouter :
   ```text
   Subsystem powershell c:/progra~1/powershell/7/pwsh.exe -sshs -NoLogo -NoProfile
   ```
   👉 Explication : ligne documentée par Microsoft (nom court 8.3 de `Program Files`) ; placer la ligne avant tout bloc `Match`.

4. Redémarrer sshd puis vérifier :
   ```powershell
   Restart-Service sshd
   Get-Service sshd
   Get-NetFirewallRule -Name '*ssh*' | Select-Object Name,Enabled,Direction
   ```
   👉 Explication : une règle de pare-feu entrante pour le port 22 est créée à l'installation : vérifier son existence et sa portée.

5. Restreindre la source du pare-feu au réseau d'administration (RESEAU_ADMIN à remplacer). GUI : wf.msc > Règles de trafic entrant > règle OpenSSH Server > Propriétés > Étendue. Ligne de commande :
   ```powershell
   Set-NetFirewallRule -Name OpenSSH-Server-In-TCP -RemoteAddress RESEAU_ADMIN
   ```
   👉 Explication : le nom de règle `OpenSSH-Server-In-TCP` est celui de la documentation Microsoft : confirmer avec la commande précédente.

6. Compte administrateur : installer la clé publique dans le fichier dédié, puis fixer les ACL (CLE_PUBLIQUE à remplacer par le contenu de la clé publique) :
   ```powershell
   Add-Content -Path "$env:ProgramData\ssh\administrators_authorized_keys" -Value 'CLE_PUBLIQUE'
   icacls.exe "$env:ProgramData\ssh\administrators_authorized_keys" /inheritance:r /grant 'Administrators:F' /grant 'SYSTEM:F'
   ```
   👉 Explication : pour les membres du groupe Administrateurs, sshd lit ce fichier et non le profil utilisateur ; les ACL strictes sont requises.

7. Connexion depuis un client PowerShell 7 (HOTE et UTILISATEUR à remplacer) puis, en comparaison, WinRM depuis 5.1 :
   ```powershell
   Enter-PSSession -HostName HOTE -UserName UTILISATEUR
   # Windows PowerShell 5.1 / WinRM :
   Test-WSMan -ComputerName HOTE
   Enter-PSSession -ComputerName HOTE -Credential (Get-Credential)
   ```
   👉 Explication : SSH n'est pas supporté par 5.1 ; WinRM (`Enable-PSRemoting`) reste le mode natif Windows et s'accompagne de Kerberos/NTLM. `Get-Credential` demande le mot de passe à la saisie.

## 2. Production — Contrôles

Choisir un seul mode de remoting par usage, journaliser les connexions et limiter les comptes autorisés. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Préférer les clés SSH ; désactiver `PasswordAuthentication` dans sshd_config après test.
- Limiter les comptes autorisés (`AllowGroups`) et la source réseau.
- Aucune clé privée ni mot de passe dans les scripts.

## Validation et retour arrière

- **Validation** : `Enter-PSSession -HostName` ouvre une session PowerShell 7 distante.
- **Retour arrière** : retirer la ligne `Subsystem powershell`, `Stop-Service sshd`, `Set-Service sshd -StartupType Disabled`, supprimer la règle de pare-feu si elle n'est plus utile.

## Si le problème n'est pas résolu

- [Microsoft Learn — remoting via SSH](https://learn.microsoft.com/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
- [Microsoft Learn — OpenSSH sur Windows](https://learn.microsoft.com/windows-server/administration/openssh/openssh-server-configuration)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-prerequis-limites)