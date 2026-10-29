# Fiche_Simple_-_Cloud_Exchange_Online_Prerequis_Limites

- **Environnement** : Tenant Microsoft 365 / Exchange Online (SaaS), administré depuis un poste d'administration
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `exchange-online`, `microsoft-365`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Cadrer l'administration défensive d'Exchange Online avant toute modification : rôles, outils, limites SaaS.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier que vous disposez d'un compte administrateur nominatif avec le rôle le plus faible suffisant (ex. Exchange Administrator), distinct du compte courant. Les valeurs en MAJUSCULES (DOMAINE, ADMIN_UPN, etc.) sont à remplacer par celles de votre tenant.
   👉 Explication : éviter d'utiliser un Global Administrator au quotidien.

2. Installer le module PowerShell Exchange Online depuis un poste d'administration :
   ```powershell
   Install-Module -Name ExchangeOnlineManagement -Scope CurrentUser
   ```
   👉 Explication : module officiel Microsoft; vérifier la version publiée sur la PowerShell Gallery.

3. Se connecter :
   ```powershell
   Connect-ExchangeOnline -UserPrincipalName ADMIN_UPN
   ```
   👉 Explication : ADMIN_UPN est à remplacer par votre compte administrateur; l'authentification (MFA) se fait dans la fenêtre interactive, aucun mot de passe en clair.

4. Noter les limites : pas d'accès au serveur, pas de journaux transport bruts, fonctions dépendantes de la licence (Defender for Office 365, Purview).
   👉 Explication : la plateforme est gérée par Microsoft; le client ne contrôle que la configuration du tenant.

## 2. Production — Contrôles

Documenter tenant, domaines, comptes administrateurs, licences et fenêtre de changement.

## 3. Production — Sécurité

- Comptes administrateurs protégés par MFA.
- Ne jamais stocker d'identifiants dans des scripts.

## Validation et retour arrière

- **Validation** : Connexion réussie et `Get-OrganizationConfig` répond.
- **Retour arrière** : Se déconnecter avec `Disconnect-ExchangeOnline -Confirm:$false`; aucune modification n'a été faite.

## Si le problème n'est pas résolu

- [Module ExchangeOnlineManagement](https://learn.microsoft.com/powershell/exchange/exchange-online-powershell)
- [Exchange Online — documentation officielle](https://learn.microsoft.com/exchange/exchange-online)
- [Fiche d'entrée Exchange Online](../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Online.md)
