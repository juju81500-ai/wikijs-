# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_SMB1

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions
- **Tags** : `windows-server`, `windows-server-2016`, `windows-server-2019`, `windows-server-2022`, `smb1`, `smb`, `securite`

---

## Problème précis à résoudre

Détecter et désactiver SMB1 (protocole obsolète) sur 2016 et 2019 sans casser d'anciens clients.

## 1. Hors-Production (Lab / Test / POC)

1. Lire l'état du serveur SMB :
   ```powershell
   Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol,EnableSMB2Protocol,AuditSmb1Access
   Get-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
   ```
   👉 Explication : sur un serveur mis à niveau ou installé en 2016, SMB1 peut être actif ; vérifier l'état réel, ne pas le supposer.
2. Auditer d'abord les accès SMB1 :
   ```powershell
   Set-SmbServerConfiguration -AuditSmb1Access $true -Force
   ```
   👉 Explication : les accès sont journalisés dans le journal `Microsoft-Windows-SMBServer/Audit` ; identifier les clients qui utilisent encore SMB1.
3. Désactiver SMB1 une fois les clients traités :
   ```powershell
   Set-SmbServerConfiguration -EnableSMB1Protocol $false -Force
   Disable-WindowsOptionalFeature -Online -FeatureName SMB1Protocol
   ```
   👉 Explication : la seconde commande retire la fonctionnalité ; un redémarrage peut être demandé.
4. GUI équivalent : **Gestionnaire de serveur > Gérer > Supprimer des rôles et fonctionnalités > Fonctionnalités > Prise en charge du partage de fichiers SMB 1.0/CIFS**.
   👉 Explication : décocher la fonctionnalité, puis valider l'assistant.

## 2. Production — Contrôles

- Conserver un inventaire des appareils réellement dépendants de SMB1 (imprimantes, NAS anciens) et prévoir leur remplacement.
- Redémarrer en fenêtre de maintenance si demandé.

## 3. Production — Sécurité

- Ne pas réactiver SMB1 durablement ; une exception temporaire doit être datée, isolée et approuvée.

## Validation et retour arrière

- **Validation** : `EnableSMB1Protocol` vaut `False` et les partages restent accessibles en SMB2/3. **Retour arrière** : `Set-SmbServerConfiguration -EnableSMB1Protocol $true -Force` (exception temporaire et justifiée seulement).

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Windows-Server-2016-2019-2022.md)
- [Microsoft Learn — Détecter, activer et désactiver SMBv1](https://learn.microsoft.com/fr-fr/windows-server/storage/file-server/troubleshoot/detect-enable-and-disable-smbv1-v2-v3)
- [Microsoft Learn — Set-SmbServerConfiguration](https://learn.microsoft.com/fr-fr/powershell/module/smbshare/set-smbserverconfiguration)
