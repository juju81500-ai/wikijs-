# Matrice de Contrôle des Fiches Simples par OS et Actions TSSR

Cette matrice récapitule les tâches du Référentiel TSSR et leur état documentaire par environnement.

> **Statut provisoire** : les états historiques n'étaient pas appuyés par un contrôle fiable. **À vérifier** signifie que l'existence, le contenu, les commandes et la validation dans un environnement cible restent à confirmer ; ce statut ne certifie pas qu'une procédure est opérationnelle.

---

## 📊 Matrice Globale de Couverture (46 Tâches Opérationnelles × 8 Environnements OS)

| Action / Tâche Opérationnelle TSSR | Windows Server 2022 | Windows 10 / 11 | Debian 12 (Bookworm) | Debian 13 (Trixie) | Ubuntu 24.04 LTS | Rocky Linux 9 | Alpine 3.19 (LXC/VM) | Hôte Docker & Conteneurs |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Fixer l'adresse IP et les DNS** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Diagnostic réseau (Netcat, SS, Tcpdump)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Tester connectivité & DNS (nslookup, dig, ping, tracepath)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Activer / Désactiver une carte réseau** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Ajouter / Supprimer une route statique** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Vider le cache DNS local & la table ARP** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Configurer le fichier hosts pour la résolution locale** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Changer le nom d'hôte (Hostname / FQDN)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Créer un utilisateur local standard** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Créer un utilisateur administrateur (Sudo/Wheel/Admin)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Changer / Réinitialiser le mot de passe d'un utilisateur** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Gérer les groupes & permissions (POSIX / NTFS)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Vérifier, démarrer et redémarrer un service système** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Trouver et fermer le processus bloquant un port** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Créer et gérer des tâches planifiées (Cron / Task Scheduler)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Changer la disposition clavier AZERTY & le fuseau horaire** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Activer & sécuriser l'accès distant (SSH / RDP)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Générer et déployer une clé d'authentification SSH** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Réinitialiser un mot de passe local perdu (Offline)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Mettre à jour le système & paquets (APT/DNF/APK)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Agrandir / Gérer l'espace disque & LVM** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Initialiser, formater et monter un nouveau disque** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Monter un partage SMB au démarrage (/etc/fstab / Map Drive)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | **À vérifier** |
| **Synchroniser deux dossiers (Rsync / Robocopy)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Archiver et compresser des dossiers (Tar / Zip)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Dépanner un disque plein 100% (Purge logs/cache)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Consulter les journaux système en direct (journalctl / EventViewer)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** |
| **Configurer un pare-feu local (nftables/UFW/awall/Windows Firewall)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A |
| **Bannir / Débannir manuellement une IP (Fail2ban / NetFirewall)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
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
| **Consulter les logs et exécuter un terminal dans un conteneur** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | **À vérifier** |
| **Exporter et importer une image / volume Docker** | N/A | N/A | N/A | N/A | N/A | N/A | N/A | **À vérifier** |
| **Joindre un domaine Active Directory (AD DS)** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Promouvoir un contrôleur de domaine (AD DS)** | **À vérifier** | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| **Configurer un serveur DHCP (Scope & Réservation MAC)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Configurer un serveur DNS (Zones, A, CNAME)** | **À vérifier** | N/A | **À vérifier** | **À vérifier** | **À vérifier** | **À vérifier** | N/A | N/A |
| **Gérer les stratégies de groupe (GPO / GPUpdate)** | **À vérifier** | **À vérifier** | N/A | N/A | N/A | N/A | N/A | N/A |
