# Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Perimetre.md

- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (Robocopy; non testé sur d'autres versions)
- **Catégorie** : copie / sauvegarde de fichiers
- **Tags** : `windows-server-2022`, `robocopy`, `perimetre`

---

## Problème précis à résoudre

Comprendre ce que Robocopy sait faire et ce qu'il ne sait pas faire avant de l'utiliser.

## 1. Hors-Production (Lab / Test / POC)

1. Retenir que Robocopy copie des arborescences de fichiers.
   👉 Explication : ce n'est ni une sauvegarde historisée, ni une sauvegarde applicative.

2. Pour fichiers verrouillés, bases de données et états système, choisir une solution adaptée (Veeam, VSS, sauvegarde native).
   👉 Explication : Robocopy ne copie pas de façon cohérente les fichiers ouverts.

3. Retenir qu'un miroir (`/MIR`) propage les suppressions.
   👉 Explication : un fichier supprimé à la source disparaît aussi de la destination.

4. Afficher l'aide intégrée pour confirmer la disponibilité de l'outil :
   ```powershell
   robocopy /?
   ```
   👉 Explication : la commande existe sur Windows Server 2022 sans installation.

## 2. Production — Contrôles

Documenter quelles données relèvent de Robocopy et lesquelles d'une sauvegarde applicative.

## 3. Production — Sécurité

- Ne pas utiliser Robocopy comme seule sauvegarde.
- Ne jamais lancer `/MIR` sans aperçu.

## Validation et retour arrière

- **Validation** : Le périmètre est écrit et les outils adaptés sont choisis pour chaque type de données.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Guide complet — périmètre et limites](../../../../../02-Fiches-Completes/Windows/Server-2022/Autres/93_Copie_Sauvegarde_Fichiers_Robocopy_Windows_Server_2022.md#1-perimetre-et-limites)
