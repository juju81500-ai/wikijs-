# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Prerequis_Limites

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix

---

## Problème précis à résoudre

Cadrer les prérequis, licences et limites avant de déployer Citrix Virtual Apps and Desktops (CVAD) sur Windows Server 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier dans la documentation officielle Citrix que Windows Server 2022 est pris en charge pour la version VERSION_CVAD (à remplacer par la version ciblée, LTSR ou CR) pour chaque composant : Delivery Controller, StoreFront, Studio, Licensing, VDA.
   👉 Explication : la matrice de support dépend de la version publiée ; ne pas supposer.

2. Lister les rôles prévus et les noms de serveurs : DC1_CITRIX (Delivery Controller), SF1_CITRIX (StoreFront), LIC_CITRIX (serveur de licences), SQL_CITRIX (SQL Server), VDA_MODELE (image de base).
   👉 Explication : ces noms sont des placeholders à remplacer par vos noms DNS ; un seul rôle par serveur est recommandé en production.

3. Contrôler le domaine et le DNS depuis chaque serveur. PowerShell :
```powershell
Get-ComputerInfo -Property CsDomain,OsName,OsVersion
Resolve-DnsName NOM_DC_AD
Test-NetConnection SQL_CITRIX -Port 1433
```
   👉 Explication : CsDomain doit être le domaine AD cible ; NOM_DC_AD est un contrôleur de domaine à remplacer ; 1433 est le port SQL par défaut (instance nommée : adapter).

4. Cadrer les licences : GUI **Citrix Cloud / compte Citrix > Licences** pour récupérer le fichier de licence ou le code, et vérifier que la date Subscription Advantage / droit est valide pour la version installée.
   👉 Explication : une version trop récente par rapport à la date de licence est refusée ; à contrôler avant installation. Les licences Windows Server RDS (CAL RDS) pour les VDA serveur sont à prévoir séparément.

5. Contrôler les droits : compte de service ou administrateur de domaine nominatif ayant droit de création de bases sur SQL_CITRIX (rôle dbcreator temporaire).
   👉 Explication : évite un échec de création de la base de site pendant l'assistant Studio.

## 2. Production — Contrôles

- Matrice de support et date de licence validées par écrit.
- Plan d'adressage, DNS et horloge NTP cohérents entre tous les serveurs.
- Test d'abord sur un lab avant toute production.

## 3. Production — Sécurité

- Aucun mot de passe dans la fiche ; comptes nominatifs.
- Pas d'exposition Internet directe : passer par un accès distant (Gateway/proxy) validé.

## Validation et retour arrière

- **Validation** : Tableau prérequis rempli, licences vérifiées, serveurs joignables.
- **Retour arrière** : Rien n'est installé à ce stade ; aucun retour arrière nécessaire.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops)