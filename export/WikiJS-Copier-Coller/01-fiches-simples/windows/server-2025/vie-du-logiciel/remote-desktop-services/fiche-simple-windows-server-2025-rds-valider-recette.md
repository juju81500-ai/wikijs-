# Fiche_Simple_-_Windows_Server_2025_RDS_Valider_Recette

- **Environnement** : Déploiement RDS Windows Server 2025 avec hôte pilote
- **OS / Version** : Windows Server 2025 Desktop Experience
- **Catégorie** : Vie du logiciel / Validation RDS

---

## Problème précis à résoudre

Prouver qu'un déploiement RDS Windows Server 2025 fonctionne, accepte les utilisateurs autorisés, refuse les autres et dispose de licences valides.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler rôles et services :
   ```powershell
   Get-WindowsFeature RDS-*  | Where-Object Installed
   Get-Service TermService, UmRdpService
   ```
   👉 Explication : Confirme que les rôles attendus sont installés et que les services RDP tournent.
2. Contrôler le port d'écoute depuis un poste client :
   ```powershell
   Test-NetConnection NOM_SERVEUR -Port 3389
   ```
   👉 Explication : NOM_SERVEUR est à remplacer par le FQDN de l'hôte; `TcpTestSucceeded : True` attendu uniquement depuis le réseau autorisé.
3. Ouvrir une session avec `mstsc /v:NOM_SERVEUR` avec un compte pilote, puis lister les sessions :
   ```powershell
   quser /server:NOM_SERVEUR
   Get-RDUserSession -ConnectionBroker NOM_BROKER
   ```
   👉 Explication : Montre la session pilote; `Get-RDUserSession` ne fonctionne qu'avec un Broker (NOM_BROKER à remplacer).
4. Vérifier les licences : ouvrir `lsdiag.msc` (Diagnostic des licences Bureau à distance) ou :
   ```powershell
   Get-RDLicenseConfiguration -ConnectionBroker NOM_BROKER
   ```
   👉 Explication : Confirme serveur et mode de licence; le diagnostic signale période de grâce ou CAL manquantes.
5. Consulter le journal **Observateur d'événements** > **Journaux des applications et des services** > **Microsoft** > **Windows** > **TerminalServices-LocalSessionManager**.
   👉 Explication : Les erreurs de connexion et de licence y sont tracées.

## 2. Production — Contrôles

- Tester un compte autorisé (succès) et un compte non autorisé (échec).
- Conserver captures et résultats comme preuves de recette.
- S'assurer que le succès ne repose pas sur la période de grâce des licences.

## 3. Production — Sécurité

- Utiliser des comptes de test dédiés, supprimés ou désactivés après la recette.
- Ne pas laisser de session pilote ouverte.

## Validation et retour arrière

- **Validation** : tous les tests ci-dessus sont conformes et documentés.
- **Retour arrière** : fermer la session pilote, désactiver le compte de test et rétablir la configuration précédente si un test critique échoue.

## Si le problème n'est pas résolu

- [Microsoft Learn — RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/welcome-to-rds)
- [Sécuriser TLS, comptes et pare-feu](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-securiser-tls-comptes-pare-feu)
- [Sauvegarder et restaurer](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-sauvegarder-restaurer)
- [Équivalent Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-valider-recette)