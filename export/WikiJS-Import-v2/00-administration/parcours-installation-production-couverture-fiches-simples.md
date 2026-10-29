---
title: "Parcours d'installation à la mise en production par OS"
description: "Ce document indique, pour chaque famille, les étapes de l'installation à la production et les fiches simples correspondantes. EXISTE signifie qu'une fiche traite l'étape; PARTIEL signale une couverture répartie entre plusieurs fiches ou plusieurs versions. Les trois manques Windows suivis plus bas s"
published: true
date: 2026-10-27T17:38:16Z
tags: []
editor: markdown
dateCreated: 2026-10-27T17:38:16Z
dateModified: 2026-10-27T17:38:16Z
---

# Parcours d'installation à la mise en production par OS

Ce document indique, pour chaque famille, les étapes de l'installation à la production et les fiches simples correspondantes. `EXISTE` signifie qu'une fiche traite l'étape; `PARTIEL` signale une couverture répartie entre plusieurs fiches ou plusieurs versions. Les trois manques Windows suivis plus bas sont maintenant couverts par des fiches simples; les étapes `PARTIEL` restent dépendantes de l'architecture ou de l'outil de gestion.

## Matrice de couverture

| Famille / cible | Étape du parcours | État | Fiche(s) existante(s) |
|---|---|---|---|
| Alpine LXC | Créer et installer un CT depuis un template maintenu | EXISTE | [[Fiche_Simple_-_LXC_Alpine_Installation_Creation_CT_Proxmox]] |
| Alpine LXC | Initialiser paquets, compte admin et services | EXISTE | `apk`, `doas`, OpenRC |
| Alpine LXC | Configurer et diagnostiquer réseau/DNS | EXISTE | IP statique et diagnostic réseau LXC |
| Alpine LXC | Configurer SSH et les services | EXISTE | OpenSSH, Chrony et services OpenRC |
| Alpine LXC | Contrôler la préparation à la production | EXISTE | [[Fiche_Simple_-_LXC_Alpine_Controle_Mise_Production]] |
| Debian VM | Installer Debian 13 sur une VM | EXISTE | [[Fiche_Simple_-_VM_Debian_13_Installation_OS_Premier_Demarrage]] |
| Debian VM | Préparer compte, hostname, mises à jour et réseau | PARTIEL | Fiches existantes Debian 12/13; vérifier la version cible |
| Debian VM | Installer rôles, stockage et services | EXISTE | Nginx, DNS, bases, systemd, LVM, RAID, NFS, iSCSI |
| Debian VM | Appliquer les contrôles de sécurité | EXISTE | SSH, AppArmor et nftables |
| Debian VM | Vérifier sauvegarde/restauration avant production | EXISTE | [[Fiche_Simple_-_VM_Debian_13_Controle_Mise_Production]] |
| Docker-LXC | Installer le moteur sur l'hôte | EXISTE | Docker Engine et Compose |
| Docker-LXC | Déployer, sécuriser et superviser une stack | EXISTE | Compose, secrets, healthcheck, journaux et réseau |
| Docker-LXC | Sauvegarder les données et bases applicatives | EXISTE | Fiches volumes et sauvegarde de stack |
| Docker-LXC | Mettre à jour une stack et revenir à la version précédente | EXISTE | [[Fiche_Simple_-_Docker_Production_Mise_A_Jour_Rollback_Compose]] |
| Docker-LXC | Reconstruire l'hôte et restaurer ses stacks | EXISTE | [[Fiche_Simple_-_Docker_Production_Reconstruire_Hote_Restaurer_Stacks]] |
| Rocky Linux VM | Installer Rocky Linux 9 sur une VM | EXISTE | [[Fiche_Simple_-_VM_Rocky_9_Installation_OS_Premier_Demarrage]] |
| Rocky Linux VM | Préparer compte, DNF, hostname et IP | PARTIEL | Utilisateur `wheel`, DNF et NetworkManager |
| Rocky Linux VM | Configurer stockage, services et conteneurs | EXISTE | LVM/XFS, quotas, Chrony, Podman/Quadlet |
| Rocky Linux VM | Configurer SELinux et firewalld | EXISTE | Fiches SELinux/firewalld et ouverture de port |
| Rocky Linux VM | Contrôler la réception en production | EXISTE | [[Fiche_Simple_-_VM_Rocky_9_Controle_Mise_Production]] |
| Ubuntu Server VM | Installer Ubuntu Server 24.04 sur une VM | EXISTE | [[Fiche_Simple_-_VM_Ubuntu_24.04_Installation_OS_Premier_Demarrage]] |
| Ubuntu Server VM | Préparer réseau, comptes, mises à jour et cloud-init | PARTIEL | Netplan, UFW, mises à jour et cloud-init |
| Ubuntu Server VM | Configurer services et contrôles de sécurité | EXISTE | SSH, AppArmor, firewall et diagnostic DNS |
| Ubuntu Server VM | Contrôler la réception en production | EXISTE | [[Fiche_Simple_-_VM_Ubuntu_24.04_Controle_Mise_Production]] |
| Windows 11 | Installer Windows 11 et terminer le premier démarrage | EXISTE | [[Fiche_Simple_-_VM_Windows_11_Installation_OS_Premier_Demarrage]] |
| Windows 11 | Configurer compte, réseau, domaine et accès distant | EXISTE | Compte local, IP/DNS, jonction domaine et OpenSSH/RDP |
| Windows 11 | Activer les protections du poste | EXISTE | BitLocker, pare-feu, mises à jour et LAPS selon gestion |
| Windows 11 | Vérifier le poste avant remise à l'utilisateur | EXISTE | [[Fiche_Simple_-_VM_Windows_11_Controle_Mise_Production]] |
| Windows Server 2022 | Installer Windows Server et préparer le premier démarrage | EXISTE | [[Fiche_Simple_-_VM_Windows_Server_2022_Installation_OS_Premier_Demarrage]] |
| Windows Server 2022 | Configurer réseau et services de rôle | EXISTE | AD DS, DNS, DHCP, IIS, SMB, GPO et RDS |
| Windows Server 2022 | Appliquer les protections et sauvegardes | EXISTE | GPO, LAPS, pare-feu et sauvegarde état système |
| Windows Server 2022 | Contrôler la mise en production et la reprise | EXISTE | [[Fiche_Simple_-_VM_Windows_Server_2022_Controle_Mise_Production]] |

## Fiches créées pour compléter le parcours

| Famille / cible | Fiche | Étape couverte |
|---|---|---|
| Alpine LXC | [[Fiche_Simple_-_LXC_Alpine_Installation_Creation_CT_Proxmox]] | Installation et création du CT |
| Alpine LXC | [[Fiche_Simple_-_LXC_Alpine_Controle_Mise_Production]] | Préparation et réception en production |
| Debian VM | [[Fiche_Simple_-_VM_Debian_13_Installation_OS_Premier_Demarrage]] | Installation et premier démarrage |
| Debian VM | [[Fiche_Simple_-_VM_Debian_13_Controle_Mise_Production]] | Contrôles et test de restauration |
| Docker-LXC | [[Fiche_Simple_-_Docker_Production_Mise_A_Jour_Rollback_Compose]] | Mise à jour et retour arrière d'une stack |
| Docker-LXC | [[Fiche_Simple_-_Docker_Production_Reconstruire_Hote_Restaurer_Stacks]] | Reprise après perte de l'hôte |
| Rocky Linux VM | [[Fiche_Simple_-_VM_Rocky_9_Installation_OS_Premier_Demarrage]] | Installation et premier démarrage |
| Rocky Linux VM | [[Fiche_Simple_-_VM_Rocky_9_Controle_Mise_Production]] | Contrôles et réception en production |
| Ubuntu Server VM | [[Fiche_Simple_-_VM_Ubuntu_24.04_Installation_OS_Premier_Demarrage]] | Installation et premier démarrage |
| Ubuntu Server VM | [[Fiche_Simple_-_VM_Ubuntu_24.04_Controle_Mise_Production]] | Contrôles et réception en production |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_Installation_OS_Premier_Demarrage]] | Installation et OOBE |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_Controle_Mise_Production]] | Contrôle avant remise du poste |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Installation_OS_Premier_Demarrage]] | Installation et premier démarrage |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Controle_Mise_Production]] | Contrôle des rôles et reprise |

## Actions simples détaillées et lacunes

Ordre de lecture conseillé : **Créer → Installer → Initialiser → Connecter → Déployer → Protéger → Sauvegarder → Tester → Basculer**.

**Légende :** `EXISTE` = fiche dédiée et directement applicable; `PARTIEL` = étapes réparties, dépendantes d'une autre procédure ou d'une version; `MANQUE` = pas de fiche simple dédiée.

## Versions et paquets de base

La matrice complète des séries et comportements des paquets se trouve dans [[Compatibilite_Versions_OS_Paquets_Base]]. Cette table indique quelles fiches d'installation/version sont disponibles dans le pack.

| Version cible | Installation / migration | Différences couvertes | État |
|---|---|---|---|
| Debian 12 Bookworm | [[Fiche_Simple_-_VM_Debian_12_Installation_OS_Premier_Demarrage]] | Séries Bookworm; MariaDB 10.11, PostgreSQL 15, PHP 8.2, Nginx 1.22 | EXISTE |
| Debian 12 → 13 | [[Fiche_Simple_-_VM_Debian_12_13_Preparer_Migration_Paquets]] | APT, /tmp, sysctl, réseau, SSH et migrations majeures | EXISTE |
| Debian 13 Trixie | [[Fiche_Simple_-_VM_Debian_13_Installation_OS_Premier_Demarrage]] | Séries Trixie; PHP 8.4, PostgreSQL 17, MariaDB 11.8, Nginx 1.26 | EXISTE |
| Ubuntu 24.04 LTS Noble | [[Fiche_Simple_-_VM_Ubuntu_24.04_Installation_OS_Premier_Demarrage]] | Série Noble : PHP 8.3, PostgreSQL 16, systemd 255 | EXISTE |
| Ubuntu 26.04 LTS Resolute | [[Fiche_Simple_-_VM_Ubuntu_26.04_Installation_OS_Premier_Demarrage]] | APT 3.1, systemd 259, Netplan 1.2, PHP 8.5, PostgreSQL 18 | EXISTE |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Installation_OS_Premier_Demarrage]] | Procédures de rôles existantes spécifiques à 2022 | EXISTE |
| Windows Server 2025 | [[Fiche_Simple_-_VM_Windows_Server_2025_Installation_OS_Premier_Demarrage]] | Installation et prérequis matériels 2025 | EXISTE |
| Windows Server 2022 → 2025 | [[Fiche_Simple_-_VM_Windows_Server_2025_Compatibilite_Fonctionnalites_2022]] | SMB, OpenSSH, AD DS/LDAP, Credential Guard et CPU | EXISTE |

**Nommage :** `26.04` désigne la série LTS Ubuntu; `26.04.1` est une image ponctuelle. Le point release ne constitue pas une nouvelle base APT.

### Alpine LXC

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Créer | Choisir le template, stockage, CPU/RAM, bridge/VLAN, ID et mode non privilégié | [[Fiche_Simple_-_LXC_Alpine_Installation_Creation_CT_Proxmox]] | EXISTE |
| Installer | Créer le CT depuis le template Alpine maintenu et faire le premier démarrage | [[Fiche_Simple_-_LXC_Alpine_Installation_Creation_CT_Proxmox]] | EXISTE |
| Initialiser | Vérifier version, dépôts `apk`, compte `doas`, services OpenRC et mises à jour | [[Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Creer_Compte_Admin_Doas]], [[Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Mise_A_Jour_Paquets_APK]], [[Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Gestion_Services_OpenRC]] | PARTIEL |
| Connecter | Définir IP/DNS au niveau Proxmox, vérifier route et résolution depuis le CT | [[Fiche_Simple_-_LXC_Alpine_3.19_IP_Statique]], [[Fiche_Simple_-_LXC_Alpine_3.19_Reseau_Diagnostic_DNS_Routes]] | EXISTE |
| Déployer | Installer et activer les services nécessaires via OpenRC | [[Fiche_Simple_-_LXC_Alpine_3.19_Services_Installation_et_Configu]], [[Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC]] | EXISTE |
| Protéger | Limiter le CT, sécuriser SSH/`doas`, filtrer au bon niveau de l'hôte | [[Fiche_Simple_-_LXC_Alpine_3.19_Securite_Configuration_Awall_Fir]], [[Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC]] | EXISTE |
| Sauvegarder | Définir une tâche PVE/PBS et conserver une copie indépendante | [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Tester | Restaurer le CT sous un ID et un réseau isolés, tester les services | [[Fiche_Simple_-_LXC_Alpine_Controle_Mise_Production]], [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Basculer | Migrer depuis 3.19, valider le nouveau CT, changer IP/DNS sans doublon | [[Fiche_Simple_-_LXC_Alpine_Migrer_3.19_Version_Maintenue]] | PARTIEL |

### Debian VM

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Créer | Définir ressources VM, firmware, disque et réseau | [[Fiche_Simple_-_VM_Debian_13_Installation_OS_Premier_Demarrage]] | EXISTE |
| Installer | Vérifier ISO, partitionner le disque, installer Debian 13 et SSH | [[Fiche_Simple_-_VM_Debian_13_Installation_OS_Premier_Demarrage]] | EXISTE |
| Initialiser | Créer compte `sudo`, hostname, mises à jour, heure et outils VM | Fiches Debian 12/13 de comptes, hostname, mises à jour et outils invités | PARTIEL |
| Connecter | Configurer IP, DNS, routes et VLAN avec le gestionnaire réseau effectif | [[Fiche_Simple_-_VM_Debian_13_IP_Statique_systemd-networkd]], [[Fiche_Simple_-_VM_Debian_13_Reseau_Configuration_VLAN_8021q]] | EXISTE |
| Déployer | Installer le rôle (Web, DNS, base, fichiers, supervision) et son unité systemd | Fiches Debian dédiées aux services et applications | EXISTE |
| Protéger | Configurer SSH, AppArmor, nftables, droits et mises à jour | Fiches Debian sécurité SSH, AppArmor et nftables | EXISTE |
| Sauvegarder | Sauvegarder les données, config et dépôts avec rétention et clé séparée | BorgBackup/Rclone Debian 12; PBS pour la VM complète | PARTIEL |
| Tester | Restaurer en isolé, vérifier le service et documenter le résultat | [[Fiche_Simple_-_VM_Debian_13_Controle_Mise_Production]], [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Basculer | Tester les accès client, DNS/IP et retour vers l'ancienne version | [[Fiche_Simple_-_VM_Debian_13_Controle_Mise_Production]] | PARTIEL |

### Docker-LXC

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Préparer | Installer et mettre à jour l'OS hôte Linux, disque, réseau et accès admin | Fiches Debian/Ubuntu d'installation; pas de système hôte Docker autonome | PARTIEL |
| Installer | Installer Docker Engine, Compose et vérifier le démon | [[Fiche_Simple_-_Hote_Docker_Installation_Engine_et_Compose]] | EXISTE |
| Déployer | Écrire Compose, réseaux, volumes, healthchecks et secrets | Fiches Docker Compose et déploiement d'applications | EXISTE |
| Protéger | Non-root, rootless, privilèges minimaux, secrets et accès socket | Fiches Docker de hardening et mode rootless | EXISTE |
| Sauvegarder | Dumper la base, arrêter les écritures, copier volumes et secrets séparément | [[Fiche_Simple_-_Docker_Sauvegarder_Stack_Compose_Base_Donnees]] | EXISTE |
| Tester | Restaurer la stack en projet isolé et vérifier les données | [[Fiche_Simple_-_Docker_Sauvegarder_Stack_Compose_Base_Donnees]] | EXISTE |
| Mettre à jour | Épingler les versions, sauvegarder, déployer et contrôler les migrations | [[Fiche_Simple_-_Docker_Production_Mise_A_Jour_Rollback_Compose]] | EXISTE |
| Revenir | Restaurer image et données compatibles; ne pas seulement downgrader une base migrée | [[Fiche_Simple_-_Docker_Production_Mise_A_Jour_Rollback_Compose]] | PARTIEL |
| Reprendre | Reconstruire l'hôte, restaurer fichiers/secrets/volumes puis rebascule | [[Fiche_Simple_-_Docker_Production_Reconstruire_Hote_Restaurer_Stacks]] | EXISTE |

### Rocky Linux

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Créer | Dimensionner VM, disque, firmware et réseau | [[Fiche_Simple_-_VM_Rocky_9_Installation_OS_Premier_Demarrage]] | EXISTE |
| Installer | Vérifier l'ISO, installer Rocky 9 et choisir le profil minimal | [[Fiche_Simple_-_VM_Rocky_9_Installation_OS_Premier_Demarrage]] | EXISTE |
| Initialiser | Créer compte `wheel`, hostname, mises à jour DNF, heure et outils VM | Fiches utilisateur, paquets et Chrony existantes | PARTIEL |
| Connecter | Créer le profil IP avec NetworkManager; valider DNS, route et VLAN | [[Fiche_Simple_-_VM_Rocky_9_Reseau_IP_Statique_NetworkManager_nmcli]] | EXISTE |
| Déployer | Installer le rôle ou conteneur Podman/Quadlet et ses volumes | Fiches services Rocky et Podman/Quadlet | EXISTE |
| Protéger | Garder SELinux Enforcing, régler firewalld et auditer les accès | Fiches Rocky firewalld/SELinux | EXISTE |
| Sauvegarder | Sauvegarder la VM et/ou les données applicatives sur une cible distincte | [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Tester | Restaurer en VM isolée, tester service, stockage et règles réseau | [[Fiche_Simple_-_VM_Rocky_9_Controle_Mise_Production]], [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Basculer | Tester le client, basculer DNS/IP et conserver un retour arrière | [[Fiche_Simple_-_VM_Rocky_9_Controle_Mise_Production]] | PARTIEL |

### Ubuntu Server

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Créer | Dimensionner VM, firmware, disque et réseau | [[Fiche_Simple_-_VM_Ubuntu_24.04_Installation_OS_Premier_Demarrage]] | EXISTE |
| Installer | Vérifier l'ISO, installer Ubuntu 24.04 et activer SSH si nécessaire | [[Fiche_Simple_-_VM_Ubuntu_24.04_Installation_OS_Premier_Demarrage]] | EXISTE |
| Initialiser | Créer compte admin, hostname, mises à jour, heure et gérer cloud-init | Fiches installation, mises à jour et cloud-init | EXISTE |
| Connecter | Configurer Netplan, DNS `systemd-resolved`, VLAN et UFW | Fiches Ubuntu réseau, DNS, VLAN et UFW | EXISTE |
| Déployer | Installer et contrôler le service attendu | Fiches Ubuntu services et OpenSSH | PARTIEL |
| Protéger | Sécuriser SSH, AppArmor, UFW et correctifs | Fiches Ubuntu SSH, AppArmor, UFW et mises à jour | EXISTE |
| Sauvegarder | Sauvegarder la VM ou données vers un stockage indépendant | [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]]; stratégie applicative à préciser | PARTIEL |
| Tester | Restaurer en VM isolée et valider le parcours applicatif | [[Fiche_Simple_-_VM_Ubuntu_24.04_Controle_Mise_Production]], [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Basculer | Vérifier DNS, accès client et retour à la configuration précédente | [[Fiche_Simple_-_VM_Ubuntu_24.04_Controle_Mise_Production]] | PARTIEL |

### Windows 11

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Créer | Définir poste/VM, édition, TPM, Secure Boot, stockage et réseau | [[Fiche_Simple_-_VM_Windows_11_Installation_OS_Premier_Demarrage]] | EXISTE |
| Installer | Installer Windows, terminer OOBE et appliquer les pilotes | [[Fiche_Simple_-_VM_Windows_11_Installation_OS_Premier_Demarrage]] | EXISTE |
| Initialiser | Nommer le poste, créer/inscrire le compte et appliquer les mises à jour | Fiches Windows 11 installation, compte local et jonction au domaine | EXISTE |
| Connecter | Configurer IP/DNS, joindre le domaine et tester les accès distants requis | Fiches Windows 11 réseau, domaine, RDP/OpenSSH | EXISTE |
| Déployer | Installer les applications approuvées et vérifier leur fonctionnement | La réception mentionne les applications, mais pas de procédure de déploiement de parc | PARTIEL |
| Protéger | Activer BitLocker, Defender, pare-feu et gestion LAPS si le poste est géré | Fiches Windows 11 BitLocker, firewall et LAPS | EXISTE |
| Sauvegarder les fichiers | Sauvegarder le profil utilisateur vers File History ou une solution gérée approuvée | [[Fiche_Simple_-_VM_Windows_11_Sauvegarder_Fichiers_File_History]] | EXISTE |
| Restaurer les fichiers | Récupérer un dossier/version et tester avant remise du poste | [[Fiche_Simple_-_VM_Windows_11_Restaurer_Fichiers_File_History_OneDrive]] | EXISTE |
| Remettre | Tester session, réseau, logiciels, récupération et support | [[Fiche_Simple_-_VM_Windows_11_Controle_Mise_Production]] | EXISTE |

### Windows Server 2022

| Action simple | Découpage concret | Fiche(s) | État |
|---|---|---|---|
| Créer | Dimensionner VM, firmware, disque, édition et accès console | [[Fiche_Simple_-_VM_Windows_Server_2022_Installation_OS_Premier_Demarrage]] | EXISTE |
| Installer | Installer Server Core ou Desktop Experience et appliquer les mises à jour | [[Fiche_Simple_-_VM_Windows_Server_2022_Installation_OS_Premier_Demarrage]] | EXISTE |
| Initialiser | Définir hostname, IP/DNS, compte admin, heure et accès d'administration | Fiches Windows Server réseau et comptes existantes | EXISTE |
| Déployer | Ajouter le rôle (AD DS, DNS, DHCP, IIS, SMB, RDS) et vérifier ses dépendances | Fiches dédiées aux rôles Windows Server | EXISTE |
| Protéger | Appliquer GPO, LAPS, pare-feu, délégations et journaux | Fiches GPO, LAPS et règles firewall | EXISTE |
| Sauvegarder | Sauvegarder état système et VM vers une cible distincte | Windows Server Backup et [[12_Proxmox_Backup_Server_3x_PBS_Deduplication]] | EXISTE |
| Restaurer un rôle | Répéter en lab isolé le scénario de récupération AD DS approuvé | [[Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Lab]] | EXISTE |
| Tester | Contrôler rôle, DNS, réplication, services, clients et restauration | [[Fiche_Simple_-_VM_Windows_Server_2022_Controle_Mise_Production]] | PARTIEL |
| Basculer | Documenter dépendances, fenêtre, DNS/IP/VIP et retour arrière | Checklist production générale, pas de procédure dédiée par rôle | PARTIEL |

## Manques confirmés

Les trois manques initiaux Windows 11 / Windows Server 2022 sont couverts par les fiches liées dans les tableaux précédents. Les points `PARTIEL` (distribution d'applications, bascules par rôle, sauvegarde applicative) restent dépendants de l'architecture et du système de gestion; ils ne sont pas déclarés manquants universellement.

| Nom d'action simple | OS | État |
|---|---|---|
| Sauvegarder les fichiers | Windows 11 | Couvert : File History avec cible approuvée |
| Restaurer les fichiers | Windows 11 | Couvert : restauration vers un emplacement alternatif |
| Restaurer un rôle | Windows Server 2022 | Couvert : exercice de reprise AD DS en lab isolé |

La distribution des applications Windows 11 et les bascules par rôle restent `PARTIEL` : elles dépendent de l'outil de gestion (Intune/MECM), du service et de l'architecture. Ne pas inventer une procédure universelle sans connaître ce choix.

## Points d'attention

- Alpine 3.19 est ancien : la fiche d'installation utilise un template maintenu disponible au moment du déploiement; la migration existante traite l'ancien CT.
- Les fiches Debian comportent encore des cibles Debian 12 et Debian 13; vérifier la version visée avant d'appliquer une commande.
- Docker-LXC décrit l'hôte et les conteneurs; ce n'est pas une distribution Linux autonome. L'installation du moteur reste liée à la distribution de l'hôte.
- `verify_wiki.py` contrôle les titres, tags et placeholders. Il ne valide pas les commandes sur une VM réelle ni la compatibilité des versions.