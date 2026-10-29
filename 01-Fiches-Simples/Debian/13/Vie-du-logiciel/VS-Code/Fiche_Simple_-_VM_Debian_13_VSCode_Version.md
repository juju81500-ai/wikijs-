# Fiche_Simple_-_VM_Debian_13_VSCode_Version.md

- **Environnement** : Poste Debian 13 amd64, VS Code Stable installé via le dépôt APT Microsoft
- **OS / Version** : Debian 13 Trixie amd64; Visual Studio Code Stable 1.143.1
- **Catégorie** : éditeur / cadrage
- **Tags** : `debian13`, `vscode`, `apt`, `prerequis`

---

## Problème précis à résoudre

Confirmer la version, l'architecture et le périmètre avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Exécuter :
   ```bash
   dpkg --print-architecture
   ```
   👉 Explication : doit afficher `amd64`, seule architecture visée ici.

2. Consulter la version Stable sur la page des mises à jour de VS Code (1.143.1 au gel du guide).
   👉 Explication : les versions ultérieures arrivent via le dépôt APT.

3. Exclure runtimes, compilateurs, extensions de langage, accès distants et Copilot.
   👉 Explication : ils s'installent seulement selon le besoin et les règles de l'organisation.

## 2. Production — Contrôles

Vérifier la licence Microsoft de VS Code; ce n'est pas la distribution communautaire Code - OSS.

## 3. Production — Sécurité

- N'installer que le nécessaire.
- Respecter la politique de l'organisation.

## Validation et retour arrière

- **Validation** : l'architecture est `amd64` et le périmètre est validé.
- **Retour arrière** : aucune modification à cette étape.

## Si le problème n'est pas résolu

- [Visual Studio Code — installation Linux](https://code.visualstudio.com/docs/setup/linux)
- [Visual Studio Code — licence](https://code.visualstudio.com/License)
- [Guide complet Déployer Visual Studio Code Stable 1.143.1 sur Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/80_Deploiement_Visual_Studio_Code_1.143.1_Debian_13.md#1-version-et-perimetre)
