---
title: "Catalogue des fiches simples par OS"
description: "Ce catalogue suit l'ajout de fiches simples par famille. Les commandes et interfaces doivent rester spécifiques à la version et au rôle de la machine; une fiche transversale ne doit pas masquer les différences entre OpenRC, systemd, NetworkManager, Netplan, Docker et Windows Server."
published: true
date: 2026-10-27T20:20:13Z
tags: []
editor: markdown
dateCreated: 2026-10-27T20:20:13Z
dateModified: 2026-10-27T20:20:13Z
---

# Catalogue des fiches simples par OS

Ce catalogue suit l'ajout de fiches simples par famille. Les commandes et interfaces doivent rester spécifiques à la version et au rôle de la machine; une fiche transversale ne doit pas masquer les différences entre OpenRC, systemd, NetworkManager, Netplan, Docker et Windows Server.

Pour le parcours détaillé par actions simples, les fiches existantes et les lacunes restantes, consulter [[Parcours_Installation_Production_Couverture_Fiches_Simples]].
Pour les versions de base, séries de paquets et changements entre versions, consulter [[Compatibilite_Versions_OS_Paquets_Base]].

## Fiches ajoutées

| Famille / OS | Fiche réalisée | Création | Installation | Paramétrage | Réseau | Stockage / diagnostic | Maintenance | Sécurité / chiffrement | État |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Alpine 3.19 | [[Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Creer_Compte_Admin_Doas]] | OK | OK | OK | — | — | — | OK | OK |
| Alpine 3.19 | [[Fiche_Simple_-_LXC_Alpine_3.19_Securite_OpenSSH_Cle_Et_OpenRC]] | — | OK | OK | — | — | — | OK | OK |
| Alpine 3.19 | [[Fiche_Simple_-_LXC_Alpine_3.19_Reseau_Diagnostic_DNS_Routes]] | — | — | OK | OK | — | — | — | OK |
| Alpine 3.19 | [[Fiche_Simple_-_LXC_Alpine_3.19_Systeme_Mise_A_Jour_Paquets_APK]] | — | — | — | — | — | OK | OK | OK |
| Alpine | [[Fiche_Simple_-_LXC_Alpine_Migrer_3.19_Version_Maintenue]] | — | — | OK | — | — | OK | — | OK |
| Alpine VM | [[Fiche_Simple_-_VM_Alpine_Chrony_NTP_OpenRC]] | — | OK | OK | OK | — | — | — | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Stockage_Diagnostic_Sante_Disque_SMART]] | — | OK | OK | — | OK | — | — | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Stockage_Monter_Disque_UUID_Fstab]] | — | — | OK | — | OK | — | — | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Services_Creer_Service_Systemd_Durci]] | — | — | OK | — | — | — | OK | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Securite_Diagnostic_AppArmor]] | — | — | OK | — | — | — | OK | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Automatisation_Creer_Timer_Systemd]] | — | — | OK | — | — | OK | — | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Stockage_Creer_RAID1_Mdadm]] | — | OK | OK | — | OK | OK | OK | OK |
| Debian 12 | [[Fiche_Simple_-_VM_Debian_12_Installation_OS_Premier_Demarrage]] | — | OK | OK | OK | OK | — | — | OK |
| Debian 12 → 13 | [[Fiche_Simple_-_VM_Debian_12_13_Preparer_Migration_Paquets]] | — | — | OK | OK | OK | OK | OK | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Web_Installation_Nginx_PHP8.4_FPM]] | — | OK | OK | OK | — | — | OK | OK |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Database_Installation_PostgreSQL_17]] | — | OK | OK | OK | — | — | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Hote_Docker_Securite_Activer_Mode_Rootless]] | — | OK | OK | — | — | — | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Docker_Sauvegarder_Restaurer_Volume]] | — | — | — | — | OK | OK | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Docker_Compose_Healthcheck_Secrets_Rotation_Journaux]] | — | — | OK | — | — | OK | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Docker_Reseau_Diagnostic_Reseaux_Compose]] | — | — | OK | OK | — | — | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Docker_Compose_Durcir_Service_NonRoot]] | — | — | OK | — | — | — | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Docker_Sauvegarder_Stack_Compose_Base_Donnees]] | — | — | OK | — | OK | OK | OK | OK |
| Rocky Linux 9 | [[Fiche_Simple_-_VM_Rocky_9_Reseau_IP_Statique_NetworkManager_nmcli]] | — | — | OK | OK | — | — | — | OK |
| Rocky Linux 9 | [[Fiche_Simple_-_VM_Rocky_9_Stockage_Etendre_LVM_XFS]] | — | — | OK | — | OK | — | — | OK |
| Rocky Linux 9 | [[Fiche_Simple_-_VM_Rocky_9_Conteneurs_Podman_Rootless_Quadlet]] | — | OK | OK | — | — | — | OK | OK |
| Rocky Linux 9 | [[Fiche_Simple_-_VM_Rocky_9_Securite_Autoriser_Port_Web_SELinux_Firewalld]] | — | — | OK | OK | — | — | OK | OK |
| Rocky Linux 9 | [[Fiche_Simple_-_VM_Rocky_9_Services_Configurer_Chrony_NTP]] | — | OK | OK | OK | — | — | — | OK |
| Rocky Linux 9 | [[Fiche_Simple_-_VM_Rocky_9_Stockage_Configurer_Quotas_Projet_XFS]] | — | OK | OK | — | OK | — | OK | OK |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Installation_SSH_Cle_Et_UFW]] | — | OK | OK | OK | — | — | OK | OK |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Reseau_Diagnostic_SystemdResolved_DNS_Split]] | — | — | OK | OK | — | — | — | OK |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Diagnostic_AppArmor]] | — | — | OK | — | — | — | OK | OK |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Gerer_Netplan_CloudInit]] | — | — | OK | OK | — | — | — | OK |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Reseau_Config_VLAN_Netplan]] | — | — | OK | OK | — | — | — | OK |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Creer_Profil_AppArmor]] | — | — | OK | — | — | — | OK | OK |
| Ubuntu Server 26.04 | [[Fiche_Simple_-_VM_Ubuntu_26.04_Installation_OS_Premier_Demarrage]] | — | OK | OK | OK | — | OK | OK | OK |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_Securite_Activer_BitLocker_TPM]] | — | — | OK | — | — | — | OK | OK |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Reseau_Regle_Firewall_Source_Limitee]] | — | — | OK | OK | — | — | OK | OK |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_Administration_Installer_OpenSSH_Cle]] | — | OK | OK | OK | — | — | OK | OK |
| Windows AD | [[Fiche_Simple_-_VM_Windows_AD_Configurer_Windows_LAPS]] | — | — | OK | — | — | — | OK | OK |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Sauvegarder_Restaurer_Etat_Systeme]] | — | OK | OK | — | OK | OK | — | OK |
| Windows Server 2025 | [[Fiche_Simple_-_VM_Windows_Server_2025_Installation_OS_Premier_Demarrage]] | — | OK | OK | OK | — | OK | OK | OK |
| Windows Server 2022/2025 | [[Fiche_Simple_-_VM_Windows_Server_2025_Compatibilite_Fonctionnalites_2022]] | — | — | OK | OK | — | — | OK | OK |
| Docker-LXC | [[Fiche_Simple_-_Docker_Snipe-IT_Importer_Actifs_CSV]] | — | — | OK | — | — | OK | OK | OK | Import test et sauvegarde préalables |
| Debian 12 | [[Fiche_Simple_-_VM_Debian_12_iTop_Cron_Taches_Arriere_Plan]] | — | — | OK | — | — | OK | OK | OK | Fichier de paramètres hors DocumentRoot |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Installer_Agent_OCS_Inventory]] | — | OK | OK | OK | — | OK | OK | OK | OCS 3, TLS vérifié, droits agent minimaux |
| Debian 12 | [[Fiche_Simple_-_VM_Debian_12_Verifier_Scheduler_Znuny]] | — | — | OK | — | — | OK | OK | OK | Znuny 7.3.x |
| Debian 12 | [[Fiche_Simple_-_VM_Debian_12_Cacti_Verifier_Poller]] | — | — | OK | OK | OK | OK | OK | OK | Vérifier un seul appareil pilote |
| Debian 12 | [[Fiche_Simple_-_VM_Debian_12_Splunk_Verifier_Service_Ingestion]] | — | — | OK | OK | OK | OK | OK | OK | Compte splunk, réseau restreint, TLS |
| Cloud / SaaS | [[Fiche_Simple_-_Jira_Service_Management_Creer_Portail_ITSM]] | — | OK | OK | — | — | OK | OK | OK | Limiter l'accès clients et tester les rôles |
| Cloud / SaaS | [[Fiche_Simple_-_Cloud_Datadog_Installer_Agent_Linux_Pilote]] | — | OK | OK | OK | — | OK | OK | OK | Secret API au coffre, déploiement pilote |
| Cloud / SaaS | [[Fiche_Simple_-_Cloud_Dynatrace_OneAgent_Installer_Pilote_Linux]] | — | OK | OK | OK | — | OK | OK | OK | Signature vérifiée, mode non privilégié |
| Windows Server | [[Fiche_Simple_-_VM_Windows_Server_Lansweeper_Scan_Pilote]] | — | — | OK | OK | — | OK | OK | OK | Scanner uniquement un périmètre autorisé |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Ajouter_Cible_Prometheus]] | — | — | OK | OK | — | OK | OK | OK | Cible autorisée, réseau restreint, TLS si besoin |
| Ubuntu Server 26.04 | [[Fiche_Simple_-_VM_Ubuntu_26.04_Configurer_SNMPv3_ReadOnly]] | — | OK | OK | OK | — | — | OK | OK | SNMPv3 authPriv en lecture seule |
| Ubuntu Server | [[Fiche_Simple_-_VM_Ubuntu_Ceph_Verifier_Sante_Cluster]] | — | — | OK | OK | OK | OK | OK | OK | Contrôles en lecture seule; ne pas redémarrer plusieurs OSD ou purger le cluster |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Centreon_Ajouter_Hote_Pilote]] | — | — | OK | OK | — | OK | OK | OK | Périmètre pilote autorisé |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Elastic_Verifier_Sante_TLS]] | — | — | OK | — | OK | OK | OK | OK | API en TLS vérifié, sauvegardes contrôlées |
| Ubuntu Server 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Graylog_Valider_Input_Syslog_Pilote]] | — | — | OK | OK | — | OK | OK | OK | Input filtré, pilote autorisé |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Ajouter_Appareil_Pilote]] | — | — | OK | OK | — | OK | OK | OK | Appareil approuvé, scan réduit |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Hyper_V_Creer_VM_Pilote]] | — | OK | OK | OK | OK | OK | OK | OK | Switch et ressources approuvés |
| VMware ESXi 8.0 | [[Fiche_Simple_-_VMware_ESXi_8_Configurer_Hote_Pilote]] | — | OK | OK | OK | OK | OK | OK | OK | Host pilote, accès gestion restreint |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Job_Hyper_V_Pilote]] | — | — | OK | OK | OK | OK | OK | OK | Job pilote et restauration vérifiés |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Bareos_Valider_Restauration]] | — | — | OK | — | OK | OK | OK | OK | Restaurer d'abord en répertoire temporaire |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Observium_Ajouter_Hote_SNMPv3]] | — | — | OK | OK | — | OK | OK | OK | Équipement autorisé, SNMPv3 authPriv, poller cinq minutes |
| pfSense CE | [[Fiche_Simple_-_pfSense_CE_2.9.0_Valider_Flux_Lab]] | — | OK | OK | OK | OK | OK | OK | OK | Deux bridges isolés, GUI LAN seulement, backup chiffré |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Zeek_Valider_Capteur]] | — | OK | OK | OK | OK | OK | OK | OK | Capteur passif autorisé, logs protégés, aucun filtrage inline |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Suricata_Valider_Capteur_IDS]] | — | OK | OK | OK | OK | OK | OK | OK | IDS passif, interface miroir autorisée, pas de NFQUEUE/IPS |
| Debian 12 | [[Fiche_Simple_-_VM_Debian_12_Bacula_Valider_Restauration]] | — | — | OK | — | OK | OK | OK | OK | Restaurer d'abord vers un emplacement temporaire et comparer le SHA-256 |
| Appliance / NAS | [[Fiche_Simple_-_TrueNAS_SCALE_25.10_Verifier_Pool_Sauvegarde]] | — | — | OK | — | OK | OK | OK | OK | Contrôler pool et test de restauration |
| Debian 13 | [[Fiche_Simple_-_Debian_13_Hashicorp_Vault_Valider_Politique]] | — | — | OK | — | — | OK | OK | OK | Tester autorisation et refus, secrets fictifs |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Services_Installation_DNS_BIND9]] | — | OK | OK | OK | — | OK | OK | OK | Zone autoritative uniquement, valider avant rechargement |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Services_Installation_DHCP_KEA]] | — | OK | OK | OK | — | OK | OK | OK | VLAN isolé, sauvegarder les baux et tester en client pilote |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_NetBox_Valider_IPAM]] | — | — | OK | OK | OK | OK | OK | OK | Pilote IPAM, permissions minimales, sauvegarde/restauration isolée |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_phpIPAM_Valider_IPAM]] | — | — | OK | OK | OK | OK | OK | OK | Pilote IPAM manuel, assistant désactivé, restauration isolée |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_KeePassXC_Valider_Coffre]] | — | OK | OK | — | OK | OK | OK | OK | AppImage vérifiée, coffre fictif, copie de sauvegarde restaurée sans toucher au coffre actif |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_VSCode_Valider_Installation]] | — | OK | OK | — | — | OK | OK | OK | Dépôt APT signé, Restricted Mode maintenu, extension vérifiée, aucun lancement en root |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Python_Valider_Venv_Pipx]] | — | OK | OK | — | — | OK | OK | OK | Vérifier le venv, le pipx et l'absence d'installation pip dans le Python système |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Git_Valider_Clone_Commit]] | — | OK | OK | OK | — | OK | OK | OK | Remote approuvé, identité correcte, diff relu, aucun secret, push sans force |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Wireshark_Valider_Capture_Locale]] | — | OK | OK | OK | OK | OK | OK | OK | Capture locale limitée, groupe wireshark justifié, PCAP protégé puis supprimé si inutile |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_PuTTY_Valider_SSH_HostKey]] | — | OK | OK | OK | — | OK | OK | OK | MSI signé, host key vérifiée hors bande, clé privée protégée et agent forwarding limité |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_PowerShell_Valider_Shell_Admin]] | — | OK | OK | — | OK | OK | OK | OK | MSI vérifié, différencier pwsh et 5.1, contrôles locaux lecture seule, stratégies d'exécution respectées |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_QGIS_Valider_Projet]] | — | — | OK | — | OK | OK | OK | OK | Projet réouvert, CRS vérifié, export contrôlé, données autorisées |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_draw_io_Valider_Diagramme]] | — | OK | OK | — | OK | OK | OK | OK | Diagramme maître réouvert, export vérifié, aucun secret inclus |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_GNS3_Valider_Lab_Isole]] | — | OK | OK | OK | OK | OK | OK | OK | Serveur local, projet rouvert, aucune liaison hors lab |
| Ubuntu 24.04 | [[Fiche_Simple_-_VM_Ubuntu_24.04_Packet_Tracer_Valider_Simulation]] | — | OK | OK | OK | OK | OK | OK | OK | Source Cisco, compte NetAcad, maquette locale non reliée au réel |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_phpIPAM_Valider_IPAM]] | — | — | OK | OK | OK | OK | OK | OK | Pilote IPAM manuel, assistant désactivé, restauration isolée |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Services_Installation_Samba_AD_DC]] | — | OK | OK | OK | — | OK | OK | OK | Domaine de lab neuf, restauration testée à part |
| Debian 13 | [[Fiche_Simple_-_VM_Debian_13_Stockage_Installation_OpenMediaVault_8]] | — | OK | OK | OK | OK | OK | OK | OK | OMV 8 sur Debian minimal; console disponible et disque de données séparé |
| Docker-LXC | [[Fiche_Simple_-_Bitwarden_Self_Hosted_Verifier_Backup_Restauration]] | — | — | OK | — | OK | OK | OK | OK | Inclure tout bwdata, restauration isolée |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_Sauvegarder_Fichiers_File_History]] | — | — | OK | — | OK | OK | OK | OK | Cible approuvée, test de restauration |
| Windows 11 | [[Fiche_Simple_-_VM_Windows_11_Restaurer_Fichiers_File_History_OneDrive]] | — | — | OK | — | OK | OK | OK | OK | Restaurer d'abord vers un autre emplacement |
| Windows Server 2022 | [[Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Lab]] | — | — | OK | — | OK | OK | OK | OK | Lab isolé, plan Microsoft validé |
| pfSense / réseau lab | [[Fiche_Simple_-_DMZ_Valider_Flux_Zone_Lab]] | — | — | OK | OK | — | OK | OK | OK | WAN simulé, DMZ et LAN isolés; flux positifs et négatifs testés, IPv4/IPv6, aucun raccord production |

**Légende :** `OK` = fonction traitée dans la fiche; `—` = fonction non couverte par cette fiche.

## Propositions pour les prochaines fiches

Les 30 sujets proposés dans les deux derniers lots ont tous été réalisés et figurent dans la matrice ci-dessus. Les prochaines propositions pourront être ajoutées ici après vérification des doublons.
Les 30 sujets proposés dans les deux premiers lots sont réalisés. Les fiches de nouvelles versions sont ajoutées au fur et à mesure après vérification des notes de version officielles.

## Règles de sélection

- Vérifier les fiches existantes et les répertoires `05-Hardening-AIS-Cyber` avant de créer un doublon.
- Garder une tâche principale par fiche et préciser les versions, prérequis, droits et risques de coupure.
- Donner une procédure adaptée aux outils de l'OS : `apk`/OpenRC pour Alpine, APT/systemd pour Debian et Ubuntu, DNF/NetworkManager/SELinux pour Rocky, interface ou PowerShell pour Windows.
- Inclure une validation observable et un retour arrière réaliste; ne pas présenter le contrôle structurel comme un test sur machine réelle.