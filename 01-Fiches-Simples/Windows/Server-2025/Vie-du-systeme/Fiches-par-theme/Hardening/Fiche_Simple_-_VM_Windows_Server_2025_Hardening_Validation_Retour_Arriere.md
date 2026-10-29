# Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Validation_Retour_Arriere.md

- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : sécurité / validation
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `securite`

---

## Problème précis à résoudre

Valider le durcissement et garder la possibilité de revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Tester authentification, SMB, LDAP, sauvegarde, applications, gestion à distance et redémarrage depuis des clients représentatifs.
   👉 Explication : détecte les régressions avant la production.

2. Contrôles rapides :
   ```powershell
   Get-SmbConnection
   Get-NetFirewallProfile | Select-Object Name, Enabled
   ```
   👉 Explication : Contrôle rapide des connexions SMB et du pare-feu (lecture seule).

3. Conserver les stratégies précédentes et procéder par changements réversibles.
   👉 Explication : facilite le retour arrière.

## 2. Production — Contrôles

Toute exception doit être limitée, documentée, datée et revue.

## 3. Production — Sécurité

- Aucune exception permanente non revue.

## Validation et retour arrière

- **Validation** : tous les tests sont passés depuis les clients représentatifs.
- **Retour arrière** : restaurer les stratégies précédentes ou la VM du lab.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Guide complet — étape 6](../../../../../../02-Fiches-Completes/Windows/Server-2025/Autres/31_Hardening_Windows_Server_2025_Production.md#6-validation-et-retour-arriere)
