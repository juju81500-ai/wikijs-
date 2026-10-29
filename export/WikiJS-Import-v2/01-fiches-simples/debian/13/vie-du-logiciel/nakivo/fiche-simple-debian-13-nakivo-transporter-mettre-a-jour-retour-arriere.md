---
title: "Fiche Simple - Debian 13 Nakivo Transporter Mettre A Jour Retour Arriere"
description: "Mettre à jour un Transporter NAKIVO installé sur Debian 13 (avec son Director) et savoir revenir en arrière ou le désinstaller proprement."
published: true
date: 2026-10-29T21:16:03Z
tags: ["debian-13", "nakivo", "transporter", "mettre-a-jour-retour-arriere"]
editor: markdown
dateCreated: 2026-10-29T21:16:03Z
dateModified: 2026-10-29T21:16:03Z
---

# Fiche_Simple_-_Debian_13_Nakivo_Transporter_Mettre_A_Jour_Retour_Arriere

- **Environnement** : Debian 13 x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Debian 13 — plateforme de déploiement listée dans les exigences NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / maintenance
- **Tags** : `debian-13`, `nakivo`, `transporter`, `mettre-a-jour-retour-arriere`

---

## Problème précis à résoudre

Mettre à jour un Transporter NAKIVO installé sur Debian 13 (avec son Director) et savoir revenir en arrière ou le désinstaller proprement.

## 1. Hors-Production (Lab / Test / POC)

1. Relever le build courant et lire les notes de version : **Settings** > **General** > **Software Update**, cliquer sur **Check for Updates** si nécessaire, puis **Release Notes**.
   👉 Explication : les notes de version indiquent la compatibilité; mettre à jour le Director avant les Transporters.

2. Lancer un self-backup (**Settings** > **General** > **Self-Backup** > **Run Self-backup Now**) et vérifier la fiche [sauvegarder / restaurer](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-sauvegarder-restaurer).
   👉 Explication : disposer d'un point de retour de configuration avant toute modification.

3. Mise à jour via l'interface (si le Transporter prend en charge l'auto-update) : cocher **I have read the Release Notes**, cliquer sur **Download & update**, puis **Update Now**.
   👉 Explication : le produit effectue un self-backup, arrête les activités en cours, met à jour le Director puis envoie la mise à jour aux Transporters; ceux non mis à jour sont à traiter manuellement.

4. Mise à jour manuelle : télécharger l'updater Linux depuis la page officielle de téléchargement NAKIVO, le transférer en mode binaire sur la machine, puis rendre le fichier exécutable :
   ```bash
   chmod +x NAKIVO_Backup_Replication_vX.X.X_Updater.sh
   ```
   👉 Explication : remplacer `X.X.X` par la version téléchargée (à remplacer); utiliser le nom exact du fichier publié.

5. Vérifier qu'aucun job ni tâche de maintenance de dépôt n'est en cours, créer un snapshot de la VM si l'hôte est virtualisé, puis exécuter l'updater avec les privilèges root :
   ```bash
   sudo ./NAKIVO_Backup_Replication_vX.X.X_Updater.sh
   ```
   👉 Explication : lire la licence (Espace pour paginer), répondre « Y » puis Entrée, et de nouveau « Y » pour confirmer l'arrêt des services; répéter sur chaque machine où un Transporter est déployé séparément.

6. Si un dépôt CIFS/NFS reste monté sur l'OS, arrêter les services Transporter concernés, vérifier les montages, démonter, puis lancer la mise à jour :
   ```bash
   mount | grep -E 'cifs|nfs'
   sudo umount CHEMIN_DU_POINT_DE_MONTAGE
   ```
   👉 Explication : CHEMIN_DU_POINT_DE_MONTAGE est à remplacer par le point de montage relevé; l'éditeur recommande ce flux pour éviter d'endommager un dépôt CIFS/NFS.

7. Contrôler le statut du nœud et lancer un job pilote après la mise à jour.
   👉 Explication : confirmer que le Transporter est joignable et fonctionnel dans le Director.

## 2. Production — Contrôles

- Planifier une fenêtre de changement; ne pas mettre à jour pendant des jobs ou une maintenance de dépôt.
- Mettre à jour tous les Transporters pour rester alignés avec le Director.
- Valider d'abord sur un lab ou un nœud pilote.
- Si la machine est virtuelle, prévoir un snapshot et une fenêtre de retour.

## 3. Production — Sécurité

- Télécharger l'updater uniquement depuis les canaux officiels NAKIVO; ne pas utiliser de miroir tiers.
- Exécuter l'updater avec les privilèges nécessaires seulement, pendant la fenêtre approuvée.
- Ne jamais copier de secrets ou de clés dans les fiches ou journaux partagés.

## Validation et retour arrière

- **Validation** : build attendu affiché, Transporter en état sain, job pilote et restauration de test réussis.
- **Retour arrière** : la documentation publiée ne décrit pas de commande de rétrogradation; restaurer le snapshot de VM ou l'image de l'hôte prise avant mise à jour, puis si nécessaire récupérer la configuration depuis le self-backup. Pour retirer seulement le Transporter, exécuter le script de désinstallation (emplacement par défaut) puis saisir « U » et Entrée :
  ```bash
  sudo /opt/nakivo/transporter/uninstall
  ```
  👉 Explication : la désinstallation retire le Transporter, pas les données des dépôts; si l'installation n'est pas à l'emplacement par défaut, utiliser le dossier `transporter` du répertoire d'installation.

## Si le problème n'est pas résolu

- [NAKIVO — Updating on Linux](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Updating-NAKIVO-Backup-and-Replication/Updating-on-Linux.htm)
- [NAKIVO — Software Update](https://helpcenter.nakivo.com/User-Guide/Content/Settings/General/Software-Update.htm)
- [NAKIVO — Uninstalling NAKIVO Backup & Replication](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Uninstalling-NAKIVO-Backup-and-Replication.htm)
- [Fiche validation et maintenance du Transporter](/01-fiches-simples/debian/13/vie-du-logiciel/nakivo/fiche-simple-debian-13-nakivo-transporter-valider-mettre-a-jour)
- [Fiche d'entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)