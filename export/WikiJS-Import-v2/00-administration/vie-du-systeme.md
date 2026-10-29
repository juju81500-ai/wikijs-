---
title: "Vie du système : cycle de vie d'un système d'exploitation (50 étapes, multi-OS)"
description: "Nomenclature : Debian/Ubuntu | RHEL/Alma/Rocky | Windows Server | FreeBSD."
published: true
date: 2026-10-29T19:52:55Z
tags: ["vie-du-systeme", "cycle-de-vie", "os", "checklist", "installation", "production"]
editor: markdown
dateCreated: 2026-10-29T19:52:55Z
dateModified: 2026-10-29T19:52:55Z
---

# Vie du système : cycle de vie d'un système d'exploitation (50 étapes, multi-OS)

- **Tags** : `vie-du-systeme`, `cycle-de-vie`, `os`, `checklist`, `installation`, `production`

Nomenclature : **Debian/Ubuntu** | **RHEL/Alma/Rocky** | **Windows Server** | **FreeBSD**.

Cette trame décrit la vie d'un système d'exploitation, de la préparation à la documentation d'exploitation. Les commandes et chemins varient selon la version et l'édition : vérifier les sources officielles, sauvegarder, prévoir un accès de secours et valider le retour arrière avant toute action en production. Les valeurs entre chevrons (`<IP_SERVEUR>`, `<service>`) sont à remplacer. Les fiches par OS reprennent ces étapes avec les seules commandes de la famille ; voir aussi la version commentée [Cycle de vie 50 étapes](/00-administration/cycle-de-vie-50-etapes).

## Phase 1 : Préparation et prérequis (étapes 1 à 5)

### 01. Définition des besoins (Sizing)

- **Tous OS** : Allocation vCPU/CPU, RAM, IOPS stockage, architecture (x86_64, ARM64).

### 02. Récupération de l'image système

- **Debian/Ubuntu** : ISO Netinst / Live Server (.iso)
- **RHEL/Rocky** : ISO Minimal / Boot (.iso)
- **Windows** : ISO Évaluation / Volume Licensing (.iso) ou image WIM (.wim)
- **FreeBSD** : Image Memstick (.img) ou Disc1 (.iso)

### 03. Vérification d'intégrité et d'authenticité

- **Linux/BSD** : sha256sum -c SHA256SUMS & vérification de la signature GPG
- **Windows** : Get-FileHash -Algorithm SHA256 (PowerShell)

### 04. Préparation du support d'amorçage

- **Bare-metal** : Clé USB bootable (dd, Rufus, Ventoy) ou montage IPMI/iDRAC/iLO
- **Virtuel** : Stockage ISO dans le datastore (Proxmox VE, VMware ESXi, Hyper-V, XCP-ng)

### 05. Configuration matérielle / Firmware

- **Tous OS** : Choix BIOS Legacy ou UEFI, Secure Boot (On/Off selon OS), Virtualisation (VT-x/AMD-V), contrôleur de stockage (AHCI, VirtIO SCSI, MegaRAID).

## Phase 2 : Installation de base : questions de l'installateur (étapes 6 à 15)

### 06. Langue et localisation (Locales)

- **Linux/BSD** : System Locale (ex: fr_FR.UTF-8 ou en_US.UTF-8)
- **Windows** : Language to install / Time and currency format

### 07. Disposition du clavier (Keymap)

- **Linux/BSD** : console-setup / keymap (ex: fr, fr-latin9, us)
- **Windows** : Keyboard or input method (ex: French AZERTY)

### 08. Configuration réseau d'installation

- **Debian** : netcfg (DHCP ou Statique temporaire)
- **RHEL** : Network & Host Name (Anaconda / NetworkManager)
- **Windows** : WinPE Network initialization
- **FreeBSD** : bsdinstall netconfig

### 09. Identité de la machine

- **Linux/BSD** : Hostname + Domain Name (FQDN)
- **Windows** : Computer Name (NetBIOS / DNS Hostname)

### 10. Compte super-administrateur

- **Linux/BSD** : Compte "root" (mot de passe ou verrouillage du compte)
- **Windows** : Compte "Administrateur" (Administrator) local

### 11. Compte d'administration délégué

- **Debian/RHEL** : Utilisateur standard + groupe "sudo" ou "wheel"
- **Windows** : Utilisateur membre du groupe "Administrateurs"
- **FreeBSD** : Utilisateur standard + groupe "wheel"

### 12. Fuseau horaire (Timezone)

- **Linux/BSD** : tzdata (ex: Europe/Paris, UTC) + horloge CMOS en UTC
- **Windows** : Time Zone (ex: Romance Standard Time) + horloge CMOS en heure locale

### 13. Partitionnement et systèmes de fichiers

- **Debian/Ubuntu** : GPT/MBR, ext4/xfs/btrfs/ZFS, LVM2, points (/boot, /boot/efi, /, /var, /home, swap)
- **RHEL/Rocky** : GPT/MBR, xfs/ext4, LVM2 / Stratis, points (/boot, /boot/efi, /, /var, /home, swap)
- **Windows** : GPT/MBR, NTFS / ReFS, Partitions (EFI, MSR, C:\ OS, D:\ Data, Recovery)
- **FreeBSD** : GPT, UFS / ZFS (zroot), partitions (freebsd-boot, freebsd-swap, freebsd-zfs)

### 14. Sélection des composants de base

- **Debian** : tasksel (Serveur SSH, Utilitaires usuels du système, sans GUI)
- **RHEL** : Base Environment "Minimal Install" ou "Server" (sans GUI)
- **Windows** : Edition "Server Core" (sans GUI) ou "Server with Desktop Experience" (GUI)
- **FreeBSD** : Distribution sets (base, kernel, lib32, ports)

### 15. Chargeur d'amorçage (Bootloader)

- **Linux** : GRUB2 (grub-pc ou grub-efi-amd64) ou systemd-boot
- **Windows** : Windows Boot Manager (bootmgfw.efi / BCD)
- **FreeBSD** : loader.efi / gptzfsboot

## Phase 3 : Configuration post-installation (étapes 16 à 25)

### 16. Adressage IP fixe définitif

- **Debian/Ubuntu** : /etc/network/interfaces (ifupdown) ou /etc/netplan/*.yaml
- **RHEL/Rocky** : nmcli / nmtui (/etc/NetworkManager/system-connections/)
- **Windows** : New-NetIPAddress (PowerShell) ou ncpa.cpl
- **FreeBSD** : /etc/rc.conf (ifconfig_em0="inet ...")

### 17. Résolution de noms (DNS Client)

- **Linux/BSD** : /etc/resolv.conf ou systemd-resolved (/etc/systemd/resolved.conf)
- **Windows** : Set-DnsClientServerAddress (PowerShell)

### 18. Table d'hôtes locale

- **Linux/BSD** : /etc/hosts
- **Windows** : C:\Windows\System32\drivers\etc\hosts

### 19. Configuration des dépôts logiciels (Repositories)

- **Debian/Ubuntu** : /etc/apt/sources.list et /etc/apt/sources.list.d/
- **RHEL/Rocky** : /etc/yum.repos.d/*.repo
- **Windows** : Configuration WSUS / Windows Update / Winget / PSGallery
- **FreeBSD** : /etc/pkg/FreeBSD.conf

### 20. Mise à jour initiale complète du système

- **Debian/Ubuntu** : apt update && apt full-upgrade -y
- **RHEL/Rocky** : dnf upgrade -y
- **Windows** : Install-WindowsUpdate / sconfig (Option 6) / Windows Update
- **FreeBSD** : freebsd-update fetch install && pkg upgrade -y

### 21. Pilotes et agents de virtualisation

- **Linux/BSD** : qemu-guest-agent, open-vm-tools, hyperv-daemons, xe-guest-utilities, fwupd
- **Windows** : VirtIO Drivers + QEMU Guest Agent, VMware Tools, Hyper-V Integration Services

### 22. Synchronisation horaire (NTP)

- **Linux** : chronyd (/etc/chrony/chrony.conf) ou systemd-timesyncd
- **Windows** : Service Windows Time (w32tm /config /syncfromflags:manual /manualpeerlist:...)
- **FreeBSD** : ntpd ou chronyd (/etc/rc.conf)

### 23. Outils d'administration fondamentaux

- **Debian/RHEL/BSD** : vim/nano, curl, wget, htop, tmux, git, lsof, tcpdump, bind-utils/dnsutils
- **Windows** : Sysinternals Suite, PowerShell 7, Windows Admin Center, OpenSSH Server

### 24. Personnalisation de l'environnement et bannières

- **Linux/BSD** : /etc/profile, ~/.bashrc, /etc/motd, /etc/issue, /etc/issue.net
- **Windows** : Profil PowerShell ($PROFILE), Bannière légale GPO (interactive logon message)

### 25. Validation de l'état initial (Baseline)

- **Tous OS** : Nettoyage des caches, arret propre et creation du Snapshot VM "01-CLEAN-INSTALL" ou capture Sysprep/Template.

## Phase 4 : Sécurisation / durcissement (étapes 26 à 35)

### 26. Authentification par clés cryptographiques (SSH / WinRM)

- **Linux/BSD** : ~/.ssh/authorized_keys (ed25519 / RSA 4096)
- **Windows** : C:\ProgramData\ssh\administrators_authorized_keys ou certificats WinRM HTTPS

### 27. Durcissement de l'accès distant

- **Linux/BSD** : /etc/ssh/sshd_config (PermitRootLogin no, PasswordAuthentication no)
- **Windows** : Durcissement RDP (NLA obligatoire, restriction d'IP) et sshd_config_default

### 28. Gestion fine des privilèges d'administration

- **Linux/BSD** : /etc/sudoers et /etc/sudoers.d/ (visudo)
- **Windows** : UAC (User Account Control), Groupes locaux Restreints, LAPS (Local Admin Password Solution)

### 29. Pare-feu hote (Host Firewall)

- **Debian/Ubuntu** : UFW ou Nftables (/etc/nftables.conf)
- **RHEL/Rocky** : Firewalld (firewall-cmd) ou Nftables
- **Windows** : Windows Defender Firewall with Advanced Security (wf.msc / New-NetFirewallRule)
- **FreeBSD** : PF (/etc/pf.conf) ou IPFW

### 30. Protection contre les intrusions et le brute-force (IPS)

- **Linux/BSD** : Fail2ban (/etc/fail2ban/jail.local) ou CrowdSec
- **Windows** : Politique de verrouillage de compte (Account Lockout Policy), CrowdSec Windows, EvlWatcher

### 31. Réduction de la surface d'attaque (Services)

- **Linux** : systemctl disable --now <service> / systemctl mask <service>
- **Windows** : Stop-Service / Set-Service -StartupType Disabled (services.msc)
- **FreeBSD** : service <nom> disable (/etc/rc.conf)

### 32. Automatisation des correctifs de sécurité

- **Debian/Ubuntu** : unattended-upgrades (/etc/apt/apt.conf.d/50unattended-upgrades)
- **RHEL/Rocky** : dnf-automatic (/etc/dnf/automatic.conf)
- **Windows** : GPO Windows Update Automatic Updates / WSUS
- **FreeBSD** : cron freebsd-update cron

### 33. Sécurisation des systèmes de fichiers et montages

- **Linux** : /etc/fstab (options nodev, nosuid, noexec sur /tmp, /var/tmp, /dev/shm)
- **Windows** : ACLs NTFS strictes (icacls), desactivation du partage administratif par defaut (AutoShareServer)
- **FreeBSD** : /etc/fstab ou proprietes ZFS (zfs set exec=off setuid=off)

### 34. Durcissement du noyau et de la pile réseau

- **Linux/BSD** : /etc/sysctl.conf et /etc/sysctl.d/ (ip_forward, tcp_syncookies, accept_redirects=0)
- **Windows** : Registre TCP/IP (HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters) & Hardening Kitty

### 35. Contrôle d'accès obligatoire (MAC) et Antivirus

- **Debian/Ubuntu** : AppArmor (aa-status, aa-enforce)
- **RHEL/Rocky** : SELinux (getenforce, setenforce 1, /etc/selinux/config)
- **Windows** : Microsoft Defender Antivirus, AppLocker / WDAC (Windows Defender Application Control)
- **FreeBSD** : MAC Framework / Jails

## Phase 5 : Mise en production et services (étapes 36 à 42)

### 36. Intégration à l'annuaire ou au réseau d'administration

- **Linux/BSD** : realmd / sssd / Winbind (Jonction AD), client FreeIPA/LDAP, VPN (WireGuard, Tailscale)
- **Windows** : Add-Computer -DomainName (Jonction Active Directory Domain Services)

### 37. Déploiement des rôles métiers et stacks applicatives

- **Linux/BSD** : Docker/Podman, Nginx/Apache, PostgreSQL/MariaDB, Bind9, etc.
- **Windows** : Server Manager Roles & Features (Install-WindowsFeature : ADDS, DNS, DHCP, IIS, Hyper-V)

### 38. Isolation des comptes de service

- **Linux/BSD** : useradd -r -s /usr/sbin/nologin <service_user>
- **Windows** : gMSA (Group Managed Service Accounts) ou Managed Service Accounts (MSA)

### 39. Chiffrement des flux (PKI / TLS)

- **Linux/BSD** : Certbot (Let's Encrypt), OpenSSL, ajout CA dans /usr/local/share/ca-certificates/
- **Windows** : AD CS (Auto-enrollment), IIS Certificate Binding, magasin de certificats (certlm.msc)

### 40. Configuration des sauvegardes (Backup)

- **Niveau VM** : Proxmox Backup Server (vzdump), Veeam Backup & Replication
- **Niveau OS** : BorgBackup, Restic, Rclone, cron dumps SQL (Linux/BSD) | Windows Server Backup (wbadmin), VSS

### 41. Supervision, métriques et inventaire (Monitoring)

- **Linux/BSD** : Zabbix Agent, Prometheus node_exporter, SNMPd, GLPI Agent
- **Windows** : Zabbix Agent 2, Prometheus windows_exporter, Service SNMP WMI, GLPI Agent

### 42. Gestion, rotation et centralisation des journaux (Logs)

- **Linux/BSD** : logrotate (/etc/logrotate.d/), journald.conf, rsyslog / syslog-ng / Promtail (envoi SIEM)
- **Windows** : Event Viewer (wevtutil - taille max des journaux), WEF (Windows Event Forwarding), Winlogbeat

## Phase 6 : Vérification, tests et documentation (étapes 43 à 50)

### 43. Contrôle de l'état des services et des ports en écoute

- **Linux** : systemctl --failed && ss -tulnp
- **Windows** : Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.StartType -eq "Automatic"} && Get-NetTCPConnection -State Listen
- **FreeBSD** : service -e && sockstat -4 -6 -l

### 44. Audit d'exposition réseau externe

- **Tous OS (depuis une sonde externe)** : nmap -sV -sC -p- <IP_SERVEUR> (validation du filtrage pare-feu)

### 45. Analyse des journaux d'erreurs système

- **Linux** : journalctl -p err -b && dmesg -l err,crit,alert,emerg
- **Windows** : Get-WinEvent -FilterHashtable @{LogName='System','Application'; Level=1,2,3}
- **FreeBSD** : dmesg && tail -n 100 /var/log/messages

### 46. Test de persistance au redémarrage (Reboot Test)

- **Tous OS** : Redémarrage complet et contrôle automatique du montage des disques, de la pile réseau et du démarrage des services métiers.

### 47. Test de résilience et d'alerte (Watchdog / Monitoring)

- **Tous OS** : Arrêt volontaire d'un service critique ou coupure d'interface pour valider le déclenchement de l'alerte de supervision et/ou la relance automatique (systemd Restart=always / Windows Service Recovery).

### 48. Test de restauration (Validation PRA / DRP)

- **Tous OS** : Restauration effective de la sauvegarde (machine virtuelle complète ou données applicatives) dans un environnement isolé pour vérifier l'intégrité des données.

### 49. Enregistrement CMDB et gestion des accès

- **Tous OS** : Intégration dans l'inventaire (GLPI, NetBox), documentation IPAM, enregistrement des secrets dans le coffre-fort (Vaultwarden / Bitwarden, KeePass, HashiCorp Vault) et configuration SSH/RDP.

### 50. Documentation d'exploitation (Runbook / Dossier d'Architecture Technique)

- **Tous OS** : Création de la fiche serveur (Wiki / BookStack / Markdown) incluant : role, architecture, ports ouverts, chemins des fichiers de configuration, procédures de mise à jour et de dépannage.