---
title: "Cycle de vie d'un système d'exploitation : 50 étapes (multi-OS)"
description: "Nomenclature du cycle : [DEBIAN/UBUNTU] | [RHEL/ALMA/ROCKY] | [WINDOWS SERVER] | [FREEBSD]. Les pages par OS reprennent ce cycle avec les seules commandes de la famille."
published: true
date: 2026-10-29T15:40:17Z
tags: ["cycle-de-vie", "checklist", "installation", "production", "reparation", "verification"]
editor: markdown
dateCreated: 2026-10-29T15:40:17Z
dateModified: 2026-10-29T15:40:17Z
---

# Cycle de vie d'un système d'exploitation : 50 étapes (multi-OS)

- **Tags** : `cycle-de-vie`, `checklist`, `installation`, `production`, `reparation`, `verification`

Nomenclature du cycle : [DEBIAN/UBUNTU] | [RHEL/ALMA/ROCKY] | [WINDOWS SERVER] | [FREEBSD]. Les pages par OS reprennent ce cycle avec les seules commandes de la famille.

Cette liste est une trame de préparation, pas un script universel ni une autorisation de changement. Les commandes et chemins varient selon la version, l'édition et l'architecture. Vérifier les sources officielles et l'état initial; sauvegarder, prévoir un accès de secours et valider le retour arrière avant toute action en production. Ne pas appliquer en bloc les exemples ou les réglages de durcissement.

## Phase 1 : préparation et prérequis (étapes 1 à 5)

### 01. Definition des besoins (Sizing)

- **Tous OS** : Allocation vCPU/CPU, RAM, IOPS stockage, architecture (x86_64, ARM64).

### 02. Recuperation de l'image systeme

- **Tous OS** : Télécharger l'image depuis le site officiel ou le portail de licence de l'éditeur. Vérifier la version, l'architecture, l'édition et les conditions de licence.
- **Debian/Ubuntu** : ISO Netinst / Server (.iso)
- **RHEL/Rocky** : ISO Boot / Minimal (.iso)
- **Windows** : ISO correspondant à l'édition sous licence; une image WIM est un format de déploiement, pas une image d'installation autonome dans tous les cas.
- **FreeBSD** : image d'installation adaptée à l'architecture (par exemple Memstick ou Disc1).

### 03. Verification d'integrite et d'authenticite

- **Tous OS** : Vérifier la somme de contrôle publiée par l'éditeur, obtenue par un canal officiel; une somme seule ne prouve pas l'authenticité si sa source n'est pas authentifiée.
- **Linux/BSD** : Vérifier la signature de la somme lorsqu'elle est fournie, puis comparer le résultat (`sha256sum -c SHA256SUMS` si le fichier et son format correspondent).
- **Windows** : `Get-FileHash -Algorithm SHA256 <fichier>` calcule une empreinte; la comparer à la valeur officielle. Vérifier aussi la signature numérique de l'éditeur quand elle est disponible.

### 04. Preparation du support d'amorcage

- **Bare-metal** : Clé USB bootable (outil adapté à l'OS) ou média virtuel via IPMI/iDRAC/iLO. `dd` écrase le périphérique cible : identifier et vérifier le disque avant écriture.
- **Virtuel** : Stockage de l'ISO dans le datastore (Proxmox VE, VMware ESXi, Hyper-V, XCP-ng); limiter et protéger les accès à la console de gestion.

### 05. Configuration materielle / Firmware

- **Tous OS** : Choisir UEFI ou BIOS selon la plateforme et les besoins; préférer Secure Boot activé lorsqu'il est pris en charge par la chaîne de démarrage. Configurer VT-x/AMD-V, stockage (AHCI, VirtIO SCSI, contrôleur matériel) et firmware selon l'hyperviseur et l'OS. Ne pas désactiver une protection sans motif documenté.


## Phase 2 : installation de base (étapes 6 à 15)

### 06. Langue et localisation (Locales)

- **Linux/BSD** : System Locale (ex: fr_FR.UTF-8 ou en_US.UTF-8)
- **Windows** : Language to install / Time and currency format

### 07. Disposition du clavier (Keymap)

- **Linux/BSD** : console-setup / keymap (ex: fr, fr-latin9, us)
- **Windows** : Keyboard or input method (ex: French AZERTY)

### 08. Configuration reseau d'installation

- **Debian** : Configuration de l'installateur (DHCP ou paramètres temporaires)
- **RHEL** : Network & Host Name (Anaconda / NetworkManager)
- **Windows** : WinPE Network initialization
- **FreeBSD** : bsdinstall netconfig
- **Tous OS** : N'activer que les flux nécessaires au déploiement; noter tout adressage temporaire à retirer ou remplacer après installation.

### 09. Identite de la machine

- **Linux/BSD** : Hostname + Domain Name (FQDN)
- **Windows** : Computer Name (NetBIOS / DNS Hostname)

### 10. Compte Super-Administrateur

- **Linux/BSD** : Protéger le compte `root`; définir un accès direct seulement si nécessaire et conforme à la politique. Prévoir un compte nominatif d'administration distinct.
- **Windows** : Protéger le compte Administrateur intégré; appliquer la politique de l'organisation et éviter les mots de passe locaux partagés.

### 11. Compte d'administration delegue

- **Debian** : Utilisateur nominatif avec privilèges `sudo` attribués selon le besoin.
- **RHEL/Rocky** : Utilisateur nominatif, groupe `wheel` si la politique sudo l'autorise.
- **Windows** : Utilisateur membre du groupe "Administrateurs"
- **FreeBSD** : Utilisateur standard + groupe "wheel"
- **Tous OS** : Limiter l'appartenance aux groupes privilégiés; vérifier la procédure de récupération avant de retirer un accès existant.

### 12. Fuseau horaire (Timezone)

- **Linux/BSD** : Fuseau horaire (par exemple `Europe/Paris` ou `UTC`) et synchronisation de l'horloge.
- **Windows** : Fuseau horaire adapté au site. La convention de l'horloge matérielle dépend de la plateforme et de la coexistence éventuelle avec d'autres OS; la définir de façon cohérente.

### 13. Partitionnement et systemes de fichiers

- **Tous OS** : Concevoir le partitionnement selon l'UEFI/BIOS, la capacité, les besoins de reprise et les outils de sauvegarde; GPT est le choix courant pour les nouveaux systèmes.
- **Debian/Ubuntu** : Choisir un système de fichiers pris en charge par l'installateur et la distribution (souvent ext4; XFS, Btrfs, ZFS ou LVM selon les besoins et le support).
- **RHEL/Rocky** : XFS ou ext4; LVM et Stratis selon l'édition et les besoins.
- **Windows** : EFI/MSR/OS/Recovery selon le mode de démarrage; NTFS pour le volume système. ReFS est destiné à des usages et éditions pris en charge, pas un remplacement universel de NTFS.
- **FreeBSD** : GPT avec UFS ou ZFS selon l'usage; vérifier le schéma de partitions de l'installateur et les exigences de démarrage.

### 14. Selection des composants de base

- **Debian** : tasksel (Serveur SSH, Utilitaires usuels du systeme, sans GUI)
- **RHEL** : Base Environment "Minimal Install" ou "Server" (sans GUI)
- **Windows** : Edition "Server Core" (sans GUI) ou "Server with Desktop Experience" (GUI)
- **FreeBSD** : Distribution sets (base, kernel, lib32, ports)

### 15. Chargeur d'amorcage (Bootloader)

- **Linux** : Chargeur pris en charge par la distribution et le mode de démarrage; GRUB est courant. Ne choisir systemd-boot que si la distribution et la configuration le prennent en charge.
- **Windows** : Windows Boot Manager (bootmgfw.efi / BCD)
- **FreeBSD** : loader.efi / gptzfsboot


## Phase 3 : configuration post-installation (étapes 16 à 25)

### 16. Adressage IP fixe definitif

- **Debian/Ubuntu** : /etc/network/interfaces (ifupdown) ou /etc/netplan/*.yaml
- **RHEL/Rocky** : nmcli / nmtui (/etc/NetworkManager/system-connections/)
- **Windows** : New-NetIPAddress (PowerShell) ou ncpa.cpl
- **FreeBSD** : /etc/rc.conf (ifconfig_em0="inet ...")

### 17. Resolution de noms (DNS Client)

- **Linux/BSD** : /etc/resolv.conf ou systemd-resolved (/etc/systemd/resolved.conf)
- **Windows** : Set-DnsClientServerAddress (PowerShell)

### 18. Table d'hotes locale

- **Linux/BSD** : /etc/hosts
- **Windows** : C:\Windows\System32\drivers\etc\hosts

### 19. Configuration des depots logiciels (Repositories)

- **Debian/Ubuntu** : /etc/apt/sources.list et /etc/apt/sources.list.d/
- **RHEL/Rocky** : /etc/yum.repos.d/*.repo
- **Windows** : Configurer Windows Update/WSUS selon la politique. Winget et PowerShell Gallery sont des sources distinctes de paquets/modules; contrôler leur origine et leur approbation.
- **FreeBSD** : /etc/pkg/FreeBSD.conf
- **Tous OS** : N'ajouter que des dépôts de confiance, vérifier leur signature et éviter les mélanges de versions ou de distributions.

### 20. Mise a jour initiale complete du systeme

- **Debian/Ubuntu** : Actualiser l'index puis examiner les changements proposés avant la mise à niveau (par exemple `apt update` puis `apt full-upgrade`).
- **RHEL/Rocky** : Examiner puis appliquer les mises à jour (`dnf upgrade`); planifier le redémarrage si le noyau ou des services l'exigent.
- **Windows** : Windows Update, WSUS ou l'outil de gestion approuvé. `Install-WindowsUpdate` dépend d'un module tiers; ne pas le présenter comme une commande intégrée.
- **FreeBSD** : Distinguer les mises à jour du système de base (`freebsd-update`, selon version et architecture) de celles des paquets (`pkg`); suivre le guide de mise à niveau de la version cible.
- **Tous OS** : Ne pas accepter automatiquement des suppressions ou changements majeurs sans les examiner; sauvegarder et prévoir une fenêtre de maintenance.

### 21. Pilotes et agents de virtualisation

- **Linux/BSD** : Installer uniquement l'agent et les pilotes correspondant à l'hyperviseur (par exemple QEMU Guest Agent, open-vm-tools ou xe-guest-utilities), si pris en charge.
- **Windows** : Pilotes VirtIO et agent QEMU, VMware Tools ou composants d'intégration Hyper-V selon la plateforme.
- **Firmware** : `fwupd` est un outil de mise à jour de firmware, pas un agent de virtualisation; l'utiliser uniquement avec du matériel et des sources compatibles.

### 22. Synchronisation horaire (NTP)

- **Linux** : Utiliser le client fourni ou approuvé par la distribution (par exemple chrony ou systemd-timesyncd); le chemin de configuration varie.
- **Windows** : Configurer Windows Time avec les sources approuvées par l'organisation ou le domaine; ne pas copier une commande contenant des serveurs fictifs.
- **FreeBSD** : Configurer le service NTP disponible pour la version et l'activer selon les règles de démarrage de FreeBSD.
- **Tous OS** : Vérifier la source, l'état de synchronisation et la cohérence des horloges entre machines.

### 23. Outils d'administration fondamentaux

- **Linux/BSD** : Installer uniquement les outils nécessaires depuis les dépôts approuvés; noms et disponibilité des paquets diffèrent (par exemple `dnsutils` sur Debian/Ubuntu et `bind-utils` sur RHEL).
- **Windows** : Outils d'administration approuvés (par exemple Sysinternals, PowerShell 7 ou Windows Admin Center selon le besoin). Activer OpenSSH Server uniquement s'il est requis et protégé.

### 24. Personnalisation de l'environnement et bannieres

- **Linux/BSD** : /etc/profile, ~/.bashrc, /etc/motd, /etc/issue, /etc/issue.net
- **Windows** : Profil PowerShell ($PROFILE), Banniere legale GPO (interactive logon message)
- **Tous OS** : Appliquer les bannières légales selon la politique et ne pas y exposer de détails sensibles sur le système.

### 25. Validation de l'etat initial (Baseline)

- **Tous OS** : Consigner versions, configuration et état des services. Créer une image de référence uniquement après validation; généraliser Windows avec Sysprep si l'image doit être clonée.
- **Virtualisation** : Un snapshot n'est ni une sauvegarde indépendante ni une preuve de restauration. Vérifier cohérence applicative, rétention, accès et procédure de suppression; éviter d'y conserver des secrets ou données non nécessaires.


## Phase 4 : sécurisation et hardening (étapes 26 à 35)

Appliquer les contrôles selon le modèle de menace, la politique et les dépendances des applications. Tester chaque changement en environnement représentatif; prévoir accès console et retour arrière avant de modifier l'accès distant, le réseau ou le démarrage.

### 26. Authentification par cles cryptographiques (SSH / WinRM)

- **Linux/BSD** : Clés SSH selon les algorithmes autorisés et compatibles; protéger la clé privée et contrôler propriétaire/permissions de `authorized_keys`.
- **Windows OpenSSH** : Fichier de clés et ACL selon le type de compte et la configuration OpenSSH Windows; vérifier la documentation de la version.
- **WinRM** : Pour l'accès hors domaine, préférer HTTPS avec certificats correctement validés; ne pas désactiver la validation TLS pour contourner une erreur.

### 27. Durcissement de l'acces distant

- **Linux/BSD** : Configurer sshd selon la version et les comptes autorisés. Avant de désactiver l'authentification par mot de passe, vérifier une seconde connexion par clé et conserver un accès de secours.
- **Windows** : Activer NLA si les clients le prennent en charge; limiter RDP à des réseaux d'administration/VPN et aux comptes nécessaires. Pour OpenSSH, utiliser la configuration effectivement chargée, généralement `C:\ProgramData\ssh\sshd_config`.

### 28. Gestion fine des privileges d'administration

- **Linux/BSD** : /etc/sudoers et /etc/sudoers.d/ (visudo)
- **Windows** : UAC (User Account Control), Groupes locaux Restreints, LAPS (Local Admin Password Solution)

### 29. Pare-feu hote (Host Firewall)

- **Debian/Ubuntu** : UFW ou Nftables (/etc/nftables.conf)
- **RHEL/Rocky** : Firewalld (firewall-cmd) ou Nftables
- **Windows** : Windows Defender Firewall with Advanced Security (wf.msc / New-NetFirewallRule)
- **FreeBSD** : PF (/etc/pf.conf) ou IPFW

### 30. Protection contre les intrusions et le brute-force (IPS)

- **Linux/BSD** : Fail2ban (/etc/fail2ban/jail.local) ou CrowdSec
- **Windows** : Protection intégrée, politiques de verrouillage définies avec précaution et outils approuvés pour la version.
- **Tous OS** : Ces contrôles complètent, sans remplacer, MFA, mises à jour, filtrage réseau et surveillance. Une politique de verrouillage trop stricte peut permettre un déni de service; tester les seuils.

### 31. Reduction de la surface d'attaque (Services)

- **Linux** : Identifier les dépendances et l'usage avant de désactiver ou masquer un service; `systemctl mask` empêche aussi son démarrage manuel.
- **Windows** : Vérifier les dépendances et la fonction avant d'arrêter ou de désactiver un service.
- **FreeBSD** : Vérifier le rôle du service avant de modifier son activation dans `/etc/rc.conf`.
- **Tous OS** : Appliquer un changement à la fois, valider les fonctions métier puis consigner le retour arrière.

### 32. Automatisation des correctifs de securite

- **Debian/Ubuntu** : Configurer et vérifier `unattended-upgrades`, ses origines autorisées, les notifications et le comportement de redémarrage.
- **RHEL/Rocky** : Configurer `dnf-automatic` (notamment téléchargement ou application) selon la politique de maintenance.
- **Windows** : GPO Windows Update Automatic Updates / WSUS
- **FreeBSD** : Planifier la vérification et l'application des mises à jour système et des paquets avec les mécanismes pris en charge par la version; `freebsd-update cron` vérifie les mises à jour, il ne remplace pas leur installation.
- **Tous OS** : Définir fenêtre, redémarrage, supervision et procédure de retour arrière; ne pas supposer que la configuration par défaut est une politique complète.

### 33. Securisation des systemes de fichiers et montages

- **Linux** : Examiner les permissions, propriétaires, quotas et options de montage. `nodev`, `nosuid` ou `noexec` ne conviennent pas indistinctement à chaque chemin et peuvent casser des applications; tester avant déploiement.
- **Windows** : Appliquer des ACL minimales et auditées. Ne désactiver les partages administratifs que si l'impact sur la gestion et les sauvegardes est compris.
- **FreeBSD** : Examiner les permissions et options de montage; les propriétés ZFS comme `exec` et `setuid` s'appliquent au dataset ciblé et peuvent empêcher des logiciels de fonctionner.

### 34. Durcissement du noyau et de la pile reseau

- **Linux/BSD** : Configurer uniquement les paramètres nécessaires dans les fichiers pris en charge par l'OS (par exemple `/etc/sysctl.d/` sous Linux). Des paramètres tels que `ip_forward` dépendent du rôle; ne pas les désactiver ou les activer globalement sans analyse.
- **Windows** : Préférer les stratégies et paramètres documentés pour la version; toute modification du registre doit être justifiée, sauvegardée et testée.
- **Tous OS** : Évaluer l'effet sur routage, VPN, conteneurs et haute disponibilité avant d'appliquer un réglage réseau.

### 35. Controle d'acces obligatoire (MAC) et Antivirus

- **Debian/Ubuntu** : Vérifier l'état AppArmor et mettre en mode enforcement les profils adaptés après validation; la disponibilité des outils varie selon l'installation.
- **RHEL/Rocky** : Vérifier le mode SELinux et les politiques; `setenforce` modifie l'état à l'exécution, tandis que la configuration persistante se traite séparément.
- **Windows** : Microsoft Defender Antivirus, AppLocker / WDAC (Windows Defender Application Control)
- **FreeBSD** : Évaluer le MAC Framework pour les contrôles MAC; les jails isolent des environnements et ne sont pas un substitut direct aux politiques MAC.
- **Tous OS** : Ne pas désactiver une protection pour masquer un problème; analyser les journaux et adapter la politique de façon ciblée.


## Phase 5 : mise en production et services (étapes 36 à 42)

### 36. Integration a l'annuaire ou au reseau d'administration

- **Linux/BSD** : Intégrer à AD ou FreeIPA/LDAP avec un client compatible et une politique d'identité testée. Le VPN est un contrôle d'accès réseau distinct, à traiter selon l'architecture.
- **Windows** : Add-Computer -DomainName (Jonction Active Directory Domain Services)
- **Tous OS** : Prévoir DNS, synchronisation horaire, comptes de secours, droits délégués et retrait propre de l'annuaire.

### 37. Deploiement des roles metiers et stacks applicatives

- **Linux/BSD** : Docker/Podman, Nginx/Apache, PostgreSQL/MariaDB, Bind9, etc.
- **Windows** : Server Manager Roles & Features (Install-WindowsFeature : ADDS, DNS, DHCP, IIS, Hyper-V)

### 38. Isolation des comptes de service

- **Linux** : Créer un compte dédié sans connexion interactive avec les outils de la distribution; `useradd -r` et le chemin de `nologin` ne sont pas uniformes.
- **BSD** : Utiliser les outils et conventions de comptes de service de la version.
- **Windows** : gMSA (Group Managed Service Accounts) ou Managed Service Accounts (MSA)
- **Tous OS** : Accorder uniquement les permissions nécessaires, protéger les secrets et documenter rotation et dépendances.

### 39. Chiffrement des flux (PKI / TLS)

- **Linux/BSD** : Utiliser la PKI de l'organisation ou une AC publique selon le besoin. Les outils et chemins d'installation des autorités varient selon l'OS; valider la chaîne et le renouvellement.
- **Windows** : AD CS (Auto-enrollment), IIS Certificate Binding, magasin de certificats (certlm.msc)
- **Tous OS** : Ne jamais installer une autorité de certification sans vérifier sa provenance et son empreinte; planifier expiration et renouvellement.

### 40. Configuration des sauvegardes (Backup)

- **Niveau VM** : Utiliser l'outil de sauvegarde de la plateforme (par exemple Proxmox Backup Server ou Veeam); `vzdump` est un outil de sauvegarde Proxmox, pas une commande PBS.
- **Niveau OS** : BorgBackup ou Restic pour des fichiers selon le besoin; `rclone` seul est une synchronisation, pas une stratégie de sauvegarde complète. Produire les dumps SQL avec une méthode cohérente avec le moteur; Windows Server Backup et VSS selon le rôle.
- **Tous OS** : Définir RPO/RTO, chiffrement, rétention, copie séparée, surveillance et test de restauration; protéger les identifiants de sauvegarde.

### 41. Supervision, metriques et inventaire (Monitoring)

- **Linux/BSD** : Déployer un agent pris en charge (Zabbix, node_exporter, GLPI Agent ou SNMP selon le besoin); limiter les sources autorisées et privilégier SNMPv3 si SNMP est requis.
- **Windows** : Agent adapté à la version et à la plateforme; contrôler le pare-feu, l'authentification et les droits de service.
- **Tous OS** : Inventorier les métriques et alertes nécessaires, protéger les identifiants et vérifier que les données ne divulguent pas d'informations sensibles.

### 42. Gestion, rotation et centralisation des journaux (Logs)

- **Linux/BSD** : Configurer la rétention et la persistance selon le service (`logrotate`, journald, syslog); protéger l'accès aux journaux et contrôler l'espace disque.
- **Windows** : Configurer les tailles et rétentions des journaux selon la politique; centraliser via WEF ou un agent approuvé et vérifier les ACL.
- **Tous OS** : Chiffrer et restreindre le transport centralisé; vérifier les versions, la maintenance et la compatibilité des agents avant déploiement.


## Phase 6 : vérification, tests et documentation (étapes 43 à 50)

### 43. Controle de l'etat des services et des ports en ecoute

- **Linux avec systemd** : `systemctl --failed` et `ss -tulnp` (les informations de processus peuvent nécessiter les privilèges administrateur).
- **Windows** : Contrôler les services attendus avec `Get-Service` et les sockets avec `Get-NetTCPConnection -State Listen`; comparer aux rôles réellement installés, pas uniquement à un état global.
- **FreeBSD** : `service -e` répertorie les scripts de service disponibles/activés; `sockstat -4 -6 -l` affiche les sockets en écoute.
- **Tous OS** : Comparer les résultats à l'inventaire des flux autorisés et identifier le processus propriétaire.

### 44. Audit d'exposition reseau externe

- **Tous OS** : Effectuer uniquement un contrôle autorisé, limité aux adresses et ports explicitement dans le périmètre, depuis un point de mesure convenu. Les scans de tous les ports et scripts de détection peuvent générer du trafic ou déclencher des alertes; ne pas les lancer sans accord, fenêtre et plan de retour arrière.
- **Validation** : Comparer les ports observés aux règles de pare-feu et à l'inventaire; consigner source, cible, portée et heure du test.

### 45. Analyse des journaux d'erreurs systeme

- **Linux** : Examiner `journalctl -p err -b` et les messages noyau selon la distribution; compléter par le journal du service concerné.
- **Windows** : Examiner System et Application avec l'Observateur d'événements ou `Get-WinEvent`; adapter filtres et période à la version et au diagnostic.
- **FreeBSD** : Examiner `dmesg` et les journaux système configurés, par exemple `/var/log/messages`.
- **Tous OS** : Corréler horodatages, fuseau, service et changement récent; ne pas considérer le seul niveau d'erreur comme une preuve de panne.

### 46. Test de persistance au redemarrage (Reboot Test)

- **Tous OS** : Planifier le redémarrage, prévenir les personnes concernées et vérifier sauvegarde, accès console et critères de retour arrière. Après redémarrage, contrôler montages, réseau, services métier et supervision.

### 47. Test de resilience et d'alerte (Watchdog / Monitoring)

- **Tous OS** : Tester en laboratoire ou lors d'une fenêtre de maintenance approuvée. Simuler une panne contrôlée et réversible; ne pas couper une interface ou arrêter un service critique en production sans scénario de bascule.
- **Validation** : Vérifier l'alerte, l'escalade et la reprise. Une politique de redémarrage automatique (par exemple systemd ou Windows Service Recovery) doit être adaptée au service et ne remplace pas le diagnostic.

### 48. Test de restauration (Validation PRA / DRP)

- **Tous OS** : Restaurer régulièrement une sauvegarde dans un environnement isolé, sans conflit d'adresses ni accès aux systèmes de production. Vérifier l'intégrité, les dépendances et les délais obtenus par rapport au RPO/RTO.

### 49. Enregistrement CMDB et Gestion des acces

- **Tous OS** : Enregistrer l'actif, ses dépendances et son adressage dans la CMDB/IPAM. Stocker les secrets uniquement dans le coffre-fort approuvé par l'organisation; documenter des références, jamais les secrets eux-mêmes.
- **Accès** : Attribuer des accès SSH/RDP nominatifs et minimaux; vérifier MFA, journalisation, révocation et comptes de secours selon la politique.

### 50. Documentation d'exploitation (Runbook / Dossier d'Architecture Technique)

- **Tous OS** : Documenter rôle, propriétaire, environnement, architecture, dépendances, flux autorisés, versions, sauvegardes/RPO/RTO, supervision, procédures de mise à jour, dépannage et retour arrière.
- **Sécurité** : Indiquer où trouver les secrets sans les reproduire. Ajouter date de vérification, sources officielles, limites connues et prochaine revue.