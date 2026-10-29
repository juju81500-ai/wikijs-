---
title: "Compatibilité des versions d'OS et des paquets de base"
description: "Référence vérifiée le : 2026-10-27"
published: true
date: 2026-10-27T14:01:23Z
tags: []
editor: markdown
dateCreated: 2026-10-27T14:01:23Z
dateModified: 2026-10-27T14:01:23Z
---

# Compatibilité des versions d'OS et des paquets de base

**Référence vérifiée le :** 2026-10-27  
**Périmètre :** Debian 12/13, Ubuntu Server 24.04/26.04 et Windows Server 2022/2025.

Les séries ci-dessous sont celles des versions de distribution. Les révisions mineures évoluent avec les mises à jour de sécurité et les mises à jour ponctuelles. Avant toute commande d'installation, vérifier l'édition, les dépôts actifs et le candidat réellement proposé sur la machine.

## Repères Debian

| Paquet / composant | Debian 12 Bookworm | Debian 13 Trixie | Conséquence pour les fiches |
|---|---:|---:|---|
| Noyau Linux | 6.1 | 6.12 | Vérifier pilotes, modules et compatibilité hyperviseur |
| systemd | 252 | 257 | Tester unités, options et services séparés |
| Python 3 par défaut | 3.11 | 3.13 | Utiliser venv/pipx; ne pas mélanger les modules système |
| PHP | 8.2 | 8.4 | Noms `php8.2-*` ou `php8.4-*`; extensions FPM assorties |
| PostgreSQL | 15 | 17 | Cluster et répertoire de données versionnés; migration majeure requise |
| MariaDB | 10.11 | 11.8 | Arrêt propre et sauvegarde avant migration majeure |
| Nginx | 1.22 | 1.26 | Les fichiers de site restent semblables; tester les modules et directives |
| OpenSSH | 9.2p1 | 10.0p1 | DSA est supprimé dans Trixie; adapter les clients anciens |
| OpenSSL | 3.0 | 3.5 | Vérifier compatibilité TLS, extensions et applications compilées |

### Changements Debian à ne pas manquer

- Debian 13 utilise `systemd-tmpfiles` pour nettoyer `/tmp` et `/var/tmp`; ne pas y stocker des données durables.
- `/etc/sysctl.conf` n'est plus lu par `systemd-sysctl` dans Trixie; placer les réglages locaux dans `/etc/sysctl.d/*.conf`.
- Le paquet `samba-ad-dc` doit être installé pour la fonction contrôleur de domaine Samba AD.
- MariaDB 10.11 vers 11.8 exige un arrêt propre; le serveur 11.8 ne doit pas tenter de récupérer directement un répertoire laissé incohérent par 10.11.
- OpenSSH 10.0 ne prend plus en charge DSA; `~/.pam_environment` n'est plus lu par sshd.
- `systemd-resolved` est un paquet distinct sous Bookworm; ne pas supposer qu'il est installé.
- La compatibilité et le support sécurité diffèrent selon l'architecture; Debian 13 réduit notamment la portée d'i386.

## Repères Ubuntu Server

| Paquet / composant | Ubuntu 24.04 LTS Noble | Ubuntu 26.04 LTS Resolute | Conséquence pour les fiches |
|---|---:|---:|---|
| Noyau GA | 6.8 | 7.0 | Vérifier pilotes, modules externes et HWE |
| systemd | 255 | 259 | Cgroup v1 est supprimé en 26.04; migrer les configurations anciennes |
| Netplan | 1.0 | 1.2 | Tester les YAML et le renderer réellement installé |
| APT | 2.8 | 3.1 | `apt-key` est supprimé en 26.04; utiliser des keyrings et sources deb822 |
| Python 3 par défaut | 3.12 | 3.14 | Tester les applications, extensions natives et environnements virtuels |
| PHP | 8.3 | 8.5 | Vérifier modules, extensions et compatibilité applicative |
| PostgreSQL | 16 | 18 | Prévoir une migration de cluster, pas une simple mise à jour des paquets |
| MySQL | 8.0 | 8.4 LTS | Vérifier l'authentification; `mysql_native_password` est désactivé par défaut en 8.4 |
| OpenSSH | 9.6p1 | 10.2p1 | DSA supprimé; tester clés, algorithmes et options sshd |
| NTP client par défaut | systemd-timesyncd | Chrony | Vérifier service, sources et fichiers de configuration |

**Attention au nom de version :** Ubuntu 26.04 LTS est la série d'avril 2026. Un nom comme `26.04.1` désigne une image ponctuelle; il ne s'agit pas d'une nouvelle série APT. Confirmer le point release disponible avant de choisir l'ISO.

### Changements Ubuntu 26.04 à vérifier

- Les nouveaux serveurs utilisent Chrony comme client horaire par défaut; l'ancien `systemd-timesyncd` peut nécessiter une migration contrôlée.
- La pile d'initialisation passe à Dracut par défaut; les procédures d'initramfs existantes doivent être vérifiées.
- `sudo-rs` devient l'implémentation `sudo` par défaut et les utilitaires coreutils évoluent; tester les scripts qui dépendent de comportements GNU précis.
- `apt-key` n'est plus disponible; ne pas copier d'anciennes procédures de dépôt tierce partie fondées sur cette commande.
- Les mises à niveau 24.04 vers 26.04 franchissent les versions intermédiaires; lire les notes de migration des services, en particulier OpenLDAP, Samba, Dovecot, MySQL et PostgreSQL.

## Repères Windows Server

| Sujet | Windows Server 2022 | Windows Server 2025 | Contrôle à faire |
|---|---|---|---|
| Installation | Server Core ou Desktop Experience | Même choix, à fixer à l'installation | Core/Desktop Experience ne se convertissent pas après installation; prévoir une réinstallation pour changer |
| CPU minimum | Exigences x64 Microsoft | Ajoute SSE4.2 et POPCNT | Vérifier les flags CPU exposés par l'hyperviseur |
| RAM minimale VM d'installation | Core: 1 Go; Desktop Experience: 2 Go | 2 Go minimum; 4 Go recommandés pour Desktop Experience | Allouer suffisamment de RAM pendant le setup |
| OpenSSH Server | Fonctionnalité à installer selon besoin | Composant serveur installé par défaut | Vérifier service, règles entrantes et groupe `OpenSSH Users` |
| SMB sortant | Réglages selon version et stratégie | Signature requise par défaut; chiffrement sortant renforcé | Tester NAS, sauvegardes et clients non-Microsoft avant bascule |
| Credential Guard | Dépend de la configuration | Activé par défaut sur matériels compatibles | Vérifier matériel et compatibilité des logiciels d'identité |
| AD DS | Comportement établi en 2022 | Nouveaux contrôles LDAP, Kerberos et niveau fonctionnel | Tester les applications LDAP; ne pas activer les options forêt-wide sans plan |
| Comptes locaux | Windows LAPS disponible selon mises à jour | Windows LAPS enrichi (comptes gérés, passphrases, rollback image) | Vérifier schéma, GPO et délégations avant déploiement |

Ces changements de Windows Server 2025 ne sont pas tous des changements de « paquet » : il s'agit aussi de prérequis matériels, valeurs par défaut et compatibilité des protocoles.

## Vérifier les candidats sur la machine

Sur Debian/Ubuntu, relever la version et le candidat APT au moment de l'installation :

```bash
cat /etc/os-release
apt-cache policy nginx php-fpm postgresql mariadb-server openssh-server systemd
apt list --upgradable
```

Pour les paquets explicitement versionnés, interroger le nom exact (`php8.4-fpm`, `postgresql-17`, etc.). Ne pas remplacer un paquet générique par un nom versionné sans confirmer sa présence dans les dépôts actifs.

Sur Windows, relever l'édition, la build et les fonctionnalités :

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Get-WindowsFeature | Where-Object Installed
Get-SmbClientConfiguration | Select-Object RequireSecuritySignature, RequireEncryption
Get-Service sshd -ErrorAction SilentlyContinue
```

## Sources officielles

- [Debian 12 Bookworm — nouveautés et versions de paquets](https://www.debian.org/releases/bookworm/amd64/release-notes/ch-whats-new.en.html)
- [Debian 12 Bookworm — changements à connaître](https://www.debian.org/releases/bookworm/amd64/release-notes/ch-information.en.html)
- [Debian 13 Trixie — nouveautés et versions de paquets](https://www.debian.org/releases/trixie/release-notes/whats-new.en.html)
- [Debian 13 Trixie — changements à connaître](https://www.debian.org/releases/trixie/release-notes/issues.en.html)
- [Ubuntu 24.04 LTS — notes de version](https://documentation.ubuntu.com/release-notes/24.04/)
- [Ubuntu 26.04 LTS — résumé des changements pour les versions LTS](https://documentation.ubuntu.com/release-notes/26.04/summary-for-lts-users/)
- [Windows Server 2025 — nouveautés](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Windows Server — exigences matérielles](https://learn.microsoft.com/en-us/windows-server/get-started/hardware-requirements)
- [Windows Server — Server Core et Desktop Experience](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server-core-desktop-experience)

Les numéros de versions ci-dessus sont les séries majeures; consulter les notes de version et les candidats des dépôts avant toute mise à niveau ou commande de production.