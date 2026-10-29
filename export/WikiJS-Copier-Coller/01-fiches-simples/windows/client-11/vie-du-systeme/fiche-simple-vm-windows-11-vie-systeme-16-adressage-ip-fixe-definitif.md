# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_16_Adressage_Ip_Fixe_Definitif

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 16 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer l'adressage réseau définitif : DHCP réservé ou IP statique.

## 1. Hors-Production (Lab / Test / POC)

1. Interface graphique : **Paramètres > Réseau et Internet > Ethernet > Modification de l'attribution IP > Manuel > IPv4**; saisir adresse, longueur du préfixe, passerelle et DNS.
   ```powershell
   Get-NetAdapter | Select-Object Name,Status
   ```
   👉 Explication : repère le nom de l'interface (`NOM_INTERFACE`, par exemple `Ethernet`).

2. Commande PowerShell équivalente (remplacer `ADRESSE_IP`, `PASSERELLE`, `DNS_1`, `DNS_2` par les valeurs du plan d'adressage).
   ```powershell
   New-NetIPAddress -InterfaceAlias 'NOM_INTERFACE' -IPAddress ADRESSE_IP -PrefixLength 24 -DefaultGateway PASSERELLE
   Set-DnsClientServerAddress -InterfaceAlias 'NOM_INTERFACE' -ServerAddresses DNS_1,DNS_2
   ```
   👉 Explication : fixe l'IP et les DNS.

3. Préférer le DHCP avec réservation pour un poste standard : **Ethernet > Attribution IP > Automatique (DHCP)**.
   ```powershell
   Set-NetIPInterface -InterfaceAlias 'NOM_INTERFACE' -Dhcp Enabled
   Set-DnsClientServerAddress -InterfaceAlias 'NOM_INTERFACE' -ResetServerAddresses
   ```
   👉 Explication : revient au DHCP pour l'adresse et les DNS.

4. Valider.
   ```powershell
   Get-NetIPConfiguration -InterfaceAlias 'NOM_INTERFACE'
   Test-Connection PASSERELLE -Count 2
   ```
   👉 Explication : contrôle la configuration et la joignabilité de la passerelle.

## 2. Production — Contrôles

Un poste utilisateur reste en DHCP; l'IP fixe est réservée aux postes spéciaux, enregistrée dans l'IPAM.

## 3. Production — Sécurité

Éviter les doublons d'adresse; documenter le VLAN et les règles de filtrage associées.

## Validation et retour arrière

- **Validation** : `Get-NetIPConfiguration` correspond au plan d'adressage.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows 11 Reseau IP Statique PowerShell](</01-fiches-simples/windows/client-11/vie-du-logiciel/powershell/fiche-simple-vm-windows-11-reseau-ip-statique-powershell>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)