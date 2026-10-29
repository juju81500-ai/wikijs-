# Fiche_Simple_-_Cloud_Entra_ID_Acces_Conditionnel_Report_Only

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services
- **Tags** : `entra-id`, `acces-conditionnel`, `report-only`, `what-if`, `graph`

---

## Problème précis à résoudre

Créer une politique d'accès conditionnel exigeant le MFA en mode report-only, la valider avec What If et les journaux, puis seulement l'activer sur pilote.

## 1. Hors-Production (Lab / Test / POC)

1. Portail : Entra admin center → Entra ID → Conditional Access → Policies → New policy (ou Protection → Conditional Access selon l'interface).
   👉 Explication : nom recommandé : CA-PILOTE-MFA (à remplacer) ; licence requise à vérifier.

2. Assignments → Users : Include = GRP-MFA-PILOTE ; Exclude = GRP-URGENCE-EXCLUS (comptes d'urgence).
   👉 Explication : ne jamais cibler Tous les utilisateurs au départ.

3. Target resources : Include = All resources (ou application pilote) ; Grant : Require multifactor authentication.
   👉 Explication : vérifier l'impact sur les applications avant d'élargir.

4. Enable policy = Report-only puis Create.
   👉 Explication : la politique est évaluée et journalisée sans bloquer.

5. Équivalent Graph PowerShell (ID_GROUPE_PILOTE et ID_GROUPE_URGENCE à remplacer) :
   ```powershell
   Connect-MgGraph -Scopes 'Policy.ReadWrite.ConditionalAccess','Application.Read.All' -ContextScope Process
   $p = @{
     displayName = 'CA-PILOTE-MFA'
     state = 'enabledForReportingButNotEnforced'
     conditions = @{
       users = @{ includeGroups = @('ID_GROUPE_PILOTE'); excludeGroups = @('ID_GROUPE_URGENCE') }
       applications = @{ includeApplications = @('All') }
       clientAppTypes = @('all')
     }
     grantControls = @{ operator = 'OR'; builtInControls = @('mfa') }
   }
   New-MgIdentityConditionalAccessPolicy -BodyParameter $p
   ```
   👉 Explication : crée la politique en report-only ; Policy.ReadWrite.ConditionalAccess est un droit d'écriture, à utiliser seulement par le rôle approprié.

6. Valider avec What If : Conditional Access → Policies → What If → saisir utilisateur pilote, application, plateforme et IP.
   👉 Explication : vérifie quelles politiques s'appliqueraient ; tester aussi un compte hors pilote et un compte d'urgence (aucune application attendue).

7. Analyser les connexions : Entra ID → Sign-in logs → onglet Conditional Access (Report-only) ; ou le classeur Conditional Access insights and reporting.
   👉 Explication : identifier les échecs probables avant activation.

8. Lister les politiques via Graph :
   ```powershell
   Connect-MgGraph -Scopes 'Policy.Read.All' -ContextScope Process
   Get-MgIdentityConditionalAccessPolicy | Select DisplayName,State,Id
   ```
   👉 Explication : contrôle de l'état ; l'API d'évaluation What If Graph est disponible en préversion selon documentation, à vérifier avant usage.

## 2. Production — Contrôles

Production : période report-only suffisante, journaux analysés, exclusions d'urgence confirmées, activation limitée au pilote (state `enabled`), puis élargissement par vagues approuvées.

## 3. Production — Sécurité

- Ne pas élargir à tous les utilisateurs sans pilote validé.
- Toujours exclure les comptes d'urgence (et surveiller leur usage).
- Éviter un blocage large des protocoles anciens sans analyse préalable.
- Utiliser un rôle dédié (administrateur d'accès conditionnel) et PIM.

## Validation et retour arrière

- **Validation** : What If conforme, journaux report-only sans refus inattendu.
- **Retour arrière** : portail Enable policy = Off, ou Graph :
  ```powershell
  Update-MgIdentityConditionalAccessPolicy -ConditionalAccessPolicyId ID_POLITIQUE -State 'disabled'
  ```
  (ID_POLITIQUE à remplacer). Une suppression n'est pas recommandée avant analyse.

## Si le problème n'est pas résolu

- [Mode report-only](https://learn.microsoft.com/entra/identity/conditional-access/concept-conditional-access-report-only)
- [Outil What If](https://learn.microsoft.com/entra/identity/conditional-access/what-if-tool)
- [Accès conditionnel via Graph](https://learn.microsoft.com/graph/api/resources/conditionalaccesspolicy)
- [Fiche Comptes d'urgence](Fiche_Simple_-_Cloud_Entra_ID_Comptes_Urgence.md)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Microsoft-Entra-ID.md)
