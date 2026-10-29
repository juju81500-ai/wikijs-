# Fiche_Simple_-_Windows_Server_2022_PowerShell_Valider

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Recette de PowerShell sur Windows Server 2022 : versions, profils, modules, remoting et signature.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les deux shells :
   ```powershell
   powershell.exe -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   & 'C:\Program Files\PowerShell\7\pwsh.exe' -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : 5.1 et la version 7 approuvée doivent répondre.

2. Contrôler le service SSH (GUI : services.msc) :
   ```powershell
   Get-Service sshd
   ```
   👉 Explication : état `Running`.

3. Tester le remoting SSH puis WinRM (HOTE et UTILISATEUR à remplacer) :
   ```powershell
   Invoke-Command -HostName HOTE -UserName UTILISATEUR -ScriptBlock { $PSVersionTable.PSVersion }
   Test-WSMan -ComputerName HOTE
   ```
   👉 Explication : valide les deux modes.

4. Contrôler un script signé (CHEMIN_SCRIPT à remplacer) :
   ```powershell
   Get-AuthenticodeSignature CHEMIN_SCRIPT | Select-Object Status
   ```
   👉 Explication : statut `Valid` attendu.

## 2. Production — Contrôles

Consigner la recette dans le dossier d'exploitation. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Supprimer les transcripts de test contenant des données sensibles.

## Validation et retour arrière

- **Validation** : toutes les commandes répondent comme attendu.
- **Retour arrière** : reprendre la fiche concernée par l'échec.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Windows](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-windows)
- [Microsoft Learn — différences 5.1 / 7](https://learn.microsoft.com/powershell/scripting/whats-new/differences-from-windows-powershell)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-prerequis-limites)