# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_05_Configuration_Materielle_Firmware

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 05 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Régler UEFI, Secure Boot et TPM avant l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. VM Hyper-V génération 2 : activer Secure Boot et le TPM virtuel (**Paramètres > Sécurité > Activer Secure Boot** et **Activer le module de plateforme sécurisée**) :
   ```powershell
   Set-VMFirmware -VMName NOM_VM -EnableSecureBoot On -SecureBootTemplate MicrosoftWindows
   Set-VMKeyProtector -VMName NOM_VM -NewLocalKeyProtector
   Enable-VMTPM -VMName NOM_VM
   ```
   👉 Explication : la VM démarre en UEFI avec Secure Boot et un TPM 2.0 virtuel utilisable par BitLocker.

2. Serveur physique : entrer dans le firmware (touche F2, Suppr ou F10 au démarrage) et activer **UEFI**, **Secure Boot**, **TPM 2.0** et la virtualisation (Intel VT-x / AMD-V). Après installation, contrôler :
   ```powershell
   Confirm-SecureBootUEFI
   Get-Tpm
   Get-CimInstance Win32_Processor | Select-Object Name, VirtualizationFirmwareEnabled
   ```
   👉 Explication : `True` pour Secure Boot, `TpmPresent` et `TpmReady` à `True`, et virtualisation activée.

3. Mettre à jour le firmware/BIOS et le BMC (iDRAC, iLO, IPMI) selon la procédure du constructeur et changer les mots de passe par défaut.
   👉 Explication : un firmware à jour corrige des failles et des incompatibilités avec Windows Server.

## 2. Production — Contrôles

Documenter la version du firmware et les réglages dans la CMDB.

## 3. Production — Sécurité

Protéger l'accès au firmware par mot de passe et désactiver l'amorçage sur périphériques non utilisés.

## Validation et retour arrière

- **Validation** : `Confirm-SecureBootUEFI` renvoie `True` et le TPM est prêt.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)