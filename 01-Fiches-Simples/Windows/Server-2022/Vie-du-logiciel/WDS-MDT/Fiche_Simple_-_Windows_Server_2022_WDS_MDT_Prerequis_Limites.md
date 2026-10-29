# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Prerequis_Limites

- **Environnement** : Windows Server 2022, rôle WDS et MDT (serveur de déploiement PXE)
- **OS / Version** : Windows Server 2022; WDS (rôle intégré), MDT et Windows ADK : vérifier la version publiée et le statut de support
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `windows-server-2022`, `wds`, `mdt`, `prerequis`, `limites`

---

## Problème précis à résoudre

Valider les prérequis et connaître les limites de WDS/MDT avant de s'engager. Le parcours d'installation et de configuration n'est pas répété ici : voir la [procédure historique WDS + MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Simple_-_WDS-MDT.md).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'OS et l'état du rôle. GUI : `Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités`.
   ```powershell
   Get-ComputerInfo | Select-Object OsName, OsVersion, CsDomain
   Get-WindowsFeature WDS* | Select-Object Name, InstallState
   ```
   👉 Explication : confirme Windows Server 2022 et l'état du rôle (avant ou après installation décrite dans la procédure historique).

2. Contrôler le volume du partage de déploiement et de `RemoteInstall` :
   ```powershell
   Get-Volume | Select-Object DriveLetter, FileSystem, SizeRemaining, Size
   ```
   👉 Explication : prévoir un volume NTFS dédié, distinct du système; la taille dépend du nombre d'images (à dimensionner).

3. Contrôler la présence de DHCP et du réseau PXE :
   ```powershell
   Get-WindowsFeature DHCP | Select-Object InstallState
   Test-NetConnection SERVEUR-DHCP.DOMAINE.LOCAL -Port 67
   ```
   👉 Explication : `SERVEUR-DHCP.DOMAINE.LOCAL` est à remplacer. Le test sur le port UDP 67 n'est pas fiable avec `Test-NetConnection` (TCP) : valider surtout le comportement PXE réel (options DHCP 66/67 ou relais) avec l'équipe réseau. Vérifier la configuration documentée par Microsoft.

4. Noter les limites à vérifier avant décision (aucune commande) :
   - MDT : Microsoft a annoncé la fin de support/retrait de MDT; vérifier le statut publié et les alternatives (Configuration Manager, Autopilot, WDS + images natives).
   - WDS : annoncé comme déprécié dans les versions récentes de Windows Server; vérifier la page « Features removed or deprecated ».
   - Le démarrage PXE UEFI/Secure Boot et les versions de WinPE/ADK dépendent de la version : vérifier la matrice ADK.
   👉 Explication : ces points relèvent de la décision d'architecture; ne pas les supposer.

## 2. Production — Contrôles

Faire valider par le responsable : périmètre (réseaux, VLAN), choix de maintenir WDS/MDT, plan de sortie, licences Windows.

## 3. Production — Sécurité

- Segmenter le réseau PXE; le serveur ne doit pas répondre à tous les postes (voir la fiche Sécurisation).
- Aucun mot de passe dans les fiches ni les fichiers de réponses.

## Validation et retour arrière

- **Validation** : prérequis consignés; décision de maintien documentée.
- **Retour arrière** : aucune modification effectuée : rien à annuler.

## Si le problème n'est pas résolu

- [Procédure historique WDS + MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Simple_-_WDS-MDT.md)
- [Fiche d'entrée WDS/MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_WDS-MDT.md)
- [Microsoft Learn — Déploiement Windows : scénarios et outils](https://learn.microsoft.com/en-us/windows/deployment/windows-deployment-scenarios-and-tools)
- [Microsoft Learn — Démarrer avec MDT](https://learn.microsoft.com/en-us/windows/deployment/deploy-windows-mdt/get-started-with-the-microsoft-deployment-toolkit)
- [Microsoft Learn — wdsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil)
