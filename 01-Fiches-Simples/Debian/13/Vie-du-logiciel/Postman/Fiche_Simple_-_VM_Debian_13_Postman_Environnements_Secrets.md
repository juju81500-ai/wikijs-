# Fiche_Simple_-_VM_Debian_13_Postman_Environnements_Secrets

- **Environnement** : VM Debian 13 Trixie avec bureau graphique, Postman Desktop et Newman
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : API / variables et secrets
- **Tags** : `debian13`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Séparer URL, paramètres et secrets avec des environnements Postman et des variables de type secret sur Debian 13, sans aucun secret en clair.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'environnement :
   ```text
   Environments > + > nommer ENV_LAB > variables : BASE_URL (type default, Initial value https://api.lab.example.net), API_TOKEN (type secret, valeurs vides) > Save
   ```
   👉 Explication : Remplacer `ENV_LAB` et l'URL par vos valeurs ; la variable `API_TOKEN` en type `secret` est masquée dans l'interface.

2. Saisir le secret en local uniquement :
   ```text
   ENV_LAB > API_TOKEN > Current value : coller le jeton de lab fourni par le coffre (ex. Bitwarden) > Save ; laisser Initial value vide
   ```
   👉 Explication : Le jeton reste en « Current value » locale, non synchronisée ; ne jamais l'écrire dans la fiche ou l'historique.

3. Sélectionner l'environnement et utiliser les variables :
   ```text
   Sélecteur en haut à droite > ENV_LAB ; Authorization > Bearer Token > Token : {{API_TOKEN}}
   ```
   👉 Explication : La requête référence le jeton par variable ; il n'apparaît pas en clair dans la requête.

4. Alternative : secret depuis une variable du système pour Newman :
   ```bash
   read -rs -p 'Jeton API : ' API_TOKEN && export API_TOKEN
   ```
   👉 Explication : Saisie masquée, valeur limitée à la session du shell ; à fermer ou effacer après usage.

5. Exporter l'environnement sans secret :
   ```text
   Environments > ENV_LAB > ⋯ > Export > vérifier que API_TOKEN n'a pas de valeur
   ```
   👉 Explication : Contrôler le JSON exporté avant de le partager.

## 2. Production — Contrôles

Définir un environnement par cible (LAB, RECETTE, PROD) ; ne mettre que des valeurs non sensibles en « Initial value » ; contrôler que l'export ne contient pas de secret.

## 3. Production — Sécurité

- Ne jamais écrire de secret dans « Initial value » : cette valeur est synchronisée et partagée.
- Utiliser le type `secret` pour masquer la valeur et la garder en « Current value » locale.
- Ne pas exporter ni committer un environnement contenant des « Current value » sensibles ; révoquer un jeton exposé.

## Validation et retour arrière

- **Validation** : Les requêtes utilisent `{{BASE_URL}}` et `{{API_TOKEN}}`, la valeur du jeton est masquée et absente de l'export.
- **Retour arrière** : Supprimer l'environnement de test, révoquer le jeton de lab et recréer l'environnement depuis le modèle sans valeurs.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](../../../../Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_Postman.md)
- [Fiche connexe Prerequis_Limites](<Fiche_Simple_-_VM_Debian_13_Postman_Prerequis_Limites.md>)
- [Fiche connexe Installer](<Fiche_Simple_-_VM_Debian_13_Postman_Installer.md>)
