# Fiche_Simple_-_Cloud_Entra_ID_Comptes_Urgence

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services

---

## Problème précis à résoudre

Préparer deux comptes d'accès d'urgence à exclure des politiques d'accès conditionnel pilotes sans perdre l'accès au tenant.

## 1. Hors-Production (Lab / Test / POC)

1. Portail : Entra admin center → Entra ID → Users → New user → Create new user ; nom d'utilisateur sur le domaine .onmicrosoft.com (COMPTE_URGENCE_1 à remplacer).
   👉 Explication : compte cloud uniquement, nominatif organisationnel, hors synchronisation.

2. Entra ID → Roles & admins → Global Administrator → Add assignments (attribution définitive, justifiée).
   👉 Explication : seuls ces comptes ont ce rôle en permanence ; documenter l'usage.

3. Entra ID → Groups → New group → type Security ; nom GRP-URGENCE-EXCLUS (à remplacer) ; ajouter les comptes d'urgence.
   👉 Explication : un groupe unique simplifie l'exclusion dans chaque politique.

4. Configurer une méthode de connexion robuste résistante à l'hameçonnage (clé FIDO2 ou certificat) selon la recommandation Microsoft, stockée hors ligne.
   👉 Explication : les secrets sont conservés dans un coffre physique ; aucun secret dans la fiche.

5. Vérifier l'état des comptes :
   ```powershell
   Connect-MgGraph -Scopes 'User.Read.All','Group.Read.All' -ContextScope Process
   Get-MgGroup -Filter "displayName eq 'GRP-URGENCE-EXCLUS'" | Select Id,DisplayName
   ```
   👉 Explication : récupérer l'identifiant du groupe (ID_GROUPE_URGENCE à remplacer) pour les exclusions.

6. Créer une alerte sur les connexions de ces comptes (Monitoring → Diagnostic settings vers Log Analytics ou règle d'alerte).
   👉 Explication : toute utilisation doit être détectée.

## 2. Production — Contrôles

Production : au moins deux comptes, tests semestriels, mots de passe longs scellés, accès contrôlé, revue après chaque utilisation.

## 3. Production — Sécurité

- Ne pas affecter ces comptes à une personne ni les utiliser au quotidien.
- Les exclure seulement des politiques d'accès conditionnel où c'est nécessaire et compenser par supervision.
- Ne jamais documenter d'identifiants.

## Validation et retour arrière

- **Validation** : connexion test d'un compte d'urgence et alerte déclenchée.
- **Retour arrière** : désactiver le compte ; ne jamais supprimer le dernier compte d'urgence.

## Si le problème n'est pas résolu

- [Gérer les comptes d'accès d'urgence](https://learn.microsoft.com/entra/identity/role-based-access-control/security-emergency-access)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id)