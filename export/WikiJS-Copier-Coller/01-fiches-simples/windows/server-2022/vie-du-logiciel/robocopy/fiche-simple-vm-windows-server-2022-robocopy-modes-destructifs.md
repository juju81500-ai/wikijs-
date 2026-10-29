# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Modes_Destructifs.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers

---

## Problème précis à résoudre

Utiliser `/PURGE` et `/MIR` seulement avec un aperçu et une approbation.

## 1. Hors-Production (Lab / Test / POC)

1. Retenir les options dangereuses : `/PURGE` supprime à la destination ce qui est absent de la source; `/MIR` équivaut à `/E` plus `/PURGE`; `/MOV` et `/MOVE` suppriment la source après copie.
   👉 Explication : ne jamais les utiliser pour une sauvegarde simple.

2. Faire d'abord l'aperçu d'un miroir :
   ```powershell
   robocopy $Src $Dst /MIR /COPY:DAT /DCOPY:DAT /R:2 /W:5 /L /FP /NP /LOG:"$Log\mirror-preview.log" /TEE
   ```
   👉 Explication : `/L` liste sans rien supprimer.

3. Examiner chaque ligne `*EXTRA File` ou `*EXTRA Dir` du journal :
   ```powershell
   Select-String -Path "$Log\mirror-preview.log" -Pattern 'EXTRA'
   ```
   👉 Explication : ce sont les éléments qu'un `/MIR` ou `/PURGE` supprimerait.

4. Tester l'accessibilité de la source avant l'exécution :
   ```powershell
   Test-Path $Src
   ```
   👉 Explication : une source vide, déconnectée ou mal saisie produit un miroir vide.

5. Utiliser une destination dédiée et une sauvegarde indépendante.
   👉 Explication : Robocopy n'a pas de plafond de suppressions.

## 2. Production — Contrôles

Exiger une approbation écrite avant tout `/MIR` ou `/PURGE`.

## 3. Production — Sécurité

- `/B` et `/ZB` contournent les ACL : réservés aux comptes autorisés.
- Ne jamais lancer `/MIR` sur une destination non dédiée.

## Validation et retour arrière

- **Validation** : L'aperçu miroir ne montre aucune suppression inattendue.
- **Retour arrière** : Restaurer depuis une sauvegarde indépendante, une copie shadow ou un snapshot du stockage.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — modes destructifs (avec approbation)](/02-fiches-completes/windows/server-2022/autres/93-copie-sauvegarde-fichiers-robocopy-windows-server-2022#5-modes-destructifs-a-nutiliser-quavec-une-approbation)