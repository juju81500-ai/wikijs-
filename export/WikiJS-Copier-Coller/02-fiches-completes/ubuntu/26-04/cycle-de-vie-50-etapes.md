# Cycle de vie 50 étapes : Ubuntu 26.04

Cycle complet multi-OS : [Cycle de vie 50 étapes](</00-administration/cycle-de-vie-50-etapes>).

Commandes Debian/Ubuntu appliquées. Vérifier les différences entre les versions présentes dans le pack.

Les fiches du pack correspondant à chaque étape ne sont pas liées automatiquement (correspondances par nom trop approximatives) : à relier à la main.
Version concernée : 26.04. Page dupliquée depuis la page de la famille Ubuntu ; les commandes sont celles de la famille.

## Phase 1 : préparation et prérequis (étapes 1 à 5)

### 01. Definition des besoins (Sizing)

- **Tous OS** : Allocation vCPU/CPU, RAM, IOPS stockage, architecture (x86_64, ARM64).

### 02. Recuperation de l'image systeme

- **Debian/Ubuntu** : ISO Netinst / Live Server (.iso)

### 03. Verification d'integrite et d'authenticite

- **Linux/BSD** : sha256sum -c SHA256SUMS & verification signature GPG

### 04. Preparation du support d'amorcage

- **Bare-metal** : Cle USB bootable (dd, Rufus, Ventoy) ou montage IPMI/iDRAC/iLO
- **Virtuel** : Stockage ISO dans le datastore (Proxmox VE, VMware ESXi, Hyper-V, XCP-ng)

### 05. Configuration materielle / Firmware

- **Tous OS** : Choix BIOS Legacy ou UEFI, Secure Boot (On/Off selon OS), Virtualisation (VT-x/AMD-V), controleur de stockage (AHCI, VirtIO SCSI, MegaRAID).

## Phase 2 : installation de base (étapes 6 à 15)

### 06. Langue et localisation (Locales)

- **Linux/BSD** : System Locale (ex: fr_FR.UTF-8 ou en_US.UTF-8)

### 07. Disposition du clavier (Keymap)

- **Linux/BSD** : console-setup / keymap (ex: fr, fr-latin9, us)

### 08. Configuration reseau d'installation

- **Debian** : netcfg (DHCP ou Statique temporaire)

### 09. Identite de la machine

- **Linux/BSD** : Hostname + Domain Name (FQDN)

### 10. Compte Super-Administrateur

- **Linux/BSD** : Compte "root" (mot de passe ou verrouillage du compte)

### 11. Compte d'administration delegue

- **Debian/RHEL** : Utilisateur standard + groupe "sudo" ou "wheel"

### 12. Fuseau horaire (Timezone)

- **Linux/BSD** : tzdata (ex: Europe/Paris, UTC) + horloge CMOS en UTC

### 13. Partitionnement et systemes de fichiers

- **Debian/Ubuntu** : GPT/MBR, ext4/xfs/btrfs/ZFS, LVM2, points (/boot, /boot/efi, /, /var, /home, swap)

### 14. Selection des composants de base

- **Debian** : tasksel (Serveur SSH, Utilitaires usuels du systeme, sans GUI)

### 15. Chargeur d'amorcage (Bootloader)

- **Linux** : GRUB2 (grub-pc ou grub-efi-amd64) ou systemd-boot

## Phase 3 : configuration post-installation (étapes 16 à 25)

### 16. Adressage IP fixe definitif

- **Debian/Ubuntu** : /etc/network/interfaces (ifupdown) ou /etc/netplan/*.yaml

### 17. Resolution de noms (DNS Client)

- **Linux/BSD** : /etc/resolv.conf ou systemd-resolved (/etc/systemd/resolved.conf)

### 18. Table d'hotes locale

- **Linux/BSD** : /etc/hosts

### 19. Configuration des depots logiciels (Repositories)

- **Debian/Ubuntu** : /etc/apt/sources.list et /etc/apt/sources.list.d/

### 20. Mise a jour initiale complete du systeme

- **Debian/Ubuntu** : apt update && apt full-upgrade -y

### 21. Pilotes et agents de virtualisation

- **Linux/BSD** : qemu-guest-agent, open-vm-tools, hyperv-daemons, xe-guest-utilities, fwupd

### 22. Synchronisation horaire (NTP)

- **Linux** : chronyd (/etc/chrony/chrony.conf) ou systemd-timesyncd

### 23. Outils d'administration fondamentaux

- **Debian/RHEL/BSD** : vim/nano, curl, wget, htop, tmux, git, lsof, tcpdump, bind-utils/dnsutils

### 24. Personnalisation de l'environnement et bannieres

- **Linux/BSD** : /etc/profile, ~/.bashrc, /etc/motd, /etc/issue, /etc/issue.net

### 25. Validation de l'etat initial (Baseline)

- **Tous OS** : Nettoyage des caches, arret propre et creation du Snapshot VM "01-CLEAN-INSTALL" ou capture Sysprep/Template.

## Phase 4 : sécurisation et hardening (étapes 26 à 35)

### 26. Authentification par cles cryptographiques (SSH / WinRM)

- **Linux/BSD** : ~/.ssh/authorized_keys (ed25519 / RSA 4096)

### 27. Durcissement de l'acces distant

- **Linux/BSD** : /etc/ssh/sshd_config (PermitRootLogin no, PasswordAuthentication no)

### 28. Gestion fine des privileges d'administration

- **Linux/BSD** : /etc/sudoers et /etc/sudoers.d/ (visudo)

### 29. Pare-feu hote (Host Firewall)

- **Debian/Ubuntu** : UFW ou Nftables (/etc/nftables.conf)

### 30. Protection contre les intrusions et le brute-force (IPS)

- **Linux/BSD** : Fail2ban (/etc/fail2ban/jail.local) ou CrowdSec

### 31. Reduction de la surface d'attaque (Services)

- **Linux** : systemctl disable --now <service> / systemctl mask <service>

### 32. Automatisation des correctifs de securite

- **Debian/Ubuntu** : unattended-upgrades (/etc/apt/apt.conf.d/50unattended-upgrades)

### 33. Securisation des systemes de fichiers et montages

- **Linux** : /etc/fstab (options nodev, nosuid, noexec sur /tmp, /var/tmp, /dev/shm)

### 34. Durcissement du noyau et de la pile reseau

- **Linux/BSD** : /etc/sysctl.conf et /etc/sysctl.d/ (ip_forward, tcp_syncookies, accept_redirects=0)

### 35. Controle d'acces obligatoire (MAC) et Antivirus

- **Debian/Ubuntu** : AppArmor (aa-status, aa-enforce)

## Phase 5 : mise en production et services (étapes 36 à 42)

### 36. Integration a l'annuaire ou au reseau d'administration

- **Linux/BSD** : realmd / sssd / Winbind (Jonction AD), client FreeIPA/LDAP, VPN (WireGuard, Tailscale)

### 37. Deploiement des roles metiers et stacks applicatives

- **Linux/BSD** : Docker/Podman, Nginx/Apache, PostgreSQL/MariaDB, Bind9, etc.

### 38. Isolation des comptes de service

- **Linux/BSD** : useradd -r -s /usr/sbin/nologin <service_user>

### 39. Chiffrement des flux (PKI / TLS)

- **Linux/BSD** : Certbot (Let's Encrypt), OpenSSL, ajout CA dans /usr/local/share/ca-certificates/

### 40. Configuration des sauvegardes (Backup)

- **Niveau VM** : Proxmox Backup Server (vzdump), Veeam Backup & Replication
- **Niveau OS** : BorgBackup, Restic, Rclone, cron dumps SQL (Linux/BSD) | Windows Server Backup (wbadmin), VSS

### 41. Supervision, metriques et inventaire (Monitoring)

- **Linux/BSD** : Zabbix Agent, Prometheus node_exporter, SNMPd, GLPI Agent

### 42. Gestion, rotation et centralisation des journaux (Logs)

- **Linux/BSD** : logrotate (/etc/logrotate.d/), journald.conf, rsyslog / syslog-ng / Promtail (envoi SIEM)

## Phase 6 : vérification, tests et documentation (étapes 43 à 50)

### 43. Controle de l'etat des services et des ports en ecoute

- **Linux** : systemctl --failed && ss -tulnp

### 44. Audit d'exposition reseau externe

- **Tous OS (depuis une sonde externe)** : nmap -sV -sC -p- <IP_SERVEUR> (validation du filtrage pare-feu)

### 45. Analyse des journaux d'erreurs systeme

- **Linux** : journalctl -p err -b && dmesg -l err,crit,alert,emerg

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