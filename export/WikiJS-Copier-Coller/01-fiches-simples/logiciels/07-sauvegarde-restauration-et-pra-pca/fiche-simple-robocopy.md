# 📄 Robocopy

- **Environnement** : VM (Windows Server 2022)
- **OS / Version** : Windows Server 2022 (Desktop Experience ou Server Core)
- **Version** : Robocopy intégré à Windows Server 2022 ; `robocopy /?` affiche l'aide de la version installée
- **Catégorie** : Sauvegarde, restauration et PRA / PCA

## 🎯 Problème précis à résoudre
Copier un dossier de données vers un volume ou un partage de sauvegarde avec Robocopy, contrôler le résultat (code de sortie, journal, empreintes), planifier la tâche, puis durcir son exécution. Attention : `/MIR` supprime dans la destination les fichiers absents de la source ; ne l'utiliser que vers une destination dédiée. Les tests ne se font que sur vos propres dossiers.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Affichage de l'aide et préparation des dossiers de test :
```powershell
robocopy /?
New-Item -ItemType Directory -Path C:\Lab\Source\Compta, C:\Lab\logs, D:\Lab\Sauvegarde -Force
Set-Content -Path C:\Lab\Source\Compta\facture-001.txt -Value "Facture de test"
```
👉 Explication : `robocopy /?` liste les options disponibles. Les commandes créent un dossier source avec un fichier de test, un dossier de journaux et un dossier de destination sur le volume de test `D:`.

2. Simulation sans copie :
```powershell
robocopy C:\Lab\Source D:\Lab\Sauvegarde /E /L /NP /LOG:C:\Lab\logs\simulation.log
```
👉 Explication : `/L` ne copie rien et liste ce qui serait fait. `/E` inclut les sous-dossiers, même vides, et `/NP` masque la progression. Le journal est écrit dans `C:\Lab\logs\simulation.log`.

3. Copie réelle :
```powershell
robocopy C:\Lab\Source D:\Lab\Sauvegarde /E /COPY:DAT /R:2 /W:5 /LOG:C:\Lab\logs\sauvegarde.log /TEE
$LASTEXITCODE
```
👉 Explication : `/R:2 /W:5` limite les tentatives à 2 avec 5 secondes d'attente, `/COPY:DAT` copie données, attributs et horodatages, `/TEE` affiche aussi le résultat à l'écran. Le code de sortie est `0` à `7` pour une copie réussie, `8` ou plus signale une erreur.

4. Vérification par empreinte :
```powershell
Get-ChildItem -Recurse D:\Lab\Sauvegarde | Measure-Object
Get-FileHash -Algorithm SHA256 -Path C:\Lab\Source\Compta\facture-001.txt, D:\Lab\Sauvegarde\Compta\facture-001.txt
```
👉 Explication : Compte les éléments copiés, puis compare les deux empreintes SHA-256 : elles doivent être identiques.

---

## ⚡ 2. Production — Façon Simplifiée
1. Sauvegarde miroir vers un partage dédié :
```powershell
robocopy D:\Partages\Compta \\srv-sauv01\Sauvegardes\Compta /MIR /R:2 /W:5 /MT:16 /COPY:DAT /DCOPY:T /LOG+:C:\Journaux\robocopy-compta.log /NP
```
👉 Explication : `/MIR` équivaut à `/E /PURGE` : la destination devient une copie exacte de la source, fichiers supprimés compris. `/MT:16` utilise 16 threads, `/LOG+:` ajoute au journal existant. À réserver à un partage dédié à la sauvegarde.

2. Planification quotidienne à 02:00 :
```powershell
$action = New-ScheduledTaskAction -Execute "robocopy.exe" -Argument 'D:\Partages\Compta \\srv-sauv01\Sauvegardes\Compta /MIR /R:2 /W:5 /MT:16 /COPY:DAT /DCOPY:T /LOG+:C:\Journaux\robocopy-compta.log /NP'
$trigger = New-ScheduledTaskTrigger -Daily -At 02:00
Register-ScheduledTask -TaskName "Sauvegarde-Compta-Robocopy" -Action $action -Trigger $trigger -User "SYSTEM" -RunLevel Highest
```
👉 Explication : Crée la tâche planifiée qui lance la copie chaque nuit. Point à vérifier : le compte `SYSTEM` doit avoir les droits sur le partage `\\srv-sauv01`, sinon remplacer par un compte de service dédié.

3. Contrôle du journal et du résultat de la tâche :
```powershell
Get-Content C:\Journaux\robocopy-compta.log -Tail 30
Get-ScheduledTask -TaskName "Sauvegarde-Compta-Robocopy" | Get-ScheduledTaskInfo
```
👉 Explication : Affiche la fin du journal et le dernier résultat de la tâche (`LastTaskResult`). Un résultat de `0` à `7` correspond à une copie réussie.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Compte de service dédié avec privilège de sauvegarde :
```powershell
Add-LocalGroupMember -Group "Backup Operators" -Member "TSSR\svc-sauvegarde"
Get-LocalGroupMember -Group "Backup Operators"
```
👉 Explication : Ajoute le compte de service au groupe `Backup Operators`, nécessaire au mode `/B`. Ce compte ne doit servir qu'à la sauvegarde et ne pas être administrateur de domaine. Le nom `TSSR\svc-sauvegarde` est un exemple de domaine à adapter. Point à vérifier : sur un contrôleur de domaine, le groupe s'appelle `Opérateurs de sauvegarde` selon la langue du système.

2. Copie en mode sauvegarde, avec ACL et journal daté :
```powershell
$date = Get-Date -Format yyyy-MM-dd
robocopy D:\Partages\Compta \\srv-sauv01\Sauvegardes\Compta /MIR /B /R:2 /W:5 /COPY:DATSO /DCOPY:T /LOG:"C:\Journaux\robocopy-compta-$date.log" /NP
```
👉 Explication : `/B` lit les fichiers avec les privilèges de sauvegarde, sans contourner les droits du partage de destination. `/COPY:DATSO` ajoute les ACL (`S`) et le propriétaire (`O`). Le journal est daté pour conserver l'historique.

3. Test de restauration sans suppression :
```powershell
robocopy \\srv-sauv01\Sauvegardes\Compta C:\Restauration\Compta-test /E /COPY:DAT /R:1 /W:1 /LOG:C:\Journaux\restauration-test.log
```
👉 Explication : Restaure dans un dossier de test. Sans `/PURGE` ni `/MIR`, rien n'est supprimé, même si le dossier de test contient d'autres fichiers.

4. Vérification d'intégrité par empreinte :
```powershell
Get-FileHash -Algorithm SHA256 -Path "D:\Partages\Compta\bilan-2025.xlsx", "C:\Restauration\Compta-test\bilan-2025.xlsx"
```
👉 Explication : Les deux empreintes SHA-256 doivent être identiques. Une différence signale une copie incomplète ou une altération, à remonter au responsable sécurité.

---