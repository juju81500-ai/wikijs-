# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Installer

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / installation
- **Tags** : `windows-server-2022`, `exchange-server`, `messagerie`, `installation`, `setup`

---

## Problème précis à résoudre

Installer le rôle Mailbox Exchange Server avec préparation du schéma et de l'organisation Active Directory.

## 1. Hors-Production (Lab / Test / POC)

1. Monter l'ISO du CU ou de Subscription Edition (vérifier le hachage publié) : clic droit sur l'ISO > Monter, noter la lettre de lecteur.
   👉 Explication : la lettre est à remplacer par celle attribuée (ex. `D:`).

2. Préparer le schéma (compte Schema Admins/Enterprise Admins, dans le site du maître de schéma) :
   ```powershell
   D:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /PrepareSchema
   ```
   👉 Explication : étend le schéma AD ; attendre la réplication avant la suite.

3. Préparer Active Directory et créer l'organisation :
   ```powershell
   D:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /PrepareAD /OrganizationName:"ORGANISATION"
   D:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /PrepareAllDomains
   ```
   👉 Explication : remplacer `ORGANISATION` par le nom d'organisation Exchange (non modifiable ensuite).

4. Installer le rôle Mailbox, par l'assistant (D:\Setup.exe > suivre les écrans, cocher la vérification des prérequis) ou en ligne de commande :
   ```powershell
   D:\Setup.exe /IAcceptExchangeServerLicenseTerms_DiagnosticDataOFF /Mode:Install /Roles:Mailbox /MdbName:DB01 /DbFilePath:"E:\DB01\DB01.edb" /LogFolderPath:"F:\DB01"
   ```
   👉 Explication : `DB01`, `E:` et `F:` sont à remplacer par le nom de base et les volumes bases/journaux.

5. Redémarrer puis ouvrir Exchange Management Shell (menu Démarrer > Exchange Management Shell) et l'Exchange Admin Center : `https://EXCH01.CONTOSO.LOCAL/ecp`.
   ```powershell
   Get-ExchangeServer | Format-List Name, Edition, AdminDisplayVersion
   ```
   👉 Explication : contrôle la version installée ; remplacer `EXCH01.CONTOSO.LOCAL` par le FQDN du serveur.

## 2. Production — Contrôles

Planifier une fenêtre de changement, exclure les chemins Exchange de l'antivirus selon la liste officielle, vérifier `C:\ExchangeSetupLogs\ExchangeSetup.log` après installation.

## 3. Production — Sécurité

- Ne pas laisser le compte d'installation avec des droits d'enterprise.
- Ne pas publier l'EAC/ECP sur Internet sans restriction.
- Choisir consciemment l'option de télémétrie.

## Validation et retour arrière

- **Validation** : Services Exchange démarrés (`Get-Service MSExchange*`), base montée (`Get-MailboxDatabase -Status`), EAC accessible en interne.
- **Retour arrière** : avant mise en production : restaurer le snapshot de la VM ; après : `Setup.exe /Mode:Uninstall` ne retire pas les extensions AD, qui restent.

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
