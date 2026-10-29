# Fiche_Simple_-_VM_Debian_13_Postman_Workspace_Collections

- **Environnement** : VM Debian 13 Trixie avec bureau graphique, Postman Desktop et Newman
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : API / workspace et collections
- **Tags** : `debian13`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Créer un workspace Postman maîtrisé et une première collection de requêtes de lab sur Debian 13, organisée en dossiers et exportable.

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
   ```bash
   grep -inE 'password|token|secret' COLLECTION_LAB.postman_collection.json
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
- [Fiche d'entrée Postman](../../../../Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_Postman.md)
- [Fiche connexe Prerequis_Limites](<Fiche_Simple_-_VM_Debian_13_Postman_Prerequis_Limites.md>)
- [Fiche connexe Installer](<Fiche_Simple_-_VM_Debian_13_Postman_Installer.md>)
