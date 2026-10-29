# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Configurer

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix

---

## Problème précis à résoudre

Configurer licences, catalogues de machines, groupes de mise à disposition et StoreFront.

## 1. Hors-Production (Lab / Test / POC)

1. Configurer le serveur de licences : GUI **Studio > Configuration > Licensing > Add license** puis **Add** le serveur LIC_CITRIX:27000 (port par défaut à vérifier), choisir l'édition et importer le fichier de licence CHEMIN_LICENCE.
   👉 Explication : CHEMIN_LICENCE est à remplacer ; le fichier de licence vient du compte Citrix et n'est jamais stocké dans la fiche.

2. Créer un catalogue : GUI **Studio > Machine Catalogs > Create Machine Catalog** ; choisir le type de système (multi-session ou session unique), le mode d'alimentation, le mode de gestion et sélectionner les machines VDA.
   👉 Explication : 

3. Équivalent PowerShell (adapter les valeurs) :
```powershell
Add-PSSnapin Citrix*
New-BrokerCatalog -Name 'CAT_SERVEURS' -AllocationType Random -SessionSupport MultiSession -ProvisioningType Manual -MachinesArePhysical $true
New-BrokerMachine -MachineName 'DOMAINE\VDA01' -CatalogUid (Get-BrokerCatalog -Name 'CAT_SERVEURS').Uid
```
   👉 Explication : CAT_SERVEURS, DOMAINE et VDA01 sont à remplacer ; vérifier les paramètres avec Get-Help New-BrokerCatalog pour votre version.

4. Créer le groupe de mise à disposition : GUI **Studio > Delivery Groups > Create Delivery Group**, choisir le catalogue, les utilisateurs autorisés (groupe AD GROUPE_UTILISATEURS) et les applications ou bureaux publiés.
   👉 Explication : GROUPE_UTILISATEURS est un groupe de sécurité AD à remplacer.

5. Ajouter le Controller à StoreFront : console StoreFront **Stores > Manage Delivery Controllers > Add** avec DC1_CITRIX, type XenDesktop, transport HTTPS si le certificat du Controller est en place.
   👉 Explication : le store affiche ensuite les ressources du site.

## 2. Production — Contrôles

- Documenter catalogues, groupes et utilisateurs autorisés.
- Appliquer la convention de nommage de l'organisation.

## 3. Production — Sécurité

- Droits Studio donnés via rôles d'administration délégués (Full Administrator limité).
- Limiter les groupes autorisés au strict nécessaire.

## Validation et retour arrière

- **Validation** : Machines enregistrées, groupe de livraison visible dans StoreFront.
- **Retour arrière** : Supprimer le groupe puis le catalogue dans Studio (Remove-BrokerDesktopGroup / Remove-BrokerCatalog) après arrêt des sessions.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops)