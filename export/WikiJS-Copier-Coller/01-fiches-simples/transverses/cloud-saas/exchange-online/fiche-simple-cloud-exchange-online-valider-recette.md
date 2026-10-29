# Fiche_Simple_-_Cloud_Exchange_Online_Valider_Recette

- **Environnement** : Tenant Microsoft 365 / Exchange Online (SaaS), administré depuis un poste d'administration
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif

---

## Problème précis à résoudre

Recetter l'ensemble de la configuration défensive d'Exchange Online.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les domaines :
   ```powershell
   Get-AcceptedDomain | Format-Table DomainName,Default
   ```
   👉 Explication : cohérence avec l'inventaire.

2. Contrôler DKIM :
   ```powershell
   Get-DkimSigningConfig | Format-Table Domain,Enabled
   ```
   👉 Explication : tous les domaines émetteurs doivent être activés.

3. Envoyer un message de test vers une boîte externe et lire les en-têtes d'authentification (SPF, DKIM, DMARC).
   👉 Explication : confirme les trois contrôles de bout en bout.

4. Contrôler dans Entra > Journaux de connexion qu'une connexion administrateur exige le MFA.
   👉 Explication : preuve de recette MFA.

## 2. Production — Contrôles

Archiver les captures et le résultat des commandes dans le dossier de recette.

## 3. Production — Sécurité

- Ne pas inclure de données personnelles dans la recette.

## Validation et retour arrière

- **Validation** : Tous les contrôles sont conformes.
- **Retour arrière** : Annuler le dernier changement (DNS, stratégie) selon la fiche concernée.

## Si le problème n'est pas résolu

- [Exchange Online — documentation officielle](https://learn.microsoft.com/exchange/exchange-online)
- [Fiche d'entrée Exchange Online](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-online)