# Fiche_Simple_-_VM_Windows_11_Sysinternals_Retour_Arriere_Limites.md

- **Environnement** : Poste Windows 11 administré, diagnostic défensif local
- **OS / Version** : Windows 11; suite Sysinternals de Microsoft Learn ou Microsoft Store
- **Catégorie** : diagnostic / retour arrière
- **Tags** : `windows11`, `sysinternals`, `diagnostic`, `defense`

---

## Problème précis à résoudre

Nettoyer après usage et connaître les limites des outils.

## 1. Hors-Production (Lab / Test / POC)

1. Fermer les outils et supprimer les exports temporaires suivant la politique :
   ```powershell
   Get-Process procexp64, procmon64, autoruns64 -ErrorAction SilentlyContinue | Stop-Process
   Remove-Item C:\Temp\Sysinternals-Exports -Recurse -Confirm
   ```
   👉 Explication : remplacer le dossier d'export; `-Confirm` demande validation avant suppression.

2. Restaurer les préférences utilisateur sauvegardées si nécessaire :
   ```powershell
   reg import C:\Sauvegardes\sysinternals-prefs.reg
   ```
   👉 Explication : réimporte les clés exportées avant l'usage (par exemple `HKCU\Software\Sysinternals`); la simple exécution ne modifie généralement pas la configuration.

3. Rappeler que Sysinternals observe mais ne donne pas de verdict antivirus.
   👉 Explication : une signature valide ne garantit pas qu'un fichier est sûr.

## 2. Production — Contrôles

Les outils de la suite qui modifient comptes, processus, démarrage ou état système ne sont pas couverts.

## 3. Production — Sécurité

- Ne pas utiliser les outils de modification hors cadre approuvé.

## Validation et retour arrière

- **Validation** : plus d'outil ouvert ni d'export temporaire résiduel.
- **Retour arrière** : sans objet : cette étape est elle-même le retour arrière.

## Si le problème n'est pas résolu

- [Microsoft Learn — Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [Guide complet — étape 5](../../../../../02-Fiches-Completes/Windows/Client-11/Installation-Deploiement/123_Administration_Microsoft_Sysinternals_Windows_11.md#5-retour-arriere-et-limites)
