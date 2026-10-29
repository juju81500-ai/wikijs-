# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Sauvegarde_Restauration

- **Environnement** : Windows Server 2022, WDS + MDT, partage de déploiement et dossier `RemoteInstall`
- **OS / Version** : Windows Server 2022 (Robocopy et `reg` intégrés); WDS, MDT : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `windows-server-2022`, `wds`, `mdt`, `sauvegarde`, `restauration`

---

## Problème précis à résoudre

Sauvegarder et restaurer la configuration WDS, `RemoteInstall` et le partage MDT. Une sauvegarde simple du partage figure déjà dans la [procédure historique WDS + MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Simple_-_WDS-MDT.md); cette fiche ajoute la configuration WDS et la restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Définir les variables (à remplacer) :
   ```powershell
   $Dest = "E:\SAUVEGARDE_WDS_MDT"
   $Share = "D:\DeploymentShare$"
   $Remote = "D:\RemoteInstall"
   New-Item -ItemType Directory -Path $Dest -Force
   ```
   👉 Explication : chemins MAJUSCULES/valeurs d'exemple à adapter; la destination ne doit pas être sur le même disque.

2. Exporter la configuration WDS :
   ```powershell
   reg export "HKLM\SYSTEM\CurrentControlSet\Services\WDSServer" "$Dest\WDSServer.reg" /y
   wdsutil /Get-Server /Show:Config | Out-File "$Dest\wds_config.txt"
   ```
   👉 Explication : on garde la configuration pour référence. La restauration directe du registre est déconseillée : elle sert à recréer les réglages à la main; vérifier l'approche supportée.

3. Copier le partage et `RemoteInstall` (arrêt des déploiements pendant la copie) :
   ```powershell
   Stop-Service WDSServer
   robocopy $Share "$Dest\Share" /MIR /COPY:DATS /R:2 /W:5 /LOG:"$Dest\share.log"
   robocopy $Remote "$Dest\RemoteInstall" /MIR /COPY:DATS /R:2 /W:5 /LOG:"$Dest\remote.log"
   Start-Service WDSServer
   ```
   👉 Explication : `/MIR` fait un miroir de la source vers la destination (supprime en destination ce qui n'existe plus en source) : ne jamais intervertir source et destination. Code de sortie Robocopy inférieur à 8 = succès.

4. Restaurer (lab, serveur reconstruit avec le rôle et MDT réinstallés selon la procédure historique) :
   ```powershell
   Stop-Service WDSServer
   robocopy "$Dest\Share" $Share /MIR /COPY:DATS /R:2 /W:5
   robocopy "$Dest\RemoteInstall" $Remote /MIR /COPY:DATS /R:2 /W:5
   Start-Service WDSServer
   ```
   👉 Explication : après restauration, recréer le partage SMB si absent (voir la procédure historique), puis rejouer la fiche Recette.

## 2. Production — Contrôles

Planifier la sauvegarde après chaque modification d'image; tester la restauration périodiquement; conserver au moins 2 générations.

## 3. Production — Sécurité

- Destination avec ACL restreintes, chiffrée, copie hors site.
- Le partage contient des identifiants éventuels dans les `.ini` : traiter la sauvegarde comme sensible.

## Validation et retour arrière

- **Validation** : journaux Robocopy sans erreur (code < 8), taille cohérente, recette réussie après restauration.
- **Retour arrière** : la sauvegarde ne modifie pas la source; en cas de mauvaise restauration, recopier la génération précédente.

## Si le problème n'est pas résolu

- [Procédure historique WDS + MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Simple_-_WDS-MDT.md)
- [Fiche d'entrée WDS/MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_WDS-MDT.md)
- [Microsoft Learn — Robocopy](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)
- [Microsoft Learn — wdsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil)
