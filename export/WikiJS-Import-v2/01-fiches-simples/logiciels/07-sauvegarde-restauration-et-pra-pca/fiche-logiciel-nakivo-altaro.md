---
title: "Nakivo / Altaro"
description: "NAKIVO : procédures Windows Server 2022 existantes et séries Linux Transporter Debian 13 et Ubuntu Server 24.04 LTS (5 fiches par OS : prérequis, installation, configuration, sécurité, validation/maintenance). La page NAKIVO « Deployment Requirements » liste explicitement Debian 13 64-bit et Ubuntu "
published: true
date: 2026-10-29T21:16:03Z
tags: ["logiciel", "07-Sauvegarde-restauration-et-PRA-PCA", "partiel"]
editor: markdown
dateCreated: 2026-10-29T21:16:03Z
dateModified: 2026-10-29T21:16:03Z
---

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

Fiches NAKIVO Debian 13 : [prérequis](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-prerequis), [installation du Transporter](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-installer), [configuration](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-configurer), [sécurité](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-securiser), [validation/maintenance](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-valider-mettre-a-jour), [sauvegarde/restauration](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-sauvegarder-restaurer), [mise à jour/retour arrière](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-mettre-a-jour-retour-arriere).

Fiches NAKIVO Ubuntu 24.04 : [prérequis](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-prerequis), [installation du Transporter](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-installer), [configuration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-configurer), [sécurité](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-securiser), [validation/maintenance](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-valider-mettre-a-jour), [sauvegarde/restauration](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-sauvegarder-restaurer), [mise à jour/retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/nakivo/fiche-simple-ubuntu-24-04-nakivo-transporter-mettre-a-jour-retour-arriere).


Cette fiche est le point d'entrée du logiciel : elle indique si le pack contient une procédure et renvoie vers elle. Pour une procédure pas à pas, ouvrir le guide ou la fiche liée ci-dessus. Lorsque le statut est `Manquant`, aucune procédure dédiée n'existe encore dans le pack.

Fiches simples du guide : [prérequis et limites NAKIVO](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-prerequis-limites), [installer NAKIVO Director et Transporter](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-installer-director-transporter), [configurer l’inventaire et le dépôt](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-configurer), [sécuriser NAKIVO](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-securiser), [créer un job de sauvegarde NAKIVO](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-job-sauvegarde), [restaurer via l'interface NAKIVO](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-restaurer-interface), [mettre à jour et revenir en arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/nakivo/fiche-simple-windows-server-2022-nakivo-mettre-a-jour-retour-arriere).