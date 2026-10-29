# Cycle de vie 50 étapes : Windows Server-2022

- **Tags** : `cycle-de-vie`, `checklist`, `windows`, `installation`, `production`, `verification`

Cycle complet multi-OS : [Cycle de vie 50 étapes](../../../../00-Administration/Cycle_de_vie_50_etapes.md).

Commandes Windows appliquées. Serveur et client n'ont pas les mêmes étapes (AD, DHCP, DNS et IIS sont réservés au serveur).


Les fiches du pack correspondant à chaque étape ne sont pas liées automatiquement (correspondances par nom trop approximatives) : à relier à la main.
Version concernée : Server-2022. Page dupliquée depuis la page de la famille Windows ; les commandes sont celles de la famille.

## Phase 1 : préparation et prérequis (étapes 1 à 5)

### 01. Definition des besoins (Sizing)

- **Tous OS** : Allocation vCPU/CPU, RAM, IOPS stockage, architecture (x86_64, ARM64).

### 02. Recuperation de l'image systeme

- **Windows** : ISO Evaluation / Volume Licensing (.iso) ou image WIM (.wim)

### 03. Verification d'integrite et d'authenticite

- **Windows** : Get-FileHash -Algorithm SHA256 (PowerShell)

### 04. Preparation du support d'amorcage

- **Bare-metal** : Cle USB bootable (dd, Rufus, Ventoy) ou montage IPMI/iDRAC/iLO
- **Virtuel** : Stockage ISO dans le datastore (Proxmox VE, VMware ESXi, Hyper-V, XCP-ng)

### 05. Configuration materielle / Firmware

- **Tous OS** : Choix BIOS Legacy ou UEFI, Secure Boot (On/Off selon OS), Virtualisation (VT-x/AMD-V), controleur de stockage (AHCI, VirtIO SCSI, MegaRAID).


## Phase 2 : installation de base (étapes 6 à 15)

### 06. Langue et localisation (Locales)

- **Windows** : Language to install / Time and currency format

### 07. Disposition du clavier (Keymap)

- **Windows** : Keyboard or input method (ex: French AZERTY)

### 08. Configuration reseau d'installation

- **Windows** : WinPE Network initialization

### 09. Identite de la machine

- **Windows** : Computer Name (NetBIOS / DNS Hostname)

### 10. Compte Super-Administrateur

- **Windows** : Compte "Administrateur" (Administrator) local

### 11. Compte d'administration delegue

- **Windows** : Utilisateur membre du groupe "Administrateurs"

### 12. Fuseau horaire (Timezone)

- **Windows** : Time Zone (ex: Romance Standard Time) + horloge CMOS en heure locale

### 13. Partitionnement et systemes de fichiers

- **Windows** : GPT/MBR, NTFS / ReFS, Partitions (EFI, MSR, C:\ OS, D:\ Data, Recovery)

### 14. Selection des composants de base

- **Windows** : Edition "Server Core" (sans GUI) ou "Server with Desktop Experience" (GUI)

### 15. Chargeur d'amorcage (Bootloader)

- **Windows** : Windows Boot Manager (bootmgfw.efi / BCD)


## Phase 3 : configuration post-installation (étapes 16 à 25)

### 16. Adressage IP fixe definitif

- **Windows** : New-NetIPAddress (PowerShell) ou ncpa.cpl

### 17. Resolution de noms (DNS Client)

- **Windows** : Set-DnsClientServerAddress (PowerShell)

### 18. Table d'hotes locale

- **Windows** : C:\Windows\System32\drivers\etc\hosts

### 19. Configuration des depots logiciels (Repositories)

- **Windows** : Configuration WSUS / Windows Update / Winget / PSGallery

### 20. Mise a jour initiale complete du systeme

- **Windows** : Install-WindowsUpdate / sconfig (Option 6) / Windows Update

### 21. Pilotes et agents de virtualisation

- **Windows** : VirtIO Drivers + QEMU Guest Agent, VMware Tools, Hyper-V Integration Services

### 22. Synchronisation horaire (NTP)

- **Windows** : Service Windows Time (w32tm /config /syncfromflags:manual /manualpeerlist:...)

### 23. Outils d'administration fondamentaux

- **Windows** : Sysinternals Suite, PowerShell 7, Windows Admin Center, OpenSSH Server

### 24. Personnalisation de l'environnement et bannieres

- **Windows** : Profil PowerShell ($PROFILE), Banniere legale GPO (interactive logon message)

### 25. Validation de l'etat initial (Baseline)

- **Tous OS** : Nettoyage des caches, arret propre et creation du Snapshot VM "01-CLEAN-INSTALL" ou capture Sysprep/Template.


## Phase 4 : sécurisation et hardening (étapes 26 à 35)

### 26. Authentification par cles cryptographiques (SSH / WinRM)

- **Windows** : C:\ProgramData\ssh\administrators_authorized_keys ou certificats WinRM HTTPS

### 27. Durcissement de l'acces distant

- **Windows** : Durcissement RDP (NLA obligatoire, restriction d'IP) et sshd_config_default

### 28. Gestion fine des privileges d'administration

- **Windows** : UAC (User Account Control), Groupes locaux Restreints, LAPS (Local Admin Password Solution)

### 29. Pare-feu hote (Host Firewall)

- **Windows** : Windows Defender Firewall with Advanced Security (wf.msc / New-NetFirewallRule)

### 30. Protection contre les intrusions et le brute-force (IPS)

- **Windows** : Politique de verrouillage de compte (Account Lockout Policy), CrowdSec Windows, EvlWatcher

### 31. Reduction de la surface d'attaque (Services)

- **Windows** : Stop-Service / Set-Service -StartupType Disabled (services.msc)

### 32. Automatisation des correctifs de securite

- **Windows** : GPO Windows Update Automatic Updates / WSUS

### 33. Securisation des systemes de fichiers et montages

- **Windows** : ACLs NTFS strictes (icacls), desactivation du partage administratif par defaut (AutoShareServer)

### 34. Durcissement du noyau et de la pile reseau

- **Windows** : Registre TCP/IP (HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters) & Hardening Kitty

### 35. Controle d'acces obligatoire (MAC) et Antivirus

- **Windows** : Microsoft Defender Antivirus, AppLocker / WDAC (Windows Defender Application Control)


## Phase 5 : mise en production et services (étapes 36 à 42)

### 36. Integration a l'annuaire ou au reseau d'administration

- **Windows** : Add-Computer -DomainName (Jonction Active Directory Domain Services)

### 37. Deploiement des roles metiers et stacks applicatives

- **Windows** : Server Manager Roles & Features (Install-WindowsFeature : ADDS, DNS, DHCP, IIS, Hyper-V)

### 38. Isolation des comptes de service

- **Windows** : gMSA (Group Managed Service Accounts) ou Managed Service Accounts (MSA)

### 39. Chiffrement des flux (PKI / TLS)

- **Windows** : AD CS (Auto-enrollment), IIS Certificate Binding, magasin de certificats (certlm.msc)

### 40. Configuration des sauvegardes (Backup)

- **Niveau VM** : Proxmox Backup Server (vzdump), Veeam Backup & Replication
- **Niveau OS** : BorgBackup, Restic, Rclone, cron dumps SQL (Linux/BSD) | Windows Server Backup (wbadmin), VSS

### 41. Supervision, metriques et inventaire (Monitoring)

- **Windows** : Zabbix Agent 2, Prometheus windows_exporter, Service SNMP WMI, GLPI Agent

### 42. Gestion, rotation et centralisation des journaux (Logs)

- **Windows** : Event Viewer (wevtutil - taille max des journaux), WEF (Windows Event Forwarding), Winlogbeat


## Phase 6 : vérification, tests et documentation (étapes 43 à 50)

### 43. Controle de l'etat des services et des ports en ecoute

- **Windows** : Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"} && Get-NetTCPConnection -State Listen

### 44. Audit d'exposition reseau externe

- **Tous OS (depuis une sonde externe)** : nmap -sV -sC -p- <IP_SERVEUR> (validation du filtrage pare-feu)

### 45. Analyse des journaux d'erreurs systeme

- **Windows** : Get-WinEvent -FilterHashtable @{LogName='System','Application'; Level=1,2,3}

### 46. Test de persistance au redemarrage (Reboot Test)

- **Tous OS** : Redemarrage complet et controle automatique du montage des disques, de la pile reseau et du demarrage des services metiers.

### 47. Test de resilience et d'alerte (Watchdog / Monitoring)

- **Tous OS** : Arret volontaire d'un service critique ou coupure d'interface pour valider le declenchement de l'alerte de supervision et/ou la relance automatique (systemd Restart=always / Windows Service Recovery).

### 48. Test de restauration (Validation PRA / DRP)

- **Tous OS** : Restauration effective de la sauvegarde (machine virtuelle complete ou donnees applicatives) dans un environnement isole pour verifier l'integrite des donnees.

### 49. Enregistrement CMDB et Gestion des acces

- **Tous OS** : Integration dans l'inventaire (GLPI, NetBox), documentation IPAM, enregistrement des secrets dans le coffre-fort (Vaultwarden / Bitwarden, KeePass, HashiCorp Vault) et configuration SSH/RDP.

### 50. Documentation d'exploitation (Runbook / Dossier d'Architecture Technique)

- **Tous OS** : Creation de la fiche serveur (Wiki / BookStack / Markdown) incluant : role, architecture, ports ouverts, chemins des fichiers de configuration, procedures de mise a jour et de depannage.
