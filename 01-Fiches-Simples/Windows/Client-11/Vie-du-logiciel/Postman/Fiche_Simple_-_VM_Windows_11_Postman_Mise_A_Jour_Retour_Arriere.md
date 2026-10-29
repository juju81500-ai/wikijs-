# Fiche_Simple_-_VM_Windows_11_Postman_Mise_A_Jour_Retour_Arriere

- **Environnement** : Poste Windows 11 géré, compte standard, Postman Desktop et Newman
- **OS / Version** : Windows 11 Client
- **Catégorie** : API / mise à jour et retour arrière
- **Tags** : `windows-11`, `postman`, `api`, `newman`, `vie-du-logiciel`

---

## Problème précis à résoudre

Mettre à jour Postman et Newman sur Windows 11 de manière contrôlée, avec sauvegarde des collections et retour arrière possible.

## 1. Hors-Production (Lab / Test / POC)

1. Sauvegarder collections et environnements :
   ```text
   Postman > COLLECTION_LAB > ⋯ > Export > enregistrer dans SAUVEGARDE_DIR
   ```
   👉 Explication : Remplacer `SAUVEGARDE_DIR` par le dossier de sauvegarde ; exporter l'environnement sans secret.

2. Relever la version actuelle :
   ```powershell
   winget list --id Postman.Postman -e
   ```
   👉 Explication : Note la version installée avant mise à jour.

3. Mettre à jour Postman :
   ```powershell
   winget upgrade --id Postman.Postman -e
   ```
   👉 Explication : Applique la version publiée. Alternative GUI : Paramètres > Update / About Postman (libellé à vérifier).

4. Mettre à jour Newman :
   ```powershell
   npm outdated -g newman
   npm install -g newman@latest
   newman --version
   ```
   👉 Explication : Vérifier d'abord les notes de version ; fixer `VERSION_NEWMAN` à la place de `latest` en production.

5. Retour arrière de Newman :
   ```powershell
   npm install -g newman@VERSION_PRECEDENTE
   ```
   👉 Explication : Remplacer `VERSION_PRECEDENTE` par la version validée.

6. Retour arrière de Postman :
   ```powershell
   winget uninstall --id Postman.Postman -e
   winget install --id Postman.Postman -e --version VERSION_PRECEDENTE
   ```
   👉 Explication : winget n'accepte une version précise que si elle est encore publiée dans la source : sinon utiliser l'installeur archivé et vérifié. Puis réimporter les collections.

## 2. Production — Contrôles

Lire les notes de version Postman avant diffusion ; mettre à jour d'abord un poste pilote ; exporter les collections et environnements (sans secrets) avant la mise à jour.

## 3. Production — Sécurité

- Télécharger les mises à jour uniquement depuis le canal officiel.
- Désactiver la mise à jour automatique sur les postes figés si la politique l'impose (à vérifier dans les paramètres).
- Sauvegarder les exports hors du poste avant de désinstaller.

## Validation et retour arrière

- **Validation** : Nouvelle version affichée, collections accessibles, recette Newman réussie.
- **Retour arrière** : Réinstaller la version précédente validée ou restaurer la copie `/opt/Postman.OLD` ; réimporter les collections exportées.

## Si le problème n'est pas résolu

- [Postman — documentation officielle](https://learning.postman.com/docs/)
- [Postman — téléchargement](https://www.postman.com/downloads/)
- [Newman — documentation](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/)
- [Fiche d'entrée Postman](../../../../Logiciels/11-Scripting-developpement-et-administration/Fiche_Logiciel_-_Postman.md)
- [Fiche connexe Prerequis_Limites](<Fiche_Simple_-_VM_Windows_11_Postman_Prerequis_Limites.md>)
- [Fiche connexe Installer](<Fiche_Simple_-_VM_Windows_11_Postman_Installer.md>)
