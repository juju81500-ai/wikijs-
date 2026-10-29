# Fiche_Simple_-_Windows_Server_2025_RDS_Mise_A_Jour_Retour_Arriere

- **Environnement** : Déploiement RDS Windows Server 2025 avec hôte pilote
- **OS / Version** : Windows Server 2025 Desktop Experience
- **Catégorie** : Vie du logiciel / Maintenance RDS

---

## Problème précis à résoudre

Appliquer les mises à jour d'un hôte RDS Windows Server 2025 avec point de retour, vérification et possibilité de revenir en arrière.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un point de retour : checkpoint de la VM pilote (Hyper-V : **Gestionnaire Hyper-V** > clic droit VM > **Point de contrôle**) ou sauvegarde d'état système.
   👉 Explication : Permet de revenir à l'état antérieur; pour un hôte physique, utiliser la sauvegarde de la fiche dédiée.
2. Relever l'état avant mise à jour :
   ```powershell
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
   Get-ComputerInfo | Select-Object OsBuildNumber
   ```
   👉 Explication : Conserve la référence pour comparer après correctif.
3. Vider l'hôte de ses nouvelles sessions puis installer les mises à jour : **Paramètres** > **Windows Update** (ou WSUS/Intune selon l'organisation).
   👉 Explication : Sur une ferme, traiter un hôte à la fois; les sessions actives sont interrompues au redémarrage.
4. Contrôler après redémarrage :
   ```powershell
   Get-Service TermService
   Get-WindowsFeature RDS-RD-Server
   ```
   👉 Explication : Confirme que le service RDP et le rôle sont toujours actifs; refaire la recette.
5. En cas de régression, désinstaller le correctif identifié :
   ```powershell
   wusa /uninstall /kb:NUMERO_KB
   ```
   👉 Explication : NUMERO_KB est à remplacer par le numéro du correctif fautif (sans « KB »); certaines mises à jour cumulatives ne sont pas désinstallables : restaurer alors le checkpoint.

## 2. Production — Contrôles

- Tester d'abord sur un hôte pilote puis déployer par vagues, hors heures ouvrées.
- Vérifier la compatibilité des CAL et des applications métier après une mise à jour majeure.
- Surveiller les journaux 24 h après mise à jour.

## 3. Production — Sécurité

- Installer uniquement des correctifs issus de sources officielles Microsoft.
- Conserver la preuve de la fenêtre de changement approuvée.

## Validation et retour arrière

- **Validation** : rôle et service actifs, recette réussie, aucune erreur de licence ni de connexion.
- **Retour arrière** : désinstaller le correctif avec `wusa` ou restaurer le checkpoint/la sauvegarde; vérifier les sessions et la recette ensuite.

## Si le problème n'est pas résolu

- [Microsoft Learn — Windows Server Update](https://learn.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus)
- [Sauvegarder et restaurer](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-sauvegarder-restaurer)
- [Valider la recette](/01-fiches-simples/windows/server-2025/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2025-rds-valider-recette)
- [Équivalent Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-logiciel/remote-desktop-services/fiche-simple-windows-server-2022-rds-mise-a-jour-retour-arriere)