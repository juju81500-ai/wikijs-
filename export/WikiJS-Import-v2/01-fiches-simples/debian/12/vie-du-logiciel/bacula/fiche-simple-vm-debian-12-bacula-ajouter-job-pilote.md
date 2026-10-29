---
title: "Fiche Simple - VM Debian 12 Bacula Ajouter Job Pilote"
description: "Créer un jeu de fichiers fictif et un job Full manuel sans planification."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "bacula", "backports", "postgresql", "job", "fileset"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Bacula_Ajouter_Job_Pilote.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / configuration
- **Tags** : `debian12`, `bacula`, `backports`, `postgresql`, `job`, `fileset`

---

## Problème précis à résoudre

Créer un jeu de fichiers fictif et un job Full manuel sans planification.

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire et le fichier de test, puis relever son empreinte :
   ```bash
   sudo install -d -m 0750 /var/tmp/bacula-pilote
   printf 'Bacula restore validation\n' | sudo tee /var/tmp/bacula-pilote/controle.txt
   sudo sha256sum /var/tmp/bacula-pilote/controle.txt
   ```
   👉 Explication : donne les données non sensibles à sauvegarder et la valeur de référence SHA-256 pour la restauration.

2. Sauvegarder la configuration avant modification :
   ```bash
   sudo cp -a /etc/bacula /etc/bacula.avant-pilote
   ```
   👉 Explication : permet le retour arrière.

3. Ajouter dans un fichier de ressources Director déjà inclus (remplacer les valeurs `NOM_CLIENT_FD`, `NOM_STORAGE` et `NOM_POOL` par les noms relevés à l'étape précédente) :
   ```text
   FileSet {
     Name = "FichiersPilote"
     Include {
       Options {
         signature = SHA256
         aclsupport = yes
         xattrsupport = yes
       }
       File = "/var/tmp/bacula-pilote"
     }
   }

   Job {
     Name = "BackupPilote"
     Type = Backup
     Level = Full
     Client = "NOM_CLIENT_FD"
     FileSet = "FichiersPilote"
     Storage = "NOM_STORAGE"
     Pool = "NOM_POOL"
     Messages = Standard
   }
   ```
   👉 Explication : le Job n'a pas de `Schedule`, donc il ne démarre que manuellement.

## 2. Production — Contrôles

Documenter le job pilote et ne l'étendre qu'après validation de la restauration.

## 3. Production — Sécurité

- Utiliser uniquement des données fictives pour le pilote.
- Si le nom du message standard diffère, reprendre celui défini dans la configuration.

## Validation et retour arrière

- **Validation** : les ressources FileSet et Job sont ajoutées sans erreur de syntaxe (voir l'étape de validation).
- **Retour arrière** : remettre la copie: `sudo rm -r /etc/bacula && sudo mv /etc/bacula.avant-pilote /etc/bacula`, puis tester avec `bacula-dir -t`.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Guide complet Bacula Debian 12](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports#4-ajouter-un-job-pilote-manuel)