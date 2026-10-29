# Fiche_Simple_-_VM_Windows_11_Bitwarden_Prerequis_Limites

- **Environnement** : Poste Windows 11 géré avec compte de test
- **OS / Version** : Windows 11 Client
- **Catégorie** : gestionnaire de mots de passe / client
- **Tags** : `windows-11`, `bitwarden`, `mots-de-passe`, `mfa`, `securite`
---

## Problème précis à résoudre

Définir client, compte autorisé, MFA, récupération et poste géré avant d’y placer des secrets.

## 1. Hors-Production (Lab / Test / POC)

1. Confirmer source et politique
   ```text
   Navigateur > saisir https://bitwarden.com/download/ puis sélectionner Windows.
   ```
   👉 Explication : vérifier domaine et usage autorisé par l’organisation.

2. Vérifier poste et architecture
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName,WindowsVersion,OsArchitecture
   ```
   👉 Explication : utiliser Windows 11 géré et compte standard.

3. Établir procédure recovery
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : tester récupération avant migration de secrets. Détail à confirmer dans la documentation officielle avant application : Documenter MFA, code récupération et contact support; ne pas écrire le mot de passe maître ici.

## 2. Production — Contrôles

Faire valider service, organisation, appareils, extension navigateur et procédure de sortie par sécurité.

## 3. Production — Sécurité

- Utiliser mot de passe maître unique et MFA.
- Ne pas inscrire secret réel sur poste partagé/non chiffré.
- Installer uniquement depuis sources officielles.

## Validation et retour arrière

- **Validation** : Poste, MFA et récupération sont définis avant transfert du coffre.
- **Retour arrière** : Ne pas migrer tant que compte et recovery ne sont pas testés.

## Si le problème n'est pas résolu

- [Bitwarden — téléchargement officiel](https://bitwarden.com/download/)
- [Bitwarden — application bureau](https://bitwarden.com/help/desktop-app/)
- [Bitwarden — exportation](https://bitwarden.com/help/export-your-data/)
- [Bitwarden — MFA](https://bitwarden.com/help/two-step-login/)
- [Fiche connexe](<Fiche_Simple_-_VM_Windows_11_Bitwarden_Installer.md>)
