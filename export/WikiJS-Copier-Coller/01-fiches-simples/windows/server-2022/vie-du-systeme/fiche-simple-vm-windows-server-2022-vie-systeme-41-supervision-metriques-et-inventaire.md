# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_41_Supervision_Metriques_Et_Inventaire

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 41 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Surveiller la disponibilité et la capacité.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Analyseur de performances** (`perfmon`) ou la sonde de supervision (PRTG, Zabbix).
   ```powershell
   Get-Counter '\Processor(_Total)\% Processor Time','\Memory\% Committed Bytes In Use' -SampleInterval 2 -MaxSamples 5
   ```
   👉 Explication : relève la charge CPU et mémoire.

2. Vérifier le stockage et les services critiques :
   ```powershell
   Get-Volume | Select-Object DriveLetter, @{n='Libre_%';e={[math]::Round($_.SizeRemaining/$_.Size*100)}}
   Get-Service W32Time, EventLog, WinRM
   ```
   👉 Explication : alertes à 15 % d'espace libre.

3. Inscrire le serveur dans la supervision avec les seuils CPU, RAM, disque et services.
   👉 Explication : les alertes doivent atteindre l'équipe d'astreinte.

## 2. Production — Contrôles

Superviser aussi les certificats, les sauvegardes et les correctifs.

## 3. Production — Sécurité

Utiliser un compte de supervision en lecture seule.

## Validation et retour arrière

- **Validation** : Le serveur apparaît dans la supervision avec des métriques.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows Server 2022 PRTG Installer](</01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-installer>)
- [Fiche détaillée : VM Windows Server 2022 PRTG Ajouter Appareil Pilote](</01-fiches-simples/windows/server-2022/vie-du-logiciel/prtg/fiche-simple-vm-windows-server-2022-prtg-ajouter-appareil-pilote>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)