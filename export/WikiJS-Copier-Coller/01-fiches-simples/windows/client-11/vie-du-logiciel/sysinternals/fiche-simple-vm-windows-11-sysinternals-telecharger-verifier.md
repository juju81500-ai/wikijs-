# Fiche_Simple_-_VM_Windows_11_Sysinternals_Telecharger_Verifier.md

- **Environnement** : Poste Windows 11 administré, diagnostic défensif local
- **OS / Version** : Windows 11; suite Sysinternals de Microsoft Learn ou Microsoft Store
- **Catégorie** : diagnostic / acquisition

---

## Problème précis à résoudre

Obtenir la suite depuis la source officielle et vérifier la signature des exécutables.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger la suite depuis **Microsoft Learn > Sysinternals Suite** et l'extraire dans un dossier contrôlé (ou installer l'application officielle depuis le **Microsoft Store**).
   👉 Explication : source officielle uniquement; pas de miroir non autorisé.

2. Vérifier la signature :
   ```powershell
   Get-AuthenticodeSignature .\procexp64.exe | Format-List Status,StatusMessage,SignerCertificate
   Get-AuthenticodeSignature .\autorunsc64.exe | Format-List Status,StatusMessage,SignerCertificate
   ```
   👉 Explication : Le statut doit être `Valid` et le signataire attendu (Microsoft).

3. En cas de signature invalide, de fichier altéré ou de source incertaine, ne pas lancer l'outil, supprimer l'archive selon la politique de poste et signaler l'incident.
   👉 Explication : évite d'exécuter un binaire compromis.

## 2. Production — Contrôles

Consigner la version de la suite utilisée.

## 3. Production — Sécurité

- Aucun outil non signé ne doit être lancé.

## Validation et retour arrière

- **Validation** : signatures `Valid` avec le bon éditeur.
- **Retour arrière** : supprimer le dossier d'extraction.

## Si le problème n'est pas résolu

- [Microsoft Learn — Get-AuthenticodeSignature](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/get-authenticodesignature)
- [Microsoft Learn — Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
- [Guide complet — étape 2](/02-fiches-completes/windows/client-11/installation-deploiement/123-administration-microsoft-sysinternals-windows-11#2-telecharger-et-verifier-la-suite)