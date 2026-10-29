# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Enregistrer le poste dans le CMDB et valider qui peut l'administrer.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter les informations d'identification du poste.
   ```powershell
   Get-CimInstance Win32_ComputerSystem | Select-Object Name,Domain,Manufacturer,Model
   Get-CimInstance Win32_BIOS | Select-Object SerialNumber
   Get-CimInstance Win32_OperatingSystem | Select-Object Caption,Version,InstallDate
   ```
   👉 Explication : nom, série, modèle, système et date d'installation pour la fiche CMDB.

2. Créer la fiche dans le CMDB (GLPI : **Parc > Ordinateurs > Ajouter**) avec le propriétaire, le site, le service, la criticité et la date de fin de support.
   👉 Explication : le CMDB est la référence du parc.

3. Revoir qui a accès : groupe d'administrateurs et accès distants.
   ```powershell
   Get-LocalGroupMember -Group 'Administrateurs'
   Get-LocalGroupMember -Group 'Utilisateurs du Bureau à distance'
   ```
   👉 Explication : valide que seuls les comptes prévus ont des droits.

4. Lier la fiche à l'inventaire automatique, aux clés BitLocker et à la gestion LAPS.
   ```powershell
   Get-BitLockerVolume C: | Select-Object -ExpandProperty KeyProtector | Select-Object KeyProtectorType,KeyProtectorId
   ```
   👉 Explication : ne note que l'identifiant du protecteur, jamais la clé elle-même.

## 2. Production — Contrôles

Fiche CMDB créée avant la remise de l'appareil; revue des accès chaque trimestre.

## 3. Production — Sécurité

Aucun mot de passe ni clé de récupération dans le CMDB; renvoyer vers le coffre.

## Validation et retour arrière

- **Validation** : Fiche CMDB complète et accès validés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
