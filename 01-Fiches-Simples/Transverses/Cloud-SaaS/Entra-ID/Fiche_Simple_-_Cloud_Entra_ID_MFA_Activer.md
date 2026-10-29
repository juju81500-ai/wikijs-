# Fiche_Simple_-_Cloud_Entra_ID_MFA_Activer

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services
- **Tags** : `entra-id`, `mfa`, `methodes-authentification`, `graph`, `pilote`

---

## Problème précis à résoudre

Déployer l'authentification multifacteur sur un groupe pilote avant extension, en commençant par vérifier l'enregistrement.

## 1. Hors-Production (Lab / Test / POC)

1. Portail : Entra admin center → Entra ID → Authentication methods → Policies ; vérifier les méthodes activées (Microsoft Authenticator, FIDO2…) et cibler un groupe pilote (GRP-MFA-PILOTE à remplacer).
   👉 Explication : les chemins de menu et la disponibilité des méthodes varient ; vérifier selon licence.

2. Portail : Entra ID → Authentication methods → User registration details.
   👉 Explication : rapport d'enregistrement MFA par utilisateur.

3. Lire la politique de méthodes via Graph :
   ```powershell
   Connect-MgGraph -Scopes 'Policy.Read.All' -ContextScope Process
   Get-MgPolicyAuthenticationMethodPolicy | Select Id,RegistrationEnforcement
   Get-MgPolicyAuthenticationMethodPolicyAuthenticationMethodConfiguration | Select Id,State
   ```
   👉 Explication : lecture seule ; la modification nécessite `Policy.ReadWrite.AuthenticationMethod` et ne doit être faite qu'après validation du pilote.

4. Rapport d'enregistrement par Graph :
   ```powershell
   Connect-MgGraph -Scopes 'AuditLog.Read.All' -ContextScope Process
   Get-MgReportAuthenticationMethodUserRegistrationDetail -Top 20 | Select UserPrincipalName,IsMfaRegistered,IsMfaCapable
   ```
   👉 Explication : les permissions exactes dépendent de la version du cmdlet ; confirmer dans la référence Graph.

5. Ne pas activer l'ancienne MFA par utilisateur à grande échelle ; préférer l'accès conditionnel (fiche suivante).
   👉 Explication : éviter la dispersion des mécanismes et les exclusions oubliées.

6. Informer les utilisateurs pilotes et planifier l'enregistrement.
   👉 Explication : l'enregistrement préalable évite des blocages à l'activation.

## 2. Production — Contrôles

Production : groupe pilote, communication, support, méthodes résistantes à l'hameçonnage pour les administrateurs, procédure de récupération des comptes, licences confirmées.

## 3. Production — Sécurité

- Exclure le groupe de comptes d'urgence de toute exigence MFA bloquante, avec supervision.
- Pas de changement large sans pilote validé.
- Ne pas désactiver les paramètres par défaut de sécurité sans politique d'accès conditionnel équivalente.

## Validation et retour arrière

- **Validation** : pilote enregistré (`IsMfaRegistered` vrai) et connexion avec MFA réussie.
- **Retour arrière** : retirer le groupe pilote du ciblage de la méthode ; restaurer la politique d'origine documentée.

## Si le problème n'est pas résolu

- [Méthodes d'authentification](https://learn.microsoft.com/entra/identity/authentication/concept-authentication-methods-manage)
- [Référence Graph authenticationMethodsPolicy](https://learn.microsoft.com/graph/api/resources/authenticationmethodspolicy)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Microsoft-Entra-ID.md)
