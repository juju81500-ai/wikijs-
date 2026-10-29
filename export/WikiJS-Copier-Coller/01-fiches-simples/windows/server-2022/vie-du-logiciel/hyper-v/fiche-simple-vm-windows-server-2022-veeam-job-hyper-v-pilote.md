# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Job_Hyper_V_Pilote.md

- **Environnement** : Veeam Backup & Replication 13.1, hôte Hyper-V et dépôt approuvés
- **OS / Version** : Windows Server 2022 / Hyper-V
- **Catégorie** : Sauvegarde / validation de job

---

## 🎯 Problème précis à résoudre

Créer et valider un job de sauvegarde Veeam pour une VM pilote Hyper-V.

## 🧪 1. Hors-Production (Lab / Test / POC)

1. Confirmer hôte et dépôt : console Veeam **Backup Infrastructure > Managed Servers / Backup Repositories** (état), ou PowerShell Veeam :
   ```powershell
   Get-VBRServer | Select-Object Name, Type
   Get-VBRBackupRepository | Select-Object Name, Path
   ```
   👉 Explication : l'hôte Hyper-V et le dépôt doivent être accessibles.

2. Créer un job pour une seule VM de test : **Home > Backup Job > Virtual machine > Hyper-V**, ajouter la VM, dépôt dédié, rétention limitée, horaire approuvé :
   ```powershell
   $vm = Find-VBRHvEntity -Name "VM-PILOTE"
   Add-VBRHvBackupJob -Name "Pilote-VM" -Entity $vm -BackupRepository (Get-VBRBackupRepository -Name "DEPOT-PILOTE")
   ```
   👉 Explication : remplacer les noms; une VM, un dépôt dédié.

3. Exécuter et contrôler :
   ```powershell
   Get-VBRJob -Name "Pilote-VM" | Start-VBRJob
   Get-VBRBackupSession | Sort-Object CreationTime -Descending | Select-Object -First 1 JobName, Result, CreationTime, EndTime
   ```
   👉 Explication : GUI **History > Jobs** (durée, taille, logs); un point de restauration doit exister.

4. Restaurer un fichier : **Home > Restore > Hyper-V > Guest files > Windows**, choisir le point, puis **Copy To** vers un dossier temporaire; si possible, faire une restauration VM isolée (**Instant Recovery** désactivé pour le lab).
   👉 Explication : emplacement temporaire, jamais sur la production.

## ⚡ 2. Production — Façon Simplifiée

1. Ajouter les VM par groupe après validation du pilote :
   ```powershell
   Get-VBRBackupRepository | Select-Object Name, @{n='LibreGo';e={[math]::Round($_.GetContainer().CachedFreeSpace.InGigabytes)}}
   ```
   👉 Explication : vérifier capacité du dépôt, SLA, fenêtre, application-aware processing et alertes; planifier une copie indépendante hors site (**Backup Copy Job**).

## 🔒 3. Production — Façon Sécurisée

- Utiliser des comptes de service dédiés et restreindre les rôles Veeam.
- Protéger le dépôt contre suppression depuis l'environnement de sauvegarde; activer l'immuabilité sur un dépôt compatible.
- Ne pas considérer les checkpoints Hyper-V comme des sauvegardes; ne pas supprimer une chaîne de sauvegarde manuellement.

## ✅ Validation et retour arrière

- **Validation** : job réussi, point de restauration visible, test de restauration lisible et données cohérentes.
- **Retour arrière** : désactiver le job pilote et conserver ses points tant que la règle de rétention n'autorise pas explicitement leur purge.

## 🔗 Si le problème n'est pas résolu

- [Veeam — Créer un job de sauvegarde Hyper-V](https://helpcenter.veeam.com/docs/vbr/userguide/backup_job_hv.html)
- [Veeam — Dépôts de sauvegarde](https://helpcenter.veeam.com/docs/vbr/userguide/backup_repository.html)