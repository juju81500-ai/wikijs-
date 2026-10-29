# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier ce qui tourne et ce qui écoute.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **services.msc** et **Moniteur de ressources > Réseau > Ports d'écoute**.
   ```powershell
   Get-Service | Where-Object Status -eq Running | Sort-Object Name | Select-Object Name, DisplayName
   ```
   👉 Explication : liste les services démarrés.

2. Associer ports d'écoute et processus :
   ```powershell
   Get-NetTCPConnection -State Listen | ForEach-Object { [pscustomobject]@{Port=$_.LocalPort; PID=$_.OwningProcess; Processus=(Get-Process -Id $_.OwningProcess).ProcessName} } | Sort-Object Port
   ```
   👉 Explication : chaque port doit avoir un propriétaire attendu.

3. Rechercher les services défaillants :
   ```powershell
   Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -ne 'Running'}
   ```
   👉 Explication : liste les services automatiques arrêtés à examiner.

## 2. Production — Contrôles

Comparer avec la baseline de l'étape 25.

## 3. Production — Sécurité

Tout port inattendu est un incident potentiel.

## Validation et retour arrière

- **Validation** : Les services et ports correspondent au document d'architecture.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
