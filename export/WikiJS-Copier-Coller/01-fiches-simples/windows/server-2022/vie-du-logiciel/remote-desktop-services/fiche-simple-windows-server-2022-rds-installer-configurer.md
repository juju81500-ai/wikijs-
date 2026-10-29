# Fiche_Simple_-_Windows_Server_2022_RDS_Installer_Configurer

- **Environnement** : VM Windows Server 2022 de lab, contrôleur de domaine exclu
- **OS / Version** : Windows Server 2022 Desktop Experience
- **Catégorie** : Vie du logiciel / Installation et configuration RDS

---

## Problème précis à résoudre

Installer le rôle hôte de session RDS sur un serveur pilote, sans confondre ce rôle avec un déploiement RDS multi-serveurs complet.

## 1. Hors-Production (Lab / Test / POC)

1. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités** > **Installation basée sur un rôle ou une fonctionnalité**, sélectionner le pilote, puis **Services Bureau à distance** > **Hôte de session Bureau à distance** et les outils d'administration requis. Examiner les dépendances avant confirmation.
   👉 Explication : Cette méthode installe le rôle sur un pilote. Pour un déploiement complet, utiliser l'assistant **Installation des services Bureau à distance** adapté à la topologie.
2. Équivalent PowerShell pour un hôte de session autonome de test :
   ```powershell
   Install-WindowsFeature -Name RDS-RD-Server -IncludeManagementTools
   Get-WindowsFeature RDS-RD-Server
   ```
   👉 Explication : Ajoute seulement le rôle hôte de session; ne crée pas une collection, un Broker, une passerelle, un serveur de licences, ni la configuration de CAL. Redémarrer si demandé.
3. Contrôler le rôle et le service après installation :
   ```powershell
   Get-WindowsFeature RDS-RD-Server
   Get-Service TermService
   ```
   👉 Explication : Confirme l'installation et le service RDP, mais ne valide ni les licences ni les droits d'accès.
4. Pour une ferme de test, dans **Gestionnaire de serveur** > **Services Bureau à distance** > **Vue d'ensemble**, utiliser **Installation** et suivre l'assistant de déploiement. Ajouter les serveurs uniquement après validation DNS/AD et capacité.
   👉 Explication : L'assistant configure les rôles associés; vérifier la topologie et la documentation de la version cible avant de continuer.

## 2. Production — Contrôles

- Valider en pilote la collection, l'affectation des groupes, les profils, applications et le serveur de licences.
- Configurer le mode et les serveurs de licences dans **Gestionnaire de serveur** > **Services Bureau à distance** > **Vue d'ensemble** > **Tâches** > **Modifier les propriétés de déploiement** > **Licences RDS**.
- Les cmdlets de gestion RDS nécessitent une infrastructure correspondante; ne pas les lancer sur un hôte autonome sans Broker.

## 3. Production — Sécurité

- Séparer les rôles critiques selon l'architecture; ne pas transformer un contrôleur de domaine en hôte de sessions.
- N'autoriser que les groupes approuvés et les applications métier requises.
- Une installation réussie ne valide pas la sécurité ou la conformité des licences.

## Validation et retour arrière

- **Validation** : rôle installé; utilisateur pilote autorisé ouvre une session depuis le réseau prévu.
- **Retour arrière** : retirer le pilote, restaurer le point de sauvegarde/VM et retirer le rôle selon le changement approuvé; ne pas désinstaller un rôle de ferme actif à chaud.

## Si le problème n'est pas résolu

- [Microsoft Learn — Déployer une infrastructure RDS](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-deploy-infrastructure)
- [Prérequis et limites RDS](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-prerequis-limites)
- [Configurer l'accès RDP existant](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-vm-windows-server-2022-rds-configuration-bureau)