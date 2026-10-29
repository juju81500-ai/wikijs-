# Fiche_Simple_-_Windows_Server_2022_StarWind_Virtual_SAN_Installer

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `stockage / SAN / StarWind`
- **Tags** : `starwind`, `virtual-san`, `windows-server`, `installation`

---

## Problème précis à résoudre

Installer StarWind Virtual SAN sur Windows Server 2022 avec le programme d'installation officiel.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'installeur depuis le portail officiel StarWind (compte requis) et noter son nom et son empreinte : PowerShell `Get-FileHash -Algorithm SHA256 -Path CHEMIN_INSTALLEUR`.
```powershell
Get-FileHash -Algorithm SHA256 -Path CHEMIN_INSTALLEUR
```
   👉 Explication : CHEMIN_INSTALLEUR est à remplacer par le chemin local du fichier ; l'empreinte permet de comparer avec celle publiée si l'éditeur en fournit une.

2. Lancer l'installeur en tant qu'administrateur (clic droit > **Exécuter en tant qu'administrateur**) et suivre l'assistant. Choisir les composants proposés par la version (service StarWind et console de gestion) ; options exactes à vérifier dans la documentation de la version.
   👉 Explication : l'assistant installe le service de stockage et l'outil d'administration ; les écrans varient selon la version.

3. Contrôler le service installé. PowerShell :
```powershell
Get-Service -Name '*StarWind*' | Format-Table Name,Status,StartType
```
   👉 Explication : le service doit être en `Running` et en démarrage automatique ; le nom exact est à confirmer sur votre version.

4. Redémarrer le serveur seulement si l'assistant le demande.
   👉 Explication : un redémarrage inutile coupe le stockage ; on suit l'assistant.

## 2. Production — Contrôles

- Conserver la version installée dans la documentation d'exploitation.
- Installer d'abord sur un lab avant production.

## 3. Production — Sécurité

- Télécharger uniquement depuis le site officiel.
- Ne jamais saisir la clé de licence dans cette fiche ni dans un dépôt.

## Validation et retour arrière

- **Validation** : Le service StarWind est `Running` et la console de gestion s'ouvre.
- **Retour arrière** : **Programmes et fonctionnalités** (`appwiz.cpl`) > désinstaller StarWind Virtual SAN, après avoir sauvegardé ou migré toute donnée présente ; vérifier la procédure de désinstallation éditeur.

## Si le problème n'est pas résolu

- [StarWind — site officiel du produit Virtual SAN](https://www.starwindsoftware.com/starwind-virtual-san)
- [StarWind — bibliothèque de ressources et guides officiels](https://www.starwindsoftware.com/resource-library)
- [Fiche d'entrée du logiciel](../../../../Logiciels/06-Stockage-et-SAN-NAS/Fiche_Logiciel_-_StarWind-Virtual-SAN.md)
