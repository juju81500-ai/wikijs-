# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Securiser_Certificats

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / sécurité TLS

---

## Problème précis à résoudre

Remplacer le certificat auto-signé par un certificat d'une autorité de confiance pour IIS et SMTP.

## 1. Hors-Production (Lab / Test / POC)

1. Générer la demande de certificat : EAC > Serveurs > Certificats > + ; ou :
   ```powershell
   $req = New-ExchangeCertificate -GenerateRequest -SubjectName "CN=mail.example.net" -DomainName mail.example.net, autodiscover.example.net, EXCH01.CONTOSO.LOCAL -PrivateKeyExportable $false -Server EXCH01
   Set-Content -Path C:\Temp\exchange.req -Value $req
   ```
   👉 Explication : remplacer les noms par ceux réellement utilisés par les clients ; transmettre le .req à l'autorité de certification.

2. Importer le certificat émis : EAC > Serveurs > Certificats > Terminer la demande en attente ; ou :
   ```powershell
   Import-ExchangeCertificate -Server EXCH01 -FileData ([System.IO.File]::ReadAllBytes("C:\Temp\exchange.cer"))
   ```
   👉 Explication : importe la réponse ; installer d'abord la chaîne intermédiaire dans le magasin approprié.

3. Lister puis assigner les services :
   ```powershell
   Get-ExchangeCertificate -Server EXCH01 | Format-List Thumbprint, Subject, Services, NotAfter
   Enable-ExchangeCertificate -Server EXCH01 -Thumbprint EMPREINTE_CERTIFICAT -Services IIS,SMTP
   ```
   👉 Explication : remplacer `EMPREINTE_CERTIFICAT` par l'empreinte relevée ; accepter le remplacement du certificat SMTP par défaut si demandé.

4. Définir le certificat du connecteur de réception/envoi si un nom TLS spécifique est utilisé :
   ```powershell
   Set-ReceiveConnector "EXCH01\Default Frontend EXCH01" -TlsCertificateName "<I>ISSUER<S>CN=mail.example.net"
   ```
   👉 Explication : la valeur `TlsCertificateName` suit le format `<I>émetteur<S>sujet` ; à relever dans `Get-ExchangeCertificate`.

5. Aligner les URL des répertoires virtuels (Autodiscover, OWA, ECP, EWS, ActiveSync) sur le nom du certificat :
   ```powershell
   Get-OwaVirtualDirectory -Server EXCH01 | Set-OwaVirtualDirectory -InternalUrl https://mail.example.net/owa -ExternalUrl https://mail.example.net/owa
   ```
   👉 Explication : répéter pour ECP, EWS, OAB, ActiveSync ; évite les alertes de certificat.

## 2. Production — Contrôles

Suivre les dates d'expiration (alerte à 30 jours), renouveler avec une nouvelle demande, tester depuis un client externe et par un contrôle STARTTLS sur le port 25.

## 3. Production — Sécurité

- Clé privée non exportable lorsque possible, certificat SAN limité aux noms nécessaires.
- Désactiver SSL 3.0/TLS 1.0/1.1 selon la politique et les prérequis du CU (vérifier la documentation officielle avant).
- Ne jamais stocker de fichier PFX avec son mot de passe en clair.

## Validation et retour arrière

- **Validation** : navigateur sur `https://mail.example.net/owa` sans alerte ; `Get-ExchangeCertificate` affiche `Services` attendus et `NotAfter` futur.
- **Retour arrière** : ré-assigner l'ancien certificat encore valide avec `Enable-ExchangeCertificate -Thumbprint ANCIENNE_EMPREINTE -Services IIS,SMTP`, puis redémarrer IIS (`iisreset`) hors heures ouvrées.

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](/01-fiches-simples/logiciels/12-messagerie-et-collaboratif/fiche-logiciel-exchange-server)