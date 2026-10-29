---
title: "Fiche Simple - VM Debian 13 Bareos Valider Restauration"
description: "Prouver qu'un job Bareos peut restaurer les données attendues vers une cible temporaire sûre."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "bareos", "restore", "bconsole", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Bareos_Valider_Restauration.md

- **Environnement** : client Bareos de test, restauration dans un répertoire temporaire non utilisé
- **OS / Version** : Debian 13 Trixie; Bareos 25 Community
- **Catégorie** : sauvegarde réseau / restauration
- **Tags** : `debian13`, `bareos`, `restore`, `bconsole`, `validation`

---

## Problème précis à résoudre

Prouver qu'un job Bareos peut restaurer les données attendues vers une cible temporaire sûre.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir la console :
   ```bash
   sudo bconsole
   ```
   👉 Explication : toute la restauration se pilote ici.

2. Dans `bconsole`, lancer l'assistant : `restore`.
   👉 Explication : choisir le client, le jeu de fichiers et le point de restauration (par ex. « derniers jobs »).

3. Avant de démarrer, vérifier le client cible et le champ **Where** : `mod`, puis modifier `where` vers `/tmp/bareos-restore`.
   👉 Explication : un `Where` vide restaurerait sur les chemins d'origine et écraserait des fichiers.

4. Démarrer (`yes`) puis contrôler :
   ```bash
   echo 'messages' | sudo bconsole
   sudo ls -la /tmp/bareos-restore
   ```
   👉 Explication : les fichiers doivent être présents et lisibles; comparer avec la source.

5. Prévoir aussi : job de sauvegarde du catalogue et bootstrap, copie hors site des médias et de la configuration, exercices périodiques.
   👉 Explication : sans catalogue sauvegardé, la restauration devient très longue.

## 2. Production — Contrôles

Répéter les restaurations par type d'OS, application et niveau de sauvegarde (Full/Incremental/Differential); documenter durée, RPO/RTO, restauration du catalogue et bootstrap.

## 3. Production — Sécurité

- Ne pas restaurer sur les données actives avant validation du propriétaire et de l'emplacement.
- Ne jamais afficher les mots de passe Director/File Daemon dans les journaux ou la fiche.
- Vérifier que le catalogue référence les volumes requis et que les médias hors site sont disponibles.
- Protéger les données restaurées selon leur classification.

## Validation et retour arrière

- **Validation** : job Restore terminé, fichier vérifié, propriétés et chemin cohérents, journaux sans erreur.
- **Retour arrière** : conserver l'original; retirer uniquement les fichiers restaurés dans le dossier temporaire après contrôle.

## Si le problème n'est pas résolu

- [Bareos — commande de restauration](https://docs.bareos.org/TasksAndConcepts/TheRestoreCommand.html)
- [Bareos — vérifications avant production](https://docs.bareos.org/IntroductionAndTutorial/CriticalItemsToImplementBeforeProduction.html)
- [Guide complet Bareos Debian 13](/02-fiches-completes/debian/13/installation-deploiement/59-deploiement-bareos-25-debian-13#5-prouver-la-restauration)