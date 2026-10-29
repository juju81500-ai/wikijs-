# Fiche_Simple_-_VM_Windows_Server_2025_Hardening_SMB_Equipements_Tiers.md

- **Environnement** : Serveur membre ou contrôleur de domaine en laboratoire avant déploiement
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : sécurité / SMB
- **Tags** : `windows-server-2025`, `hardening`, `smb`, `ldap`, `securite`

---

## Problème précis à résoudre

Anticiper l'impact des nouveaux défauts SMB sur clients, NAS et appliances.

## 1. Hors-Production (Lab / Test / POC)

1. Lire la configuration SMB :
   ```powershell
   Get-SmbClientConfiguration
   Get-SmbServerConfiguration
   Get-SmbConnection
   ```
   👉 Explication : Affiche la configuration SMB client et serveur et les connexions actives (lecture seule).

2. Confirmer que les partages nécessaires négocient un dialecte moderne et que signature et chiffrement correspondent à la politique; utiliser les événements d'audit de compatibilité lorsqu'ils existent.
   👉 Explication : Server 2025 renforce la signature sortante et le chiffrement des connexions clientes.

3. Tester clients, NAS et appliances avant migration.
   👉 Explication : un matériel ancien peut cesser de se connecter.

## 2. Production — Contrôles

Ne jamais réactiver SMB1 pour contourner un matériel obsolète.

## 3. Production — Sécurité

- Pas de SMB1.

## Validation et retour arrière

- **Validation** : les partages nécessaires fonctionnent avec les nouveaux défauts.
- **Retour arrière** : remonter l'exception formellement documentée, limitée et datée, jamais SMB1.

## Si le problème n'est pas résolu

- [Microsoft Learn — Sécuriser le trafic SMB](https://learn.microsoft.com/en-us/windows-server/storage/file-server/smb-secure-traffic)
- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Guide complet — étape 2](../../../../../../02-Fiches-Completes/Windows/Server-2025/Autres/31_Hardening_Windows_Server_2025_Production.md#2-verifier-smb-et-les-equipements-tiers)
