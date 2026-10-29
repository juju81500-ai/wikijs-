# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier que seuls les services et les ports prévus sont actifs.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les services en cours : **services.msc** ou commande.
   ```powershell
   Get-Service | Where-Object Status -eq Running | Sort-Object DisplayName | Select-Object Name,DisplayName
   ```
   👉 Explication : inventaire des services actifs.

2. Lister les ports en écoute et le processus associé : **Moniteur de ressources (resmon) > Réseau > Ports d'écoute**.
   ```powershell
   Get-NetTCPConnection -State Listen | Sort-Object LocalPort | Select-Object LocalAddress,LocalPort,@{n='Processus';e={(Get-Process -Id $_.OwningProcess).ProcessName}}
   Get-NetUDPEndpoint | Select-Object LocalAddress,LocalPort,OwningProcess
   ```
   👉 Explication : associe chaque port à son processus.

3. Comparer à la baseline.
   ```powershell
   Compare-Object (Import-Csv "$env:USERPROFILE\baseline_ports.csv") (Get-NetTCPConnection -State Listen | Select-Object LocalAddress,LocalPort,OwningProcess) -Property LocalPort
   ```
   👉 Explication : montre les ports qui ont apparu ou disparu depuis l'étape 25.

4. Rechercher les programmes lancés au démarrage : **Gestionnaire des tâches > Démarrage**.
   ```powershell
   Get-CimInstance Win32_StartupCommand | Select-Object Name,Command,Location
   ```
   👉 Explication : liste les démarrages automatiques à revoir.

## 2. Production — Contrôles

Tout écart avec la baseline est justifié ou corrigé.

## 3. Production — Sécurité

Fermer ou filtrer tout port d'écoute non documenté.

## Validation et retour arrière

- **Validation** : Les ports ouverts correspondent à la liste approuvée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
