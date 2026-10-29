# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Valider_Restaurer.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers

---

## Problème précis à résoudre

Valider le résultat, restaurer vers un dossier de test et planifier.

## 1. Hors-Production (Lab / Test / POC)

1. Lire le code retour :
   ```powershell
   echo $LASTEXITCODE
   ```
   👉 Explication : 0 à 7 n'indiquent pas d'échec de copie; 8 ou plus indique au moins un échec.

2. Relancer la commande avec `/L` :
   ```powershell
   robocopy $Src $Dst /E /COPY:DAT /DCOPY:DAT /R:2 /W:5 /L /NP
   ```
   👉 Explication : aucun fichier à copier ne doit rester.

3. Comparer nombre de fichiers et taille source/destination :
   ```powershell
   Get-ChildItem $Src -Recurse -File | Measure-Object Length -Sum
   Get-ChildItem $Dst -Recurse -File | Measure-Object Length -Sum
   ```
   👉 Explication : les totaux doivent concorder.

4. Contrôler les ACL d'un échantillon si `/COPY:DATS` a été utilisé (chemin d'exemple à remplacer) :
   ```powershell
   icacls 'D:\Data\exemple.txt'
   ```
   👉 Explication : on vérifie les droits copiés.

5. Restaurer vers un répertoire de test en inversant source et destination, toujours après `/L`.
   👉 Explication : ne jamais restaurer par-dessus la production sans approbation.

6. Planifier une tâche planifiée avec le compte de service : **Planificateur de tâches > Créer une tâche**.
   👉 Explication : surveiller le journal et le code retour; traiter `>= 8` comme erreur.

## 2. Production — Contrôles

Alerter sur tout code retour supérieur ou égal à 8.

## 3. Production — Sécurité

- Ne pas restaurer par-dessus la production sans approbation.

## Validation et retour arrière

- **Validation** : Aperçu relancé sans fichier restant, totaux concordants, restauration de test réussie.
- **Retour arrière** : Supprimer le dossier de test de restauration.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — valider et restaurer](/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022#6-valider-et-restaurer)