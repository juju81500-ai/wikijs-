# Fiche_Simple_-_Hote_Windows_11_Deploiement_Installer_Applications_Profils.md

- **Environnement** : Parc de postes utilisateur: poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Catégorie** : déploiement de poste de travail

---

## Problème précis à résoudre

Déployer uniquement les applications autorisées.

## 1. Hors-Production (Lab / Test / POC)

1. Déployer les applications par le catalogue ou l'outil de gestion du parc (ex. **Portail d'entreprise** ou **Centre logiciel**).
   👉 Explication : seules les applications autorisées sont installées.

2. Valider le lancement, les mises à jour, les licences et l'accès aux services métiers.
   👉 Explication : vérifie le fonctionnement réel.

3. Lister les applications installées :
   ```powershell
   Get-Package | Select-Object Name, Version
   ```
   👉 Explication : permet de comparer avec la liste autorisée.

4. Ne pas installer de logiciel tiers par script non approuvé.
   👉 Explication : évite l'introduction de logiciels non maîtrisés.

## 2. Production — Contrôles

Comparer la liste installée au catalogue approuvé.

## 3. Production — Sécurité

- Pas de téléchargement d'installateurs depuis des sources non approuvées.

## Validation et retour arrière

- **Validation** : les applications prévues sont installées et fonctionnent, aucune autre n'est présente.
- **Retour arrière** : désinstaller l'application fautive via l'outil de gestion du parc.

## Si le problème n'est pas résolu

- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Guide complet](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production#5-installer-les-applications-et-profils)