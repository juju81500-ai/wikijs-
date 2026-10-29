# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver que la sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les sauvegardes disponibles (**Sauvegarde Windows Server > Récupérer**) :
   ```powershell
   wbadmin get versions
   ```
   👉 Explication : affiche les identifiants de version.

2. Restaurer un dossier dans un emplacement de test (remplacer `VERSION` par l'identifiant) :
   ```powershell
   wbadmin start recovery -version:VERSION -itemType:File -items:D:\Donnees -recoveryTarget:D:\Restauration -recursive
   ```
   👉 Explication : restaure sans écraser l'original.

3. Comparer le contenu restauré :
   ```powershell
   Compare-Object (Get-ChildItem D:\Donnees -Recurse) (Get-ChildItem D:\Restauration\Donnees -Recurse) -Property Name, Length
   ```
   👉 Explication : aucune différence attendue.

## 2. Production — Contrôles

Tester une restauration complète périodiquement et chronométrer (RTO) pour la comparer à l'objectif.

## 3. Production — Sécurité

Restaurer dans un réseau isolé pour ne pas dupliquer le service.

## Validation et retour arrière

- **Validation** : Données restaurées identiques et durée conforme au RTO.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows Server 2022 Veeam Recette Obligatoire](<../Vie-du-logiciel/Veeam/Fiche_Simple_-_VM_Windows_Server_2022_Veeam_Recette_Obligatoire.md>)
- [Fiche détaillée : VM Windows Server 2022 Robocopy Valider Restaurer](<../Vie-du-logiciel/Robocopy/Fiche_Simple_-_VM_Windows_Server_2022_Robocopy_Valider_Restaurer.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
