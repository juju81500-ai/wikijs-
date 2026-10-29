# Copier et sauvegarder des fichiers avec Robocopy sur Windows Server 2022

- **Type de fiche** : Autres — copie / sauvegarde de fichiers
- **Environnement** : Windows Server 2022 (Robocopy intégré); partages SMB et volumes NTFS
- **OS / Version** : Windows Server 2022 (valable pour les versions Windows qui incluent Robocopy; non testé sur d'autres)
- **Rôle** : Prévisualiser puis exécuter une copie de fichiers avec journal et garde-fous contre les suppressions

## 1. Périmètre et limites

Fiche simple : [périmètre et limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-perimetre).

Robocopy copie des arborescences de fichiers. Ce n'est pas une sauvegarde historisée ni applicative : les fichiers verrouillés, bases de données et états système exigent une solution adaptée ([Veeam](/02-fiches-completes/windows/server-2022/installation-deploiement/58-deploiement-veeam-backup-replication-13-windows-server-2022), VSS, sauvegarde native). Un miroir propage les suppressions. Ce guide n'a pas été testé sur un serveur Windows 2022.

## 2. Préparer

Fiche simple : [préparer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-preparer).

Exécuter dans un PowerShell ou une invite de commandes avec un compte de service limité, pas avec un administrateur de domaine. Définir les chemins :

```powershell
$Src = 'D:\Data'
$Dst = '\\sauvegarde\backup\Data'
$Log = 'C:\Logs\robocopy'
New-Item -ItemType Directory -Force $Log | Out-Null
```

Vérifier l'existence de la source et l'espace de la destination. En PowerShell, éviter de terminer un chemin entre guillemets par `\` (`"D:\Data\"` casse l'analyse des arguments) : ne pas ajouter de barre oblique finale.

## 3. Prévisualiser (mode par défaut)

Fiche simple : [prévisualiser (mode par défaut)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-previsualiser).

`/L` liste sans copier, supprimer ni modifier les dates. Utiliser `/R` et `/W` explicites : les valeurs par défaut sont 1 000 000 tentatives et 30 secondes, ce qui peut bloquer un travail.

```powershell
robocopy $Src $Dst /E /COPY:DAT /DCOPY:DAT /R:2 /W:5 /L /FP /NP /LOG:"$Log\preview.log" /TEE
echo $LASTEXITCODE
```

`/E` copie les sous-répertoires, vides compris; `/COPY:DAT` copie données, attributs et dates; `/DCOPY:DAT` ajoute les dates des répertoires. Pour conserver les ACL NTFS, ajouter `S` (`/COPY:DATS`) avec les droits nécessaires; `/COPYALL` ajoute propriétaire et audit et exige des privilèges élevés. Relire le journal avant l'étape suivante.

## 4. Exécuter la copie sans suppression

Fiche simple : [exécuter la copie sans suppression](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-copie).

Après validation de l'aperçu, retirer uniquement `/L` :

```powershell
robocopy $Src $Dst /E /COPY:DAT /DCOPY:DAT /R:2 /W:5 /NP /LOG+:"$Log\copy.log" /TEE
echo $LASTEXITCODE
```

Sans `/PURGE` ni `/MIR`, rien n'est supprimé à la destination. Ajouter `/XF`, `/XD` pour exclure fichiers/répertoires, `/MT:n` (1 à 128) pour le multithread en redirigeant le journal avec `/LOG`.

## 5. Modes destructifs (à n'utiliser qu'avec une approbation)

Fiche simple : [modes destructifs (avec approbation)](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-modes-destructifs).

| Option | Effet | Garde-fou |
|---|---|---|
| `/PURGE` | Supprime à la destination fichiers et répertoires absents de la source | Aperçu `/L` obligatoire |
| `/MIR` | Équivaut à `/E` plus `/PURGE`; avec un répertoire de destination, remplace aussi ses paramètres de sécurité | Aperçu `/L`, source vérifiée, destination dédiée |
| `/MOV` | Déplace les fichiers et les supprime de la source après copie | Ne pas l'utiliser pour une sauvegarde |
| `/MOVE` | Déplace fichiers et répertoires, les supprime de la source | Idem |
| `/B`, `/ZB` | Mode sauvegarde : contourne les ACL | Réservé aux comptes autorisés |
| `/SECFIX`, `/TIMFIX` | Corrigent sécurité ou dates, même pour les fichiers ignorés | Aperçu préalable |

Aperçu d'un miroir :

```powershell
robocopy $Src $Dst /MIR /COPY:DAT /DCOPY:DAT /R:2 /W:5 /L /FP /NP /LOG:"$Log\mirror-preview.log" /TEE
```

Examiner chaque ligne « *EXTRA File » ou « *EXTRA Dir » : ce sont les éléments qu'un `/MIR` ou `/PURGE` supprimerait. Une source vide, déconnectée ou mal saisie produit un miroir vide : tester l'accessibilité de la source avant l'exécution. La page de référence ne documente aucun plafond de suppressions : employer une destination dédiée et une sauvegarde indépendante.

## 6. Valider et restaurer

Fiche simple : [valider et restaurer](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-valider-restaurer).

- Code retour : les valeurs de 0 à 7 n'indiquent pas d'échec de copie (bits : fichiers copiés, fichiers en trop, éléments non appariés); une valeur de 8 ou plus indique au moins un échec. L'automatisation doit traiter `>= 8` comme erreur et alerter.
- Relancer la commande avec `/L` : aucun fichier à copier ne doit rester.
- Comparer le nombre de fichiers et la taille source/destination, puis ouvrir un échantillon.
- Contrôler les ACL d'un échantillon (`icacls`) si `/COPY:DATS` a été utilisé.
- Restauration : inverser source et destination, vers un répertoire de test, toujours après `/L`; ne pas restaurer par-dessus la production sans approbation.
- Planification : tâche planifiée utilisant le compte de service; surveiller le journal et le code retour.

## 7. Retour arrière

Fiche simple : [retour arrière](/01-fiches-simples/windows/server-2022/vie-du-logiciel/robocopy/fiche-simple-vm-windows-server-2022-robocopy-retour-arriere).

Sans `/PURGE`/`/MIR`/`/MOV`, supprimer les copies indésirables de la destination après relecture du journal. Après un `/MIR` ou un `/MOVE` erroné, les fichiers supprimés ne sont pas récupérables par Robocopy : les restaurer depuis une sauvegarde indépendante, une copie shadow ou un snapshot du stockage. Conserver les journaux de chaque exécution.

## Sources

- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)

Aucune copie, aucun miroir ni aucune restauration n'ont été testés. Conserver les statuts **À revoir** et **À tester**.