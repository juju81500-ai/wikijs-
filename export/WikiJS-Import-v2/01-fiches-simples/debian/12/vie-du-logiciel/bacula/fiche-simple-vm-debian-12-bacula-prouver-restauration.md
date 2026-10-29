---
title: "Fiche Simple - VM Debian 12 Bacula Prouver Restauration"
description: "Prouver qu'un fichier sauvegardé peut être restauré à l'identique."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "bacula", "backports", "postgresql", "restore", "sha256"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Bacula_Prouver_Restauration.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / restauration
- **Tags** : `debian12`, `bacula`, `backports`, `postgresql`, `restore`, `sha256`

---

## Problème précis à résoudre

Prouver qu'un fichier sauvegardé peut être restauré à l'identique.

## 1. Hors-Production (Lab / Test / POC)

1. Dans `bconsole`, lancer `restore`, choisir le client et le JobId du pilote, puis marquer uniquement `controle.txt` :
   ```text
   restore
   ```
   👉 Explication : avant de démarrer, vérifier Storage, client cible et champ `Where`.

2. Définir `Where` sur un emplacement isolé (par défaut `/tmp/bacula-restores`) :
   ```text
   mod
   ```
   👉 Explication : jamais `/` ni un répertoire de données actif pour le premier test.

3. Comparer l'empreinte du fichier restauré (chemin d'exemple selon `Where`) :
   ```bash
   sudo find /tmp/bacula-restores -name controle.txt -exec sha256sum {} \;
   sudo find /tmp/bacula-restores -name controle.txt -exec ls -l {} \;
   ```
   👉 Explication : la valeur doit être identique à celle relevée avant la sauvegarde.

## 2. Production — Contrôles

Répéter périodiquement et tester séparément la restauration du catalogue et du bootstrap.

## 3. Production — Sécurité

- Un job `OK` ne prouve pas la restaurabilité.
- Ne supprimer que les données de test du répertoire temporaire.

## Validation et retour arrière

- **Validation** : empreinte, propriétaire et permissions identiques; JobId noté.
- **Retour arrière** : supprimer le répertoire de test restauré: `sudo rm -r /tmp/bacula-restores`.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Guide complet Bacula Debian 12](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports#7-prouver-la-restauration)