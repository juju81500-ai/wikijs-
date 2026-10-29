# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Niveaux_Fonctionnels_Foret

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions
- **Tags** : `windows-server`, `windows-server-2016`, `windows-server-2019`, `windows-server-2022`, `active-directory`, `niveaux-fonctionnels`, `adprep`

---

## Problème précis à résoudre

Contrôler les niveaux fonctionnels et préparer la forêt avant d'introduire un contrôleur de domaine 2022 dans un annuaire 2016/2019.

## 1. Hors-Production (Lab / Test / POC)

1. Lire les niveaux et la version de schéma :
   ```powershell
   Get-ADForest | Select-Object ForestMode
   Get-ADDomain | Select-Object DomainMode
   Get-ADObject (Get-ADRootDSE).schemaNamingContext -Property objectVersion
   ```
   👉 Explication : ForestMode/DomainMode donnent les niveaux actuels ; `objectVersion` donne la version du schéma.
2. Contrôler l'état de la réplication avant toute modification :
   ```powershell
   repadmin /replsummary
   dcdiag /q
   ```
   👉 Explication : ne rien faire sur une forêt en erreur de réplication.
3. Préparer le schéma (nécessite Administrateur de l'entreprise et Administrateur du schéma) : l'assistant de promotion d'un DC 2022 l'exécute automatiquement ; à défaut, lancer manuellement depuis le média 2022 (dossier `support\adprep`) :
   ```powershell
   adprep.exe /forestprep
   adprep.exe /domainprep
   ```
   👉 Explication : à exécuter sur le maître de schéma puis l'émulateur PDC, après sauvegarde de l'état système.
4. Relever le niveau fonctionnel seulement quand plus aucun DC ancien n'existe (exemple ; remplacer `NOM_FORET`) :
   ```powershell
   Set-ADForestMode -Identity NOM_FORET -ForestMode Windows2016Forest
   ```
   👉 Explication : Windows Server 2022 n'introduit pas de niveau supérieur à celui de 2016 ; vérifier la liste publiée par Microsoft.

## 2. Production — Contrôles

- Sauvegarder l'état système de chaque DC et noter le rôle FSMO de chacun avant l'extension du schéma.
- Considérer l'élévation de niveau comme non réversible en pratique.

## 3. Production — Sécurité

- Limiter les groupes Administrateurs de l'entreprise/du schéma dans le temps de l'opération.

## Validation et retour arrière

- **Validation** : `repadmin /replsummary` sans erreur, nouvelles versions de schéma visibles. **Retour arrière** : l'extension du schéma ne s'annule pas ; seule une restauration d'annuaire de la forêt le permet (procédure de récupération de forêt Microsoft).

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Windows-Server-2016-2019-2022.md)
- [Microsoft Learn — Niveaux fonctionnels AD DS](https://learn.microsoft.com/fr-fr/windows-server/identity/ad-ds/active-directory-functional-levels)
- [Microsoft Learn — Adprep](https://learn.microsoft.com/fr-fr/windows-server/identity/ad-ds/deploy/upgrade-domain-controllers)
