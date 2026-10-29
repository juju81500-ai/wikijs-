---
title: "Fiche Simple - VM Ubuntu 24.04 EVE-NG Sauvegarder Restaurer"
description: "Exporter des labs et sauvegarder EVE-NG vers un serveur SFTP/FTP externe, puis restaurer."
published: true
date: 2026-10-29T20:47:13Z
tags: ["ubuntu24.04", "eve-ng", "sauvegarde", "restauration", "sftp", "backup-manager"]
editor: markdown
dateCreated: 2026-10-29T20:47:13Z
dateModified: 2026-10-29T20:47:13Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_EVE-NG_Sauvegarder_Restaurer

- **Environnement** : VM EVE-NG (appliance basée sur Ubuntu Server 24.04 LTS) hébergée sur un poste ou serveur de virtualisation
- **OS / Version** : EVE-NG 7.x (7.2.0-18 au contrôle du 29/10/2026), Ubuntu 24.04 LTS embarqué; Community 6.2.0-4 (Ubuntu 22.04) en fin de support juin 2026
- **Catégorie** : simulation réseau / sauvegarde
- **Tags** : `ubuntu24.04`, `eve-ng`, `sauvegarde`, `restauration`, `sftp`, `backup-manager`

---

## Problème précis à résoudre

Exporter des labs et sauvegarder EVE-NG vers un serveur SFTP/FTP externe, puis restaurer.

## 1. Hors-Production (Lab / Test / POC)

1. Export simple d'un lab : dans le gestionnaire de fichiers, sélectionner le lab puis **Export**.
   👉 Explication : télécharge un fichier `.zip` importable dans un autre EVE-NG.

2. Pour réimporter : **Import**, sélectionner le `.zip` (sans le décompresser), puis **Import**.
   👉 Explication : le cookbook précise que le fichier doit rester au format zip.

3. Arrêter tous les labs : **System > Stop All Nodes**.
   👉 Explication : le Backup Manager exige que tous les nœuds soient arrêtés.

4. Installer le gestionnaire (en root, Internet et DNS requis) :
   ```bash
   apt update
   apt install eve-backup-manager
   reboot
   ```
   👉 Explication : paquet officiel cité par le cookbook (section 19).

5. Préparer un serveur SFTP externe joignable dans les deux sens (aucune procédure de serveur n'est fournie ici : sa mise en place est à votre charge et hors support éditeur).
   👉 Explication : le cookbook renvoie à un document SFTP séparé de l'éditeur.

6. Lancer le gestionnaire, puis **(e) Edit Backup Server** : protocole `SFTP`, adresse `IP_SFTP`, répertoire `REPERTOIRE_SFTP`, utilisateur `UTILISATEUR_SFTP`, mot de passe `MOT_DE_PASSE_SFTP`, **Submit**.
   ```bash
   backup-manager
   ```
   👉 Explication : menu interactif; les valeurs en majuscules sont à remplacer et le mot de passe n'est jamais noté dans une fiche.

7. Dans `backup-manager` : **(c) Create Backup**, choisir **All** ou une sélection personnalisée; l'option Mirroring crée un dossier `[hôte]-eve-ng-mirror` mis à jour.
   👉 Explication : All inclut labs, base utilisateurs, images, templates et dossier TMP.

8. Restaurer : `backup-manager` > **(r) Restore Backup**, sélectionner le dossier de sauvegarde puis les éléments.
   ```bash
   backup-manager
   ```
   👉 Explication : sans Mirroring, seules les données manquantes sont restaurées; ⚠️ avec Mirroring, les données absentes de la sauvegarde sont détruites : à éviter sauf choix explicite.

## 2. Production — Contrôles

- Contrôler la présence du dossier `[hôte]-[date]-[ID]` sur le serveur SFTP après chaque sauvegarde.
- Tester une restauration sur une VM de test avant d'en dépendre.
- Prendre aussi un instantané de la VM avant tout changement majeur.

## 3. Production — Sécurité

- Stocker la sauvegarde sur un serveur à accès restreint et chiffré au repos : elle contient la base d'utilisateurs et les images.
- Utiliser SFTP plutôt que FTP en clair.
- Ne pas laisser le mot de passe SFTP dans l'historique shell ni dans un script partagé.

## Validation et retour arrière

- **Validation** : la sauvegarde apparaît sur le serveur SFTP et une restauration de test retrouve les labs.
- **Retour arrière** : interrompre une opération en cours avec `pkill eve_backup.sh`, ou restaurer l'instantané de la VM.

## Si le problème n'est pas résolu

- [EVE-NG — sauvegarder le contenu](https://www.eve-ng.net/index.php/backup-eve-ng-content/)
- [EVE-NG — Professional Cookbook (PDF, chapitre 19)](https://www.eve-ng.net/wp-content/uploads/2026/09/EVE-PE-BOOK-7.9-2026.pdf)
[EVE-NG — documentation officielle](https://www.eve-ng.net/index.php/documentation/)
- [Fiche logiciel EVE-NG](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-eve-ng)
- [Mettre à jour avec retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/eve-ng/fiche-simple-vm-ubuntu-24-04-eve-ng-mettre-a-jour-retour)