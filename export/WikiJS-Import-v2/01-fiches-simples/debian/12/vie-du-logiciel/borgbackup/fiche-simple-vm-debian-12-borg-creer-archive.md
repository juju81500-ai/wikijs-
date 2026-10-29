---
title: "Fiche Simple - VM Debian 12 Borg Creer Archive"
description: "Créer une archive Borg avec les chemins attendus après avoir vérifié les montages et les exclusions."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "borgbackup", "archive", "compression", "backup"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Borg_Creer_Archive.md

- **Environnement** : serveur Debian 12, dépôt Borg initialisé et monté/accessible
- **OS / Version** : Debian 12 Bookworm
- **Catégorie** : sauvegarde / création d'archive Borg
- **Tags** : `debian12`, `borgbackup`, `archive`, `compression`, `backup`

---

## Problème précis à résoudre

Créer une archive Borg avec les chemins attendus après avoir vérifié les montages et les exclusions.

## 1. Hors-Production (Lab / Test / POC)

1. Valider chemins et montages :
   ```bash
   findmnt
   ```
   👉 Explication : repérer les montages réseau ou temporaires à exclure.

2. Fournir la phrase de passe sans l'inscrire en clair dans la ligne de commande :
   ```bash
   read -rsp "Phrase de passe Borg : " BORG_PASSPHRASE; echo; export BORG_PASSPHRASE
   ```
   👉 Explication : la valeur n'apparaît ni dans l'historique ni dans `ps`; en automatique, utiliser un fichier lisible par le compte seul (`BORG_PASSCOMMAND`).

3. Créer l'archive :
   ```bash
   export REPO=ssh://borgbackup@sauvegarde.example.net/srv/borg/depot
   sudo -E borg create --stats --progress --compression zstd,3 "$REPO::{hostname}-{now:%Y-%m-%d_%H:%M}" /etc /home /var/www
   ```
   👉 Explication : adapter dépôt et chemins; exclure caches et répertoires temporaires seulement après revue (`--exclude`).

4. Lister les archives puis effacer la phrase :
   ```bash
   sudo -E borg list "$REPO"
   unset BORG_PASSPHRASE
   ```
   👉 Explication : la nouvelle archive doit apparaître.

## 2. Production — Contrôles

Vérifier code retour, statistiques, volume, date, archive, chemins, fichiers exclus et journaux.

## 3. Production — Sécurité

- Ne pas mettre phrase de passe ou secret directement sur la ligne de commande.
- Ne pas exclure des données sans approbation du propriétaire.
- Ne pas considérer une archive réussie comme une preuve de restauration.
- Protéger les journaux et noms de fichiers qui peuvent révéler des informations sensibles.

## Validation et retour arrière

- **Validation** : archive listée, contenu conforme et journaux sans erreur.
- **Arrêt** : suspendre le job si un montage requis manque ou si le périmètre archivé est inattendu.

## Si le problème n'est pas résolu

- [BorgBackup — créer une archive](https://borgbackup.readthedocs.io/en/stable/usage/create.html)
- [BorgBackup — documentation](https://borgbackup.readthedocs.io/en/stable/)
- [Guide complet BorgBackup Debian 12](/02-fiches-completes/debian/12/autres/19-sauvegarde-restauration-borgbackup-debian-12)