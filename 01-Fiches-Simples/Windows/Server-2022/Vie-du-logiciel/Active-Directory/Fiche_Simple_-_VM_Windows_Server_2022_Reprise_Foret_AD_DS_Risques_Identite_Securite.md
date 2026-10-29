# Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Risques_Identite_Securite.md

- **Environnement** : Forêt AD DS d'entreprise; laboratoire isolé recommandé
- **OS / Version** : Windows Server 2022 pour les contrôleurs de domaine concernés
- **Catégorie** : Active Directory / sécurité
- **Tags** : `windows-server-2022`, `active-directory`, `ad-ds`, `forest-recovery`

---

## Problème précis à résoudre

Appliquer les opérations d'identité documentées par Microsoft avant la reconnexion.

## 1. Hors-Production (Lab / Test / POC)

1. Selon le scénario, exécuter avec un responsable AD les opérations documentées : rôles FSMO, nettoyage des métadonnées des DC perdus, DNS, invalidation/réattribution des pools RID.
   👉 Explication : étapes exactes et ordre du guide officiel à respecter.

2. Réinitialiser les secrets krbtgt et comptes privilégiés, puis les mots de passe des comptes de service gérés si une compromission est suspectée.
   👉 Explication : empêche la réutilisation d'identifiants volés.

3. Vérifier les rôles FSMO :
   ```powershell
   netdom query fsmo
   ```
   👉 Explication : Contrôle en lecture seule des détenteurs FSMO après opérations.

## 2. Production — Contrôles

Coordonner avec les équipes applicatives avant toute réinitialisation globale.

## 3. Production — Sécurité

- Ces actions peuvent affecter l'authentification de toute la forêt.
- Aucun mot de passe en argument de commande.

## Validation et retour arrière

- **Validation** : opérations réalisées dans l'ordre prévu et consignées.
- **Retour arrière** : selon le runbook; pas d'annulation simple sur les secrets réinitialisés, d'où la coordination préalable.

## Si le problème n'est pas résolu

- [Microsoft Learn — Étapes de reprise d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest)
- [Guide complet — étape 4](../../../../../02-Fiches-Completes/Windows/Server-2022/Autres/26_Reprise_Foret_AD_DS_Windows_Server_2022.md#4-traiter-les-risques-didentite-et-de-securite)
