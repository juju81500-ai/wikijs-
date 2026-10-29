# Fiche_Simple_-_VM_Windows_Server_2022_Reprise_Foret_AD_DS_Valider_Avant_Production.md

- **Environnement** : Forêt AD DS d'entreprise; laboratoire isolé recommandé
- **OS / Version** : Windows Server 2022 pour les contrôleurs de domaine concernés
- **Catégorie** : Active Directory / validation

---

## Problème précis à résoudre

Valider la forêt restaurée en réseau isolé avant de la reconnecter.

## 1. Hors-Production (Lab / Test / POC)

1. Diagnostiquer :
   ```powershell
   dcdiag /v
   ```
   👉 Explication : Diagnostic détaillé des DC (lecture seule).

2. Vérifier la réplication :
   ```powershell
   repadmin /replsummary
   ```
   👉 Explication : Contrôle de la réplication (lecture seule).

3. Vérifier SYSVOL/NETLOGON :
   ```powershell
   Get-SmbShare | Where-Object Name -in "SYSVOL","NETLOGON"
   ```
   👉 Explication : Vérifie que SYSVOL et NETLOGON sont partagés (lecture seule).

4. **Observateur d'événements > Journaux des applications et des services > Directory Service** : relire les erreurs.
   👉 Explication : contrôle de santé AD DS.

5. Authentifier des comptes de test; reconnecter à la production seulement après validation formelle du responsable AD/sécurité et application des recommandations Microsoft pour les autres DC.
   👉 Explication : évite de propager une forêt incohérente.

## 2. Production — Contrôles

Recréer ou redéployer les DC restants selon le plan, puis effectuer une nouvelle sauvegarde saine.

## 3. Production — Sécurité

- Ne pas reconnecter sans validation formelle.

## Validation et retour arrière

- **Validation** : DNS, SYSVOL/NETLOGON, DC, événements et réplication sains en isolation.
- **Retour arrière** : garder le réseau de reprise isolé et corriger avant toute reconnexion.

## Si le problème n'est pas résolu

- [Microsoft Learn — Redéployer les autres contrôleurs de domaine](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-restore-additional-dcs)
- [Microsoft Learn — Étapes de reprise d'une forêt AD](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-steps-for-restoring-the-forest)
- [Guide complet — étape 5](/02-fiches-completes/windows/server-2022/autres/26-reprise-foret-ad-ds-windows-server-2022#5-valider-avant-retour-en-production)