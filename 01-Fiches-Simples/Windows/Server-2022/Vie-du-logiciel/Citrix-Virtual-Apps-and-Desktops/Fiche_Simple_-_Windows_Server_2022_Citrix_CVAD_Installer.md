# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Installer

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix
- **Tags** : `citrix`, `cvad`, `windows-server`, `installation`

---

## Problème précis à résoudre

Installer le Delivery Controller, Studio, StoreFront, le serveur de licences et le VDA de CVAD sur Windows Server 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Récupérer l'ISO officielle de VERSION_CVAD sur le portail Citrix et contrôler son empreinte. PowerShell :
```powershell
Get-FileHash -Algorithm SHA256 -Path CHEMIN_ISO
```
   👉 Explication : CHEMIN_ISO est à remplacer par le chemin de l'ISO ; comparer avec l'empreinte publiée si fournie.

2. Monter l'ISO sur SF1_CITRIX/DC1_CITRIX puis lancer GUI : **autorun > Delivery Controller** ; cocher Delivery Controller, Studio, License Server (ou serveur de licences dédié) selon le plan, puis valider le pare-feu automatique proposé.
   👉 Explication : l'assistant installe les prérequis (.NET, VC++) ; un redémarrage peut être demandé.

3. Créer le site : GUI **Citrix Studio > Deliver applications and desktops > Site** ; saisir le nom du site, le serveur SQL (SQL_CITRIX) et les noms des bases (SITE_DB, MONITOR_DB, LOG_DB à remplacer).
   👉 Explication : les trois bases (site, supervision, journalisation de configuration) sont créées par Studio.

4. Installer StoreFront depuis l'ISO sur SF1_CITRIX : **autorun > StoreFront**, puis créer le déploiement dans la console StoreFront (**Create a new deployment**) avec l'URL de base HTTPS https://STORE_FQDN (à remplacer).
   👉 Explication : STORE_FQDN doit correspondre au certificat TLS posé à l'étape sécurité.

5. Installer le VDA sur l'image VDA_MODELE : ISO **autorun > Virtual Delivery Agent for Windows Server OS** (session multiutilisateur) ou **Desktop OS** selon la cible, et renseigner les Delivery Controllers DC1_CITRIX:80 lorsque demandé.
   👉 Explication : le VDA s'enregistre auprès du Controller ; un VDA serveur nécessite le rôle RDS et les CAL correspondantes.

6. Contrôler les snap-ins PowerShell Citrix depuis un Controller :
```powershell
Add-PSSnapin Citrix*
Get-PSSnapin Citrix* | Select-Object Name,Version
Get-BrokerSite
```
   👉 Explication : les snap-ins Citrix.* sont installés avec les Controllers/Studio ; Get-BrokerSite doit retourner le site créé.

## 2. Production — Contrôles

- Noter la version installée de chaque composant.
- Snapshot de la VM avant installation.
- Journaux d'installation conservés.

## 3. Production — Sécurité

- Exécuter l'installation avec un compte nominatif administrateur.
- Ne pas ouvrir les ports du Controller hors réseau d'administration.

## Validation et retour arrière

- **Validation** : Studio s'ouvre sans erreur, Get-BrokerSite répond, StoreFront affiche le déploiement.
- **Retour arrière** : Restaurer le snapshot de la VM ; supprimer le site depuis Studio seulement si les bases sont à abandonner.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](../../../../Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_Citrix-Virtual-Apps-and-Desktops.md)
