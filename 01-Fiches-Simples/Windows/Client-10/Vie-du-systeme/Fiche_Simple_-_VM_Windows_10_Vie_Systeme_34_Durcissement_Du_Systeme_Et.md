# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_34_Durcissement_Du_Systeme_Et

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 34 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-34`

---

## Problème précis à résoudre

Appliquer les paramètres de sécurité recommandés : SMB, NTLM, protocoles hérités.

## 1. Hors-Production (Lab / Test / POC)

1. Désactiver SMB 1 et exiger la signature SMB : **Fonctionnalités Windows > Support de partage de fichiers SMB 1.0** décoché.
   ```powershell
   Get-SmbServerConfiguration | Select-Object EnableSMB1Protocol,RequireSecuritySignature
   Set-SmbServerConfiguration -EnableSMB1Protocol $false -RequireSecuritySignature $true -Force
   ```
   👉 Explication : supprime SMB 1 et force la signature.

2. Désactiver les protocoles de résolution locaux LLMNR et NetBIOS : GPO **Modèles d'administration > Réseau > Client DNS > Désactiver la résolution multidiffusion**.
   ```powershell
   New-Item 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' -Force | Out-Null
   Set-ItemProperty 'HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient' EnableMulticast 0 -Type DWord
   ```
   👉 Explication : coupe LLMNR, vecteur d'attaque courant d'interception d'identifiants.

3. Restreindre NTLM : GPO **Options de sécurité > Sécurité réseau : niveau d'authentification LAN Manager = Envoyer uniquement les réponses NTLMv2, refuser LM et NTLM**.
   ```powershell
   Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa LmCompatibilityLevel 5 -Type DWord
   ```
   👉 Explication : n'accepte que NTLMv2 (tester d'abord auprès des applications anciennes).

4. Activer la protection LSA et l'intégrité de la mémoire : **Sécurité Windows > Sécurité de l'appareil > Isolation du noyau**.
   ```powershell
   Set-ItemProperty HKLM:\SYSTEM\CurrentControlSet\Control\Lsa RunAsPPL 1 -Type DWord
   ```
   👉 Explication : protège le processus qui gère les identifiants (redémarrage requis).

## 2. Production — Contrôles

Appliquer un référentiel reconnu (ANSSI, Microsoft Security Baseline, CIS) par GPO ou Intune.

## 3. Production — Sécurité

Tester sur un poste pilote : certains durcissements cassent des applications anciennes.

## Validation et retour arrière

- **Validation** : Les valeurs de registre correspondent au référentiel retenu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
