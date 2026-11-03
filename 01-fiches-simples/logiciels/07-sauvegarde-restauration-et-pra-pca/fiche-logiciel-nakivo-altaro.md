# 📄 Nakivo / Altaro

- **Catégorie** : Sauvegarde, restauration et PRA / PCA
- **Plateforme** : Windows et Linux selon compatibilités explicitement publiées
- **Produit (matrice)** : Nakivo / Altaro (Hornetsecurity)
- **Statut dans le pack** : Partiel — NAKIVO Windows Server 2022 et Transporter Linux sur Debian 13 et Ubuntu Server 24-04; Altaro/Hornetsecurity limité à la documentation publique de [[Glossary:VM]] Backup
- **Tags** : `logiciel`, `07-sauvegarde-restauration-et-pra-pca`, `partiel`

## 📚 Couverture dans le pack

NAKIVO : procédures Windows Server 2022 existantes et séries Linux Transporter Debian 13 et Ubuntu Server 24-04 [[Glossary:LTS]] (5 fiches par OS : prérequis, installation, configuration, sécurité, validation/maintenance). La page NAKIVO « Deployment Requirements » liste explicitement Debian 13 64-bit et Ubuntu 24-04 Server LTS x64 comme plateformes de déploiement. La liste « Supported Platforms » des machines physiques protégées est distincte et ne doit pas être interprétée comme la matrice des hôtes Transporter. Altaro/Hornetsecurity : fiche d’entrée seulement; la base de connaissances publique confirme l’installation et l’ouverture de la VM Backup Management Console, sans série de déploiement créée ici.

Référence OS de déploiement : [NAKIVO Deployment Requirements](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm).

Références publiques : [installation VM Backup et ouverture de la Management Console](https://support.hornetsecurity.com/hc/en-us/articles/19687951120145-Installing-VM-Backup) et [exigences système VM Backup](https://support.hornetsecurity.com/hc/en-us/articles/19687996547601).

## 🧭 Utilisation

Fiches NAKIVO Debian 13 : [prérequis](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-prerequis.md), [installation du Transporter](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-installer.md), [configuration](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-configurer.md), [sécurité](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-securiser.md), [validation/maintenance](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-valider-mettre-a-jour.md), [sauvegarde/restauration](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-sauvegarder-restaurer.md), [mise à jour/retour arrière](../../debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-mettre-a-jour-retour-arriere.md).

Fiches NAKIVO Ubuntu 24-04 : [prérequis](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-prerequis.md), [installation du Transporter](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-installer.md), [configuration](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-configurer.md), [sécurité](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-securiser.md), [validation/maintenance](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-valider-mettre-a-jour.md), [sauvegarde/restauration](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-sauvegarder-restaurer.md), [mise à jour/retour arrière](../../ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-mettre-a-jour-retour-arriere.md).


Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Fiches simples du guide : [prérequis et limites NAKIVO](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-prerequis-limites.md), [installer NAKIVO Director et Transporter](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-installer-director-transporter.md), [configurer l’inventaire et le dépôt](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-configurer.md), [sécuriser NAKIVO](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-securiser.md), [créer un job de sauvegarde NAKIVO](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-job-sauvegarde.md), [restaurer via l'interface NAKIVO](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-restaurer-interface.md), [mettre à jour et revenir en arrière](../../windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-mettre-a-jour-retour-arriere.md).
