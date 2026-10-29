# Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Determiner_Necessite.md

- **Environnement** : Forêt AD DS d'entreprise; laboratoire isolé recommandé
- **OS / Version** : Windows Server 2022 pour les contrôleurs de domaine concernés
- **Catégorie** : Active Directory / reprise après sinistre
- **Tags** : `windows-server-2022`, `active-directory`, `ad-ds`, `forest-recovery`

---

## Problème précis à résoudre

Décider si une restauration de forêt est vraiment justifiée avant toute action.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la réplication :
   ```powershell
   repadmin /replsummary
   repadmin /showrepl *
   ```
   👉 Explication : Résume l'état de la réplication entre contrôleurs de domaine (lecture seule).

2. Lister les DC :
   ```powershell
   Get-ADDomainController -Filter * | Select-Object Name, Site, IsGlobalCatalog, OperatingSystem
   ```
   👉 Explication : Liste les contrôleurs de domaine disponibles (lecture seule, module ActiveDirectory requis).

3. Diagnostiquer les DC et le DNS :
   ```powershell
   dcdiag /q
   ```
   👉 Explication : N'affiche que les tests en échec (lecture seule).

4. Associer l'équipe AD et sécurité; en cas d'incident de sécurité, isoler les systèmes suspectés et conserver les preuves selon le plan de réponse.
   👉 Explication : une panne isolée d'un DC ne justifie pas à elle seule une restauration de forêt.

## 2. Production — Contrôles

Ne jamais improviser une reprise sur la production; le guide est un cadre, pas un substitut à la procédure Microsoft et au runbook de la forêt.

## 3. Production — Sécurité

- Isoler et conserver les preuves en cas de compromission.

## Validation et retour arrière

- **Validation** : décision documentée et validée par les responsables AD et sécurité.
- **Retour arrière** : aucune action destructive n'est faite à cette étape.

## Si le problème n'est pas résolu

- [Microsoft Learn — Étapes de reprise d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest)
- [Guide complet — étape 1](../../../../../02-Fiches-Completes/Windows/Server-2022/Autres/26_Reprise_Foret_AD_DS_Windows_Server_2022.md#1-determiner-si-la-reprise-de-foret-est-necessaire)
