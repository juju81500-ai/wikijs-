---
title: "Fiche Simple - VM Windows 11 Postman Workspace Collections"
description: "Créer un workspace Postman maîtrisé et une première collection de requêtes de lab, organisée en dossiers et exportable."
published: true
date: 2026-10-29T20:56:02Z
tags: ["windows-11", "postman", "api", "newman", "vie-du-logiciel"]
editor: markdown
dateCreated: 2026-10-29T20:56:02Z
dateModified: 2026-10-29T20:56:02Z
---

# Fiche_Simple_-_VM_Windows_11_Postman_Workspace_Collections

- **Environnement** : Poste Windows 11 géré, compte standard, Postman Desktop et Newman
- **OS / Version** : Windows 11 Client
- **Catégorie** : API / workspace et collections
- **Tags** : `windows-11`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Créer un workspace Postman maîtrisé et une première collection de requêtes de lab, organisée en dossiers et exportable.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un workspace :
   ```text
   Postman > Workspaces > Create Workspace > Blank workspace > Nom : WORKSPACE_LAB > Visibilité : Personal ou Private > Create
   ```
   👉 Explication : Remplacer `WORKSPACE_LAB` par le nom du workspace ; choisir une visibilité privée par défaut.

2. Créer la collection et un dossier :
   ```text
   Collections > + > Blank collection > nommer COLLECTION_LAB > Add folder > Santé
   ```
   👉 Explication : Remplacer `COLLECTION_LAB` par le nom de la collection ; un dossier par domaine fonctionnel facilite la recette.

3. Ajouter une requête de test :
   ```text
   COLLECTION_LAB > Add request > GET {{BASE_URL}}/health > Save
   ```
   👉 Explication : La variable `{{BASE_URL}}` sera définie dans la fiche Environnements et secrets ; `/health` est un exemple de point de contrôle à adapter.

4. Exporter la collection (sauvegarde) :
   ```text
   COLLECTION_LAB > ⋯ > Export > Collection v2.1 > enregistrer COLLECTION_LAB.postman_collection.json
   ```
   👉 Explication : Le JSON sert de sauvegarde et d'entrée à Newman ; vérifier qu'il ne contient aucun secret avant stockage.

5. Contrôler le fichier exporté :
   ```powershell
   Select-String -Path .\COLLECTION_LAB.postman_collection.json -Pattern 'password|token|secret' -CaseSensitive:$false
   ```
   👉 Explication : Doit ne retourner aucune valeur réelle ; seuls des noms de variables sont admis.

## 2. Production — Contrôles

Choisir le type de workspace (Personal, Team, Private) selon la politique de partage ; nommer collections et dossiers selon une convention ; versionner les exports JSON hors des secrets.

## 3. Production — Sécurité

- Préférer un workspace privé tant que la collection contient des URL internes.
- Ne jamais enregistrer de jeton ou mot de passe dans une requête, un en-tête ou un exemple de réponse.
- Limiter les droits d'édition du workspace d'équipe au strict nécessaire.

## Validation et retour arrière

- **Validation** : Workspace et collection existent, la requête de lab renvoie le code attendu et l'export JSON est lisible.
- **Retour arrière** : Supprimer la collection de test ou restaurer l'export JSON précédent via Import.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Prerequis_Limites](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-prerequis-limites>)
- [Fiche connexe Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-installer>)