# Fiche_Simple_-_VM_Windows_11_Sysinternals_Collecte_Validation.md

- **Environnement** : Poste Windows 11 administré, diagnostic défensif local
- **OS / Version** : Windows 11; suite Sysinternals de Microsoft Learn ou Microsoft Store
- **Catégorie** : diagnostic / collecte

---

## Problème précis à résoudre

Consigner et valider une collecte de diagnostic.

## 1. Hors-Production (Lab / Test / POC)

1. Consigner poste, utilisateur/consentement, heure, version de Sysinternals, motif et filtres choisis.
   👉 Explication : traçabilité de la collecte.

2. Vérifier la signature :
   ```powershell
   Get-AuthenticodeSignature .\procmon64.exe | Format-List Status,SignerCertificate
   ```
   👉 Explication : Contrôle la signature avant d'interpréter le comportement d'un outil.

3. Corroborer avec Defender, journaux Windows, inventaire de gestion et supervision.
   👉 Explication : un seul outil ne donne pas un verdict.

4. Faire relire toute action corrective, conserver l'état initial et un plan de restauration.
   👉 Explication : permet de revenir en arrière.

5. Supprimer les traces temporaires de façon approuvée après transfert vers le dépôt sécurisé.
   👉 Explication : évite de laisser des données personnelles sur le poste.

## 2. Production — Contrôles

Respecter la politique de conservation de l'organisation.

## 3. Production — Sécurité

- Dépôt sécurisé à accès restreint pour les traces.

## Validation et retour arrière

- **Validation** : collecte consignée et corroborée.
- **Retour arrière** : supprimer les traces temporaires selon la politique.

## Si le problème n'est pas résolu

- [Microsoft Learn — Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [Guide complet — étape 4](/02-fiches-completes/windows/client-11/installation-deploiement/123-administration-microsoft-sysinternals-windows-11#4-collecte-et-validation)