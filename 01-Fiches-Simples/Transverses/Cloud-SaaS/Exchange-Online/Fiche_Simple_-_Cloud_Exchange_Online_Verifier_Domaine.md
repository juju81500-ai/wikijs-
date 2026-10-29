# Fiche_Simple_-_Cloud_Exchange_Online_Verifier_Domaine

- **Environnement** : Tenant Microsoft 365 / Exchange Online (SaaS), administré depuis un poste d'administration
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer)
- **Catégorie** : messagerie et collaboratif
- **Tags** : `exchange-online`, `microsoft-365`, `cloud-saas`, `administration-defensive`, `messagerie`, `tssr`

---

## Problème précis à résoudre

Contrôler et ajouter le domaine de messagerie accepté dans le tenant.

## 1. Hors-Production (Lab / Test / POC)

1. Interface : centre d'administration Microsoft 365 > Paramètres > Domaines > Ajouter un domaine, puis suivre l'assistant de vérification (enregistrement TXT).
   👉 Explication : la propriété du domaine est prouvée par un enregistrement TXT DNS.

2. Lister les domaines acceptés :
   ```powershell
   Get-AcceptedDomain | Format-Table Name,DomainName,DomainType,Default
   ```
   👉 Explication : vérifie que DOMAINE (à remplacer) est présent avec le type attendu.

3. Vérifier les enregistrements MX demandés par l'assistant (valeur propre au tenant, affichée dans l'assistant).
   👉 Explication : ne pas modifier le MX avant d'avoir validé la bascule de messagerie.

## 2. Production — Contrôles

Valider la propriété DNS et planifier la bascule MX avec TTL réduit.

## 3. Production — Sécurité

- Limiter l'accès à la zone DNS.
- Supprimer les domaines inutilisés.

## Validation et retour arrière

- **Validation** : Le domaine apparaît comme « Healthy » dans le centre d'administration.
- **Retour arrière** : Retirer le domaine (Paramètres > Domaines) si ajouté par erreur et non utilisé; restaurer l'ancien MX si modifié.

## Si le problème n'est pas résolu

- [Ajouter un domaine à Microsoft 365](https://learn.microsoft.com/microsoft-365/admin/setup/add-domain)
- [Exchange Online — documentation officielle](https://learn.microsoft.com/exchange/exchange-online)
- [Fiche d'entrée Exchange Online](../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Online.md)
