# Fiche_Simple_-_Windows_Server_2025_RDS_Installer_Configurer

- **Environnement** : VM Windows Server 2025 de lab, contrôleur de domaine exclu
- **OS / Version** : Windows Server 2025 Desktop Experience
- **Catégorie** : Vie du logiciel / Installation et configuration RDS

---

## Problème précis à résoudre

Installer l'hôte de session RDS et configurer le serveur de licences sur un serveur pilote Windows Server 2025, sans confondre rôle isolé et déploiement multi-serveurs.

## 1. Hors-Production (Lab / Test / POC)

1. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités** > **Installation basée sur un rôle ou une fonctionnalité**, choisir le pilote, puis **Services Bureau à distance** > **Hôte de session Bureau à distance**, avec les outils de gestion.
   👉 Explication : Installe le rôle sur un pilote; pour une ferme (Broker, Web Access), utiliser plutôt l'option **Installation des services Bureau à distance** du même assistant.
2. Équivalent PowerShell pour un hôte de session autonome de test :
   ```powershell
   Install-WindowsFeature -Name RDS-RD-Server -IncludeManagementTools
   Get-WindowsFeature RDS-RD-Server
   ```
   👉 Explication : Ajoute uniquement le rôle hôte de session; ne crée ni collection, ni Broker, ni licences. Redémarrer si demandé.
3. Installer le rôle de licences sur le serveur désigné (GUI : même assistant, service de rôle **Gestionnaire de licences Bureau à distance**) :
   ```powershell
   Install-WindowsFeature -Name RDS-Licensing -IncludeManagementTools
   ```
   👉 Explication : Ajoute le serveur de licences RDS; l'activation et l'ajout des CAL se font ensuite dans **Outils d'administration** > **Services Bureau à distance** > **Gestionnaire de licences Bureau à distance** (`licmgr.msc`).
4. Déclarer le mode de licence et le serveur sur l'hôte de session, via GPO ou `gpedit.msc` : **Configuration ordinateur** > **Modèles d'administration** > **Composants Windows** > **Services Bureau à distance** > **Hôte de session Bureau à distance** > **Licences** > **Utiliser les serveurs de licence spécifiés** et **Définir le mode de gestion des licences**. Pour un déploiement RDS avec Broker :
   ```powershell
   Set-RDLicenseConfiguration -LicenseServer NOM_SERVEUR_LICENCES -Mode PerUser -ConnectionBroker NOM_BROKER
   Get-RDLicenseConfiguration -ConnectionBroker NOM_BROKER
   ```
   👉 Explication : NOM_SERVEUR_LICENCES et NOM_BROKER sont à remplacer par les FQDN réels; `PerUser` est à remplacer par `PerDevice` selon les CAL achetées. Cette cmdlet exige un Broker existant.
5. Contrôler le rôle et le service :
   ```powershell
   Get-WindowsFeature RDS-RD-Server
   Get-Service TermService, TermServLicensing -ErrorAction SilentlyContinue
   ```
   👉 Explication : Confirme l'installation et les services; ne valide ni les droits d'accès ni la conformité des CAL.

## 2. Production — Contrôles

- Valider en pilote la collection, l'affectation des groupes, les profils et la communication avec le serveur de licences.
- Activer le serveur de licences et installer les CAL 2025 uniquement avec des licences acquises; vérifier avec le Diagnostic des licences (`lsdiag.msc`).
- Les cmdlets RDS de gestion exigent une infrastructure Broker; ne pas les lancer sur un hôte autonome.

## 3. Production — Sécurité

- Séparer les rôles critiques selon l'architecture; jamais d'hôte de session sur un contrôleur de domaine.
- N'autoriser que les groupes et applications approuvés.
- Une installation réussie ne prouve ni la sécurité ni la conformité des licences.

## Validation et retour arrière

- **Validation** : rôle installé, licences configurées et reconnues, utilisateur pilote connecté depuis le réseau prévu.
- **Retour arrière** : restaurer le point de sauvegarde ou la VM, ou retirer les rôles via le changement approuvé; ne pas retirer à chaud un rôle de ferme active.

## Si le problème n'est pas résolu

- [Microsoft Learn — Déployer une infrastructure RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-deploy-infrastructure)
- [Microsoft Learn — Licences RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license)
- [Prérequis et licences](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-prerequis-licences-cal)
- [Sécuriser TLS, comptes et pare-feu](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-securiser-tls-comptes-pare-feu)