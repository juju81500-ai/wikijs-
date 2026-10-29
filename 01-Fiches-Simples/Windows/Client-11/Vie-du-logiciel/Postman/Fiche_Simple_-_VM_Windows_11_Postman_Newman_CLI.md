# Fiche_Simple_-_VM_Windows_11_Postman_Newman_CLI

- **Environnement** : Poste Windows 11 géré, compte standard, Postman Desktop et Newman
- **OS / Version** : Windows 11 Client
- **Catégorie** : API / exécution en ligne de commande
- **Tags** : `windows-11`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Installer Newman et exécuter une collection Postman exportée en ligne de commande PowerShell, avec rapport JUnit et secret injecté par variable.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Node.js puis Newman :
   ```powershell
   node --version
   npm --version
   npm install -g newman
   newman --version
   ```
   👉 Explication : Node.js LTS est requis (`winget install --id OpenJS.NodeJS.LTS -e` si absent). Si npm global est interdit, voir la politique du poste.

2. Exécuter la collection avec l'environnement exporté :
   ```powershell
   newman run .\COLLECTION_LAB.postman_collection.json `
     -e .\ENV_LAB.postman_environment.json `
     --env-var "API_TOKEN=$env:API_TOKEN" `
     --reporters cli,junit --reporter-junit-export .\newman-report.xml
   ```
   👉 Explication : Remplacer les noms de fichiers ; le jeton est lu depuis la variable `API_TOKEN` de la session et n'est pas écrit dans le fichier.

3. Lire le code de sortie :
   ```powershell
   $LASTEXITCODE
   ```
   👉 Explication : `0` = tous les tests réussis ; non nul = au moins une assertion en échec.

4. Nettoyer le secret de la session :
   ```powershell
   Remove-Item Env:API_TOKEN
   ```
   👉 Explication : Évite qu'un processus ultérieur hérite du jeton.

## 2. Production — Contrôles

Fixer la version de Newman et de Node.js ; exécuter en CI avec un compte de service ; conserver le rapport JUnit comme preuve de recette.

## 3. Production — Sécurité

- Ne pas utiliser `--insecure` en production ; importer plutôt l'autorité de certification interne.
- Injecter les secrets via variable d'environnement ou coffre CI, jamais dans le fichier d'environnement exporté.
- Éviter les secrets dans l'historique du shell : saisie masquée.

## Validation et retour arrière

- **Validation** : `newman run` termine avec le code de sortie 0 et produit le rapport attendu.
- **Retour arrière** : Réinstaller la version précédente : `npm install -g newman@VERSION_PRECEDENTE` et relancer la recette.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](../../../../Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_Postman.md)
- [Fiche connexe Prerequis_Limites](<Fiche_Simple_-_VM_Windows_11_Postman_Prerequis_Limites.md>)
- [Fiche connexe Installer](<Fiche_Simple_-_VM_Windows_11_Postman_Installer.md>)
