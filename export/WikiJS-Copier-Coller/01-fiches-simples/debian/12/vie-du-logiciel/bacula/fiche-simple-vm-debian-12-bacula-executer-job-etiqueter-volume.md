# Fiche_Simple_-_VM_Debian_12_Bacula_Executer_Job_Etiqueter_Volume.md

- **Environnement** : VM Debian 12 dédiée à Bacula (Director, Storage Daemon, File Daemon, catalogue PostgreSQL)
- **OS / Version** : Debian 12 Bookworm; Bacula Community 15.0.3 (backports)
- **Catégorie** : sauvegarde / exploitation

---

## Problème précis à résoudre

Lancer le job pilote et obtenir `Backup OK`.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir la console Bacula :
   ```bash
   sudo bconsole
   ```
   👉 Explication : permet de piloter le Director.

2. Dans `bconsole`, contrôler les composants :
   ```text
   status dir
   status client
   status storage
   ```
   👉 Explication : chaque composant doit répondre.

3. Toujours dans `bconsole`, lancer `run` et sélectionner `BackupPilote` :
   ```text
   run
   ```
   👉 Explication : vérifier client, FileSet, Storage, Pool et niveau `Full` avant de confirmer.

4. Si aucun volume n'est inscriptible, utiliser `label` :
   ```text
   label
   ```
   👉 Explication : créer un volume au nom unique dans le Pool et le Storage attendus.

5. Relever le résultat :
   ```text
   list jobs
   ```
   👉 Explication : noter JobId, statut, nombre de fichiers, volume et erreurs; attendu: `Backup OK` avec un seul fichier.

## 2. Production — Contrôles

Planifier ensuite les jobs et surveiller les échecs et l'espace disque.

## 3. Production — Sécurité

- Ne pas relabeler ni purger un volume existant pour débloquer un essai.

## Validation et retour arrière

- **Validation** : le job pilote se termine par `Backup OK`.
- **Retour arrière** : supprimer uniquement le volume de test créé par vous, après accord, et conserver les journaux.

## Si le problème n'est pas résolu

- [Bacula — manuels 15.0.x](https://www.bacula.org/15.0.x-manuals/en/main/)
- [Guide complet Bacula Debian 12](/02-fiches-completes/debian/12/installation-deploiement/68-deploiement-bacula-15-debian-12-backports#6-executer-le-job-et-etiqueter-un-volume)