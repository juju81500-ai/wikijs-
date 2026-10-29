# Fiche_Simple_-_Cloud_Google_Workspace_Prerequis_Limites

- **Environnement** : Tenant Google Workspace (SaaS), administré via la console d'administration admin.google.com
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `google-workspace`, `gmail`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Cadrer l'administration défensive de Google Workspace : rôles, outils et limites SaaS.

## 1. Hors-Production (Lab / Test / POC)

1. Utiliser un compte super-administrateur nominatif protégé par MFA, distinct du compte courant, et déléguer le reste par rôles d'administrateur (console : Compte > Rôles d'administrateur). Les valeurs en MAJUSCULES (DOMAINE, ADMIN_UPN, etc.) sont à remplacer par celles de votre tenant.
   👉 Explication : limite le nombre de super-administrateurs.

2. Ouvrir la console : https://admin.google.com et vérifier Compte > Paramètres du compte.
   👉 Explication : point d'entrée de toute la configuration.

3. Optionnel : installer GAM (outil en ligne de commande open source) en suivant le wiki officiel, puis vérifier :
   ```bash
   gam info domain
   ```
   👉 Explication : affiche les informations du domaine si GAM est correctement autorisé; procédure d'installation et version : voir le dépôt officiel GAM.

4. Noter les limites : fonctions variables selon l'édition (Vault, alertes avancées).
   👉 Explication : vérifier l'édition avant de planifier.

## 2. Production — Contrôles

Documenter édition, domaines, super-administrateurs et fenêtre de changement.

## 3. Production — Sécurité

- Au moins deux super-administrateurs, un compte d'urgence hors ligne.
- Ne jamais stocker le jeton ou les secrets GAM dans un dépôt.

## Validation et retour arrière

- **Validation** : La console s'ouvre avec le compte nominatif.
- **Retour arrière** : Aucune modification effectuée; révoquer l'autorisation GAM si elle a été créée.

## Si le problème n'est pas résolu

- [Bonnes pratiques de sécurité administrateur](https://support.google.com/a/answer/9011077)
- [GAM — dépôt officiel](https://github.com/GAM-team/GAM/wiki)
- [Centre d'aide Google Workspace Admin](https://support.google.com/a/)
- [Fiche d'entrée Google Workspace](../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Google-Workspace.md)
