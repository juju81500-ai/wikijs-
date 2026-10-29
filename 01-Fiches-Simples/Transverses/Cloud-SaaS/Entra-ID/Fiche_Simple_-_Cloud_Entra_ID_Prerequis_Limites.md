# Fiche_Simple_-_Cloud_Entra_ID_Prerequis_Limites

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services
- **Tags** : `entra-id`, `cloud-saas`, `prerequis`, `licences`, `graph`

---

## Problème précis à résoudre

Valider licences, rôles et outils avant de toucher MFA, accès conditionnel ou synchronisation.

## 1. Hors-Production (Lab / Test / POC)

1. Installer uniquement les modules Graph nécessaires dans PowerShell 7 :
   ```powershell
   Install-PSResource Microsoft.Graph.Authentication -Scope CurrentUser
   Install-PSResource Microsoft.Graph.Identity.SignIns -Scope CurrentUser
   Get-Module Microsoft.Graph* -ListAvailable | Select Name,Version
   ```
   👉 Explication : évite le métamodule complet ; en cas d'absence de `Install-PSResource`, utiliser `Install-Module` selon la politique de l'organisation.

2. Portail : Microsoft Entra admin center → Entra ID → Vue d'ensemble → Licences, puis Entra ID → Users → utilisateurs pilotes.
   👉 Explication : vérifier que les licences requises (accès conditionnel, MFA avancé, Connect Health) sont attribuées ; elles varient selon l'offre (vérifier la page de licences Microsoft).

3. Se connecter en délégué avec le moindre privilège (lecture seule d'abord) :
   ```powershell
   Connect-MgGraph -Scopes 'Policy.Read.All','Directory.Read.All' -ContextScope Process
   Get-MgContext | Select Account,Scopes
   Get-MgOrganization | Select DisplayName,Id
   ```
   👉 Explication : connexion interactive par un compte administrateur nominatif ; consentir seulement les permissions de lecture.

4. Identifier les rôles requis dans Entra admin center → Entra ID → Roles & admins (par exemple lecteur de sécurité, administrateur d'accès conditionnel, administrateur d'authentification).
   👉 Explication : ne pas utiliser Administrateur général pour les tâches courantes ; activer les rôles via PIM si disponible.

5. Consulter les limites : certaines fonctions sont en préversion ou dépendent de la licence.
   👉 Explication : vérifier la matrice de support et licences actuelle sur Microsoft Learn.

## 2. Production — Contrôles

Production : licences confirmées, rôles attribués à durée limitée, comptes d'urgence créés et testés (fiche Comptes d'urgence), tenant pilote ou groupe pilote défini, journalisation active.

## 3. Production — Sécurité

- Ne pas utiliser d'application avec secret client pour des tâches manuelles courantes.
- Toujours `Connect-MgGraph -ContextScope Process` sur poste partagé et `Disconnect-MgGraph` ensuite.
- Ne pas accorder `*.ReadWrite.All` par défaut.

## Validation et retour arrière

- **Validation** : `Get-MgContext` affiche uniquement les permissions de lecture nécessaires.
- **Retour arrière** : `Disconnect-MgGraph`, retirer les rôles temporaires.

## Si le problème n'est pas résolu

- [Installer le SDK Microsoft Graph PowerShell](https://learn.microsoft.com/powershell/microsoftgraph/installation)
- [Licences Entra](https://learn.microsoft.com/entra/fundamentals/licensing)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Microsoft-Entra-ID.md)
