# Fiche_Simple_-_VM_Windows_11_Postman_Tests

- **Environnement** : Poste Windows 11 géré, compte standard, Postman Desktop et Newman
- **OS / Version** : Windows 11 Client
- **Catégorie** : API / tests automatisés

---

## Problème précis à résoudre

Ajouter des tests Postman (scripts de test) vérifiant statut, temps de réponse et contenu pour une collection de lab sous Windows 11.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l'onglet de scripts de la requête :
   ```text
   COLLECTION_LAB > GET {{BASE_URL}}/health > onglet Scripts (ou Tests selon la version) > Post-response
   ```
   👉 Explication : L'emplacement exact de l'onglet varie selon la version de Postman : à vérifier dans l'interface.

2. Ajouter les assertions (JavaScript Postman) :
   ```javascript
   pm.test('Statut 200', function () { pm.response.to.have.status(200); });
   pm.test('Temps de réponse < 800 ms', function () { pm.expect(pm.response.responseTime).to.be.below(800); });
   pm.test('Corps JSON', function () { pm.response.to.be.json; });
   ```
   👉 Explication : Vérifie le statut, le temps de réponse (seuil à adapter) et le format JSON.

3. Lancer la recette dans le Collection Runner :
   ```text
   COLLECTION_LAB > Run > choisir ENV_LAB > Run COLLECTION_LAB
   ```
   👉 Explication : Le résumé affiche les tests réussis et en échec ; corriger avant toute exécution automatisée.

4. Exporter la collection mise à jour :
   ```text
   COLLECTION_LAB > ⋯ > Export > Collection v2.1
   ```
   👉 Explication : Prépare l'exécution Newman avec les mêmes tests.

## 2. Production — Contrôles

Chaque requête critique a au moins un test de statut et de structure ; les tests ne modifient pas de données de production ; le Collection Runner sert de recette locale.

## 3. Production — Sécurité

- Ne pas journaliser `pm.environment.get('API_TOKEN')` dans `console.log`.
- Relire tout script de test importé d'un tiers avant exécution.
- Limiter les tests destructifs (DELETE, PUT) aux environnements de lab.

## Validation et retour arrière

- **Validation** : Le Collection Runner indique tous les tests passés sur l'environnement LAB.
- **Retour arrière** : Restaurer la version précédente de la collection (Import du JSON sauvegardé) ou retirer les scripts ajoutés.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-postman)
- [Fiche connexe Prerequis_Limites](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-prerequis-limites>)
- [Fiche connexe Installer](</01-fiches-simples/windows/client-11/vie-du-logiciel/postman/fiche-simple-vm-windows-11-postman-installer>)