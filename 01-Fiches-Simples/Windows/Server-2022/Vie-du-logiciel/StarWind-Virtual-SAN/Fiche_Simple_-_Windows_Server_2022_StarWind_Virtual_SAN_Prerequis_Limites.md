# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Prerequis_Limites

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `stockage / SAN / StarWind`
- **Tags** : `starwind`, `virtual-san`, `windows-server`, `prerequis`, `stockage`

---

## Problème précis à résoudre

Valider qu'un serveur Windows Server 2022 peut accueillir StarWind Virtual SAN et connaître les limites de ce guide (Windows Server 2022 uniquement).

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version de Windows. PowerShell : `Get-ComputerInfo -Property OsName,OsVersion,OsBuildNumber`.
```powershell
Get-ComputerInfo -Property OsName,OsVersion,OsBuildNumber
```
   👉 Explication : on confirme un Windows Server 2022 ; ce guide ne couvre aucun autre système.

2. Lister les volumes et disques candidats au stockage. GUI : **Gestionnaire de serveur > Services de fichiers et de stockage > Volumes**. PowerShell :
```powershell
Get-Disk
Get-Volume
```
   👉 Explication : le stockage servi par StarWind doit être dédié ; on repère disque système et disques de données.

3. Lister les cartes réseau. GUI : **Panneau de configuration > Réseau et Internet > Connexions réseau**. PowerShell :
```powershell
Get-NetAdapter | Format-Table Name,Status,LinkSpeed
```
   👉 Explication : StarWind demande en pratique des réseaux séparés (gestion, iSCSI, synchronisation) ; le nombre de cartes doit être connu avant l'installation.

4. Relever dans la documentation éditeur les exigences matérielles et la matrice de compatibilité (liens en bas de fiche). Vérifier la compatibilité et la version courante du produit dans la documentation éditeur avant toute action.
   👉 Explication : les exigences exactes (CPU, RAM, réseau, hyperviseur supporté) dépendent de la version et ne sont pas recopiées ici pour ne pas les inventer.

5. Noter les limites du pack : seule l'installation sur Windows Server 2022 est documentée ici ; pas de déploiement Linux ni d'appliance couvert, et la prise en charge d'autres usages n'est ni affirmée ni exclue.
   👉 Explication : on évite d'induire une compatibilité non vérifiée.

## 2. Production — Contrôles

- Documenter version de Windows, disques dédiés et plan d'adressage (VOLUME, réseau iSCSI, réseau de synchronisation).
- Vérifier la licence ou l'édition choisie auprès de l'éditeur.

## 3. Production — Sécurité

- Ne pas installer sur un contrôleur de domaine ni sur un serveur multi-rôle non maîtrisé.
- Prévoir un compte administrateur nominatif, pas de mot de passe dans la fiche.

## Validation et retour arrière

- **Validation** : Version de Windows confirmée, disques et cartes réseau inventoriés, exigences éditeur lues.
- **Retour arrière** : Aucune modification effectuée dans cette fiche : rien à annuler.

## Si le problème n'est pas résolu

- [StarWind — site officiel du produit Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque de ressources et guides officiels](https://www.starwindsoftware.com/resource-library)
- [Fiche d'entrée du logiciel](../../../../Logiciels/06-Stockage-et-SAN-NAS/Fiche_Logiciel_-_StarWind-Virtual-SAN.md)
