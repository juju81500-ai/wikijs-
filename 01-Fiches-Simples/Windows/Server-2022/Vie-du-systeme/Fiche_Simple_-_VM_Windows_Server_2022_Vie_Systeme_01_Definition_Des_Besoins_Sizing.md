# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner le serveur Windows Server 2022 avant de le créer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources d'un serveur comparable (**Gestionnaire des tâches > Performance** ou **Moniteur de ressources**) :
   ```powershell
   Get-CimInstance Win32_ComputerSystem | Select-Object NumberOfLogicalProcessors, @{n='RAM_Go';e={[math]::Round($_.TotalPhysicalMemory/1GB,1)}}
   Get-Disk | Select-Object Number, FriendlyName, @{n='Taille_Go';e={[math]::Round($_.Size/1GB)}}
   (Get-CimInstance Win32_OperatingSystem).OSArchitecture
   ```
   👉 Explication : nombre de vCPU, RAM, disques et architecture (64 bits) pour comparer au besoin.

2. Mesurer la charge disque et mémoire sur quelques minutes :
   ```powershell
   Get-Counter '\PhysicalDisk(_Total)\Avg. Disk sec/Transfer','\Memory\Available MBytes' -SampleInterval 5 -MaxSamples 12
   ```
   👉 Explication : une latence disque durablement supérieure à 20 ms ou peu de mémoire disponible indique un sous-dimensionnement.

3. Noter vCPU, RAM, disque système, disques de données, IOPS et réseau dans le dossier du projet.
   👉 Explication : ce tableau sert de référence pour l'hyperviseur et pour la recette; Windows Server 2022 exige un processeur 64 bits et une RAM minimale (consulter la page officielle des exigences système).

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge, valider le dimensionnement avec le propriétaire du service et prévoir la place des mises à jour (disque système de 80 Go ou plus conseillé).

## 3. Production — Sécurité

Prévoir un disque de données séparé du disque système pour les rôles qui écrivent beaucoup (bases, partages, journaux).

## Validation et retour arrière

- **Validation** : Tableau de sizing signé et conservé avec le dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
