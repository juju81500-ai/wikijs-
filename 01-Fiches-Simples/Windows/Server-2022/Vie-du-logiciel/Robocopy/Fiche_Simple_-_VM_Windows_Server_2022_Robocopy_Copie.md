# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Copie.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers
- **Tags** : `windows-server-2022`, `robocopy`, `copie`

---

## Problème précis à résoudre

Copier réellement les fichiers sans rien supprimer à la destination.

## 1. Hors-Production (Lab / Test / POC)

1. Après validation de l'aperçu, relancer en retirant uniquement `/L` :
   ```powershell
   robocopy $Src $Dst /E /COPY:DAT /DCOPY:DAT /R:2 /W:5 /NP /LOG+:"$Log\copy.log" /TEE
   echo $LASTEXITCODE
   ```
   👉 Explication : sans `/PURGE` ni `/MIR`, rien n'est supprimé à la destination; `/LOG+` ajoute au journal existant.

2. Exclure si besoin avec `/XF` (fichiers) et `/XD` (dossiers), et accélérer avec `/MT:8`.
   👉 Explication : `/MT:n` (1 à 128) active le multithread; rediriger alors le journal avec `/LOG`.

## 2. Production — Contrôles

Planifier la copie via une tâche planifiée utilisant le compte de service.

## 3. Production — Sécurité

- Ne pas ajouter `/PURGE`, `/MIR`, `/MOV` ni `/MOVE` sans approbation.

## Validation et retour arrière

- **Validation** : Code retour inférieur à 8 et fichiers présents à la destination.
- **Retour arrière** : Supprimer les copies indésirables de la destination après relecture du journal.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — exécuter la copie sans suppression](../../../../../02-Fiches-Completes/Windows/Server-2022/Autres/93_Copie_Sauvegarde_Fichiers_Robocopy_Windows_Server_2022.md#4-executer-la-copie-sans-suppression)
