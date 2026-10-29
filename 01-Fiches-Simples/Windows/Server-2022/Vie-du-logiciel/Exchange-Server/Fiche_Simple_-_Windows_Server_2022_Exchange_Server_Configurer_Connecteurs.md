# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Configurer_Connecteurs

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / flux SMTP
- **Tags** : `windows-server-2022`, `exchange-server`, `messagerie`, `connecteurs`, `smtp`, `transport`

---

## Problème précis à résoudre

Configurer le flux de messagerie : domaine accepté, connecteur d'envoi vers Internet ou un relais, et connecteur de réception pour des applications.

## 1. Hors-Production (Lab / Test / POC)

1. Déclarer le domaine accepté : EAC > Flux de messagerie > Domaines acceptés > + ; ou :
   ```powershell
   New-AcceptedDomain -Name "example.net" -DomainName example.net -DomainType Authoritative
   ```
   👉 Explication : remplacer `example.net` par le domaine de messagerie.

2. Créer le connecteur d'envoi : EAC > Flux de messagerie > Connecteurs d'envoi > + ; ou :
   ```powershell
   New-SendConnector -Name "Vers-Internet" -Usage Internet -AddressSpaces "SMTP:*;1" -SourceTransportServers EXCH01 -DNSRoutingEnabled $true
   ```
   👉 Explication : remplacer `EXCH01`. Pour un relais, remplacer le routage DNS par `-DNSRoutingEnabled $false -SmartHosts RELAIS.EXAMPLE.NET`.

3. Créer un connecteur de réception dédié aux applications (relais restreint par IP) : EAC > Flux de messagerie > Connecteurs de réception > + ; ou :
   ```powershell
   New-ReceiveConnector -Name "Relais-Applications" -TransportRole FrontendTransport -Custom -Bindings 0.0.0.0:25 -RemoteIPRanges IP_APPLICATION
   ```
   👉 Explication : remplacer `IP_APPLICATION` par l'adresse ou plage autorisée ; le port 25 est partagé avec le connecteur par défaut, d'où la restriction par IP.

4. Autoriser le relais pour ce seul connecteur :
   ```powershell
   Set-ReceiveConnector "EXCH01\Relais-Applications" -PermissionGroups AnonymousUsers
   Get-ReceiveConnector "EXCH01\Relais-Applications" | Add-ADPermission -User "NT AUTHORITY\ANONYMOUS LOGON" -ExtendedRights "Ms-Exch-SMTP-Accept-Any-Recipient"
   ```
   👉 Explication : ouvre le relais uniquement pour les IP listées ; ne jamais l'ouvrir à 0.0.0.0/0.

5. Tester l'envoi depuis un hôte autorisé :
   ```powershell
   Send-MailMessage -SmtpServer EXCH01.CONTOSO.LOCAL -From APP@example.net -To DESTINATAIRE@example.net -Subject "Test relais" -Body "Test"
   ```
   👉 Explication : remplacer expéditeur et destinataire ; cmdlet signalée obsolète mais utilisable pour un test.

## 2. Production — Contrôles

Vérifier MX, SPF, DKIM/DMARC côté DNS, le reverse DNS de l'IP d'envoi, l'ouverture du port 25 sortant au pare-feu et la liste des IP du connecteur de relais.

## 3. Production — Sécurité

- Aucun relais ouvert : restreindre par IP et journaliser.
- Activer TLS sur les connecteurs (certificat valide, voir fiche Certificats).
- Ne pas modifier les connecteurs par défaut sans nécessité.

## Validation et retour arrière

- **Validation** : `Get-Queue` vide, `Get-MessageTrackingLog -Recipients DESTINATAIRE@example.net` montre la remise, message de test reçu.
- **Retour arrière** : supprimer le connecteur créé (`Remove-SendConnector` / `Remove-ReceiveConnector`) après export de sa configuration (`Get-ReceiveConnector | Format-List`).

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
