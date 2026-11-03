---
title: "Gestion des IDs d'import des commandes"
description: "Ce guide concerne les données commandblocks de txt.txt. Il ne concerne pas les identifiants internes des pages Wiki.js."
published: true
date: 2026-11-03T14:22:28Z
tags: []
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Gestion des IDs d'import des commandes

Ce guide concerne les données `command_blocks` de `txt.txt`. Il ne concerne pas les identifiants internes des pages Wiki.js.

## Règles

- Chaque commande doit avoir un ID non vide et unique dans le fichier.
- Les IDs existants (`c-*` ou `cmd-*`) sont stables : ne pas les renommer pour corriger une erreur d'import, car des données de l'application peuvent déjà les référencer.
- Pour une nouvelle commande, utiliser le prochain ID numérique `cmd-*` indiqué par le vérificateur.
- Un `folder_id`, lorsqu'il existe, doit respecter le format `f-*`. Le fichier actuel ne contient pas la définition des dossiers; le vérificateur ne peut donc pas confirmer leur existence dans l'application cible.
- Ne pas importer un [[Glossary:JSON]] tronqué ou invalide. Restaurer l'export complet avant toute tentative; ne pas supprimer automatiquement la dernière commande incomplète.

## Vérification

Depuis la racine du pack :

```bash
python3 00-administration/02-operations-wikijs/verify-command-import.py
```

Pour contrôler un autre export et obtenir le prochain ID proposé :

```bash
python3 00-administration/02-operations-wikijs/verify-command-import.py chemin/vers/export.json --next-id
```

Le contrôle valide la syntaxe JSON, la structure `command_blocks.commands`, le format des IDs, leur unicité et le format des `folder_id`. Il ne remplace pas l'import de test et ne vérifie pas les contraintes propres à l'application cible.