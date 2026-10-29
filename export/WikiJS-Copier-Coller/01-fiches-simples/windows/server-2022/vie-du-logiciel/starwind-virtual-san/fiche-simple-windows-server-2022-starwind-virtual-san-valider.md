# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Valider

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `stockage / SAN / StarWind`

---

## Problème précis à résoudre

Contrôler que StarWind fonctionne et qu'un client accède au stockage de manière fiable.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le service. PowerShell :
```powershell
Get-Service -Name '*StarWind*'
```
   👉 Explication : le service doit être `Running`.

2. Tester la joignabilité réseau depuis un client. PowerShell :
```powershell
Test-NetConnection -ComputerName ADRESSE_IP_ISCSI -Port PORT_ISCSI
```
   👉 Explication : ADRESSE_IP_ISCSI et PORT_ISCSI sont à remplacer (port iSCSI à confirmer dans la doc) ; `TcpTestSucceeded` doit valoir True.

3. Contrôler la session iSCSI. GUI : **Initiateur iSCSI > Cibles** ; PowerShell :
```powershell
Get-IscsiSession
Get-Disk
```
   👉 Explication : la cible est connectée et un disque distant apparaît.

4. Dans la console StarWind, vérifier l'état des dispositifs de stockage (menu exact selon version).
   👉 Explication : l'état affiché est l'indicateur de santé propre au produit.

5. Tester la panne d'un chemin ou d'un nœud uniquement en lab, hors production.
   👉 Explication : on valide la tolérance avant de la considérer acquise.

## 2. Production — Contrôles

- Conserver une preuve de recette (date, version, résultat).
- Surveiller disque, réseau et journaux Windows.

## 3. Production — Sécurité

- Ne pas tester de panne sur la production sans fenêtre de maintenance.
- Aucun secret dans les captures.

## Validation et retour arrière

- **Validation** : Service actif, cible connectée, disque présent et lisible.
- **Retour arrière** : Déconnecter la cible (`Disconnect-IscsiTarget`) et supprimer le volume de test ; rien à annuler en lecture seule.

## Si le problème n'est pas résolu

- [StarWind — site officiel du produit Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque de ressources et guides officiels](https://www.starwindsoftware.com/resource-library)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/06-stockage-et-san-nas/fiche-logiciel-starwind-virtual-san)