# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_34_Durcissement_Systeme_Et_Reseau

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer les protections du système (SMB, TLS, NTLM, LLMNR).

## 1. Hors-Production (Lab / Test / POC)

1. Exiger la signature SMB et désactiver le chiffrement faible (**gpedit.msc > Options de sécurité > Client/Serveur réseau Microsoft : communications signées numériquement**) :
   ```powershell
   Set-SmbServerConfiguration -RequireSecuritySignature $true -EncryptData $true -Force
   Get-SmbServerConfiguration | Select-Object RequireSecuritySignature, EncryptData, EnableSMB1Protocol
   ```
   👉 Explication : protège contre l'interception; tester la compatibilité des clients anciens.

2. Désactiver LLMNR (**Modèles d'administration > Réseau > Client DNS > Désactiver la résolution de noms multidiffusion**) :
   ```powershell
   New-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' -Force | Out-Null
   Set-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' EnableMulticast 0
   ```
   👉 Explication : réduit les risques d'usurpation de noms.

3. Contrôler le niveau d'authentification NTLM :
   ```powershell
   Get-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\Lsa' -Name LmCompatibilityLevel -ErrorAction SilentlyContinue
   ```
   👉 Explication : la valeur 5 impose NTLMv2 uniquement. Sous Windows Server 2025 : des options de blocage de NTLM sont proposées, à valider avec la documentation officielle.

## 2. Production — Contrôles

Appliquer ces paramètres par GPO et par baseline de sécurité.

## 3. Production — Sécurité

Tester sur un serveur pilote : les protocoles anciens peuvent casser des applications.

## Validation et retour arrière

- **Validation** : Les contrôles de configuration affichent les valeurs attendues.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
