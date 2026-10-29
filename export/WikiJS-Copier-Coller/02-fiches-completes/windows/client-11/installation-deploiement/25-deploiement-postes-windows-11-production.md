# Déployer un poste Windows 11 en production

- **Type de fiche** : Installation / Déploiement
- **Environnement** : Parc de postes utilisateur, poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Rôle** : Installer, sécuriser, inscrire et remettre un poste à l'utilisateur

## 1. Choisir le mode de déploiement

Fiche simple : [choisir le mode de déploiement](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-choisir-mode).

Avant installation, déterminer si le poste sera géré par Autopilot/Intune, MECM, AD DS/GPO, une image d'entreprise ou un processus autonome. Cette fiche décrit les contrôles communs; les étapes d'enrôlement en masse dépendent de la solution de parc et doivent suivre son runbook.

Vérifier édition/licence, compatibilité matérielle, TPM 2.0, Secure Boot, stockage, pilote réseau, utilisateur assigné et compte de récupération.

## 2. Installer Windows 11

Fiche simple : [installer Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-installer-windows-11).

1. Utiliser un média Microsoft ou un média d'entreprise signé et approuvé.
2. Démarrer en UEFI, sélectionner l'édition conforme à la licence et vérifier le disque cible avant suppression/partitionnement.
3. Terminer l'OOBE selon le mode de gestion décidé; ne pas créer un compte personnel lorsque le poste doit être enrôlé par l'organisation.
4. Installer pilotes et mises à jour depuis les sources approuvées, redémarrer puis vérifier l'édition et le build.

## 3. Inscrire et configurer le poste

Fiche simple : [inscrire et configurer le poste](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-inscrire-configurer-poste).

- Définir un hostname conforme à la convention de parc.
- Inscrire le poste dans le mécanisme prévu (Entra ID/Intune, AD DS ou MECM) et vérifier qu'il apparaît dans la console d'administration.
- Appliquer les stratégies, certificats, VPN, Wi-Fi et applications attribuées; ces étapes diffèrent selon l'outil de gestion.
- Utiliser un compte utilisateur standard; l'administration locale doit être gérée par Windows LAPS ou un mécanisme approuvé.

## 4. Protéger les données et le système

Fiche simple : [protéger les données et le système](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-proteger-donnees-systeme).

1. Vérifier Microsoft Defender et le pare-feu sur les profils requis.
2. Activer BitLocker lorsque la stratégie le demande; confirmer que la clé de récupération a été déposée dans le coffre prévu avant de remettre le poste.
3. Limiter RDP, OpenSSH et les règles entrantes au besoin approuvé.
4. Confirmer mises à jour, Secure Boot, TPM, chiffrement et état d'enrôlement.

Exemple de contrôles non secrets en PowerShell :

```powershell
Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
Get-Tpm
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
Get-NetFirewallProfile | Select-Object Name, Enabled
Get-BitLockerVolume -MountPoint C: | Select-Object VolumeStatus, ProtectionStatus, EncryptionPercentage
```

## 5. Installer les applications et profils

Fiche simple : [installer les applications et profils](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-installer-applications-profils).

Déployer uniquement les applications autorisées via le catalogue ou l'outil de gestion du parc. Valider lancement, mises à jour, licences et accès aux services métiers; ne pas installer de logiciel tiers par script non approuvé.

## 6. Recette et remise

Fiche simple : [recette et remise](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-recette-remise).

- Tester ouverture de session, réseau, DNS, VPN, applications, imprimantes/périphériques et outils de support.
- Vérifier récupération des fichiers utilisateurs via OneDrive/File History ou la solution de sauvegarde retenue.
- Documenter hostname, utilisateur, build, état BitLocker et réception; ne jamais inscrire le mot de passe ou la clé de récupération dans le procès-verbal.

## 7. Retour arrière

Fiche simple : [retour arrière du déploiement](/01-fiches-simples/windows/client-11/vie-du-systeme/fiches-par-theme/deploiement-production/fiche-simple-hote-windows-11-deploiement-retour-arriere).

Si l'enrôlement, le chiffrement ou les applications échouent, maintenir l'appareil hors remise utilisateur. Reprendre le déploiement depuis l'image approuvée ou la séquence de l'outil de parc; confirmer l'absence de données à conserver avant réinitialisation.

## Sources

- [Microsoft Learn — Déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Microsoft Learn — Windows Autopilot](https://learn.microsoft.com/en-us/autopilot/)
- [Microsoft Learn — BitLocker](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/)