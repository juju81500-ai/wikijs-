# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_15_Chargeur_D_Amorcage

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 15 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-15`

---

## Problème précis à résoudre

Vérifier l'amorçage UEFI et la partition de démarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le mode de démarrage (**msinfo32 > Mode BIOS : UEFI**) :
   ```powershell
   bcdedit /enum '{current}'
   Get-Partition | Where-Object Type -eq 'System' | Select-Object DiskNumber, PartitionNumber, Size
   ```
   👉 Explication : montre l'entrée d'amorçage active et la partition système EFI.

2. Lister les entrées de démarrage :
   ```powershell
   bcdedit /enum all
   ```
   👉 Explication : affiche le gestionnaire d'amorçage Windows et ses chemins.

3. Réduire le délai d'attente du menu si un seul système est installé (**msconfig > Démarrer > Délai d'attente**) :
   ```powershell
   bcdedit /timeout 5
   ```
   👉 Explication : le menu n'attend que 5 secondes.

## 2. Production — Contrôles

Sauvegarder la configuration avant toute modification : `bcdedit /export C:\Sauvegardes\bcd.bak`.

## 3. Production — Sécurité

Secure Boot actif et accès console protégé empêchent le démarrage d'un système altéré.

## Validation et retour arrière

- **Validation** : Le serveur redémarre sans intervention jusqu'à l'ouverture de session.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
