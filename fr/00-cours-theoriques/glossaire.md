---
title: "Glossaire TSSR et AIS"
description: "Définitions des termes et sigles employés dans les fiches du pack et dans les référentiels de formation TSSR (Technicien Supérieur Systèmes et Réseaux) et AIS (Administrateur d'Infrastructures Sécurisées). Les entrées sont regroupées par domaine, puis classées par ordre alphabétique."
published: true
date: 2026-11-03T10:06:20Z
tags: ["glossaire", "tssr", "ais", "definitions", "reference"]
editor: markdown
dateCreated: 2026-11-03T10:06:20Z
dateModified: 2026-11-03T10:06:20Z
---

# Glossaire TSSR et AIS

- **Tags** : `glossaire`, `tssr`, `ais`, `definitions`, `reference`

Définitions des termes et sigles employés dans les fiches du pack et dans les référentiels de formation TSSR (Technicien Supérieur Systèmes et Réseaux) et AIS (Administrateur d'Infrastructures Sécurisées). Les entrées sont regroupées par domaine, puis classées par ordre alphabétique.

## Sommaire

1. Formation et démarche
2. Réseaux et protocoles
3. Systèmes et virtualisation
4. Matériel et démarrage
5. Stockage, sauvegarde et continuité
6. Identités, annuaires et accès
7. Sécurité et durcissement
8. Supervision, ITSM et exploitation
9. Déploiement, automatisation et services applicatifs
10. Gouvernance et conformité

## 1. Formation et démarche

- **AIS** (Administrateur d'Infrastructures Sécurisées) : titre professionnel de niveau 6 (RNCP37680, ministère du Travail). L'AIS met en œuvre, administre et sécurise les infrastructures locales et cloud, conçoit et met en production des évolutions, déploie la supervision et participe à la gestion de la cybersécurité. Il est responsable du MCO et du MCS et assure un support de niveaux 2 et 3. Trois blocs de compétences : administrer et sécuriser les infrastructures (BC01), concevoir et mettre en œuvre une solution en réponse à un besoin d'évolution (BC02), participer à la gestion de la cybersécurité (BC03).
- **TSSR** (Technicien Supérieur Systèmes et Réseaux) : titre professionnel de niveau 5 (RNCP37682, remplacé par RNCP42463 pour les sessions postérieures à septembre 2026). Le technicien assure le support aux utilisateurs, l'exploitation quotidienne des serveurs Windows et Linux et du réseau IP, la maintenance de l'infrastructure virtualisée, l'automatisation par scripts, les sauvegardes et le déploiement des postes. Deux blocs : exploiter l'infrastructure et assurer le support (BC01), maintenir l'infrastructure et contribuer à son évolution et à sa sécurisation (BC02).
- **RNCP** (Répertoire National des Certifications Professionnelles) : registre public tenu par France compétences qui recense les certifications reconnues par l'État, avec leur niveau de qualification et leurs blocs de compétences.
- **CCP / CCS** (Certificat de Compétences Professionnelles / Certificat Complémentaire de Spécialisation) : blocs de compétences d'un titre professionnel, validés séparément ; les CCS complètent un titre par une spécialisation.
- **MCO** (Maintien en Condition Opérationnelle) : ensemble des actions qui conservent un système en état de fonctionnement (supervision, correctifs, maintenance, support).
- **MCS** (Maintien en Condition de Sécurité) : ensemble des actions qui conservent le niveau de sécurité d'un système dans le temps (correctifs de sécurité, veille sur les vulnérabilités, revue des configurations).
- **PRI / PCI** (Plan de Reprise Informatique / Plan de Continuité Informatique) : déclinaisons informatiques du PRA et du PCA.
- **Support de niveau 1, 2, 3** : organisation du support en paliers ; le niveau 1 enregistre et traite les demandes courantes, le niveau 2 traite les incidents techniques complexes, le niveau 3 mobilise les experts et les éditeurs pour les problèmes de fond.
- **ESN** (Entreprise de Services du Numérique) : société de services informatiques qui intervient chez ses clients en projet ou en infogérance.
- **Infogérance** : externalisation de l'exploitation d'un système d'information à un prestataire, encadrée par un contrat de service.
- **On-premise** : infrastructure hébergée dans les locaux de l'organisation, par opposition au cloud.
- **Cloud public / privé / hybride** : modèle de mise à disposition de ressources informatiques à la demande, chez un fournisseur tiers (public), dédié à une organisation (privé) ou combinant les deux (hybride).
- **IaaS / PaaS / SaaS** (Infrastructure / Platform / Software as a Service) : niveaux de service cloud qui fournissent respectivement l'infrastructure, une plateforme d'exécution ou une application complète.
- **Veille technologique** : surveillance organisée des évolutions techniques, des vulnérabilités et des menaces pour actualiser ses compétences et ses systèmes.
- **CECRL** (Cadre Européen Commun de Référence pour les Langues) : échelle de niveaux de langue de A1 à C2 ; les titres TSSR et AIS exigent le niveau B1 en anglais écrit.
- **RSSI** (Responsable de la Sécurité des Systèmes d'Information) : responsable de la définition et du pilotage de la politique de sécurité du système d'information.
- **RSI** (Responsable des Systèmes d'Information) : responsable de l'exploitation et de l'évolution du système d'information.
- **Fiche simple** : procédure courte et ciblée qui décrit une opération unique (installation, configuration, vérification) avec ses prérequis, ses étapes, ses contrôles et son retour arrière.
- **Fiche complète** : document de référence qui traite un sujet de bout en bout (conception, installation, configuration, exploitation, sécurisation, dépannage).
- **Fiche tout-en-un** : fiche de cours qui regroupe sur une seule page la théorie, les commandes, les pièges courants et les exercices d'un thème.
- **Retour arrière** (rollback) : ensemble d'actions qui rétablit l'état antérieur d'un système après une modification ou un déploiement échoué.
- **POC** (Proof of Concept, preuve de concept) : réalisation limitée et jetable qui démontre la faisabilité d'une solution sans modifier la production.
- **Production** : environnement qui supporte l'activité réelle des utilisateurs, par opposition aux environnements de test, de recette ou de laboratoire.
- **Laboratoire** (lab) : environnement isolé de la production, utilisé pour s'entraîner, tester ou valider une procédure.
- **Prérequis** : conditions techniques et organisationnelles à réunir avant d'exécuter une procédure.
- **Runbook** : procédure d'exploitation documentée et rejouable, utilisée pour traiter un incident ou une opération courante.

## 2. Réseaux et protocoles

- **AAAA (enregistrement)** : enregistrement DNS qui associe un nom à une adresse IPv6.
- **A (enregistrement)** : enregistrement DNS qui associe un nom à une adresse IPv4.
- **ARP** (Address Resolution Protocol) : protocole qui associe une adresse IPv4 à l'adresse MAC correspondante sur un segment de niveau 2.
- **BIND** (Berkeley Internet Name Domain) : serveur DNS libre de référence, utilisé pour l'autorité de zones et la résolution récursive.
- **CARP** (Common Address Redundancy Protocol) : protocole libre de redondance d'adresse IP virtuelle entre pare-feu, utilisé notamment par OPNsense et pfSense.
- **CIDR** (Classless Inter-Domain Routing) : notation qui exprime un réseau IP par son adresse et la longueur de son préfixe, par exemple `192.168.10.0/24`.
- **CNAME** : enregistrement DNS qui définit un alias vers un autre nom canonique.
- **DHCP** (Dynamic Host Configuration Protocol) : protocole qui attribue automatiquement une configuration IP (adresse, masque, passerelle, DNS) aux clients d'un réseau.
- **DMZ** (zone démilitarisée) : segment réseau intermédiaire, isolé du réseau interne et d'Internet, qui héberge les services exposés.
- **DNS** (Domain Name System) : service distribué qui traduit des noms de domaine en adresses IP et publie d'autres informations de zone.
- **DNSSEC** (DNS Security Extensions) : extensions qui signent cryptographiquement les réponses DNS afin d'en garantir l'authenticité et l'intégrité.
- **FQDN** (Fully Qualified Domain Name) : nom de domaine complet qui désigne sans ambiguïté un hôte, par exemple `srv01.exemple.local`.
- **FTP** (File Transfer Protocol) : protocole historique de transfert de fichiers, sans chiffrement natif.
- **HSTS** (HTTP Strict Transport Security) : en-tête HTTP qui impose au navigateur l'usage exclusif de HTTPS pour un site.
- **HTTP / HTTPS** (HyperText Transfer Protocol / Secure) : protocole applicatif du web ; HTTPS l'encapsule dans une session TLS.
- **ICMP** (Internet Control Message Protocol) : protocole de diagnostic et de contrôle de la couche IP, utilisé par `ping` et `traceroute`.
- **IMAP / IMAPS** (Internet Message Access Protocol) : protocole d'accès à une boîte aux lettres qui laisse les messages sur le serveur ; IMAPS le protège par TLS.
- **IP** (Internet Protocol) : protocole de la couche réseau qui adresse et achemine les paquets.
- **IPAM** (IP Address Management) : outil ou processus de planification et de suivi des plans d'adressage, des sous-réseaux et des adresses affectées.
- **IPv4 / IPv6** : versions du protocole IP, respectivement sur 32 et 128 bits.
- **LAN** (Local Area Network) : réseau local couvrant un site restreint.
- **LDAP / LDAPS** : voir la section Identités, annuaires et accès.
- **MAC (adresse)** (Media Access Control) : identifiant de 48 bits d'une interface réseau, utilisé au niveau 2.
- **MTU** (Maximum Transmission Unit) : taille maximale, en octets, d'une trame ou d'un paquet transmissible sans fragmentation sur un lien.
- **MX (enregistrement)** : enregistrement DNS qui désigne les serveurs de messagerie d'un domaine et leur priorité.
- **NAT** (Network Address Translation) : traduction d'adresses IP, utilisée pour partager une adresse publique ou publier un service interne.
- **NTP** (Network Time Protocol) : protocole de synchronisation de l'horloge des systèmes sur une source de temps de référence.
- **OSI (modèle)** : modèle de référence en sept couches (physique, liaison, réseau, transport, session, présentation, application) qui structure l'analyse des communications réseau.
- **PTR (enregistrement)** : enregistrement DNS de résolution inverse, qui associe une adresse IP à un nom.
- **PXE** (Preboot Execution Environment) : mécanisme de démarrage par le réseau, utilisé pour déployer des systèmes.
- **RADIUS** (Remote Authentication Dial-In User Service) : protocole d'authentification, d'autorisation et de traçabilité des accès réseau (Wi-Fi 802.1X, VPN).
- **SMTP** (Simple Mail Transfer Protocol) : protocole d'envoi et de relais des courriers électroniques.
- **SNMP** (Simple Network Management Protocol) : protocole de supervision et d'administration d'équipements réseau par interrogation (get) ou notification (trap).
- **SPAN** (Switched Port Analyzer) : duplication du trafic d'un ou plusieurs ports d'un commutateur vers un port d'analyse.
- **SSH** (Secure Shell) : protocole d'administration à distance chiffré, qui authentifie par mot de passe ou par clé.
- **STP** (Spanning Tree Protocol) : protocole de niveau 2 qui évite les boucles dans un réseau commuté redondant.
- **TCP** (Transmission Control Protocol) : protocole de transport orienté connexion, fiable et ordonné.
- **TFTP** (Trivial File Transfer Protocol) : protocole simplifié de transfert de fichiers, employé pour le démarrage PXE et la configuration d'équipements.
- **TLS** (Transport Layer Security) : protocole qui chiffre et authentifie les échanges réseau ; successeur de SSL.
- **TTL** (Time To Live) : durée de vie d'un paquet IP (nombre de sauts) ou d'une réponse DNS en cache (secondes).
- **TXT (enregistrement)** : enregistrement DNS de texte libre, utilisé notamment pour SPF, DKIM et DMARC.
- **UDP** (User Datagram Protocol) : protocole de transport sans connexion, léger et sans garantie de livraison.
- **VIP** (Virtual IP) : adresse IP flottante partagée entre plusieurs nœuds et portée par celui qui est actif.
- **VLAN** (Virtual LAN) : segmentation logique d'un réseau de niveau 2, identifiée par une étiquette 802.1Q.
- **VPN** (Virtual Private Network) : tunnel chiffré qui relie des postes ou des sites à travers un réseau non maîtrisé.
- **VRRP** (Virtual Router Redundancy Protocol) : protocole de redondance de passerelle par adresse IP virtuelle.
- **WAN** (Wide Area Network) : réseau étendu qui relie des sites distants ou donne accès à Internet.
- **WireGuard** : protocole VPN moderne, léger, fondé sur des clés publiques et une cryptographie récente.
- **802.1X** : norme de contrôle d'accès au réseau par port, qui authentifie un équipement ou un utilisateur (via RADIUS) avant de l'autoriser à communiquer.
- **Agrégation de liens (LACP)** : regroupement de plusieurs liens physiques en un lien logique pour la bande passante et la redondance (norme 802.3ad).
- **BGP** (Border Gateway Protocol) : protocole de routage entre systèmes autonomes, fondement du routage sur Internet.
- **Commutateur (switch)** : équipement de niveau 2 qui transfère les trames selon la table d'adresses MAC.
- **Dual stack** : exploitation simultanée d'IPv4 et d'IPv6 sur un même réseau.
- **EVE-NG / GNS3** : plateformes d'émulation de réseaux qui exécutent des images d'équipements réels pour simuler des topologies en laboratoire.
- **IPsec** : suite de protocoles qui authentifie et chiffre le trafic IP, utilisée pour les VPN de site à site et d'accès distant.
- **Load balancer (répartiteur de charge)** : équipement ou service qui distribue les requêtes entre plusieurs serveurs.
- **NAT / PAT** : le PAT (Port Address Translation) traduit aussi les ports pour partager une adresse publique entre plusieurs hôtes.
- **OpenVPN** : solution VPN libre fondée sur TLS.
- **OSPF** (Open Shortest Path First) : protocole de routage dynamique à état de liens, utilisé à l'intérieur d'un système autonome.
- **QoS** (Quality of Service) : mécanismes qui priorisent certains flux pour garantir un niveau de service.
- **Routage statique / dynamique** : définition manuelle des routes, ou apprentissage automatique par un protocole de routage.
- **Sous-réseau (subnet)** : portion d'un réseau IP définie par un masque ou un préfixe.
- **Trunk** : lien qui transporte plusieurs VLAN grâce à l'étiquetage 802.1Q.
- **VLSM** (Variable Length Subnet Mask) : découpage d'un réseau en sous-réseaux de tailles différentes.
- **WLAN / Wi-Fi** : réseau local sans fil, normalisé IEEE 802.11 ; WPA2 et WPA3 en sont les protocoles de sécurité.
- **Zone DNS (directe / inverse)** : base d'enregistrements d'un domaine, qui résout les noms en adresses (directe) ou les adresses en noms (inverse).

## 3. Systèmes et virtualisation

- **AHV** (Acropolis Hypervisor) : hyperviseur KVM de la plateforme Nutanix.
- **Alpine Linux** : distribution Linux minimale, fondée sur musl libc et BusyBox, très utilisée pour les conteneurs et les systèmes légers.
- **APK** (Alpine Package Keeper) : gestionnaire de paquets d'Alpine Linux.
- **APT** (Advanced Package Tool) : gestionnaire de paquets des familles Debian et Ubuntu.
- **BSD** (Berkeley Software Distribution) : famille de systèmes Unix libres (FreeBSD, OpenBSD) et licence permissive associée ; base d'OPNsense, de pfSense et de TrueNAS CORE.
- **Cgroups** : mécanisme du noyau Linux qui limite et comptabilise les ressources (processeur, mémoire, entrées-sorties) d'un groupe de processus.
- **CLI** (Command-Line Interface) : interface d'administration en ligne de commande.
- **Conteneur** : unité d'exécution isolée qui partage le noyau de l'hôte et embarque une application avec ses dépendances.
- **Core (installation Server Core)** : mode d'installation minimal de Windows Server, sans interface graphique complète.
- **CT / CTID** (Container / Container ID) : conteneur LXC et son identifiant numérique dans Proxmox VE.
- **Debian** : distribution Linux communautaire réputée pour sa stabilité ; base d'Ubuntu et de Proxmox VE.
- **DNF** (Dandified YUM) : gestionnaire de paquets des familles Red Hat (RHEL, Rocky Linux).
- **Docker** : plateforme de création et d'exécution de conteneurs à partir d'images.
- **Docker Compose** : outil qui décrit et pilote une application multi-conteneurs à partir d'un fichier YAML.
- **EOL** (End Of Life) : fin de vie d'un produit, après laquelle il ne reçoit plus de correctifs.
- **ESU** (Extended Security Updates) : mises à jour de sécurité étendues, payantes, proposées après la fin du support standard.
- **ESXi** : hyperviseur de type 1 de VMware.
- **GUI** (Graphical User Interface) : interface graphique d'administration.
- **Hyperviseur** : logiciel qui crée et exécute des machines virtuelles ; de type 1 (directement sur le matériel) ou de type 2 (sur un système hôte).
- **Hyper-V** : hyperviseur de type 1 de Microsoft intégré à Windows Server.
- **IIS** (Internet Information Services) : serveur web et d'applications de Windows Server.
- **ISO (image)** : fichier image d'un disque optique, utilisé pour installer un système.
- **Kubernetes (K8s)** : orchestrateur de conteneurs qui automatise le déploiement, la mise à l'échelle et la reprise des applications.
- **K3s** : distribution Kubernetes légère, adaptée aux petites infrastructures et à la périphérie.
- **KVM** (Kernel-based Virtual Machine) : module de virtualisation du noyau Linux ; avec QEMU, il fournit l'hyperviseur de Proxmox VE.
- **LEMP** : pile web composée de Linux, Nginx (« Engine X »), MariaDB ou MySQL et PHP.
- **LTS** (Long Term Support) : version à support prolongé d'un logiciel ou d'un système.
- **LVM / LVM2** (Logical Volume Manager) : couche de gestion de volumes logiques qui permet de redimensionner et d'agréger des disques.
- **LXC** (Linux Containers) : technologie de conteneurs système Linux, utilisée par Proxmox VE.
- **Nginx** : serveur web et proxy inverse hautes performances.
- **OPNsense / pfSense** : distributions de pare-feu et de routage fondées sur FreeBSD.
- **OVMF** (Open Virtual Machine Firmware) : micrologiciel UEFI libre pour les machines virtuelles.
- **PHP-FPM** (FastCGI Process Manager) : gestionnaire de processus PHP, associé à un serveur web.
- **Proxmox VE** (Virtual Environment) : plateforme libre de virtualisation qui combine KVM, LXC, stockage et haute disponibilité.
- **QEMU** : émulateur et virtualiseur qui fournit les périphériques des machines virtuelles KVM.
- **RHEL** (Red Hat Enterprise Linux) : distribution Linux commerciale de Red Hat ; Rocky Linux en est un dérivé compatible.
- **Rocky Linux** : distribution communautaire compatible RHEL, successeur de CentOS.
- **RPM** (RPM Package Manager) : format de paquets des familles Red Hat.
- **Snapshot** (instantané) : capture de l'état d'une machine virtuelle ou d'un volume à un instant donné, qui permet un retour rapide.
- **systemd** : gestionnaire de système et de services de la plupart des distributions Linux.
- **Template (modèle)** : machine virtuelle ou conteneur préparé qui sert de base de clonage.
- **Ubuntu** : distribution Linux dérivée de Debian, publiée avec des versions LTS tous les deux ans.
- **UFW** (Uncomplicated Firewall) : interface simplifiée de configuration du pare-feu Netfilter sous Linux.
- **VM** (Virtual Machine) : machine virtuelle, qui émule un ordinateur complet exécuté par un hyperviseur.
- **VMID** : identifiant numérique unique d'une machine virtuelle dans Proxmox VE.
- **vSphere / vCenter (VCSA)** : suite de virtualisation VMware et serveur de gestion centralisée (vCenter Server Appliance).
- **WSL** (Windows Subsystem for Linux) : couche de compatibilité qui exécute un environnement Linux dans Windows.
- **Cluster** : groupe de serveurs qui fonctionnent de concert pour assurer la haute disponibilité ou la répartition de charge.
- **DRS** (Distributed Resource Scheduler) : fonction VMware qui répartit automatiquement les machines virtuelles entre les hôtes d'un cluster.
- **Live migration (vMotion)** : déplacement d'une machine virtuelle en fonctionnement d'un hôte à un autre sans interruption.
- **Hyper-V (rôle) / Failover Cluster** : cluster de basculement Windows Server, qui redémarre les machines virtuelles sur un autre nœud en cas de panne.
- **Overcommit** : allocation de plus de ressources virtuelles (processeur, mémoire) que l'hôte n'en possède physiquement.
- **Pare-feu de zone** : filtrage fondé sur des zones de confiance (LAN, WAN, DMZ) plutôt que sur des interfaces isolées.
- **Registre Windows (Registry)** : base hiérarchique de configuration de Windows ; `HKLM` désigne la ruche de la machine locale.
- **Service Windows / daemon** : processus d'arrière-plan démarré par le système, sans session utilisateur.
- **Sysprep** : outil Microsoft qui généralise une installation Windows avant de la capturer comme modèle.
- **VDI** (Virtual Desktop Infrastructure) : infrastructure de bureaux virtuels hébergés sur des serveurs et accessibles à distance.
- **WinRM** (Windows Remote Management) : service d'administration à distance de Windows fondé sur WS-Management, utilisé par PowerShell Remoting.
- **WMI** (Windows Management Instrumentation) : interface d'administration et de collecte d'informations système de Windows.
- **chmod / chown** : commandes Linux qui modifient les droits d'accès et le propriétaire d'un fichier.
- **Droits POSIX** : modèle Unix de permissions lecture, écriture, exécution pour le propriétaire, le groupe et les autres.
- **FHS** (Filesystem Hierarchy Standard) : norme d'organisation des répertoires des systèmes Linux (`/etc`, `/var`, `/usr`).
- **Image de conteneur / registre** : modèle immuable d'un conteneur et dépôt qui le stocke et le distribue (Docker Hub, registre privé).
- **Inode** : structure d'un système de fichiers Unix qui décrit un fichier (droits, taille, emplacement des données).
- **journalctl** : commande de consultation des journaux collectés par systemd-journald.
- **Namespaces** : mécanisme du noyau Linux qui isole la vue d'un processus (processus, réseau, montages, utilisateurs).
- **PID** (Process ID) : identifiant numérique d'un processus.
- **Pool de stockage / datastore** : espace de stockage logique déclaré dans un hyperviseur ou un système de stockage.
- **Sudo / sudoers** : mécanisme qui délègue des droits administrateurs à un utilisateur selon une politique.
- **SUID / SGID** : bits de permission qui font exécuter un programme avec les droits de son propriétaire ou groupe.
- **Swap** : espace disque qui complète la mémoire vive.
- **Volume (conteneur)** : espace persistant monté dans un conteneur pour conserver des données hors de sa couche éphémère.

## 4. Matériel et démarrage

- **AHCI** (Advanced Host Controller Interface) : interface standard de contrôleur SATA.
- **AMD64 / x86-64** : architecture 64 bits des processeurs Intel et AMD.
- **ARM64 (AArch64)** : architecture 64 bits ARM.
- **BIOS** (Basic Input/Output System) : micrologiciel de démarrage historique, remplacé par UEFI.
- **BMC** (Baseboard Management Controller) : contrôleur matériel qui permet l'administration à distance d'un serveur hors système.
- **CMOS** : mémoire du firmware qui conserve les paramètres matériels ; par extension, sa réinitialisation.
- **CPU / vCPU** (Central Processing Unit / virtual CPU) : processeur, et cœur virtuel alloué à une machine virtuelle.
- **EFI / UEFI** (Unified Extensible Firmware Interface) : micrologiciel moderne de démarrage qui prend en charge GPT, le démarrage sécurisé et les disques volumineux.
- **GPT** (GUID Partition Table) : schéma de partitionnement moderne qui remplace MBR.
- **GRUB / GRUB2** : chargeur d'amorçage standard des systèmes Linux.
- **HBA** (Host Bus Adapter) : carte qui relie un serveur à un bus de stockage (SAS, Fibre Channel).
- **IPMI** (Intelligent Platform Management Interface) : interface de gestion matérielle à distance (alimentation, capteurs, console).
- **iDRAC / iLO** : contrôleurs BMC des serveurs Dell et HPE.
- **MBR** (Master Boot Record) : schéma de partitionnement historique, limité à 2 To.
- **NIC** (Network Interface Card) : carte d'interface réseau.
- **NVMe** (Non-Volatile Memory Express) : protocole d'accès aux SSD sur bus PCIe.
- **OEM** (Original Equipment Manufacturer) : licence ou image fournie par le constructeur du matériel.
- **PCIe** : bus d'extension haut débit des ordinateurs.
- **RAID** (Redundant Array of Independent Disks) : regroupement de disques pour améliorer la tolérance aux pannes ou les performances (niveaux 0, 1, 5, 6, 10).
- **RAM** (Random Access Memory) : mémoire vive.
- **SATA / SAS / SCSI** : interfaces de connexion de disques ; SAS est la version série de SCSI, destinée aux serveurs.
- **SMART** (Self-Monitoring, Analysis and Reporting Technology) : mécanisme d'auto-diagnostic des disques.
- **SSD** (Solid-State Drive) : disque à mémoire flash, sans pièce mécanique.
- **TPM** (Trusted Platform Module) : composant de sécurité qui stocke des clés et atteste de l'intégrité du démarrage.
- **Secure Boot** : fonction UEFI qui n'exécute que des chargeurs d'amorçage signés.
- **USB** (Universal Serial Bus) : bus standard de périphériques externes.
- **VT-x / AMD-V** : extensions processeur d'assistance à la virtualisation.

## 5. Stockage, sauvegarde et continuité

- **3-2-1 (règle)** : bonne pratique de sauvegarde qui impose trois copies des données, sur deux supports différents, dont une hors site.
- **CIFS / SMB** (Common Internet File System / Server Message Block) : protocole de partage de fichiers de Windows ; CIFS désigne une ancienne variante de SMB.
- **Déduplication** : technique qui supprime les blocs de données identiques afin de réduire l'espace occupé.
- **DRP / PRA** (Disaster Recovery Plan / Plan de Reprise d'Activité) : plan qui décrit comment rétablir les services après un sinistre majeur.
- **BCP / PCA** (Business Continuity Plan / Plan de Continuité d'Activité) : plan qui maintient l'activité essentielle pendant une perturbation.
- **Haute disponibilité (HA)** : architecture redondante qui limite l'interruption de service lors de la panne d'un composant.
- **iSCSI** : protocole qui transporte des commandes SCSI sur TCP/IP pour exposer des volumes de stockage en réseau.
- **IOPS** (Input/Output Operations Per Second) : nombre d'opérations d'entrée-sortie par seconde, mesure de performance d'un stockage.
- **LUN** (Logical Unit Number) : volume logique présenté par une baie de stockage à un ou plusieurs serveurs.
- **NAS** (Network Attached Storage) : serveur de fichiers dédié, accessible par le réseau (SMB, NFS).
- **NFS** (Network File System) : protocole de partage de fichiers des systèmes Unix et Linux.
- **NTFS** (New Technology File System) : système de fichiers de Windows, avec droits, journalisation et chiffrement.
- **PBS** (Proxmox Backup Server) : serveur de sauvegarde incrémentale et dédupliquée pour Proxmox VE.
- **Quorum** : nombre minimal de nœuds qui doivent être d'accord pour qu'un cluster fonctionne et évite le « split-brain ».
- **RPO** (Recovery Point Objective) : perte de données maximale tolérée, exprimée en durée.
- **RTO** (Recovery Time Objective) : durée maximale tolérée d'interruption avant la reprise du service.
- **SAN** (Storage Area Network) : réseau dédié qui expose du stockage en mode bloc.
- **Sauvegarde complète / incrémentale / différentielle** : sauvegarde de toutes les données, des seules modifications depuis la dernière sauvegarde, ou depuis la dernière complète.
- **Scrub** : vérification périodique de l'intégrité des données d'un pool ZFS.
- **VSS** (Volume Shadow Copy Service) : service Windows qui produit des copies cohérentes de volumes en cours d'utilisation.
- **XFS** : système de fichiers journalisé hautes performances, par défaut sous RHEL.
- **ZFS** : système de fichiers et gestionnaire de volumes avec sommes de contrôle, instantanés, réplication et RAID logiciel intégrés.
- **TrueNAS (CORE / SCALE)** : système de stockage fondé sur ZFS ; CORE repose sur FreeBSD et SCALE sur Debian.
- **Bloc / fichier / objet** : trois modes d'accès au stockage ; le mode bloc expose des volumes bruts, le mode fichier des arborescences (SMB, NFS), le mode objet des données adressées par identifiant (S3).
- **Chiffrement au repos / en transit** : protection des données stockées sur un support, ou pendant leur transmission.
- **Quota** : limite d'espace attribuée à un utilisateur, un groupe ou un volume.
- **Réplication** : copie continue ou périodique de données vers un autre système pour la reprise après sinistre.
- **Rétention** : durée de conservation d'une sauvegarde avant sa suppression.
- **Test de restauration** : vérification régulière qu'une sauvegarde est exploitable ; une sauvegarde non testée n'est pas garantie.
- **Thin / thick provisioning** : allocation d'un volume à la demande (thin) ou entièrement réservée dès la création (thick).

## 6. Identités, annuaires et accès

- **AD / AD DS** (Active Directory / Domain Services) : service d'annuaire de Microsoft qui centralise utilisateurs, ordinateurs, groupes et stratégies d'un domaine.
- **ADK** (Assessment and Deployment Kit) : outils de Microsoft pour personnaliser et déployer Windows.
- **AGDLP** (Account, Global, Domain Local, Permission) : modèle d'affectation de droits qui place les comptes dans des groupes globaux, eux-mêmes membres de groupes de domaine local qui portent les permissions.
- **ACL** (Access Control List) : liste de règles qui précise qui peut accéder à une ressource et avec quels droits.
- **Authentification** : vérification de l'identité d'un utilisateur ou d'un système.
- **Autorisation** : détermination des droits d'une identité authentifiée.
- **DC** (Domain Controller) : serveur qui héberge l'annuaire Active Directory et authentifie les accès du domaine.
- **DN** (Distinguished Name) : nom unique d'un objet dans un annuaire LDAP.
- **DSRM** (Directory Services Restore Mode) : mode de démarrage d'un contrôleur de domaine pour la restauration de l'annuaire.
- **FIDO2** : standard d'authentification forte sans mot de passe, fondé sur des clés matérielles ou des passkeys.
- **FSMO** (Flexible Single Master Operations) : rôles uniques d'un domaine Active Directory (maître de schéma, maître d'attribution de noms, émulateur PDC, maître RID, maître d'infrastructure).
- **GID / UID** (Group ID / User ID) : identifiants numériques d'un groupe et d'un utilisateur sous Unix et Linux.
- **GPO** (Group Policy Object) : objet de stratégie de groupe qui applique des paramètres de configuration et de sécurité aux utilisateurs et ordinateurs d'un domaine.
- **IAM** (Identity and Access Management) : gestion des identités et des accès.
- **Kerberos** : protocole d'authentification par tickets, utilisé par Active Directory.
- **LAPS** (Local Administrator Password Solution) : solution qui génère et fait tourner un mot de passe d'administrateur local unique par machine.
- **LDAP / LDAPS** (Lightweight Directory Access Protocol) : protocole d'interrogation et de mise à jour d'annuaires ; LDAPS le protège par TLS.
- **MFA** (Multi-Factor Authentication) : authentification qui exige au moins deux facteurs de natures différentes (connaissance, possession, inhérence).
- **NLA** (Network Level Authentication) : authentification préalable à l'ouverture d'une session RDP.
- **NTLM** : ancien protocole d'authentification Windows par challenge-réponse, supplanté par Kerberos.
- **OIDC** (OpenID Connect) : couche d'identité au-dessus d'OAuth 2.0 pour l'authentification unique.
- **OU** (Organizational Unit) : conteneur d'un annuaire qui regroupe des objets et sur lequel on applique des GPO ou une délégation.
- **PAM** : selon le contexte, Pluggable Authentication Modules (Linux) ou Privileged Access Management (gestion des accès à privilèges).
- **RBAC** (Role-Based Access Control) : contrôle d'accès fondé sur des rôles.
- **RDP / RDS** (Remote Desktop Protocol / Services) : protocole et services de bureau à distance de Windows.
- **SAML** (Security Assertion Markup Language) : standard d'échange d'assertions d'authentification pour l'authentification unique.
- **SID** (Security Identifier) : identifiant unique d'un compte ou d'un groupe de sécurité Windows.
- **SSO** (Single Sign-On) : authentification unique, qui donne accès à plusieurs applications après une seule connexion.
- **SSSD** (System Security Services Daemon) : service Linux qui relie le système à des annuaires distants (AD, LDAP, FreeIPA).
- **SYSVOL** : dossier partagé des contrôleurs de domaine, qui contient les stratégies de groupe et les scripts.
- **TOTP** (Time-based One-Time Password) : mot de passe à usage unique dérivé de l'heure, utilisé en MFA.
- **UAC** (User Account Control) : mécanisme de Windows qui demande une élévation pour les actions administratives.
- **Compte de service** : compte non interactif dédié à l'exécution d'une application ou d'un service.
- **Contrôleur de domaine en lecture seule (RODC)** : contrôleur de domaine qui ne réplique l'annuaire qu'en lecture, destiné aux sites peu sûrs.
- **Forêt / domaine / arbre** : structures logiques d'Active Directory ; la forêt regroupe un ou plusieurs domaines qui partagent un schéma.
- **Relation d'approbation (trust)** : lien qui permet aux utilisateurs d'un domaine d'accéder aux ressources d'un autre.
- **Schéma (annuaire)** : définition des classes d'objets et attributs possibles dans un annuaire.
- **Tiering (modèle en niveaux)** : segmentation des comptes et postes d'administration en niveaux pour empêcher le vol d'identifiants privilégiés.

## 7. Sécurité et durcissement

- **ACME** (Automatic Certificate Management Environment) : protocole d'obtention et de renouvellement automatiques de certificats (Let's Encrypt).
- **AES** (Advanced Encryption Standard) : algorithme de chiffrement symétrique par blocs, standard actuel.
- **ANSSI** (Agence nationale de la sécurité des systèmes d'information) : autorité française de cybersécurité, qui publie guides et référentiels.
- **CA** (Certificate Authority) : autorité de certification qui émet et signe les certificats.
- **CIS Benchmarks** : guides de configuration sécurisée publiés par le Center for Internet Security.
- **CRL** (Certificate Revocation List) : liste des certificats révoqués avant leur expiration.
- **CVE** (Common Vulnerabilities and Exposures) : identifiant normalisé d'une vulnérabilité connue, par exemple `CVE-2024-3094`.
- **CVSS** (Common Vulnerability Scoring System) : échelle de 0 à 10 qui note la gravité d'une vulnérabilité.
- **DKIM** (DomainKeys Identified Mail) : signature cryptographique des messages qui authentifie le domaine émetteur.
- **DMARC** (Domain-based Message Authentication, Reporting and Conformance) : politique qui précise le traitement des messages dont SPF ou DKIM échoue.
- **ED25519** : algorithme de signature à courbe elliptique, recommandé pour les clés SSH.
- **Fail2ban** : outil qui bannit temporairement les adresses sources après des échecs d'authentification répétés.
- **Durcissement** (hardening) : réduction de la surface d'attaque d'un système par configuration restrictive, suppression du superflu et application de correctifs.
- **GPG** (GNU Privacy Guard) : implémentation libre d'OpenPGP pour le chiffrement et la signature.
- **Hachage** : fonction à sens unique qui produit une empreinte de taille fixe, utilisée pour vérifier l'intégrité et stocker des mots de passe.
- **IDS / IPS** (Intrusion Detection / Prevention System) : système qui détecte, ou détecte et bloque, les activités malveillantes.
- **MITRE ATT&CK** : base de connaissances des tactiques et techniques d'attaque observées.
- **Moindre privilège** : principe qui n'accorde que les droits strictement nécessaires.
- **NIST** (National Institute of Standards and Technology) : organisme américain de normalisation, auteur de référentiels de cybersécurité.
- **Pare-feu** (firewall) : équipement ou logiciel qui filtre les flux selon des règles.
- **PKI** (Public Key Infrastructure) : infrastructure à clés publiques qui gère l'émission, la distribution et la révocation de certificats.
- **RSA** : algorithme de cryptographie asymétrique fondé sur la factorisation de grands entiers.
- **SELinux / AppArmor** : modules de contrôle d'accès obligatoire du noyau Linux.
- **SHA-256** (Secure Hash Algorithm) : fonction de hachage de 256 bits.
- **SIEM** (Security Information and Event Management) : plateforme qui centralise, corrèle et analyse les journaux pour détecter les incidents.
- **SPF** (Sender Policy Framework) : enregistrement DNS qui liste les serveurs autorisés à envoyer du courrier pour un domaine.
- **SSL** (Secure Sockets Layer) : ancêtre de TLS, obsolète.
- **STARTTLS** : commande qui bascule une connexion en clair vers TLS (SMTP, IMAP).
- **Surface d'attaque** : ensemble des points par lesquels un attaquant peut tenter d'accéder à un système.
- **WDAC** (Windows Defender Application Control) : fonction de Windows qui limite l'exécution aux applications et pilotes approuvés.
- **Vulnérabilité** : faiblesse d'un système exploitable pour compromettre la confidentialité, l'intégrité ou la disponibilité.
- **WAF** (Web Application Firewall) : pare-feu applicatif qui filtre le trafic HTTP.
- **XDR** (Extended Detection and Response) : détection et réponse étendues à plusieurs sources (postes, réseau, messagerie, cloud).
- **Zero trust** (confiance zéro) : modèle de sécurité qui vérifie chaque accès sans considérer le réseau interne comme sûr.
- **Analyse de risques** : démarche qui identifie les menaces, les vulnérabilités et les impacts pour prioriser les mesures de sécurité.
- **Bastion** : serveur d'administration durci, point de passage unique et tracé vers les ressources sensibles.
- **CERT / CSIRT** : équipe de réponse aux incidents de sécurité ; le CERT-FR est celui de l'ANSSI.
- **Chiffrement symétrique / asymétrique** : méthode qui utilise la même clé pour chiffrer et déchiffrer, ou une paire de clés publique et privée.
- **Cyber Kill Chain** : modèle qui décrit les étapes d'une attaque, de la reconnaissance à l'action sur l'objectif.
- **EBIOS Risk Manager** : méthode d'analyse de risques numériques publiée par l'ANSSI.
- **Hygiène informatique** : règles de base de sécurité formalisées par l'ANSSI dans son guide des bonnes pratiques.
- **Journaux d'audit** : traces des accès et des actions, conservées pour l'investigation et la conformité.
- **Pentest** (test d'intrusion) : simulation d'attaque autorisée pour évaluer la sécurité d'un système.
- **Phishing** (hameçonnage) : tentative de tromper un utilisateur par un message frauduleux pour obtenir des identifiants ou lui faire exécuter une action.
- **Ransomware** (rançongiciel) : logiciel malveillant qui chiffre les données et exige une rançon.
- **SecNumCloud** : qualification de l'ANSSI pour les services de cloud de confiance.
- **Segmentation réseau** : découpage du réseau en zones isolées pour limiter la propagation d'une attaque.
- **SOC** (Security Operations Center) : centre qui surveille, détecte et traite les événements de sécurité.
- **Sel (salt)** : valeur aléatoire ajoutée à un mot de passe avant hachage pour éviter les attaques par tables précalculées.
- **Sandbox (bac à sable)** : environnement isolé pour exécuter ou analyser du code non fiable.
- **Shadow IT** : usage de services ou de matériels informatiques sans validation de la DSI.
- **WEF** (Windows Event Forwarding) : mécanisme de collecte centralisée des événements Windows.

## 8. Supervision, ITSM et exploitation

- **CMDB** (Configuration Management Database) : base qui recense les éléments de configuration du système d'information (CI) et leurs relations.
- **DCIM** (Data Center Infrastructure Management) : gestion de l'infrastructure physique d'un centre de données (baies, énergie, câblage).
- **ELK** (Elasticsearch, Logstash, Kibana) : pile de collecte, d'indexation et de visualisation de journaux.
- **GLPI** (Gestion Libre de Parc Informatique) : application libre de gestion de parc et de service d'assistance.
- **Helpdesk** : service d'assistance qui reçoit et traite les demandes et incidents des utilisateurs.
- **Incident** : interruption ou dégradation non planifiée d'un service.
- **Inventaire** : relevé du matériel et des logiciels d'un parc, manuel ou automatisé.
- **ITIL** (Information Technology Infrastructure Library) : référentiel de bonnes pratiques de gestion des services informatiques.
- **ITSM** (IT Service Management) : gestion des services informatiques selon une approche processus.
- **Journalisation** (logging) : enregistrement horodaté des événements d'un système.
- **Journald / syslog** : mécanismes de collecte des journaux sous Linux ; syslog est aussi un protocole de transmission.
- **MTTR** (Mean Time To Repair) : durée moyenne de rétablissement d'un service après une panne.
- **OCS Inventory** : outil libre d'inventaire matériel et logiciel.
- **PRTG** : sonde de supervision commerciale de Paessler, fondée sur des capteurs.
- **Problème** : cause sous-jacente d'un ou plusieurs incidents, traitée par une analyse de cause racine.
- **SLA** (Service Level Agreement) : accord de niveau de service qui fixe des engagements de disponibilité et de délai.
- **Supervision** : surveillance continue de l'état et de la performance des systèmes, avec alertes.
- **Ticket** : enregistrement d'une demande ou d'un incident dans un outil ITSM.
- **Zabbix / Nagios / Centreon** : outils libres de supervision.
- **Alerte** : notification émise quand un indicateur franchit un seuil défini.
- **Baseline (référence)** : niveau normal de performance ou de configuration, auquel on compare les mesures.
- **Disponibilité** : proportion du temps pendant laquelle un service est utilisable, souvent exprimée en pourcentage (99,9 %).
- **KPI** (Key Performance Indicator) : indicateur clé de performance qui mesure l'atteinte d'un objectif.
- **Gestion des actifs (asset management)** : suivi du cycle de vie des matériels et logiciels, de l'acquisition à la mise au rebut.
- **Gestion des problèmes / des changements / des configurations** : processus ITIL qui traitent respectivement les causes d'incidents, les évolutions planifiées et la tenue de la CMDB.
- **Prometheus / Grafana** : outils de collecte de métriques et de tableaux de bord.
- **Sonde (probe)** : composant qui mesure l'état d'un équipement ou d'un service.
- **SLO / SLI** (Service Level Objective / Indicator) : objectif visé et indicateur mesuré qui sert à le vérifier.
- **Astreinte** : période pendant laquelle un technicien doit pouvoir intervenir à distance ou sur site en dehors des heures de travail.

## 9. Déploiement, automatisation et services applicatifs

- **Ansible** : outil d'automatisation sans agent, qui décrit l'état souhaité en playbooks YAML exécutés par SSH.
- **API** (Application Programming Interface) : interface qui permet à des programmes d'échanger des données et d'invoquer des fonctions.
- **Bash** : interpréteur de commandes et langage de script standard des systèmes Linux.
- **CI/CD** (Continuous Integration / Continuous Delivery) : chaîne d'intégration et de livraison continues, qui automatise tests et déploiements.
- **Cloud-init** : outil d'initialisation de machines virtuelles au premier démarrage à partir de métadonnées.
- **Cron** : planificateur de tâches périodiques sous Unix et Linux.
- **Dockerfile** : fichier de description de la construction d'une image de conteneur.
- **Git** : système de gestion de versions décentralisé.
- **HCL / HCL2** (HashiCorp Configuration Language) : langage de configuration de Terraform et de Packer.
- **Idempotence** : propriété d'une opération qui produit le même résultat quand elle est exécutée plusieurs fois.
- **Infrastructure as Code (IaC)** : gestion de l'infrastructure par des fichiers versionnés plutôt que par des actions manuelles.
- **JSON / YAML / XML / CSV** : formats d'échange et de configuration de données structurées ou tabulaires.
- **MDT / WDS / MECM (SCCM)** : outils Microsoft de déploiement de systèmes (Microsoft Deployment Toolkit, Windows Deployment Services) et de gestion de parc (Configuration Manager).
- **MariaDB / MySQL / PostgreSQL** : systèmes de gestion de bases de données relationnelles libres.
- **MSI** : format de paquet d'installation Windows.
- **Packer** : outil de HashiCorp qui construit des images de machines de façon reproductible.
- **PowerShell** : interpréteur et langage de script orientés objets de Microsoft.
- **Proxy inverse** (reverse proxy) : serveur frontal qui reçoit les requêtes et les transmet à des serveurs applicatifs.
- **Terraform** : outil d'Infrastructure as Code déclaratif.
- **SQL** (Structured Query Language) : langage d'interrogation et de manipulation de bases relationnelles.
- **WSUS** (Windows Server Update Services) : service de gestion centralisée des mises à jour Windows.
- **WinGet / Chocolatey** : gestionnaires de paquets pour Windows.

## 10. Gouvernance et conformité

- **Audit** : examen indépendant et documenté d'un système au regard d'un référentiel.
- **DSI** (Direction des systèmes d'information) : direction responsable du système d'information d'une organisation.
- **Gestion des correctifs** (patch management) : processus d'évaluation, de test et de déploiement des mises à jour.
- **Gestion du changement** : processus qui encadre la demande, l'évaluation, l'approbation et le suivi des modifications.
- **ISO/IEC 27001** : norme de système de management de la sécurité de l'information.
- **PSSI** (Politique de sécurité des systèmes d'information) : document qui fixe les objectifs et règles de sécurité d'une organisation.
- **RGPD** (Règlement général sur la protection des données) : règlement européen qui encadre le traitement des données personnelles.
- **Traçabilité** : capacité à reconstituer l'historique d'une action ou d'une donnée.
- **DIC** (Disponibilité, Intégrité, Confidentialité) : trois critères fondamentaux de la sécurité de l'information.
- **Charte informatique** : document qui fixe les règles d'usage du système d'information par les utilisateurs.
- **CNIL** (Commission nationale de l'informatique et des libertés) : autorité française de protection des données personnelles.
- **DPO / DPD** (Data Protection Officer / Délégué à la protection des données) : personne chargée de veiller à la conformité au RGPD.
- **Donnée personnelle** : information qui permet d'identifier directement ou indirectement une personne physique.
- **Gouvernance** : ensemble des règles, rôles et processus de décision qui encadrent le système d'information.
- **HDS** (Hébergeur de Données de Santé) : certification obligatoire pour héberger des données de santé en France.
- **NIS 2** : directive européenne qui renforce les obligations de cybersécurité des entités essentielles et importantes.
- **Registre des traitements** : inventaire des traitements de données personnelles exigé par le RGPD.