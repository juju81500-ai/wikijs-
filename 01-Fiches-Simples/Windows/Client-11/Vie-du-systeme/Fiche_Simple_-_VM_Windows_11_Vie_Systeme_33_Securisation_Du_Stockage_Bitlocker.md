# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_33_Securisation_Du_Stockage_Bitlocker

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 33 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-33`

---

## Problème précis à résoudre

Chiffrer les volumes et restreindre les droits NTFS.

## 1. Hors-Production (Lab / Test / POC)

1. Activer BitLocker : **Paramètres > Confidentialité et sécurité > Chiffrement de l'appareil**, ou **Panneau de configuration > Chiffrement de lecteur BitLocker > Activer**.
   ```powershell
   Get-BitLockerVolume
   Enable-BitLocker -MountPoint 'C:' -EncryptionMethod XtsAes256 -TpmProtector
   ```
   👉 Explication : chiffre C: avec protecteur TPM (réaliser l'étape suivante avant tout redémarrage).

2. Créer et sauvegarder la clé de récupération dans l'annuaire (jamais sur le poste).
   ```powershell
   Add-BitLockerKeyProtector -MountPoint 'C:' -RecoveryPasswordProtector
   BackupToAAD-BitLockerKeyProtector -MountPoint 'C:' -KeyProtectorId 'ID_PROTECTEUR'
   ```
   👉 Explication : ajoute la clé de récupération et la copie dans Entra ID (en AD : `Backup-BitLockerKeyProtector`); `ID_PROTECTEUR` provient de `(Get-BitLockerVolume C:).KeyProtector`.

3. Contrôler les droits NTFS d'un dossier sensible : **clic droit > Propriétés > Sécurité**.
   ```powershell
   Get-Acl 'C:\DONNEES' | Format-List
   icacls 'C:\DONNEES'
   ```
   👉 Explication : affiche les permissions pour supprimer les accès trop larges (`Tout le monde`, `Utilisateurs` en modification).

4. Interdire l'écriture sur supports USB non autorisés par GPO : **Modèles d'administration > Système > Accès au stockage amovible**.
   👉 Explication : limite les fuites de données.

## 2. Production — Contrôles

Chiffrement obligatoire de tous les volumes fixes, avec clé de récupération stockée dans l'annuaire.

## 3. Production — Sécurité

Ne jamais écrire la clé de récupération dans une fiche ou un ticket; accès restreint au support N2.

## Validation et retour arrière

- **Validation** : `Get-BitLockerVolume` retourne `ProtectionStatus : On`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
