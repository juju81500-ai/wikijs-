# Fiche_Simple_-_Cloud_Google_Workspace_Activer_MFA

- **Environnement** : Tenant Google Workspace (SaaS), administré via la console d'administration admin.google.com
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif

---

## Problème précis à résoudre

Imposer la validation en deux étapes (2SV) aux utilisateurs, administrateurs en priorité.

## 1. Hors-Production (Lab / Test / POC)

1. Interface : console d'administration > Sécurité > Authentification > Validation en deux étapes. Choisir l'unité organisationnelle (commencer par un groupe pilote).
   👉 Explication : la configuration s'applique par unité organisationnelle ou groupe.

2. Activer « Autoriser les utilisateurs à activer la validation en deux étapes », puis « Application » : imposer avec une période d'enrôlement. Privilégier les clés de sécurité pour les administrateurs.
   👉 Explication : l'imposition sans enrôlement préalable bloquerait les comptes.

3. Contrôler l'enrôlement avec GAM (si installé) :
   ```bash
   gam print users fields isenrolledin2sv,isenforcedin2sv
   ```
   👉 Explication : liste l'état 2SV; vérifier les noms de champs dans la version de GAM utilisée.

## 2. Production — Contrôles

Suivre le taux d'enrôlement (Rapports > Sécurité) avant d'étendre.

## 3. Production — Sécurité

- Exiger des méthodes résistantes au hameçonnage pour les administrateurs.
- Conserver des codes de secours hors ligne.

## Validation et retour arrière

- **Validation** : Un utilisateur pilote se voit exiger la 2SV à la connexion.
- **Retour arrière** : Désactiver l'application sur l'unité organisationnelle concernée.

## Si le problème n'est pas résolu

- [Déployer la validation en deux étapes](https://support.google.com/a/answer/175197)
- [Centre d'aide Google Workspace Admin](https://support.google.com/a/)
- [Fiche d'entrée Google Workspace](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-google-workspace)