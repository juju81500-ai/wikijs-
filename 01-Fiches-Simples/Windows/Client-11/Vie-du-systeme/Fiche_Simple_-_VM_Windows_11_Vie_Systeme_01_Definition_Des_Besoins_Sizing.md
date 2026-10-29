# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_01_Definition_Des_Besoins_Sizing

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 01 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-01`

---

## Problème précis à résoudre

Dimensionner le poste Windows 11 avant de l'acheter, de le créer ou de le déployer.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les ressources de la machine ou du modèle comparable : **Paramètres > Système > À propos de** (processeur, RAM installée, type de système) et **Paramètres > Système > Stockage** (espace disque).
   ```powershell
   Get-CimInstance Win32_Processor | Select-Object Name,NumberOfCores,NumberOfLogicalProcessors
   Get-CimInstance Win32_ComputerSystem | Select-Object @{n='RAM_Go';e={[math]::Round($_.TotalPhysicalMemory/1GB,1)}}
   Get-PhysicalDisk | Select-Object FriendlyName,MediaType,@{n='Taille_Go';e={[math]::Round($_.Size/1GB)}}
   (Get-CimInstance Win32_OperatingSystem).OSArchitecture
   ```
   👉 Explication : affiche cœurs, RAM, type de disque (SSD/HDD) et architecture 64 bits pour comparer au besoin des applications métier.

2. Mesurer la charge d'un poste comparable : **Gestionnaire des tâches (Ctrl+Maj+Échap) > Performances**, ou la commande ci-contre.
   ```powershell
   Get-Counter '\Processor(_Total)\% Processor Time','\Memory\Available MBytes','\PhysicalDisk(_Total)\Avg. Disk Queue Length' -SampleInterval 2 -MaxSamples 5
   ```
   👉 Explication : un processeur proche de 100 %, peu de mémoire disponible ou une file disque élevée indiquent un poste sous-dimensionné.

3. Vérifier les prérequis matériels de Windows 11 (TPM 2.0, démarrage sécurisé, 4 Go de RAM, 64 Go de stockage) : lancer l'application **Contrôle d'intégrité du PC** ou lire l'état du TPM.
   ```powershell
   Get-Tpm | Select-Object TpmPresent,TpmReady,ManufacturerVersion
   Confirm-SecureBootUEFI
   ```
   👉 Explication : `TpmPresent : True` avec une version 2.0 et `True` pour Secure Boot sont attendus; `Confirm-SecureBootUEFI` échoue sur un BIOS hérité (Legacy).

4. Noter processeur, RAM, disque, GPU éventuel, écrans, périphériques et applications métier dans le dossier du projet.
   👉 Explication : ce tableau sert de référence pour la commande de matériel et pour la recette.

## 2. Production — Contrôles

Ajouter 20 à 30 % de marge, valider avec le métier et avec la DSI; viser au moins 8 Go de RAM et un SSD pour un usage bureautique en entreprise.

## 3. Production — Sécurité

Prévoir un TPM 2.0 et le démarrage sécurisé dès l'achat (BitLocker et Windows 11 en dépendent). Sur Windows 10, qui est en fin de support, prévoir la migration vers Windows 11 plutôt que de dimensionner un nouveau poste.

## Validation et retour arrière

- **Validation** : Tableau de sizing signé et conservé avec le dossier.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
