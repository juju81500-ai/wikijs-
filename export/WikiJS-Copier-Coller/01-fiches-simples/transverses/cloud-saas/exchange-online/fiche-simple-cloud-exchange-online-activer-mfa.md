# Fiche_Simple_-_Cloud_Exchange_Online_Activer_MFA

- **Environnement** : Tenant Microsoft 365 / Exchange Online (SaaS), administré depuis un poste d'administration
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif

---

## Problème précis à résoudre

Imposer l'authentification multifacteur aux comptes du tenant, administrateurs en priorité.

## 1. Hors-Production (Lab / Test / POC)

1. Interface : centre d'administration Microsoft Entra > Protection > Accès conditionnel > Nouvelle stratégie : cibler les rôles d'administration, application « toutes les ressources », accorder l'accès en exigeant l'authentification multifacteur. Commencer en mode « Rapport seul ».
   👉 Explication : l'accès conditionnel nécessite une licence Entra ID P1; sans licence, utiliser les paramètres de sécurité par défaut (Entra > Vue d'ensemble > Propriétés > Gérer les paramètres de sécurité par défaut).

2. Créer un compte d'accès d'urgence (« break glass ») exclu de la stratégie, mot de passe long généré et conservé hors ligne.
   👉 Explication : évite de se verrouiller hors du tenant.

3. Passer la stratégie de « Rapport seul » à « Activé » après analyse des journaux de connexion.
   👉 Explication : limite l'impact sur les utilisateurs.

## 2. Production — Contrôles

Vérifier que tous les administrateurs sont enrôlés et que les protocoles hérités (authentification de base) ne contournent pas le MFA.

## 3. Production — Sécurité

- Privilégier les méthodes résistantes au hameçonnage (clé FIDO2, Microsoft Authenticator).
- Surveiller le compte d'urgence.

## Validation et retour arrière

- **Validation** : Une connexion d'un administrateur de test déclenche bien une demande MFA.
- **Retour arrière** : Passer la stratégie en « Désactivé » ou « Rapport seul ».

## Si le problème n'est pas résolu

- [Accès conditionnel : exiger le MFA](https://learn.microsoft.com/entra/identity/conditional-access/howto-conditional-access-policy-admin-mfa)
- [Exchange Online — documentation officielle](https://learn.microsoft.com/exchange/exchange-online)
- [Fiche d'entrée Exchange Online](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-online)