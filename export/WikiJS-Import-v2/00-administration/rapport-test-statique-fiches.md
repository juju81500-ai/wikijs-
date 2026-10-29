---
title: "Rapport du test statique de toutes les fiches"
description: "Test automatique du 29 octobre 2026 sur les 2 854 documents de 01-Fiches-Simples et 02-Fiches-Completes (hors 06-Documentation-ext, 05-Referentiel et export/). Ce n'est pas un test d'exécution : aucune commande n'a été lancée sur un OS réel. Il détecte seulement les erreurs visibles sans exécuter. L"
published: true
date: 2026-10-29T21:35:05Z
tags: ["controle", "tests", "rapport", "qualite"]
editor: markdown
dateCreated: 2026-10-29T21:35:05Z
dateModified: 2026-10-29T21:35:05Z
---

# Rapport du test statique de toutes les fiches

- **Tags** : `controle`, `tests`, `rapport`, `qualite`

Test automatique du 29 octobre 2026 sur les 2 854 documents de `01-Fiches-Simples` et `02-Fiches-Completes` (hors `06-Documentation-ext`, `05-Referentiel*` et `export/`). **Ce n'est pas un test d'exécution** : aucune commande n'a été lancée sur un OS réel. Il détecte seulement les erreurs visibles sans exécuter. La [liste de contrôle stricte](/00-administration/liste-controle-tests-fiches-simples) reste obligatoire avant la production.

## Contrôles réalisés

| Contrôle | Résultat |
|---|---|
| Structure obligatoire (titre, problème, hors-production, production, sécurité) | Conforme. Les 40 fiches qui s'écartent du modèle ont une structure équivalente (« Objectif », « Méthode GUI / PowerShell », « Diagnostic ») ; aucune fiche vide |
| Liens relatifs | 0 lien cassé |
| Blocs de code non fermés | 0 |
| Fiche avec commandes mais sans « 👉 Explication » | 0 |
| Syntaxe `bash -n` des blocs `bash` (placeholders `<X>` neutralisés) | 17 alertes, toutes des fichiers de configuration (BIND, etc.) placés dans un bloc `bash` : faux positifs |
| Secrets en clair | 1 corrigé (Keycloak : mot de passe de lab remplacé par `<MOT_DE_PASSE_ADMIN_A_REMPLACER>`). Les autres occurrences sont des placeholders |
| `curl \| sh` ou `curl \| bash` exécutés | 2 corrigés (K3s, GitLab : téléchargement, lecture avec `less`, puis exécution). Les autres occurrences sont des avertissements « ne jamais faire » |
| `chmod 777` | Uniquement dans des avertissements |
| URL en `http://` | Dépôts APT (signés par GPG), WSUS interne, exemples : acceptables |

## Ce que le test ne couvre pas

- Existence réelle des paquets, versions, URL de dépôts et menus d'interface.
- Syntaxe PowerShell (`pwsh` absent de la machine de test).
- Comportement des commandes, retours arrière, droits, réseau.

Ces points relèvent de la liste de contrôle stricte (verdicts OK / OK avec écarts / KO).