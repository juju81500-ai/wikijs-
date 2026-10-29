# 📄 Microsoft RDS

- **Environnement** : VM Windows Server 2022 (lab) ; serveur physique ou VM de production derrière VPN ou passerelle RD Gateway
- **OS / Version** : Windows Server 2022 Standard ou Datacenter - Remote Desktop Services (rôle Hôte Session Bureau à distance, à vérifier sur la version déployée)
- **Catégorie** : Poste de travail et VDI

## 🎯 Problème précis à résoudre
Installer le rôle Hôte Session Bureau à distance sur Windows Server 2022, activer RDP avec authentification NLA, limiter le pare-feu au réseau d'administration et valider une connexion. Le broker, les collections et les licences RDS (serveur de licences, CAL) sont hors périmètre de cette fiche simple.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification de l'état des rôles RDS dans PowerShell lancé en administrateur :
   ```powershell
   Get-WindowsFeature -Name RDS-RD-Server, RDS-Licensing | Select-Object Name, InstallState
   ```
   👉 Explication : Confirme que les rôles existent sur le serveur et indique s'ils sont déjà installés (`Installed`) ou non (`Available`).

2. Installation du rôle Hôte Session Bureau à distance avec ses outils de gestion :
   ```powershell
   Install-WindowsFeature -Name RDS-RD-Server -IncludeManagementTools -Restart
   ```
   👉 Explication : Installe le rôle sur le serveur et le redémarre automatiquement. Sur un serveur de lab, le serveur joue le rôle d'hôte de sessions sans broker ni collection.

3. Activation du Bureau à distance et ouverture du pare-feu :
   ```powershell
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server' -Name 'fDenyTSConnections' -Value 0
   Enable-NetFirewallRule -DisplayGroup 'Bureau à distance'
   ```
   👉 Explication : La valeur `0` autorise les connexions Bureau à distance ; le groupe de règles pare-feu les autorise sur le port TCP 3389. Sur un Windows Server en anglais, le nom du groupe est `Remote Desktop` (à vérifier sur la version déployée).

4. Contrôle du service et test de connexion :
   ```powershell
   Get-Service -Name TermService | Select-Object Name, Status, StartType
   ```
   👉 Explication : Le service `TermService` doit être `Running`. Depuis un poste de test, lancer `mstsc` et saisir le nom ou l'adresse du serveur.

---

## ⚡ 2. Production — Façon Simplifiée
1. Activation de l'authentification NLA (Network Level Authentication) pour les connexions RDP :
   ```powershell
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name 'UserAuthentication' -Value 1
   ```
   👉 Explication : La valeur `1` impose l'authentification NLA avant l'ouverture de la session. Le client doit la supporter (Windows 10 ou 11 récents).

2. Vérification des paramètres de connexion :
   ```powershell
   Get-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name 'UserAuthentication', 'SecurityLayer', 'MinEncryptionLevel'
   ```
   👉 Explication : Affiche l'état NLA et les réglages de chiffrement. `UserAuthentication` doit valoir `1`.

3. Test de connexion depuis un poste autorisé :
   ```powershell
   mstsc /v:<nom_de_l_hote>
   ```
   👉 Explication : Ouvre le client Bureau à distance vers `<nom_de_l_hote>`, nom DNS du serveur. Depuis un poste hors du réseau d'administration, la connexion doit être refusée une fois la règle restreinte (étape 3 de la section sécurisée).

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exiger le chiffrement TLS et un niveau de chiffrement élevé :
   ```powershell
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name 'SecurityLayer' -Value 2
   Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -Name 'MinEncryptionLevel' -Value 3
   ```
   👉 Explication : `SecurityLayer` à `2` impose TLS, `MinEncryptionLevel` à `3` impose un chiffrement élevé. Ces valeurs sont à vérifier sur la version déployée et avec les clients de l'entreprise.

2. Restriction des règles pare-feu au réseau d'administration ou au VPN :
   ```powershell
   Set-NetFirewallRule -DisplayGroup 'Bureau à distance' -Direction Inbound -RemoteAddress '<reseau_administration>'
   ```
   👉 Explication : Remplacer `<reseau_administration>` par le sous-réseau de gestion au format CIDR (exemple : `192.168.10.0/24`). Les connexions RDP venant d'autres adresses sont alors bloquées. Ne pas exposer le port 3389 directement sur Internet : passer par un VPN ou une passerelle RD Gateway.

3. Contrôle des sessions ouvertes :
   ```powershell
   qwinsta
   ```
   👉 Explication : Liste les sessions actives et déconnectées. Vérifier qu'aucune session inattendue n'est ouverte avant de considérer le serveur prêt.

4. Vérification de l'état de la configuration pare-feu :
   ```powershell
   Get-NetFirewallRule -DisplayGroup 'Bureau à distance' | Select-Object DisplayName, Enabled, Direction
   ```
   👉 Explication : Contrôle en lecture seule que les règles sont actives et en sens entrant. Un ticket de changement doit tracer ces réglages, et la gestion des licences RDS reste à traiter selon la politique de l'entreprise.