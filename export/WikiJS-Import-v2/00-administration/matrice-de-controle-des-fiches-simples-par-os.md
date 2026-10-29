---
title: "Matrice de Contrôle des Fiches Simples par OS et Actions TSSR"
description: "Cette matrice récapitule les tâches du Référentiel TSSR et leur état documentaire par environnement."
published: true
date: 2026-10-27T10:57:18Z
tags: []
editor: markdown
dateCreated: 2026-10-27T10:57:18Z
dateModified: 2026-10-27T10:57:18Z
---

# Matrice de Contrôle des Fiches Simples par OS et Actions TSSR

Cette matrice récapitule les tâches du Référentiel TSSR et leur état documentaire par environnement.

> **Statut provisoire** : les états historiques n'étaient pas appuyés par un contrôle fiable. **À vérifier** signifie que l'existence, le contenu, les commandes et la validation dans un environnement cible restent à confirmer ; ce statut ne certifie pas qu'une procédure est opérationnelle.

---

## 📊 Matrice Global de Couverture (Actions TSSR × Systèmes d'Exploitation)

| Action / Tâche Opérationnelle TSSR | Windows Server 2022 | Windows 10 / 11 | Debian 12 (Bookworm) | Debian 13 (Trixie) | Ubuntu 24.04 LTS | Rocky Linux 9 | Alpine 3.19 (LXC/VM) | Hôte Docker & Conteneurs |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Fixer l'adresse IP et les DNS** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Diagnostic réseau (Netcat, SS, Tcpdump)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Changer le nom d'hôte (Hostname / FQDN)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Créer un utilisateur local standard** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Créer un utilisateur administrateur (Sudo/Wheel/Admin)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Gérer les groupes & permissions (POSIX / NTFS)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Activer & sécuriser l'accès distant (SSH / RDP)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Réinitialiser un mot de passe local perdu** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Mettre à jour le système & paquets (APT/DNF/APK)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Agrandir / Gérer l'espace disque & LVM** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Dépanner un disque plein 100% (Purge logs/cache)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Configurer un pare-feu local (nftables/UFW/awall)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Installer & configurer un serveur Web (Nginx/PHP)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Configurer le chiffrement SSL/TLS (Certbot)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | **À vérifier** |
| **Installer une base de données (PostgreSQL/MariaDB)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | **À vérifier** |
| **Configurer un partage de fichiers (SMB / NFSv4)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | N/A | **À vérifier** | N/A | **À vérifier** |
| **Configurer un stockage SAN / iSCSI Target LIO** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | N/A | N/A | N/A | N/A |
| **Haute Disponibilité & IP virtuelle (VRRP Keepalived)** | N/A | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Installer un agent de supervision (Zabbix/Prometheus)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Centraliser les logs à distance (Rsyslog TLS)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Synchronisation horaire / NTP (Chrony/W32Time)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Déployer Docker Engine & Compose / Portainer** | N/A | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | **À vérifier** |
| **Joindre un domaine Active Directory (AD DS)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Promouvoir un contrôleur de domaine (AD DS)** | **À vérifier** | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **Configurer un serveur DHCP (Scope & Réservation MAC)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Configurer un serveur DNS (Zones, A, CNAME)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Gérer les stratégies de groupe (GPO / GPUpdate)** | **À vérifier** | **À vérifier** | N/A | N/A | N/A | N/A | N/A | N/A |

---

## 🔍 Légende & Explications

- **À vérifier** : Couverture non validée ; vérifier le fichier correspondant, son contenu et ses prérequis.
- **À FAIRE** : Aucun document correspondant repéré ; confirmer le périmètre avant rédaction.
- **N/A** : Non Applicable pour cet environnement.