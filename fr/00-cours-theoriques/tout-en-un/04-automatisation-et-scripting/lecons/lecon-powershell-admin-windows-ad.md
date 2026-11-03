---
title: "Leçon — PowerShell pour l'administration Windows et Active Directory"
description: "À la fin de cette leçon, vous serez capable de :"
published: true
date: 2026-11-03T14:22:28Z
tags: ["transverse", "tout-en-un", "lecon", "automatisation", "powershell", "active-directory", "windows-server", "journalisation"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Leçon — PowerShell pour l'administration Windows et Active Directory

- **Tags** : `transverse`, `tout-en-un`, `lecon`, `automatisation`, `powershell`, `active-directory`, `windows-server`, `journalisation`
- **Niveau** : Intermédiaire (bases de PowerShell acquises)
- **Durée estimée** : 4 h (cours 1 h 45, laboratoire 1 h 15, exercices et quiz 1 h)

---

## Objectifs pédagogiques

À la fin de cette leçon, vous serez capable de :

1. administrer des **services** Windows (lecture, démarrage, arrêt, type de démarrage) en simulant d'abord ;
2. interroger les **journaux d'événements** avec `Get-WinEvent` et un filtre efficace ;
3. inventorier, copier et nettoyer des **fichiers** de façon contrôlée ;
4. utiliser le module **ActiveDirectory** pour rechercher, créer et modifier des comptes et des groupes ;
5. automatiser des créations à partir d'un **fichier CSV** avec contrôles préalables ;
6. appliquer `-WhatIf` et `-Confirm`, et les intégrer à vos propres fonctions ;
7. gérer les erreurs avec `-ErrorAction Stop` et `try/catch/finally` ;
8. **journaliser** ses actions sans y écrire de secret.

## Prérequis et durée

- Leçon « PowerShell pour débuter » maîtrisée : pipeline, `Where-Object`, `Select-Object`, `Get-Help`.
- Connaissance des notions d'annuaire : domaine, unité d'organisation ([[Glossary:OU]]), utilisateur, groupe.
- Un **laboratoire jetable** : un contrôleur de domaine Windows Server de test pour le domaine fictif `example.test` et un poste ou serveur membre avec les outils RSAT. Prenez un instantané avant chaque séance. **Ne testez jamais d'abord sur un annuaire de production.**
- Durée : environ 4 h.

> Valeurs de documentation uniquement : 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24, 2001:db8::/32, domaine `example.test`. Aucun mot de passe réel n'apparaît dans cette leçon.

## L'essentiel en bref

- Toute automatisation d'administration suit le cycle : **lire → simuler → appliquer → vérifier → journaliser**.
- `Get-Service`, `Get-WinEvent`, `Get-ChildItem` lisent ; `Set-*`, `Restart-*`, `Remove-*` modifient.
- Le module **ActiveDirectory** (outils RSAT) fournit `Get-ADUser`, `New-ADUser`, `Get-ADGroup`, `Add-ADGroupMember`…
- `Import-Csv` transforme chaque ligne en objet : une ligne = un compte à traiter.
- `-WhatIf` simule, `-Confirm` demande validation ; vos fonctions peuvent les gérer avec `SupportsShouldProcess`.
- Une erreur n'est « attrapable » par `try/catch` que si elle est **terminante** : ajoutez `-ErrorAction Stop`.
- Un journal sert de preuve, de diagnostic et de point de reprise ; il ne contient jamais de mot de passe.

---

## 1. Un cycle de travail sûr

Administrer par script, c'est multiplier la portée d'un geste : une faute de frappe touche mille comptes au lieu d'un. On compense par une discipline.

![Cycle en quatre étapes : lire, simuler, appliquer, vérifier avec journalisation](images/powershell-admin-ad-4.svg)

*Figure 1 — Cycle de travail sûr : lire, simuler, appliquer, vérifier. Création originale du projet Pack Master (CC0).*

**Analogie.** Un chirurgien fait un « time-out » avant d'opérer : il vérifie le patient, le côté, l'acte. Le script fait pareil : il lit l'état, simule, n'applique qu'après relecture, puis contrôle le résultat.

Vérifications de départ sur la machine d'administration :

```powershell
$PSVersionTable.PSVersion
whoami
Get-Command -Module ActiveDirectory | Measure-Object
```

👉 Explication : vérifie la version de PowerShell, le compte utilisé (principe du **moindre privilège** : un compte d'administration dédié, jamais votre compte de messagerie) et la présence du module Active Directory. Si le comptage est nul, installez les outils RSAT dans le laboratoire (fonctionnalité optionnelle « Outils RSAT Active Directory » sur un poste, ou rôle d'outils sur un serveur).

## 2. Administrer les services Windows

### 2.1 Lire

```powershell
Get-Service -Name Spooler
Get-Service | Where-Object { $_.Status -eq 'Running' } | Sort-Object DisplayName | Select-Object -First 10 Name, DisplayName
Get-Service -Name Spooler -DependentServices
```

👉 Explication : état d'un service, dix services démarrés par ordre alphabétique, puis les services qui **dépendent** de celui-ci (à connaître avant un arrêt). `Status` vaut `Running`, `Stopped`, `Paused`…

Pour le mode de démarrage détaillé et le compte d'exécution, le fournisseur CIM est plus complet :

```powershell
Get-CimInstance -ClassName Win32_Service -Filter "Name='Spooler'" | Select-Object Name, State, StartMode, StartName
```

👉 Explication : interroge Windows Management via CIM ; `StartMode` (`Auto`, `Manual`, `Disabled`) et `StartName` (compte d'exécution) sont utiles pour un audit.

### 2.2 Modifier, toujours avec simulation

```powershell
Restart-Service -Name Spooler -WhatIf
Restart-Service -Name Spooler -Confirm
Set-Service -Name Spooler -StartupType Manual -WhatIf
```

👉 Explication : `-WhatIf` affiche « What if: Performing the operation "Restart-Service"… » sans toucher au service ; `-Confirm` demande validation ; `Set-Service` change le type de démarrage. Après avoir relu la simulation, retirez `-WhatIf` pour agir, dans le laboratoire d'abord.

### 2.3 Exécuter sur un serveur distant (principe)

```powershell
Invoke-Command -ComputerName srv01.example.test -ScriptBlock { Get-Service -Name W32Time }
```

👉 Explication : exécute un bloc sur un serveur géré à distance (WinRM, port 5985/5986) et rapatrie les objets. Prérequis : accès réseau autorisé, droits adaptés et remoting activé ; à ne tenter qu'en laboratoire.

## 3. Lire les journaux d'événements

`Get-WinEvent` est la cmdlet moderne ; `Get-EventLog` n'existe qu'en Windows PowerShell 5.1 et ne lit que les journaux classiques.

```powershell
Get-WinEvent -ListLog System, Application | Select-Object LogName, RecordCount, IsEnabled
Get-WinEvent -LogName System -MaxEvents 20 | Select-Object TimeCreated, Id, LevelDisplayName, ProviderName
```

👉 Explication : la première ligne énumère des journaux et leur volume ; la seconde lit les vingt événements les plus récents. Les événements sont renvoyés du plus récent au plus ancien.

### 3.1 Filtrer à la source avec FilterHashtable

```powershell
$debut = (Get-Date).AddHours(-24)
Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 1, 2; StartTime = $debut } |
    Select-Object TimeCreated, Id, ProviderName, Message |
    Format-Table -Wrap -AutoSize
```

👉 Explication : demande au système de ne renvoyer que les événements **critiques (1) et erreurs (2)** des dernières 24 heures. Le filtrage côté source est bien plus rapide que de tout lire puis d'appliquer `Where-Object`. Niveaux : 1 critique, 2 erreur, 3 avertissement, 4 information.

### 3.2 Résumer

```powershell
Get-WinEvent -FilterHashtable @{ LogName = 'System'; Level = 2; StartTime = $debut } |
    Group-Object -Property ProviderName |
    Sort-Object Count -Descending |
    Select-Object -First 5 Count, Name
```

👉 Explication : montre les cinq sources qui génèrent le plus d'erreurs, un point d'entrée classique pour un diagnostic.

## 4. Gérer les fichiers avec méthode

```powershell
$racine = "D:\Partage\Projets"
Test-Path -Path $racine
Get-ChildItem -Path $racine -Recurse -File |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-365) } |
    Sort-Object Length -Descending |
    Select-Object -First 20 FullName, Length, LastWriteTime
```

👉 Explication : vérifie que le chemin existe puis liste les vingt plus gros fichiers non modifiés depuis un an. Cette étape de **lecture** précède tout archivage.

Pour archiver puis nettoyer :

```powershell
$archive = "D:\Archives\Projets-2026"
New-Item -Path $archive -ItemType Directory -Force | Out-Null
Get-ChildItem -Path $racine -Recurse -File |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-365) } |
    Copy-Item -Destination $archive -WhatIf
```

👉 Explication : crée la destination si besoin, puis **simule** la copie des fichiers anciens. Copier d'abord, vérifier (`Get-FileHash` compare les empreintes), supprimer ensuite seulement après validation. Cette copie à plat écraserait des homonymes : pour conserver l'arborescence, préférez `robocopy`.

```powershell
(Get-FileHash -Path .\rapport.docx -Algorithm SHA256).Hash
Remove-Item -Path "D:\Temp\*.tmp" -WhatIf
```

👉 Explication : l'empreinte SHA-256 d'un fichier prouve qu'une copie est identique à l'original ; la suppression est encore simulée.

## 5. Active Directory avec le module ActiveDirectory

![Arborescence d'un domaine example.test avec deux unités d'organisation, des utilisateurs et des groupes](images/powershell-admin-ad-1.svg)

*Figure 2 — Structure d'un annuaire (exemple fictif). Création originale du projet Pack Master (CC0).*

Chargement du module et prise en main :

```powershell
Import-Module ActiveDirectory
Get-ADDomain | Select-Object DNSRoot, NetBIOSName, DomainMode
Get-ADOrganizationalUnit -Filter * | Select-Object Name, DistinguishedName
```

👉 Explication : charge le module, affiche des informations sur le domaine, puis liste les OU avec leur **nom distinctif** (`DistinguishedName`, par exemple `OU=Comptabilite,DC=example,DC=test`), qui désigne l'emplacement exact d'un objet dans l'arbre.

### 5.1 Rechercher des utilisateurs

```powershell
Get-ADUser -Identity alice.durand -Properties Mail, Department, LastLogonDate, Enabled
Get-ADUser -Filter "Department -eq 'Comptabilite' -and Enabled -eq 'True'" -SearchBase "OU=Comptabilite,DC=example,DC=test" |
    Select-Object Name, SamAccountName
```

👉 Explication : la première commande lit un compte et des attributs supplémentaires (par défaut, seuls quelques attributs sont renvoyés : il faut les demander avec `-Properties`). La seconde utilise `-Filter`, dont la syntaxe est un **mini-langage propre au module** (chaîne, valeurs entre apostrophes), et limite la recherche à une OU avec `-SearchBase`.

Deux requêtes d'audit courantes :

```powershell
Search-ADAccount -LockedOut | Select-Object Name, SamAccountName, LastLogonDate
Search-ADAccount -AccountInactive -TimeSpan 90.00:00:00 -UsersOnly | Select-Object Name, LastLogonDate
```

👉 Explication : comptes verrouillés, puis comptes inactifs depuis 90 jours. Cette sortie sert à **examiner**, pas à désactiver automatiquement : une revue humaine reste nécessaire.

### 5.2 Groupes

```powershell
Get-ADGroup -Identity GG-Compta | Select-Object Name, GroupScope, GroupCategory
Get-ADGroupMember -Identity GG-Compta -Recursive | Select-Object Name, ObjectClass
Add-ADGroupMember -Identity GG-Compta -Members alice.durand -WhatIf
```

👉 Explication : lit un groupe (étendue et catégorie), liste ses membres y compris ceux des groupes imbriqués (`-Recursive`), puis simule l'ajout d'un compte. Retirez `-WhatIf` après validation. Testez d'abord sur un groupe de laboratoire.

### 5.3 Créer et modifier un utilisateur

```powershell
$mdp = Read-Host -Prompt "Mot de passe initial (temporaire)" -AsSecureString

New-ADUser -Name "Claire Petit" `
    -GivenName "Claire" -Surname "Petit" `
    -SamAccountName "claire.petit" `
    -UserPrincipalName "claire.petit@example.test" `
    -Path "OU=Comptabilite,DC=example,DC=test" `
    -AccountPassword $mdp `
    -Enabled $true -ChangePasswordAtLogon $true `
    -WhatIf
```

👉 Explication : `Read-Host -AsSecureString` demande le mot de passe à la saisie et le garde sous forme chiffrée en mémoire (rien n'est écrit dans le script ni le journal). `New-ADUser` reçoit nom, identifiants, emplacement et obligation de changer le mot de passe à la première connexion ; ici avec `-WhatIf`. Les accents graves (`` ` ``) à la fin des lignes continuent la commande ; préférez le *splatting* (une table de hachage passée avec `@parametres`) pour la lisibilité.

```powershell
Set-ADUser -Identity claire.petit -Department "Comptabilite" -Title "Assistante" -WhatIf
Unlock-ADAccount -Identity claire.petit -WhatIf
Disable-ADAccount -Identity claire.petit -WhatIf
```

👉 Explication : modifie des attributs, déverrouille, désactive. La **désactivation** est préférable à la suppression lors d'un départ : elle est réversible et conserve l'historique.

## 6. Importer des comptes depuis un CSV

![Flux d'import CSV : lecture, vérification, simulation, création, journalisation](images/powershell-admin-ad-2.svg)

*Figure 3 — Import CSV : lire, vérifier, simuler, appliquer, journaliser. Création originale du projet Pack Master (CC0).*

Fichier `utilisateurs.csv` (données fictives, séparateur point-virgule, encodage UTF-8) :

```text
Prenom;Nom;Sam;Service;OU
Alice;Durand;alice.durand;Comptabilite;OU=Comptabilite,DC=example,DC=test
Bob;Martin;bob.martin;Informatique;OU=Informatique,DC=example,DC=test
Claire;Petit;claire.petit;Comptabilite;OU=Comptabilite,DC=example,DC=test
```

👉 Explication : une ligne d'en-tête nomme les colonnes ; chaque ligne suivante devient un objet dont les propriétés portent ces noms. Aucun mot de passe n'y figure : ne mettez jamais de secret dans un CSV.

```powershell
$lignes = Import-Csv -Path .\utilisateurs.csv -Delimiter ';' -Encoding UTF8
$lignes | Format-Table -AutoSize
$lignes | Group-Object Sam | Where-Object Count -gt 1
```

👉 Explication : lit le fichier, l'affiche puis détecte les **doublons** de `Sam` (si la dernière commande renvoie quelque chose, corrigez le fichier avant d'aller plus loin).

Un script complet (à enregistrer sous `Import-Utilisateurs.ps1`) avec contrôles, simulation et journal :

```powershell
[CmdletBinding(SupportsShouldProcess)]
param(
    [Parameter(Mandatory)][string]$Csv,
    [string]$Journal = ".\creation-$(Get-Date -Format 'yyyyMMdd-HHmmss').log"
)

function Write-Log {
    param([string]$Niveau, [string]$Message)
    $ligne = "{0} [{1}] {2}" -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Niveau, $Message
    Add-Content -Path $Journal -Value $ligne -Encoding UTF8
    Write-Verbose $ligne
}

Import-Module ActiveDirectory -ErrorAction Stop
$mdp = Read-Host -Prompt "Mot de passe initial (temporaire)" -AsSecureString

foreach ($u in Import-Csv -Path $Csv -Delimiter ';' -Encoding UTF8) {
    if ([string]::IsNullOrWhiteSpace($u.Sam) -or [string]::IsNullOrWhiteSpace($u.OU)) {
        Write-Log 'WARN' "Ligne ignorée (champ vide) : $($u.Prenom) $($u.Nom)"
        continue
    }
    try {
        if (Get-ADUser -Filter "SamAccountName -eq '$($u.Sam)'") {
            Write-Log 'INFO' "$($u.Sam) existe déjà : aucune action"
            continue
        }
        if ($PSCmdlet.ShouldProcess($u.Sam, 'Créer le compte')) {
            New-ADUser -Name "$($u.Prenom) $($u.Nom)" -GivenName $u.Prenom -Surname $u.Nom `
                -SamAccountName $u.Sam -UserPrincipalName "$($u.Sam)@example.test" `
                -Department $u.Service -Path $u.OU -AccountPassword $mdp `
                -Enabled $true -ChangePasswordAtLogon $true -ErrorAction Stop
            Write-Log 'OK' "$($u.Sam) créé dans $($u.OU)"
        }
    }
    catch {
        Write-Log 'ERREUR' "$($u.Sam) : $($_.Exception.Message)"
    }
}
```

👉 Explication : `SupportsShouldProcess` ajoute `-WhatIf`/`-Confirm` au script lui-même ; `$PSCmdlet.ShouldProcess()` décide si l'action a lieu. Le script ignore les lignes incomplètes, ne recrée pas un compte existant (**idempotence**), attrape chaque erreur ligne par ligne sans arrêter toute la boucle, et écrit un journal sans secret. Lancez-le d'abord avec `.\Import-Utilisateurs.ps1 -Csv .\utilisateurs.csv -WhatIf -Verbose`.

## 7. -WhatIf et -Confirm dans vos fonctions

```powershell
function Remove-FichiersAnciens {
    [CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'High')]
    param(
        [Parameter(Mandatory)][string]$Chemin,
        [int]$JoursAnciennete = 365
    )
    Get-ChildItem -Path $Chemin -File -Recurse |
        Where-Object LastWriteTime -lt (Get-Date).AddDays(-$JoursAnciennete) |
        ForEach-Object {
            if ($PSCmdlet.ShouldProcess($_.FullName, 'Supprimer')) { Remove-Item -LiteralPath $_.FullName }
        }
}
```

👉 Explication : la fonction déclare qu'elle modifie le système (`SupportsShouldProcess`) et que l'impact est élevé (`ConfirmImpact = 'High'` provoque une demande de confirmation par défaut). Appeler `Remove-FichiersAnciens -Chemin D:\Temp -WhatIf` ne supprime rien. `-LiteralPath` évite d'interpréter des crochets ou jokers dans les noms de fichiers.

La variable `$WhatIfPreference = $true` active la simulation pour toute la session ; `-Confirm:$false` supprime la question dans une tâche planifiée, uniquement après validation en simulation.

## 8. Gestion des erreurs : try / catch / finally

PowerShell distingue deux types d'erreurs :

- **non terminante** : la cmdlet signale l'erreur et continue (elle ne déclenche pas `catch`) ;
- **terminante** : l'exécution du bloc s'arrête et le `catch` prend la main.

![Organigramme try, catch, finally](images/powershell-admin-ad-3.svg)

*Figure 4 — Le bloc try s'exécute ; une erreur terminante déclenche catch ; finally s'exécute dans tous les cas. Création originale du projet Pack Master (CC0).*

Pour rendre une erreur attrapable, ajoutez `-ErrorAction Stop` :

```powershell
try {
    $u = Get-ADUser -Identity "inconnu.test" -ErrorAction Stop
    Write-Output "Trouvé : $($u.Name)"
}
catch [Microsoft.ActiveDirectory.Management.ADIdentityNotFoundException] {
    Write-Warning "Utilisateur absent de l'annuaire."
}
catch {
    Write-Error "Erreur inattendue : $($_.Exception.Message)"
}
finally {
    Write-Verbose "Contrôle terminé" -Verbose
}
```

👉 Explication : un premier `catch` cible le type d'erreur « identité introuvable », un second attrape le reste ; `finally` s'exécute dans tous les cas (fermeture de session, nettoyage). Dans un `catch`, `$_` est l'enregistrement d'erreur : `$_.Exception.Message` donne le message, `$_.InvocationInfo.ScriptLineNumber` la ligne.

```powershell
$ErrorActionPreference = 'Stop'
Get-Help about_Try_Catch_Finally
$Error[0] | Format-List * -Force
```

👉 Explication : la première ligne rend toutes les erreurs terminantes pour le script en cours (à placer en tête de script, avec discernement) ; l'aide `about_Try_Catch_Finally` détaille la syntaxe ; `$Error[0]` est la dernière erreur de la session, à examiner en détail.

Bonnes pratiques :
- ne jamais avaler une erreur sans la consigner (`catch {}` vide) ;
- distinguer l'erreur attendue (compte déjà présent) de l'erreur grave (annuaire injoignable) ;
- prévoir une **sortie propre** : code de retour (`exit 1`) pour un script lancé par un planificateur.

## 9. Journaliser ses actions

Un bon journal répond à : *quand, qui, quoi, sur quoi, quel résultat ?*

```powershell
Start-Transcript -Path ".\transcript-$(Get-Date -Format 'yyyyMMdd').txt" -Append
Get-Service -Name Spooler
Stop-Transcript
```

👉 Explication : `Start-Transcript` enregistre tout ce qui s'affiche dans la session ; pratique en laboratoire et pour des interventions ponctuelles. Attention : une transcription capture aussi ce que vous tapez ou affichez, donc potentiellement un secret affiché par erreur.

Pour une journalisation maîtrisée, une fonction dédiée (comme `Write-Log` plus haut) produit des lignes structurées. Autre option pratique, un journal CSV exploitable :

```powershell
[pscustomobject]@{
    Date     = Get-Date -Format 'o'
    Operateur = $env:USERNAME
    Action   = 'Creation'
    Cible    = 'claire.petit'
    Resultat = 'OK'
} | Export-Csv -Path .\journal-actions.csv -Append -NoTypeInformation -Encoding UTF8
```

👉 Explication : une ligne par action avec date au format ISO 8601, opérateur, cible et résultat ; l'option `-Append` ajoute sans écraser. Protégez les journaux en écriture et définissez leur durée de conservation. N'y consignez jamais de mot de passe ni de jeton.

## Mise en pratique guidée

**Contexte.** Laboratoire : contrôleur de domaine de test (`example.test`, adresse 192.0.2.10) et poste d'administration avec RSAT. Instantanés pris. Tout commence en **simulation**.

1. **Créer une OU de test** (dans le labo uniquement).
   ```powershell
   New-ADOrganizationalUnit -Name "LabLecon" -Path "DC=example,DC=test" -ProtectedFromAccidentalDeletion $true -WhatIf
   ```
   👉 Explication : simule la création d'une OU protégée contre la suppression accidentelle ; retirez `-WhatIf` pour la créer.

2. **Préparer le CSV** `utilisateurs.csv` avec trois comptes fictifs, en remplaçant la colonne OU par `OU=LabLecon,DC=example,DC=test`.

3. **Lancer le script en simulation.**
   ```powershell
   .\Import-Utilisateurs.ps1 -Csv .\utilisateurs.csv -WhatIf -Verbose
   ```
   👉 Explication : doit afficher trois « What if » de création ; la simulation ne teste pas la politique de mot de passe du domaine.

4. **Lancer réellement**, puis contrôler.
   ```powershell
   .\Import-Utilisateurs.ps1 -Csv .\utilisateurs.csv
   Get-ADUser -SearchBase "OU=LabLecon,DC=example,DC=test" -Filter * | Select-Object Name, Enabled
   Get-Content (Get-ChildItem .\creation-*.log | Sort-Object LastWriteTime -Descending | Select-Object -First 1)
   ```
   👉 Explication : crée les comptes, vérifie leur présence et lit le dernier journal. Relancez une seconde fois : chaque ligne doit afficher « existe déjà », preuve d'idempotence.

5. **Provoquer une erreur** : ajoutez une ligne avec une OU inexistante et relancez ; le journal doit contenir une ligne `ERREUR` sans interrompre les autres lignes.

6. **Groupes.** Créez un groupe de test et ajoutez-y un membre :
   ```powershell
   New-ADGroup -Name "GG-Lab" -GroupScope Global -GroupCategory Security -Path "OU=LabLecon,DC=example,DC=test" -WhatIf
   Add-ADGroupMember -Identity "GG-Lab" -Members "claire.petit" -WhatIf
   ```
   👉 Explication : simule la création puis l'ajout ; enlevez `-WhatIf` dans l'ordre pour les exécuter réellement.

7. **Nettoyage.** Désactivez la protection de l'OU puis supprimez-la, ou restaurez l'instantané de la [[Glossary:VM]].
   ```powershell
   Set-ADOrganizationalUnit -Identity "OU=LabLecon,DC=example,DC=test" -ProtectedFromAccidentalDeletion $false
   Remove-ADOrganizationalUnit -Identity "OU=LabLecon,DC=example,DC=test" -Recursive -WhatIf
   ```
   👉 Explication : sans la première commande, la suppression est refusée ; relisez la simulation avant de retirer `-WhatIf`. La restauration d'instantané est plus simple pour un contrôleur de domaine de laboratoire.

## Exercices

1. **(facile)** Listez les services dont le type de démarrage est `Automatic` mais qui sont `Stopped`. Affichez `Name` et `DisplayName`.
2. **(facile)** Écrivez la commande qui **simule** l'arrêt du service `Spooler` et celle qui demande confirmation avant de l'arrêter.
3. **(moyen)** Récupérez les erreurs du journal `Application` des 7 derniers jours avec `FilterHashtable` et comptez-les par `ProviderName`.
4. **(moyen)** Listez les dix plus gros fichiers de `D:\Partage` modifiés il y a plus de 180 jours, avec taille en Mo.
5. **(moyen)** Affichez les membres directs du groupe `GG-Compta` puis les membres récursifs, et expliquez la différence.
6. **(moyen)** Écrivez le bloc `try/catch` qui tente de lire un utilisateur absent, journalise un avertissement et poursuit.
7. **(avancé)** Complétez le script d'import pour qu'il ajoute chaque compte créé au groupe nommé dans une colonne `Groupe` du CSV, avec `-WhatIf` géré et journalisation.
8. **(avancé)** Proposez un contrôle préalable qui refuse un CSV contenant des doublons de `Sam` ou des champs vides avant toute création.

## Corrigés des exercices

1. ```powershell
   Get-Service | Where-Object { $_.StartType -eq 'Automatic' -and $_.Status -eq 'Stopped' } | Select-Object Name, DisplayName
   ```
   👉 Explication : deux conditions en `-and`. Certains services « à démarrage différé ou déclenché » peuvent être arrêtés légitimement : vérifiez avant d'agir.

2. ```powershell
   Stop-Service -Name Spooler -WhatIf
   Stop-Service -Name Spooler -Confirm
   ```
   👉 Explication : la première simule seulement ; la seconde demande confirmation. Regardez d'abord `Get-Service Spooler -DependentServices`.

3. ```powershell
   Get-WinEvent -FilterHashtable @{ LogName='Application'; Level=2; StartTime=(Get-Date).AddDays(-7) } |
       Group-Object ProviderName | Sort-Object Count -Descending | Select-Object Count, Name
   ```
   👉 Explication : filtre côté source puis regroupe ; si aucun événement n'existe, l'erreur « No events were found » est un résultat vide.

4. ```powershell
   Get-ChildItem D:\Partage -Recurse -File |
       Where-Object LastWriteTime -lt (Get-Date).AddDays(-180) |
       Sort-Object Length -Descending | Select-Object -First 10 FullName,
           @{Name='Taille_Mo'; Expression={ [math]::Round($_.Length / 1MB, 2) }}
   ```
   👉 Explication : lecture seule ; la propriété calculée convertit les octets en Mo.

5. ```powershell
   Get-ADGroupMember -Identity GG-Compta
   Get-ADGroupMember -Identity GG-Compta -Recursive
   ```
   👉 Explication : la première commande ne montre que les membres directs (utilisateurs et groupes imbriqués) ; la seconde « aplatit » les groupes imbriqués et renvoie les comptes finaux.

6. ```powershell
   try { Get-ADUser -Identity 'absent.test' -ErrorAction Stop }
   catch [Microsoft.ActiveDirectory.Management.ADIdentityNotFoundException] {
       Write-Log 'WARN' 'absent.test introuvable'
   }
   ```
   👉 Explication : le type d'exception cible précisément l'absence ; sans `-ErrorAction Stop`, le `catch` ne serait pas déclenché sur certaines cmdlets.

7. Ajouter dans le bloc `ShouldProcess`, après `New-ADUser` :
   ```powershell
   if ($u.Groupe) {
       Add-ADGroupMember -Identity $u.Groupe -Members $u.Sam -ErrorAction Stop
       Write-Log 'OK' "$($u.Sam) ajouté à $($u.Groupe)"
   }
   ```
   👉 Explication : le `ShouldProcess` englobant couvre aussi cette étape ; en simulation rien n'est ajouté. Prévoyez un `catch` distinct si le groupe n'existe pas.

8. ```powershell
   $doublons = $lignes | Group-Object Sam | Where-Object Count -gt 1
   $vides    = $lignes | Where-Object { -not $_.Sam -or -not $_.OU }
   if ($doublons -or $vides) { Write-Error "CSV invalide : corrigez avant import."; exit 1 }
   ```
   👉 Explication : on valide **tout** le fichier avant le premier changement, car un import partiel est plus difficile à rattraper.

## Quiz

**1. Pourquoi `try/catch` ne réagit-il pas toujours à une erreur de cmdlet ?**
a) Il ne marche qu'en PowerShell 7 ; b) l'erreur est non terminante par défaut ; c) `catch` est réservé aux fonctions ; d) il faut `Write-Host`.
**Réponse : b.** Beaucoup d'erreurs de cmdlet n'arrêtent pas l'exécution ; `-ErrorAction Stop` les rend terminantes.

**2. Quel est l'avantage de `-FilterHashtable` avec `Get-WinEvent` ?**
a) Il formate le texte ; b) il filtre à la source et évite de lire tout le journal ; c) il supprime les événements ; d) il chiffre le journal.
**Réponse : b.** Le filtrage est réalisé par le service d'événements, donc bien plus rapide.

**3. Quelle option demande seulement d'afficher ce qui serait fait ?**
a) `-Force` ; b) `-Verbose` ; c) `-WhatIf` ; d) `-PassThru`.
**Réponse : c.** `-WhatIf` simule l'action sans l'exécuter.

**4. Comment demander à `Get-ADUser` l'attribut `Mail` ?**
a) Il est toujours renvoyé ; b) `-Properties Mail` ; c) `-Attribute Mail` ; d) `-Select Mail`.
**Réponse : b.** Seuls certains attributs sont renvoyés par défaut ; `-Properties` ajoute les autres.

**5. Que renvoie `Get-ADGroupMember -Recursive` ?**
a) Seulement les groupes ; b) les membres, y compris ceux des groupes imbriqués ; c) les groupes parents ; d) les OU.
**Réponse : b.** Il parcourt les groupes imbriqués et renvoie les membres finaux.

**6. Où saisir le mot de passe initial lors d'un import CSV ?**
a) Dans une colonne du CSV ; b) en clair dans le script ; c) via `Read-Host -AsSecureString` à l'exécution ; d) dans le journal.
**Réponse : c.** Aucun secret ne doit se trouver dans un fichier, un script ou un journal.

**7. Que garantit un script idempotent ?**
a) Qu'il s'exécute vite ; b) que relancé il ne recrée ni ne modifie ce qui est déjà conforme ; c) qu'il ne produit pas de journal ; d) qu'il n'exige pas de droits.
**Réponse : b.** Il teste l'état avant d'agir, ce qui permet de reprendre après une panne.

**8. Pourquoi désactiver plutôt que supprimer un compte lors d'un départ ?**
a) C'est plus rapide ; b) la désactivation est réversible et conserve l'historique ; c) la suppression est interdite par Windows ; d) cela libère une licence.
**Réponse : b.** La désactivation permet une reprise et un audit ; la suppression suit la procédure de conservation de l'organisation.

**9. Quel est le rôle de `finally` ?**
a) S'exécuter seulement en cas d'erreur ; b) s'exécuter seulement en cas de succès ; c) s'exécuter dans tous les cas ; d) remplacer `catch`.
**Réponse : c.** Il sert au nettoyage (fermeture, libération) quel que soit le résultat.

**10. Que ne faut-il jamais écrire dans un journal ?**
a) La date ; b) le nom de la cible ; c) un mot de passe ou un jeton ; d) le résultat de l'action.
**Réponse : c.** Un journal est souvent lu par plus de personnes que le script lui-même ; un secret y serait exposé.

## Erreurs fréquentes et dépannage

| Symptôme | Cause probable | Remède |
|---|---|---|
| `Get-ADUser` « n'est pas reconnu » | Module ActiveDirectory/RSAT absent | Installer RSAT dans le labo, `Import-Module ActiveDirectory` |
| « Impossible de contacter le serveur » (AD Web Services) | Port 9389 bloqué, DC injoignable | Vérifier DNS et pare-feu, préciser `-Server dc01.example.test` |
| « Accès refusé » | Compte sans délégation sur l'OU | Utiliser un compte délégué ; ne pas élever par réflexe |
| `catch` jamais déclenché | Erreur non terminante | Ajouter `-ErrorAction Stop` |
| `-Filter` renvoie une erreur de syntaxe | Mauvais guillemets ou bloc de script | Chaîne entre guillemets, valeurs entre apostrophes |
| Caractères accentués corrompus à l'import | Encodage ou séparateur incorrect | `-Encoding UTF8 -Delimiter ';'` |
| Mot de passe refusé à la création | Politique de complexité du domaine | Respecter la politique ; c'est le DC qui valide |
| Journal vide | Chemin inexistant ou non inscriptible | `Test-Path`, droits sur le dossier |
| Simulation correcte mais exécution en échec | `-WhatIf` ne teste pas tout (droits, politique de mot de passe) | Essayer d'abord sur un objet de labo |
| `Get-WinEvent` « No events were found » | Filtre trop étroit ou journal désactivé | Élargir la période, `Get-WinEvent -ListLog` |

## À retenir

- Cycle : **lire → simuler → appliquer → vérifier → journaliser**.
- `Get-WinEvent -FilterHashtable` filtre à la source ; les niveaux 1 et 2 sont critique et erreur.
- Le module ActiveDirectory demande `-Properties` pour les attributs hors défaut et un `-SearchBase` pour cibler une OU.
- Un import CSV se valide en entier avant d'agir, ligne par ligne ensuite, sans arrêter tout le lot sur une erreur.
- `SupportsShouldProcess` et `ShouldProcess()` donnent `-WhatIf` et `-Confirm` à vos propres commandes.
- `try/catch` exige des erreurs **terminantes** (`-ErrorAction Stop`).
- Aucun secret dans un CSV, un script, un journal ou un dépôt.
- Un script idempotent et journalisé peut être relancé sans crainte.

## Pour aller plus loin

- Module ActiveDirectory : <https://learn.microsoft.com/powershell/module/activedirectory/>
- `Get-WinEvent` : <https://learn.microsoft.com/powershell/module/microsoft.powershell.diagnostics/get-winevent>
- `about_Try_Catch_Finally` : <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_try_catch_finally>
- `about_Common_Parameters` : <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_commonparameters>
- Guide de la méthode `ShouldProcess` : <https://learn.microsoft.com/powershell/scripting/learn/deep-dives/everything-about-shouldprocess>
- Adresses réservées à la documentation (RFC 5737) : <https://www.rfc-editor.org/rfc/rfc5737>
- Noms de domaine réservés aux tests (RFC 6761) : <https://www.rfc-editor.org/rfc/rfc6761>

## Crédits des images

Aucune image libre adaptée n'a été retenue (captures de produits propriétaires et logos exclus) : les quatre schémas ont été dessinés pour cette leçon.

| Fichier | Source (URL de la page) | Auteur | Licence | Modifications |
|---|---|---|---|---|
| `images/powershell-admin-ad-1.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0, dédiée au domaine public — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/powershell-admin-ad-2.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/powershell-admin-ad-3.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |
| `images/powershell-admin-ad-4.svg` | Création originale du projet Pack Master | Projet Pack Master | CC0 1.0 — <https://creativecommons.org/publicdomain/zero/1.0/deed.fr> | Aucune |

Création originale du projet Pack Master, dédiée au domaine public (CC0).

## Historique de vérification

| Date | OS/logiciel | Testeur | Verdict |
|---|---|---|---|
| 2026-11-01 | Windows Server (contrôleur de domaine) / PowerShell 5.1 et 7 / module ActiveDirectory | Rédaction assistée (agent Copilot) — relecture statique ; aucune commande PowerShell exécutée | Non testé sur plateforme cible |