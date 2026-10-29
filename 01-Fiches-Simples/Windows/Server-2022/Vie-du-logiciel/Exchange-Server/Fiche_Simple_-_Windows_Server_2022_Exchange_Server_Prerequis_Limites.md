# Fiche_Simple_-_Windows_Server_2022_Exchange_Server_Prerequis_Limites

- **Environnement** : Windows Server 2022; Exchange Server 2019 CU14 ou ultérieur, ou Exchange Server Subscription Edition (vérifier la matrice de support publiée)
- **OS / Version** : Windows Server 2022
- **Catégorie** : Messagerie / prérequis
- **Tags** : `windows-server-2022`, `exchange-server`, `messagerie`, `prerequis`, `active-directory`

---

## Problème précis à résoudre

Vérifier qu'un serveur Windows Server 2022 et l'annuaire Active Directory sont prêts à recevoir Exchange Server, et connaître les limites de support.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version supportée : Exchange 2016 n'est pas supporté sur Windows Server 2022 ; retenir Exchange 2019 CU14 ou ultérieur, ou Subscription Edition, après lecture de la matrice officielle.
   👉 Explication : la combinaison OS / CU / .NET / niveau fonctionnel AD doit figurer dans la matrice de support avant tout déploiement.

2. Contrôler le niveau fonctionnel de la forêt et du domaine, et le rôle FSMO :
   ```powershell
   Get-ADForest | Select-Object ForestMode, SchemaMaster
   Get-ADDomain | Select-Object DomainMode, PDCEmulator
   ```
   👉 Explication : relever les niveaux ; les comparer au minimum exigé par la matrice (à vérifier).

3. Dimensionner la VM (RAM, CPU, disques séparés pour système, bases et journaux) : ouvrir Gestionnaire Hyper-V > Paramètres de la VM, ou consulter l'outil de dimensionnement Microsoft.
   👉 Explication : ne pas activer la mémoire dynamique ; prévoir un volume de bases et un volume de journaux distincts (ReFS ou NTFS selon recommandation officielle).

4. Joindre le serveur au domaine, fixer une IP statique et un nom DNS : Gestionnaire de serveur > Serveur local > Nom de l'ordinateur ; ou :
   ```powershell
   Add-Computer -DomainName CONTOSO.LOCAL -NewName EXCH01 -Restart
   ```
   👉 Explication : remplacer `CONTOSO.LOCAL` (domaine AD) et `EXCH01` (nom du serveur).

5. Installer les fonctionnalités Windows (une ligne, la liste exacte est à comparer à la page officielle des prérequis) :
   ```powershell
   Install-WindowsFeature Server-Media-Foundation, NET-Framework-45-Features, RPC-over-HTTP-proxy, RSAT-Clustering, RSAT-Clustering-CmdInterface, RSAT-Clustering-Mgmt, RSAT-Clustering-PowerShell, WAS-Process-Model, Web-Asp-Net45, Web-Basic-Auth, Web-Client-Auth, Web-Digest-Auth, Web-Dir-Browsing, Web-Dyn-Compression, Web-Http-Errors, Web-Http-Logging, Web-Http-Redirect, Web-Http-Tracing, Web-ISAPI-Ext, Web-ISAPI-Filter, Web-Lgcy-Mgmt-Console, Web-Metabase, Web-Mgmt-Console, Web-Mgmt-Service, Web-Net-Ext45, Web-Request-Monitor, Web-Server, Web-Stat-Compression, Web-Static-Content, Web-Windows-Auth, Web-WMI, Windows-Identity-Foundation, RSAT-ADDS
   ```
   👉 Explication : installe IIS, clustering et outils AD requis par le rôle Mailbox.

6. Installer les composants tiers depuis les sources officielles Microsoft : .NET Framework (version exigée par le CU), Visual C++ Redistributable (versions exigées par le CU), et UCMA 4.0 si le CU 2019 le demande. Vérifier les hachages des installeurs.
   👉 Explication : les versions exactes dépendent du CU : vérifier la page « prérequis » publiée.

## 2. Production — Contrôles

Valider le plan d'adressage, les noms DNS publics (mail, autodiscover), le MX, la réplication AD saine (`dcdiag`, `repadmin /replsummary`) et la sauvegarde récente de l'AD avant extension de schéma.

## 3. Production — Sécurité

- Étendre le schéma depuis un compte dédié membre de Schema Admins et Enterprise Admins, retiré du groupe ensuite.
- Ne pas installer Exchange sur un contrôleur de domaine.
- Exchange 2019 est hors support standard depuis octobre 2025 : privilégier Subscription Edition (vérifier le calendrier publié).

## Validation et retour arrière

- **Validation** : `Get-WindowsFeature | Where-Object Installed` contient la liste, le serveur est joint au domaine et résout les DNS.
- **Retour arrière** : retirer les fonctionnalités ajoutées ou restaurer le snapshot de la VM ; aucune modification AD n'a encore eu lieu à cette étape.

## Si le problème n'est pas résolu

- [Exchange Server — documentation Microsoft](https://learn.microsoft.com/exchange/exchange-server)
- [Matrice de support Exchange Server](https://learn.microsoft.com/exchange/plan-and-deploy/supportability-matrix)
- [Fiche d'entrée Exchange Server](../../../../Logiciels/12-Messagerie-et-collaboratif/Fiche_Logiciel_-_Exchange-Server.md)
