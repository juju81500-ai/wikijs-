# Méthodes d'installation officielles des logiciels du pack

- **Tags** : `installation`, `documentation-officielle`, `logiciels`, `versions`, `sysadmin`
- **Liens revus** : 31 octobre 2026

Ce guide centralise les points d'entrée officiels d'installation des plateformes et logiciels recensés dans le pack. Il oriente vers la procédure adaptée à l'OS, à l'architecture et à la version; il ne remplace pas une procédure locale testée.

## Méthode commune

1. Identifier précisément le produit, sa version, l'OS, l'architecture CPU et le mode de déploiement (machine, VM, conteneur ou service hébergé).
2. Consulter la matrice de compatibilité et les prérequis, puis choisir la procédure officielle correspondante. Ne pas transposer une commande d'une distribution ou d'une version à une autre.
3. Privilégier l'ISO signée, le dépôt officiel signé ou le gestionnaire de paquets de la distribution. Vérifier la signature ou le checksum quand l'éditeur les publie; éviter les dépôts tiers et les scripts distants non audités.
4. En production, préparer sauvegarde, fenêtre de changement, comptes minimaux, filtrage réseau, supervision et retour arrière avant l'installation.
5. Après installation, contrôler la version, l'état du service, les ports exposés, le journal de démarrage, les mises à jour et les paramètres par défaut à sécuriser.

## Systèmes et plateformes

| Produit | Méthode et documentation officielle | Points à vérifier |
|---|---|---|
| Debian | [Guide d'installation Debian](https://www.debian.org/releases/stable/amd64/) et [images officielles](https://www.debian.org/CD/) | Le guide `stable` suit la version stable courante; choisir l'architecture exacte et vérifier l'image avant de l'écrire sur un support. |
| Ubuntu Server | [Tutoriel d'installation Ubuntu Server](https://ubuntu.com/server/docs/tutorial/installation) | Choisir une version LTS prise en charge et son image serveur; relire les notes de version et les prérequis matériels. |
| Alpine Linux | [Installation Alpine](https://wiki.alpinelinux.org/wiki/Installation) | Choisir l'architecture et le mode `diskless`, `data` ou `sys`; contrôler checksum et signature de l'image. Le mode `sys` écrit sur le disque cible. |
| Rocky Linux | [Guide d'installation Rocky Linux](https://docs.rockylinux.org/guides/installation/) et [téléchargements](https://rockylinux.org/download/) | Le guide suit la version courante de la documentation; choisir explicitement Rocky 9 ou 10 et vérifier l'ISO. |
| Red Hat Enterprise Linux | [Guide d'installation RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/performing_a_standard_rhel_9_installation/index) | La page est spécifique à RHEL 9; sélectionner le guide de la version cible, vérifier l'abonnement et le profil d'installation. |
| Windows client | [Téléchargement et installation de Windows 11](https://www.microsoft.com/software-download/windows11) | Choisir l'assistant, le support d'installation ou l'ISO selon le besoin; vérifier compatibilité matérielle, licence et état de version. |
| Windows Server | [Options d'installation Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server) | Choisir Server Core ou Desktop Experience et la version réellement licenciée; utiliser les médias fournis par l'organisation ou Microsoft. |
| Proxmox VE | [Installation de Proxmox VE](https://pve.proxmox.com/pve-docs/chapter-pve-installation.html) | L'ISO est la méthode recommandée. L'installation efface les disques sélectionnés; vérifier le matériel, le stockage et le support ZFS avant de lancer l'installeur. |
| Proxmox Backup Server | [Installation de PBS](https://pbs.proxmox.com/docs/installation.html) | L'ISO est recommandée pour un serveur dédié; une installation sur Debian est prévue pour les utilisateurs avancés. Éviter de colocaliser PBS sur l'hyperviseur en production. |
| Docker Engine | [Procédures par distribution](https://docs.docker.com/engine/install/) | Utiliser la page dédiée à Debian, Ubuntu, Rocky/RHEL ou Fedora; Docker Engine n'est pas Docker Desktop. Vérifier la politique de licence de Docker Desktop si choisi. |
| Docker Compose | [Installation du plugin Compose](https://docs.docker.com/compose/install/linux/) | La méthode dépôt nécessite Docker Engine et son dépôt configuré. L'installation manuelle ne bénéficie pas des mises à jour automatiques. |
| Kubernetes | [Installation de kubeadm, kubelet et kubectl](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/) | Choisir la branche mineure voulue : dépôt et versions sont spécifiques. Installer et mettre à niveau les composants selon la politique de compatibilité Kubernetes; choisir aussi un runtime CRI et un CNI. |

## Administration, scripting et réseau

| Produit | Méthode et documentation officielle | Points à vérifier |
|---|---|---|
| Bash | [Sources GNU Bash](https://ftp.gnu.org/gnu/bash/) et [manuel Bash](https://www.gnu.org/software/bash/manual/bash.html) | Sur un poste ou serveur, installer le paquet `bash` fourni par la distribution. Compiler depuis GNU seulement si le besoin le justifie; ne pas confondre Bash et `sh`. |
| PowerShell | [Installation multiplateforme](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell) et [Windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows) | Windows PowerShell 5.1 et PowerShell 7 coexistent. WinGet n'est pas disponible sur Windows Server 2022 et antérieurs; suivre la méthode MSI/ZIP adaptée au serveur. |
| Python | [Téléchargements officiels](https://www.python.org/downloads/) et [guide de configuration par OS](https://docs.python.org/3/using/) | Pour un système géré par paquets, préférer le paquet de la distribution; ne pas remplacer le Python système. Choisir une version encore maintenue et vérifier la signature des binaires. |
| Git | [Installation de Git par plateforme](https://git-scm.com/downloads) et [guide d'installation](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) | Installer le paquet du système ou le binaire officiel, puis configurer identité, authentification et signature des commits selon la politique locale. |
| Ansible | [Guide d'installation](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html) | Installer sur un nœud de contrôle compatible. Choisir `ansible` ou `ansible-core`, isoler les dépendances Python et épingler versions et collections. Windows nécessite WSL pour le nœud de contrôle. |
| OpenSSH | [OpenSSH portable](https://www.openssh.com/portable.html) et [installation OpenSSH sur Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) | Sur Linux, utiliser le paquet de la distribution; sur Windows, activer la fonctionnalité facultative. Avant d'activer le serveur, limiter les accès et contrôler la règle de pare-feu. |
| Wireshark / TShark | [Téléchargements officiels et notes d'installation](https://www.wireshark.org/download.html) | Utiliser les paquets pour l'OS et l'architecture; sur Windows, le pilote de capture Npcap est un composant séparé. Les captures peuvent contenir des données sensibles. |
| PuTTY | [Dernière version, paquets et signatures](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) | Choisir MSI ou binaire portable selon l'administration voulue; vérifier la signature ou le checksum publié. Le lien `latest` évolue avec les versions. |

## Services et applications

| Produit | Méthode et documentation officielle | Points à vérifier |
|---|---|---|
| Nginx | [Paquets Linux officiels Nginx](https://nginx.org/en/linux_packages.html) | Les paquets Nginx.org nécessitent l'ajout de son dépôt et de sa clé; comparer avec les paquets maintenus par la distribution et choisir stable ou mainline. |
| MariaDB Server | [Guide d'installation MariaDB](https://mariadb.com/docs/server/server-management/install-and-upgrade-mariadb/installing-mariadb) | Choisir le dépôt et la version adaptés à la distribution; sauvegarder les bases avant une mise à niveau majeure. |
| PostgreSQL | [Paquets et installateurs par OS](https://www.postgresql.org/download/) | Utiliser le dépôt de la distribution ou les paquets officiels PostgreSQL, puis le manuel de la version choisie; planifier séparément l'initialisation et la migration des données. |
| Centreon | [Introduction à l'installation Centreon](https://docs.centreon.com/docs/installation/introduction/) | Les dépôts Centreon sont la méthode recommandée. Contrôler compatibilité OS/DB, architecture, prérequis et version avant l'installation. |
| Zabbix | [Téléchargement et instructions par OS](https://www.zabbix.com/download) | Sélectionner la version, la distribution, les composants, la base de données et le serveur Web; ne pas mélanger les versions serveur, proxy et agent. |
| Prometheus | [Méthodes d'installation](https://prometheus.io/docs/prometheus/latest/installation/) | Choisir binaire signé/publié, conteneur officiel ou gestion de configuration. Prévoir configuration et stockage persistant; la page `latest` change avec la version. |
| Grafana | [Installation Grafana par OS](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) | Utiliser la procédure Debian/Ubuntu, RHEL/Fedora, SUSE, macOS ou Windows correspondante. SQLite convient à l'évaluation, pas à une plateforme de production ou HA. |
| Elastic Stack | [Installation Elasticsearch auto-hébergé](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch) et [paquet Debian](https://www.elastic.co/docs/deploy-manage/deploy/self-managed/install-elasticsearch-with-debian-package) | Sélectionner le paquet par OS, installer depuis un dépôt signé et suivre l'auto-configuration TLS; ne pas exposer Elasticsearch avant le contrôle sécurité. |
| Wazuh | [Guide d'installation Wazuh](https://documentation.wazuh.com/current/installation-guide/index.html) et [démarrage rapide](https://documentation.wazuh.com/current/quickstart.html) | Le quickstart installe les composants centraux sur un seul hôte pour un déploiement limité; choisir l'architecture distribuée pour la production et vérifier les capacités. |
| GLPI | [Guide officiel d'installation GLPI](https://glpi-install.readthedocs.io/en/latest/) | Vérifier les prérequis Web/PHP/base de données de la version visée, puis suivre séparément l'installation, l'assistant et les tâches post-installation. |
| OCS Inventory NG | [Documentation officielle OCS](https://wiki.ocsinventory-ng.org/) | L'ancien chemin direct d'installation n'est plus accessible lors de cette revue. Depuis le wiki, choisir le guide serveur ou agent correspondant à la version; ne pas réutiliser un lien historique sans contrôle. |
| NetBox | [Installation NetBox](https://netbox.readthedocs.io/en/stable/installation/) | Le guide stable consulté a été testé sur Ubuntu 24-04 et nécessite PostgreSQL, Redis et Python compatibles. Les autres distributions peuvent demander d'adapter les dépendances système. |
| KeePassXC | [Téléchargements et méthodes par OS](https://keepassxc.org/download/) | Linux : préférer les paquets officiels de la distribution ou Flatpak recommandé par le projet; vérifier les signatures des AppImage. Ne pas installer les secrets dans un profil partagé. |
| Visual Studio Code | [Installation par plateforme](https://code.visualstudio.com/docs/setup/setup-overview) | Utiliser l'installateur Windows/macOS ou les dépôts officiels Linux; sur un poste administré, respecter les règles d'entreprise et de mise à jour. |
| QGIS | [Guide d'installation QGIS](https://qgis.org/resources/installation-guide/) et [téléchargements](https://qgis.org/download/) | Choisir l'installateur ou le dépôt selon l'OS; les extensions doivent correspondre à la version du client et à la politique de sécurité. |
| OpenMediaVault | [Guide d'installation OMV](https://docs.openmediavault.org/en/latest/installation/index.html) | ISO dédiée recommandée sur x86/AMD64; pour les cartes ARM, suivre la méthode sur Debian. La documentation ne prend pas en charge l'installation en LXC ou autre conteneur. |
| TrueNAS | [Documentation TrueNAS](https://www.truenas.com/docs/) | Utiliser le sélecteur de produit/version puis suivre le guide ISO de l'édition choisie. Vérifier la version stable et la compatibilité des contrôleurs avant de réinstaller un NAS. |
| OPNsense | [Installation et configuration initiale](https://docs.opnsense.org/manual/install.html) | Choisir l'image Full ou Nano selon le matériel et le support; vérifier la signature et le checksum. L'installeur peut effacer entièrement le disque sélectionné. |
| WireGuard | [Installation WireGuard par plateforme](https://www.wireguard.com/install/) | Sur les distributions, installer les paquets du système; pour Windows/macOS, employer l'installateur officiel. Contrôler l'état de maintenance des paquets proposés pour les anciennes distributions. |
| HashiCorp Vault | [Options d'installation Vault](https://developer.hashicorp.com/vault/docs/install) | Choisir le paquet, le binaire ou Helm en fonction de la plateforme. L'installation de production exige ensuite TLS, stockage, initialisation et gestion des clés; le mode dev est uniquement destiné aux essais. |
| Bitwarden | [Déploiement auto-hébergé Linux](https://bitwarden.com/help/install-on-premise-linux/) | Le déploiement standard repose sur Docker/Compose et un script éditeur. Utiliser un compte dédié, HTTPS, sauvegardes testées et installation ID/key obtenus auprès de Bitwarden; ne jamais publier les secrets. |

## Limites de ce catalogue

- Les liens `latest`, `stable` et les pages de téléchargement évoluent. Ouvrir la documentation juste avant l'intervention et choisir la version compatible avec le pack.
- Une page qui liste plusieurs méthodes ne les rend pas équivalentes : préférer celle officiellement supportée pour le système cible et le contexte d'exploitation.
- L'installation d'un hyperviseur, d'un pare-feu, d'un serveur de stockage ou d'une base de données peut écraser des disques, exposer des ports ou modifier le démarrage. Utiliser une fiche dédiée, un environnement isolé et une sauvegarde vérifiée.
- Pour OCS Inventory NG, le wiki officiel était accessible mais son ancienne URL directe d'installation ne l'était pas au 31 octobre 2026; revalider le guide serveur/agent avant publication d'une procédure détaillée.

## Références

- [Index des documentations officielles](liens-docs-logicielles.md)
- [Aide-mémoire des précautions d'exécution](../01-aide-memoire/fiches-aide-informatique.md)
- [Contribution et règles de citation](../../contributing.md)
