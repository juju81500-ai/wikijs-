# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_08_Configuration_Reseau_D_Installation

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 08 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-08`

---

## Problème précis à résoudre

Disposer d'un réseau fonctionnel pendant et juste après l'installation.

## 1. Hors-Production (Lab / Test / POC)

1. Pendant l'installation : choisir **Je n'ai pas Internet** si le poste doit rester en compte local ou rejoindre le domaine; sinon se connecter au Wi-Fi ou au câble.
   👉 Explication : le choix conditionne la création d'un compte local ou d'un compte Microsoft/Entra ID.

2. Après installation, contrôler la connexion : **Paramètres > Réseau et Internet > Ethernet (ou Wi-Fi) > Propriétés**.
   ```powershell
   Get-NetIPConfiguration
   Get-NetAdapter | Select-Object Name,Status,LinkSpeed,MacAddress
   ```
   👉 Explication : affiche l'adresse IP, la passerelle, les DNS et l'état des cartes.

3. Vérifier la sortie réseau et la résolution.
   ```powershell
   Test-Connection 1.1.1.1 -Count 2
   Resolve-DnsName learn.microsoft.com
   Test-NetConnection learn.microsoft.com -Port 443
   ```
   👉 Explication : valide la route, le DNS et l'accès HTTPS.

4. Si un proxy d'entreprise est imposé : **Paramètres > Réseau et Internet > Proxy**.
   ```powershell
   netsh winhttp show proxy
   netsh winhttp set proxy proxy-server="PROXY:PORT"
   ```
   👉 Explication : affiche ou définit le proxy utilisé par les services système (`PROXY:PORT` fourni par la DSI).

## 2. Production — Contrôles

Utiliser le réseau d'installation ou VLAN de déploiement prévu; le poste ne doit pas rester sur un réseau invité.

## 3. Production — Sécurité

Éviter le Wi-Fi public pendant l'installation; ne jamais saisir de clé Wi-Fi dans la documentation.

## Validation et retour arrière

- **Validation** : `Test-NetConnection learn.microsoft.com -Port 443` retourne `TcpTestSucceeded : True`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
