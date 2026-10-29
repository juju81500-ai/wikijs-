# Fiche_Simple_-_VM_Debian_13_VSCode_Premiere_Ouverture.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / configuration
- **Tags** : `debian13`, `vscode`, `apt`, `profil`, `configuration`

---

## Problème précis à résoudre

Ouvrir VS Code et configurer le profil utilisateur sans fuite de secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir un dossier de travail utilisateur et vérifier le chemin dans la barre de titre.
   👉 Explication : confirme le bon espace de travail.

2. Garder les réglages par défaut pour mises à jour, espaces de travail et extensions, sauf politique contraire.
   👉 Explication : évite les écarts avec l'organisation.

3. Créer des profils séparés avec **Fichier > Préférences > Profils** si plusieurs rôles nécessitent des extensions différentes.
   👉 Explication : isole les extensions par usage.

4. En cas de problème de terminal intégré, vérifier le PATH, le shell et les journaux de l'application avant de modifier des permissions.
   👉 Explication : évite un diagnostic erroné.

## 2. Production — Contrôles

Ne synchroniser les paramètres qu'avec un compte et un service autorisés.

## 3. Production — Sécurité

- Aucun secret ni identifiant dans les réglages versionnés du workspace.
- Pas de synchronisation vers un compte non autorisé.

## Validation et retour arrière

- **Validation** : VS Code ouvre le dossier avec le profil attendu.
- **Retour arrière** : supprimer le profil créé ou rétablir les réglages par défaut.

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/80_Deploiement_Visual_Studio_Code_1.143.1_Debian_13.md#4-premiere-ouverture-et-configuration)
