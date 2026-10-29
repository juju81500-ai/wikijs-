# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-16`

---

## Problème précis à résoudre

Attribuer l'adresse IP définitive.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Panneau de configuration > Réseau et Internet > Centre Réseau et partage > Modifier les paramètres de la carte > Propriétés > Protocole Internet version 4 (TCP/IPv4)**.
   ```powershell
   Get-NetIPConfiguration
   ```
   👉 Explication : montre la configuration en cours.

2. Appliquer l'adresse fixe (remplacer `ALIAS`, `IP`, `PASSERELLE`, `IP_DNS`) :
   ```powershell
   Remove-NetIPAddress -InterfaceAlias 'ALIAS' -AddressFamily IPv4 -Confirm:$false
   New-NetIPAddress -InterfaceAlias 'ALIAS' -IPAddress IP -PrefixLength 24 -DefaultGateway PASSERELLE
   Set-DnsClientServerAddress -InterfaceAlias 'ALIAS' -ServerAddresses IP_DNS
   ```
   👉 Explication : `IP_DNS` est l'adresse du serveur DNS interne; à lancer depuis la console de la VM car la connexion distante sera coupée.

3. Contrôler :
   ```powershell
   Get-NetIPAddress -InterfaceAlias 'ALIAS' -AddressFamily IPv4
   Test-NetConnection PASSERELLE
   ```
   👉 Explication : l'adresse attendue est portée et la passerelle répond.

## 2. Production — Contrôles

Déclarer l'adresse dans l'IPAM et le DNS (enregistrement A et PTR).

## 3. Production — Sécurité

Désactiver IPv6 uniquement si la politique l'impose; sinon le configurer proprement.

## Validation et retour arrière

- **Validation** : Adresse, passerelle et DNS corrects, et accès depuis le poste d'administration.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
