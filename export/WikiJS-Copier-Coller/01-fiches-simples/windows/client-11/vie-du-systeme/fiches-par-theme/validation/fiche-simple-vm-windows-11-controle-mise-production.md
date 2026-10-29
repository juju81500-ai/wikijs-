# 📄 Fiche_Simple_-_VM_Windows_11_Controle_Mise_Production.md

- **Environnement** : Poste utilisateur Windows 11 géré ou autonome
- **OS / Version** : Windows 11 Pro / Enterprise selon les services requis
- **Catégorie** : Production / Validation / Poste de travail

## 🎯 Problème précis à résoudre
Vérifier un poste Windows 11 avant remise à l'utilisateur : mises à jour, identité, accès, chiffrement, pare-feu, protection et capacité de récupération.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Relever édition, build et redémarrage en attente : GUI **Paramètres > Système > À propos**, ou :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-WindowsUpdateLog
   ```
   👉 Explication : `Get-WindowsUpdateLog` produit le journal de mises à jour sur le Bureau; GUI **Paramètres > Windows Update**.

2. Vérifier protections et BitLocker : GUI **Sécurité Windows**, **Chiffrement de l'appareil**, ou :
   ```powershell
   Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled
   Get-NetFirewallProfile | Select-Object Name, Enabled
   Get-BitLockerVolume -MountPoint C: | Select-Object VolumeStatus, ProtectionStatus, EncryptionPercentage
   ```
   👉 Explication : tout doit être activé; clé de récupération déposée dans le coffre approuvé.

3. Tester ouverture de session, réseau d'entreprise et outils de support autorisés :
   ```powershell
   Test-NetConnection NOM_SERVEUR -Port 443
   ```
   👉 Explication : remplacer le serveur; tester aussi VPN et impression avec le profil de l'utilisateur.

## ⚡ 2. Production — Façon Simplifiée
1. **Identité :** nom de poste, utilisateur, domaine/gestion centrale et groupe de support documentés.
2. **Protection :** correctifs appliqués, Defender actif, pare-feu actif, BitLocker protégé et clé de récupération déposée dans le coffre approuvé.
3. **Accès :** compte utilisateur standard, administrateur local géré, RDP/OpenSSH désactivés sauf besoin autorisé.
4. **Récupération :** fichiers utilisateur couverts par la stratégie de sauvegarde/synchronisation; méthode de réinstallation ou de restauration connue.
5. **Acceptation :** périphériques, réseau, applications, VPN et impression testés avec le profil de l'utilisateur.

## 🔒 3. Production — Façon Sécurisée
- Ne pas remettre le poste si la clé de récupération BitLocker est absente, si Defender/pare-feu est désactivé ou si un compte de test reste actif.
- Vérifier que les administrateurs locaux et logiciels installés correspondent à la politique du parc.
- Éviter de collecter ou d'inscrire des mots de passe dans le procès-verbal de remise.

## ✅ Validation et retour arrière
- Documenter build, nom, état BitLocker, source de récupération et résultats des tests sans exporter le secret de récupération.
- Tester une récupération de fichiers ou la procédure de réinstallation sur un poste de test.
- En cas d'échec, ne pas remettre l'appareil; réappliquer l'image de référence ou corriger la configuration puis reprendre la checklist.