# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_33_Securisation_Des_Systemes_De

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Appliquer des permissions NTFS et du chiffrement.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Explorateur > Clic droit sur le dossier > Propriétés > Sécurité > Avancé**.
   ```powershell
   Get-Acl D:\Donnees | Format-List
   icacls D:\Donnees
   ```
   👉 Explication : affiche les permissions; vérifier l'absence de `Tout le monde` en écriture.

2. Retirer l'héritage et ne laisser que les groupes nécessaires (remplacer `GROUPE_METIER`) :
   ```powershell
   icacls D:\Donnees /inheritance:r /grant 'Administrateurs:(OI)(CI)F' 'SYSTEM:(OI)(CI)F' 'GROUPE_METIER:(OI)(CI)M'
   ```
   👉 Explication : droits explicites pour les administrateurs, le système et le groupe métier.

3. Chiffrer un volume de données avec BitLocker (**Gestionnaire de serveur > Ajouter des fonctionnalités > Chiffrement de lecteur BitLocker**) :
   ```powershell
   Install-WindowsFeature BitLocker -IncludeManagementTools -Restart
   Enable-BitLocker -MountPoint D: -RecoveryPasswordProtector -UsedSpaceOnly
   ```
   👉 Explication : protège les données au repos; sauvegarder la clé de récupération dans AD ou le coffre, jamais sur le même volume.

## 2. Production — Contrôles

Journaliser les accès sensibles par audit des objets.

## 3. Production — Sécurité

Conserver les clés de récupération BitLocker hors du serveur.

## Validation et retour arrière

- **Validation** : `icacls` montre les droits attendus et `Get-BitLockerVolume` indique `FullyEncrypted`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
