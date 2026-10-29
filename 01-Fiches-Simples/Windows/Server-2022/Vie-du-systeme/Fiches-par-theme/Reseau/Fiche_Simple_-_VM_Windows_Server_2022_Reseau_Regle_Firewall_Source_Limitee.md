# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Reseau_Regle_Firewall_Source_Limitee.md

- **Environnement** : VM Windows Server
- **OS / Version** : Windows Server 2022
- **Catégorie** : Réseau / Sécurité
- **Tags** : `[windows-server-2022]`, `[firewall]`, `[reseau]`, `[powershell]`, `[gui]`, `[hardening]`

## 🎯 Problème précis à résoudre
Autoriser un port TCP entrant uniquement sur les profils réseau et depuis les adresses sources nécessaires, avec le pare-feu Microsoft Defender actif.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier les profils actifs et les règles correspondantes :
   ```powershell
   Get-NetConnectionProfile
   Get-NetFirewallProfile | Select-Object Name, Enabled, DefaultInboundAction
   ```
2. Créer une règle d'exemple limitée au réseau documentaire :
   ```powershell
   New-NetFirewallRule -DisplayName "Application TCP 8443 - Lab" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 8443 -RemoteAddress 192.0.2.0/24 -Profile Domain
   ```
   👉 *Explication : remplacer port, profil et source par les valeurs du lab; `192.0.2.0/24` est réservé à la documentation.*

## ⚡ 2. Production — Façon Simplifiée
1. Confirmer le port réellement écouté, le profil réseau de l'interface et la plage source autorisée.
2. En GUI, ouvrir `wf.msc`, choisir **Règles de trafic entrant > Nouvelle règle... > Port**, sélectionner TCP et le port, puis **Autoriser la connexion**.
3. Dans **Étendue**, limiter l'adresse IP distante; dans **Profil**, ne cocher que le profil approprié. Donner un nom explicite et terminer l'assistant.
4. Vérifier la règle et le service :
   ```powershell
   Get-NetFirewallRule -DisplayName "Application TCP 8443 - Lab" | Get-NetFirewallAddressFilter
   Get-NetFirewallProfile | Select-Object Name, Enabled
   ```
   👉 *Explication : la règle autorise le trafic correspondant; elle ne démarre pas le service et ne remplace pas un test depuis le réseau client.*

## 🔒 3. Production — Façon Sécurisée
1. Ne pas désactiver le pare-feu globalement pour résoudre un problème de connectivité.
2. Limiter l'adresse source, les protocoles, le port et les profils; éviter `Any` si une plage précise est connue.
3. Vérifier qu'aucune règle large existante n'autorise déjà le même flux, car une règle restrictive supplémentaire ne réduit pas une autorisation plus large.

## ✅ Validation et retour arrière
- Tester depuis une adresse autorisée puis non autorisée, et vérifier les journaux du service.
- Pour annuler, supprimer uniquement la règle créée :
  ```powershell
  Remove-NetFirewallRule -DisplayName "Application TCP 8443 - Lab"
  ```
- Conserver l'accès console d'administration avant de restreindre le profil Domain.