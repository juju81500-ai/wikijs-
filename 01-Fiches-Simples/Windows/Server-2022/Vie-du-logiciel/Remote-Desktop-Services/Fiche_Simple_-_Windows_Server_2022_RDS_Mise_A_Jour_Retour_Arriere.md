# Fiche_Simple_-_Windows_Server_2022_RDS_Mise_A_Jour_Retour_Arriere

- **Environnement** : Déploiement RDS Windows Server 2022 avec hôte pilote
- **OS / Version** : Windows Server 2022
- **Catégorie** : Vie du logiciel / Maintenance RDS
- **Tags** : `windows-server-2022`, `rds`, `mise-a-jour`, `retour-arriere`

---

## Problème précis à résoudre

Appliquer les mises à jour de sécurité Windows et de composants RDS par vagues, avec sauvegarde préalable et plan de retour arrière réaliste.

## 1. Hors-Production (Lab / Test / POC)

1. Établir la référence des correctifs installés :
   ```powershell
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10 HotFixID, InstalledOn, Description
   ```
   👉 Explication : Consigne les correctifs présents; vérifier les mises à jour disponibles dans Windows Update ou l'outil d'entreprise approuvé.
2. Dans **Paramètres** > **Windows Update** (ou **Gestionnaire de serveur** > **Windows Update**, selon l'outil), vérifier le correctif et la fenêtre, puis mettre à jour l'hôte pilote.
   👉 Explication : Les libellés dépendent de la stratégie de mise à jour; ne pas contourner l'outil de gestion centralisé.
3. Après le redémarrage demandé, contrôler les rôles et services :
   ```powershell
   Get-WindowsFeature RDS-RD-Server
   Get-Service TermService
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5 HotFixID, InstalledOn
   ```
   👉 Explication : Confirme le retour du service; compléter par un test de connexion pilote.

## 2. Production — Contrôles

- Vérifier bulletins Microsoft et cycle de vie du produit précis; ne pas déduire une échéance de la seule version de Windows.
- Pour une ferme, drainer les sessions et mettre à jour par vagues selon la topologie et la haute disponibilité.
- Prévoir redémarrage et vérifier licences, capacité de sessions et santé des rôles après chaque vague.

## 3. Production — Sécurité

- Déployer les correctifs de sécurité dans les délais approuvés après validation pilote.
- Ne pas retirer un correctif ni rétrograder un rôle sans analyse de risque et approbation.
- Conserver accès console, sauvegardes vérifiées et plan de retour arrière avant intervention.

## Validation et retour arrière

- **Validation** : services actifs, aucune alerte critique, test utilisateur pilote réussi et capacité nominale.
- **Retour arrière** : isoler le nœud défaillant et restaurer son image/sauvegarde approuvée ou suivre la procédure Microsoft; ne pas supposer que la désinstallation d'une KB suffit.

## Si le problème n'est pas résolu

- [Microsoft Learn — Résoudre les problèmes RDS](https://learn.microsoft.com/en-us/troubleshoot/windows-server/remote/remote-desktop-services-troubleshoot)
- [Microsoft Lifecycle — Windows Server 2022](https://learn.microsoft.com/en-us/lifecycle/products/windows-server-2022)
- [Sauvegarder et restaurer RDS](./Fiche_Simple_-_Windows_Server_2022_RDS_Sauvegarder_Restaurer.md)
