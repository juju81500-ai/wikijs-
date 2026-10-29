# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier que tout revient seul après un redémarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Planifier une fenêtre puis redémarrer (**Démarrer > Alimentation > Redémarrer**) :
   ```powershell
   Restart-Computer -Force
   ```
   👉 Explication : redémarre le serveur.

2. Après reconnexion, contrôler la durée d'activité et les services :
   ```powershell
   (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
   Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -ne 'Running'}
   ```
   👉 Explication : la liste d'échecs doit être vide.

3. Vérifier réseau, nom et montages :
   ```powershell
   Get-NetIPConfiguration
   Get-SmbMapping
   Get-Volume
   ```
   👉 Explication : adresse, partages et volumes sont revenus.

## 2. Production — Contrôles

Mesurer le temps de retour en service et l'inscrire au runbook.

## 3. Production — Sécurité

Après redémarrage, vérifier que le pare-feu et Defender sont actifs.

## Validation et retour arrière

- **Validation** : Tous les services reviennent sans intervention.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)