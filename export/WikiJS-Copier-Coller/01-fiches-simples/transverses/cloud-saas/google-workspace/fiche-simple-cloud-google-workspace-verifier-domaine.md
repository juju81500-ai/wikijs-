# Fiche_Simple_-_Cloud_Google_Workspace_Verifier_Domaine

- **Environnement** : Tenant Google Workspace (SaaS), administré via la console d'administration admin.google.com
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif

---

## Problème précis à résoudre

Contrôler et ajouter le domaine du tenant Google Workspace.

## 1. Hors-Production (Lab / Test / POC)

1. Interface : console d'administration > Compte > Domaines > Gérer les domaines > Ajouter un domaine, puis valider la propriété (enregistrement TXT).
   👉 Explication : la propriété est prouvée par DNS.

2. Contrôler l'état avec GAM (si installé) :
   ```bash
   gam info domain
   ```
   👉 Explication : vérifie le domaine principal.

3. Configurer les enregistrements MX indiqués par Google dans l'assistant, après validation de la bascule.
   👉 Explication : valeurs affichées dans la console.

## 2. Production — Contrôles

Planifier la bascule MX avec TTL réduit.

## 3. Production — Sécurité

- Limiter l'accès à la zone DNS.
- Supprimer les domaines inutilisés.

## Validation et retour arrière

- **Validation** : Le domaine apparaît comme validé dans la console.
- **Retour arrière** : Supprimer le domaine ajouté par erreur; restaurer l'ancien MX si modifié.

## Si le problème n'est pas résolu

- [Ajouter un domaine](https://support.google.com/a/answer/7502379)
- [Centre d'aide Google Workspace Admin](https://support.google.com/a/)
- [Fiche d'entrée Google Workspace](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-google-workspace)