# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer et tester le client DNS et les suffixes de recherche.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les serveurs DNS : **Paramètres > Réseau et Internet > Ethernet > Propriétés > Serveurs DNS**.
   ```powershell
   Get-DnsClientServerAddress -AddressFamily IPv4
   Get-DnsClient | Select-Object InterfaceAlias,ConnectionSpecificSuffix,RegisterThisConnectionsAddress
   ```
   👉 Explication : affiche serveurs DNS et suffixes par interface.

2. Définir les serveurs DNS de l'entreprise (`DNS_1`, `DNS_2`) et le suffixe de domaine (`DOMAINE.LOCAL`).
   ```powershell
   Set-DnsClientServerAddress -InterfaceAlias 'NOM_INTERFACE' -ServerAddresses DNS_1,DNS_2
   Set-DnsClientGlobalSetting -SuffixSearchList @('DOMAINE.LOCAL')
   ```
   👉 Explication : applique les DNS et la liste de suffixes de recherche.

3. Tester la résolution d'un nom interne et externe.
   ```powershell
   Resolve-DnsName NOM_SERVEUR.DOMAINE.LOCAL
   Resolve-DnsName learn.microsoft.com
   nslookup NOM_SERVEUR
   ```
   👉 Explication : valide les enregistrements A et le chemin de résolution.

4. Vider le cache en cas de réponse périmée.
   ```powershell
   Clear-DnsClientCache
   Get-DnsClientCache | Select-Object -First 5
   ```
   👉 Explication : force une nouvelle résolution.

## 2. Production — Contrôles

DNS internes en premier pour l'annuaire; DNS externes via le résolveur de l'entreprise.

## 3. Production — Sécurité

Ne pas utiliser de DNS publics sur un poste joint au domaine : la jonction et les GPO en dépendent.

## Validation et retour arrière

- **Validation** : `Resolve-DnsName` réussit pour un nom interne.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
