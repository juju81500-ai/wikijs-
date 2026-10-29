# Fiche_Simple_-_Windows_Server_2022_VMware_Horizon_Configurer

- **Environnement** : Serveurs Windows Server 2022 (Connection Server), vCenter, UAG, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version Horizon à vérifier auprès de l'éditeur
- **Catégorie** : VDI / Horizon
- **Tags** : `vmware-horizon`, `horizon`, `windows-server`, `configuration`

---

## Problème précis à résoudre

Configurer pools de bureaux, droits et Unified Access Gateway pour Horizon.

## 1. Hors-Production (Lab / Test / POC)

1. Créer l'image parente : snapshot de VM_MODELE après installation de l'agent.
   👉 Explication : base des clones.

2. Créer le pool : GUI **Inventory > Desktops > Add**, choisir le type (pool automatisé ou manuel), le clonage depuis vCenter, le modèle VM_MODELE, le snapshot, le datastore et la convention de nommage NOM_POOL (à remplacer).
   👉 Explication : le libellé exact des étapes dépend de la version.

3. Donner les droits : GUI **Inventory > Desktops > NOM_POOL > Entitlements > Add** avec le groupe AD GROUPE_UTILISATEURS.
   👉 Explication : seuls ces utilisateurs voient le pool.

4. Déployer UAG : importer l'OVA officielle dans vCenter ; renseigner le fichier INI avec le script de déploiement officiel (vérifier le nom du script dans la doc) :
```powershell
# Exemple de lancement, depuis le dossier du script officiel
.\uagdeploy.ps1 -iniFile CHEMIN_UAG.ini
```
   👉 Explication : CHEMIN_UAG.ini est à remplacer ; il référence les mots de passe saisis à l'invite, pas en clair.

5. Dans l'UAG (interface d'administration en HTTPS, port à vérifier), activer Horizon : **Edge Service Settings > Horizon Settings**, URL du Connection Server https://CS1_HORIZON.
   👉 Explication : l'UAG relaie les sessions externes.

6. Option PowerShell (module VMware.VimAutomation.HorizonView de PowerCLI, à confirmer) :
```powershell
Connect-HVServer -Server CS1_HORIZON
Get-HVPool | Select-Object -ExpandProperty Base
```
   👉 Explication : retourne les pools existants.

## 2. Production — Contrôles

- Documenter pools, droits et UAG.
- Tester avec un seul utilisateur.

## 3. Production — Sécurité

- Droits via groupes AD.
- UAG dans une DMZ avec pare-feu strict.

## Validation et retour arrière

- **Validation** : Pool visible dans Horizon Client, machines Available.
- **Retour arrière** : Supprimer le pool depuis la console et retirer les droits.

## Si le problème n'est pas résolu

- [Documentation Horizon (Omnissa/VMware)](https://docs.omnissa.com/)
- [Broadcom TechDocs — Horizon](https://techdocs.broadcom.com/)
- [Fiche d'entrée du logiciel](../../../../Logiciels/13-Poste-de-travail-et-VDI/Fiche_Logiciel_-_VMware-Horizon.md)
