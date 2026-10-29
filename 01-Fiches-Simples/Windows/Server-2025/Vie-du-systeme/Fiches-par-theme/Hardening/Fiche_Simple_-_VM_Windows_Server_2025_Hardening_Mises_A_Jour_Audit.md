# Fiche_Simple_-_VM_Windows_Server_2025_Hardening_Mises_A_Jour_Audit.md

- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : sécurité / maintenance
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `securite`

---

## Problème précis à résoudre

Maîtriser les mises à jour et centraliser les journaux d'audit.

## 1. Hors-Production (Lab / Test / POC)

1. Voir les derniers correctifs :
   ```powershell
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
   ```
   👉 Explication : Liste les dernières mises à jour installées (lecture seule).

2. Contrôler l'heure :
   ```powershell
   w32tm /query /status
   ```
   👉 Explication : Vérifie la synchronisation de l'heure (lecture seule).

3. Gérer les mises à jour via le mécanisme de parc, tester sur un groupe pilote et planifier les redémarrages.
   👉 Explication : limite les incidents.

4. Centraliser événements sécurité, Defender, SMB et AD DS et contrôler la rétention.
   👉 Explication : permet l'investigation.

## 2. Production — Contrôles

Vérifier la rétention des journaux.

## 3. Production — Sécurité

- Journaux centralisés protégés en écriture.

## Validation et retour arrière

- **Validation** : groupe pilote validé, journaux centralisés, heure correcte.
- **Retour arrière** : désinstaller ou différer le correctif en cause selon la procédure du parc.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Guide complet — étape 5](../../../../../../02-Fiches-Completes/Windows/Server-2025/Autres/31_Hardening_Windows_Server_2025_Production.md#5-mises-a-jour-et-audit)
