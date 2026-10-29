---
title: "Fiche Simple - Windows Server 2022 Nakivo Configurer"
description: "Configurer l’inventaire et le dépôt avant de lancer un premier job de sauvegarde."
published: true
date: 2026-10-29T20:47:51Z
tags: ["nakivo", "director", "transporter", "windows-server", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:47:51Z
dateModified: 2026-10-29T20:47:51Z
---

# Fiche_Simple_-_Windows_Server_2022_Nakivo_Configurer

- **Environnement** : Windows Server 2022 avec NAKIVO Director et Transporter; environnement de test
- **OS / Version** : Windows Server 2022; version NAKIVO et exigences à confirmer dans le Help Center
- **Catégorie** : sauvegarde / configuration initiale
- **Tags** : `nakivo`, `director`, `transporter`, `windows-server`, `configuration`

---

## Problème précis à résoudre

Configurer l’inventaire et le dépôt avant de lancer un premier job de sauvegarde.

## 1. Hors-Production (Lab / Test / POC)

1. Dans l’interface web, ouvrir **Settings > Inventory** (libellé à vérifier), ajouter une source de test et saisir un compte nominatif dédié.
   👉 Explication : l’inventaire et les autorisations dépendent de la plateforme protégée et de la version.
2. Ouvrir **Settings > Repositories** ou le menu équivalent, suivre l’assistant d’ajout du dépôt et choisir un volume de laboratoire séparé.
   👉 Explication : confirmer auparavant dans l’aide de la version les systèmes de fichiers et protocoles supportés.
3. Associer le Transporter proposé par l’assistant, puis vérifier son état dans l’interface.
   👉 Explication : les rôles et flux exacts dépendent de la topologie; consulter les exigences officielles.
4. Contrôler l’espace Windows en PowerShell :
   ```powershell
   Get-Volume | Format-Table DriveLetter,FileSystemLabel,SizeRemaining,Size
   ```
   👉 Explication : commande en lecture seule; les lettres de volume sont celles du serveur local.
5. Créer un job pilote avec un petit jeu de données et lancer une exécution manuelle.
   👉 Explication : le test valide inventaire, Transporter, dépôt et accès avant élargissement.

## 2. Production — Contrôles

- Documenter sources, rôles, emplacement, capacité, rétention et fenêtres.
- Vérifier les libellés, plateformes, systèmes de fichiers et flux dans la documentation de la version installée.

## 3. Production — Sécurité

- Appliquer le moindre privilège aux comptes sources; isoler le dépôt des machines sauvegardées.
- N’autoriser que les flux requis et documentés pour cette version.

## Validation et retour arrière

- **Validation** : source joignable, Transporter disponible, dépôt reconnu et job pilote terminé.
- **Retour arrière** : retirer uniquement les entrées de test après vérification qu’aucun job ni point de restauration ne les utilise.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d’entrée du logiciel](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)