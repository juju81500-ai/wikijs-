# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_46_Test_De_Persistance_Au

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 46 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Vérifier que la configuration survit à un redémarrage.

## 1. Hors-Production (Lab / Test / POC)

1. Redémarrer proprement : **Démarrer > Alimentation > Redémarrer**.
   ```powershell
   Restart-Computer -Force
   ```
   👉 Explication : redémarre le poste après avoir fermé les sessions.

2. Après redémarrage, contrôler le temps de fonctionnement et les services automatiques arrêtés.
   ```powershell
   (Get-Date) - (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
   Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -ne 'Running'} | Select-Object Name,Status
   ```
   👉 Explication : les services en démarrage automatique doivent tourner (hors services déclenchés).

3. Vérifier réseau, nom, domaine, pare-feu et chiffrement.
   ```powershell
   Get-NetIPConfiguration | Select-Object InterfaceAlias,IPv4Address
   Get-NetFirewallProfile | Select-Object Name,Enabled
   Get-BitLockerVolume | Select-Object MountPoint,ProtectionStatus
   ```
   👉 Explication : tout doit être conforme à la baseline.

4. Ouvrir une session avec le compte utilisateur de test.
   ```powershell
   whoami
   gpresult /r | Select-String 'Domaine|Domain Name'
   ```
   👉 Explication : confirme l'identité, les GPO et le domaine.

## 2. Production — Contrôles

Test réalisé avant la remise à l'utilisateur et après chaque changement important.

## 3. Production — Sécurité

Planifier les redémarrages hors des heures de service et prévenir l'utilisateur.

## Validation et retour arrière

- **Validation** : Tout est conforme après redémarrage sans intervention manuelle.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)