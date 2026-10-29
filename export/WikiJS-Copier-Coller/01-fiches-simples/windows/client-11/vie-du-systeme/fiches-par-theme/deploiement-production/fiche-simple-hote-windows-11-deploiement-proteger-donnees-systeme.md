# Fiche_Simple_-_Hote_Windows_11_Deploiement_Proteger_Donnees_Systeme.md

- **Environnement** : Parc de postes utilisateur: poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Catégorie** : déploiement de poste de travail

---

## Problème précis à résoudre

Vérifier Defender, pare-feu et BitLocker avant remise.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier Microsoft Defender :
   ```powershell
   Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
   ```
   👉 Explication : les deux valeurs doivent être vraies; GUI: **Sécurité Windows > Protection contre les virus et menaces**.

2. Vérifier le pare-feu :
   ```powershell
   Get-NetFirewallProfile | Select-Object Name, Enabled
   ```
   👉 Explication : les profils requis doivent être activés; GUI: **Sécurité Windows > Pare-feu**.

3. Contrôler le TPM :
   ```powershell
   Get-Tpm
   ```
   👉 Explication : TPM présent et prêt.

4. Activer BitLocker si la stratégie le demande : **Paramètres > Confidentialité et sécurité > Chiffrement de l'appareil**, ou **Panneau de configuration > BitLocker**.
   👉 Explication : confirmer que la clé de récupération a été déposée dans le coffre prévu avant remise.

5. Contrôler BitLocker :
   ```powershell
   Get-BitLockerVolume -MountPoint C: | Select-Object VolumeStatus, ProtectionStatus, EncryptionPercentage
   ```
   👉 Explication : la protection doit être activée et le chiffrement terminé.

6. Limiter RDP, OpenSSH et les règles entrantes au besoin approuvé.
   👉 Explication : réduit la surface d'attaque.

## 2. Production — Contrôles

Confirmer mises à jour, Secure Boot, TPM, chiffrement et état d'enrôlement avant remise.

## 3. Production — Sécurité

- Ne jamais inscrire la clé de récupération dans un document de remise.
- Déposer la clé dans le coffre approuvé.

## Validation et retour arrière

- **Validation** : Defender, pare-feu et BitLocker actifs, clé de récupération déposée.
- **Retour arrière** : suspendre BitLocker uniquement pour une opération approuvée (`Suspend-BitLocker -MountPoint C: -RebootCount 1`) puis le rétablir.

## Si le problème n'est pas résolu

- [Microsoft Learn — BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/)
- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Guide complet](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production#4-proteger-les-donnees-et-le-systeme)