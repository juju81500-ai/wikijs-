# Fiche_Simple_-_VM_Windows_Server_2025_Production_Gestion_Socle_Securite.md

- **Environnement** : Serveur physique ou VM Windows Server 2025 administré par l'organisation
- **OS / Version** : Windows Server 2025 Standard ou Datacenter
- **Catégorie** : installation / déploiement

---

## Problème précis à résoudre

Mettre le serveur sous gestion et appliquer la baseline de sécurité.

## 1. Hors-Production (Lab / Test / POC)

1. Inscrire le serveur dans l'outil de gestion prévu (GPO, Windows Admin Center, MECM, Azure Arc ou autre).
   👉 Explication : le serveur doit être géré.

2. Appliquer la baseline et les stratégies approuvées pour le rôle.
   👉 Explication : on harmonise la sécurité.

3. Vérifier Defender et le pare-feu :
   ```powershell
   Get-MpComputerStatus | Select-Object AMServiceEnabled, AntivirusEnabled, RealTimeProtectionEnabled
   Get-NetFirewallProfile | Select-Object Name, Enabled
   ```
   👉 Explication : les protections doivent être actives.

4. Examiner Credential Guard, Secure Boot et VBS selon la compatibilité matérielle et applicative; contrôler journalisation, sauvegarde et comptes privilégiés.
   👉 Explication : ces fonctions dépendent du matériel.

5. N'installer que les rôles/features nécessaires, après vérification des prérequis officiels.
   👉 Explication : on limite la surface.

## 2. Production — Contrôles

Tracer les exceptions de sécurité acceptées.

## 3. Production — Sécurité

- Pas de rôle superflu.
- Comptes privilégiés séparés et limités.

## Validation et retour arrière

- **Validation** : Defender et pare-feu actifs, baseline appliquée.
- **Retour arrière** : Retirer la stratégie appliquée en erreur et restaurer l'état précédent depuis la sauvegarde.

## Si le problème n'est pas résolu

- [Microsoft Learn — Nouveautés de Windows Server 2025](https://learn.microsoft.com/en-us/windows-server/get-started/whats-new-windows-server-2025)
- [Microsoft Learn — Installation de Windows Server](https://learn.microsoft.com/en-us/windows-server/get-started/install-options-server)
- [Guide complet déploiement Windows Server 2025](/02-fiches-completes/windows/server-2025/installation-deploiement/30-deploiement-windows-server-2025-production#4-appliquer-la-gestion-et-le-socle-de-securite)