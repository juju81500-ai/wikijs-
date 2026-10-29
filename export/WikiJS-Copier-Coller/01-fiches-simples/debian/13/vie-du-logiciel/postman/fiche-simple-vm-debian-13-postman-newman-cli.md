# Fiche_Simple_-_VM_Debian_13_Postman_Newman_CLI

- **Environnement** : VM Debian 13 Trixie avec bureau graphique, Postman Desktop et Newman
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : API / exécution en ligne de commande

---

## Problème précis à résoudre

Installer Newman et exécuter une collection Postman exportée depuis le shell Debian 13, avec rapport JUnit et secret injecté par variable d'environnement.

## 1. Hors-Production (Lab / Test / POC)

1. Installer Node.js puis Newman :
   ```bash
   sudo apt update
   sudo apt install -y nodejs npm
   node --version
   sudo npm install -g newman
   newman --version
   ```
   👉 Explication : Utilise Node.js et npm du dépôt Debian ; vérifier que la version de Node.js est supportée par la version de Newman choisie (documentation Newman). `npm install -g` installe sous `/usr/local`.

2. Exécuter la collection avec l'environnement exporté :
   ```bash
   newman run COLLECTION_LAB.postman_collection.json \
     -e ENV_LAB.postman_environment.json \
     --env-var "API_TOKEN=$API_TOKEN" \
     --reporters cli,junit --reporter-junit-export newman-report.xml
   ```
   👉 Explication : Remplacer les noms de fichiers ; le jeton est lu depuis la variable `API_TOKEN` de la session et n'est pas écrit dans le fichier.

3. Lire le code de sortie :
   ```bash
   echo $?
   ```
   👉 Explication : `0` = tous les tests réussis ; non nul = au moins une assertion en échec.

4. Nettoyer le secret de la session :
   ```bash
   unset API_TOKEN
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
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Prerequis_Limites](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-prerequis-limites>)
- [Fiche connexe Installer](</01-fiches-simples/debian/13/vie-du-logiciel/postman/fiche-simple-vm-debian-13-postman-installer>)