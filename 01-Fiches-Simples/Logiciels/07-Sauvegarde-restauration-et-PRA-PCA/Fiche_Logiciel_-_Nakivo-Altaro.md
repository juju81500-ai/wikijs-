# 📄 Nakivo / Altaro

- **Catégorie** : Sauvegarde, restauration et PRA / PCA
- **Plateforme** : Windows et Linux selon compatibilités explicitement publiées
- **Produit (matrice)** : Nakivo / Altaro (Hornetsecurity)
- **Statut dans le pack** : Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24.04; Altaro/Hornetsecurity limité à la documentation publique de VM Backup
- **Tags** : `logiciel`, `07-Sauvegarde-restauration-et-PRA-PCA`, `partiel`

## 📚 Couverture dans le pack

NAKIVO : procédures Windows Server 2022 existantes et séries Linux Transporter Debian 13 et Ubuntu Server 24.04 LTS (5 fiches par OS : prérequis, installation, configuration, sécurité, validation/maintenance). La page NAKIVO « Deployment Requirements » liste explicitement Debian 13 64-bit et Ubuntu 24.04 Server LTS x64 comme plateformes de déploiement. La liste « Supported Platforms » des machines physiques protégées est distincte et ne doit pas être interprétée comme la matrice des hôtes Transporter. Altaro/Hornetsecurity : fiche d’entrée seulement; la base de connaissances publique confirme l’installation et l’ouverture de la VM Backup Management Console, sans série de déploiement créée ici.

Référence OS de déploiement : [NAKIVO Deployment Requirements](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm).

Références publiques : [installation VM Backup et ouverture de la Management Console](https://support.hornetsecurity.com/hc/en-us/articles/19687951120145-Installing-VM-Backup) et [exigences système VM Backup](https://support.hornetsecurity.com/hc/en-us/articles/19687996547601).

## 🧭 Utilisation

Fiches NAKIVO Debian 13 : [prérequis](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Prerequis.md), [installation du Transporter](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Installer.md), [configuration](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Configurer.md), [sécurité](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Securiser.md), [validation/maintenance](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Valider_Mettre_A_Jour.md), [sauvegarde/restauration](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Sauvegarder_Restaurer.md), [mise à jour/retour arrière](../../Debian/13/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Debian_13_Nakivo_Transporter_Mettre_A_Jour_Retour_Arriere.md).

Fiches NAKIVO Ubuntu 24.04 : [prérequis](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Prerequis.md), [installation du Transporter](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Installer.md), [configuration](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Configurer.md), [sécurité](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Securiser.md), [validation/maintenance](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Valider_Mettre_A_Jour.md), [sauvegarde/restauration](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Sauvegarder_Restaurer.md), [mise à jour/retour arrière](../../Ubuntu/24.04/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Ubuntu_24.04_Nakivo_Transporter_Mettre_A_Jour_Retour_Arriere.md).


Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Fiches simples du guide : [prérequis et limites NAKIVO](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Prerequis_Limites.md), [installer NAKIVO Director et Transporter](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Installer_Director_Transporter.md), [configurer l’inventaire et le dépôt](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Configurer.md), [sécuriser NAKIVO](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Securiser.md), [créer un job de sauvegarde NAKIVO](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Job_Sauvegarde.md), [restaurer via l'interface NAKIVO](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Restaurer_Interface.md), [mettre à jour et revenir en arrière](../../Windows/Server-2022/Vie-du-logiciel/Nakivo/Fiche_Simple_-_Windows_Server_2022_Nakivo_Mettre_A_Jour_Retour_Arriere.md).
