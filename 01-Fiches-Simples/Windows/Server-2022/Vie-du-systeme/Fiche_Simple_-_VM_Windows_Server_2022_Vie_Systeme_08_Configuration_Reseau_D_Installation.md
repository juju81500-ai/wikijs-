# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Donner un accès réseau provisoire pour l'installation et les mises à jour.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier la carte : **Panneau de configuration > Centre Réseau et partage > Modifier les paramètres de la carte**.
   ```powershell
   Get-NetAdapter | Select-Object Name, Status, LinkSpeed, MacAddress
   Get-NetIPConfiguration
   ```
   👉 Explication : liste les cartes, leur état et leur adresse (DHCP par défaut).

2. Vérifier l'accès à la passerelle, au DNS et à Internet :
   ```powershell
   Test-NetConnection 8.8.8.8
   Test-NetConnection www.microsoft.com -Port 443
   Resolve-DnsName www.microsoft.com
   ```
   👉 Explication : confirme la connectivité IP, la résolution et l'accès HTTPS nécessaire à Windows Update.

3. Si le DHCP est absent, fixer provisoirement l'adresse (remplacer `ALIAS`, `IP`, `PASSERELLE`) :
   ```powershell
   New-NetIPAddress -InterfaceAlias 'ALIAS' -IPAddress IP -PrefixLength 24 -DefaultGateway PASSERELLE
   ```
   👉 Explication : `ALIAS` est le nom de la carte (ex. Ethernet), `IP` l'adresse libre réservée et `PASSERELLE` le routeur.

## 2. Production — Contrôles

Réserver l'adresse définitive dans l'IPAM avant la mise en production.

## 3. Production — Sécurité

Installer sur un VLAN de préparation isolé et limiter les flux sortants aux sites de mise à jour.

## Validation et retour arrière

- **Validation** : Résolution DNS et accès HTTPS réussis.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows Server 2022 IP Statique PowerShell](<../Vie-du-logiciel/PowerShell/Fiche_Simple_-_VM_Windows_Server_2022_IP_Statique_PowerShell.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
