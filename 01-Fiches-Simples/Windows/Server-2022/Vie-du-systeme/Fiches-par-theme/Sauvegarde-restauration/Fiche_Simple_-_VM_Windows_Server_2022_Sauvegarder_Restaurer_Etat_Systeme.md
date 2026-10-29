# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Sauvegarder_Restaurer_Etat_Systeme.md

- **Environnement** : VM ou serveur Windows Server avec volume de sauvegarde dédié
- **OS / Version** : Windows Server 2022 avec Windows Server Backup
- **Catégorie** : Sauvegarde / Restauration / Système
- **Tags** : `[windows-server-2022]`, `[windows-server-backup]`, `[wbadmin]`, `[sauvegarde]`, `[restauration]`, `[system-state]`

## 🎯 Problème précis à résoudre
Installer Windows Server Backup, effectuer une sauvegarde de l'état système sur une cible dédiée et vérifier qu'une version exploitable est disponible avant une procédure de restauration.

> Une sauvegarde de l'état système n'est pas une sauvegarde complète des données applicatives. Pour un contrôleur de domaine, suivre le plan de récupération AD DS/forêt et ne pas improviser une restauration autoritaire.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer le composant et vérifier son état :
   ```powershell
   Install-WindowsFeature Windows-Server-Backup
   Get-WindowsFeature Windows-Server-Backup
   ```
2. Avec un volume de sauvegarde distinct, lancer une sauvegarde unique de l'état système :
   ```powershell
   wbadmin start systemstatebackup -backuptarget:E: -quiet
   ```
3. Vérifier que la version est cataloguée :
   ```powershell
   wbadmin get versions -backuptarget:E:
   ```
   👉 *Explication : remplacer `E:` par la cible validée; ne pas utiliser comme seule sauvegarde un volume du même disque que le serveur.*

## ⚡ 2. Production — Façon Simplifiée
1. Installer **Sauvegarde Windows Server** depuis Gestionnaire de serveur ou PowerShell et choisir une cible dédiée conforme à la politique de rétention.
2. En GUI, ouvrir `wbadmin.msc`, choisir **Sauvegarde locale > Sauvegarde unique > Options différentes > Personnalisée**, sélectionner **État du système**, puis définir la destination.
3. Vérifier l'historique avec `wbadmin get versions -backuptarget:<cible>` et documenter la date, la cible, la rétention et les composants concernés.

## 🔒 3. Production — Façon Sécurisée
1. Chiffrer et contrôler l'accès au support de sauvegarde; conserver une copie hors du serveur et tester régulièrement sa lisibilité.
2. Pour restaurer, démarrer dans l'environnement de récupération Windows approprié, sélectionner la version vérifiée et suivre le runbook correspondant au rôle du serveur.
3. Sur un contrôleur de domaine, appliquer la procédure Microsoft de récupération AD DS et déterminer explicitement si la restauration est non autoritaire ou autoritaire avant toute action.

## ✅ Validation et retour arrière
- Contrôler le succès de la tâche dans Windows Server Backup et confirmer la présence de la version avec `wbadmin get versions`.
- Effectuer les exercices de restauration sur une VM isolée représentative; une sauvegarde non restaurée en test n'est pas une preuve de reprise.
- Ne pas lancer une restauration système sur le serveur actif pour tester; conserver l'accès console et un plan de reprise documenté.