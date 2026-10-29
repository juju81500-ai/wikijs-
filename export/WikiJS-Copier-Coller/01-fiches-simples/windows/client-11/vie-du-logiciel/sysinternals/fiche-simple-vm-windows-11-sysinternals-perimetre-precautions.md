# Fiche_Simple_-_VM_Windows_11_Sysinternals_Perimetre_Precautions.md

- **Environnement** : Poste Windows 11 administré, diagnostic défensif local
- **OS / Version** : Windows 11; suite Sysinternals de Microsoft Learn ou Microsoft Store
- **Catégorie** : diagnostic / cadrage

---

## Problème précis à résoudre

Cadrer l'usage de Sysinternals et obtenir l'autorisation avant d'examiner un poste.

## 1. Hors-Production (Lab / Test / POC)

1. Obtenir l'autorisation avant d'examiner un poste d'utilisateur ou de recueillir une trace.
   👉 Explication : les traces contiennent noms, chemins, arguments, données personnelles ou secrets.

2. Se limiter à l'inventaire local, au diagnostic de processus et au démarrage automatique sur un poste administré.
   👉 Explication : aucun accès distant, modification de comptes ni exécution sur des tiers.

3. Contrôler le contexte de droits :
   ```powershell
   whoami /groups
   ```
   👉 Explication : Affiche les groupes de la session; utiliser un compte standard et n'élever les droits que si le diagnostic l'exige.

## 2. Production — Contrôles

Limiter la collecte et protéger les fichiers produits.

## 3. Production — Sécurité

- Minimisation des données et conservation définie.

## Validation et retour arrière

- **Validation** : autorisation obtenue et périmètre écrit.
- **Retour arrière** : aucun changement n'a été fait.

## Si le problème n'est pas résolu

- [Microsoft Learn — Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [Guide complet — étape 1](/02-fiches-completes/windows/client-11/installation-deploiement/123-administration-microsoft-sysinternals-windows-11#1-perimetre-et-precautions)