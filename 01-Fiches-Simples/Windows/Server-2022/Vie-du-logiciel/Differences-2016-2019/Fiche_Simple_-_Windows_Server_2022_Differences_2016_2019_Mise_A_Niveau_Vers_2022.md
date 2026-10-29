# Fiche_Simple_-_Windows_Server_2022_Differences_2016_2019_Mise_A_Niveau_Vers_2022

- **Environnement** : Windows Server 2016 et 2019 (comparés à 2022), lab ou serveur de test
- **OS / Version** : Windows Server 2016 / 2019 (référence 2022)
- **Catégorie** : systèmes / différences de versions
- **Tags** : `windows-server`, `windows-server-2016`, `windows-server-2019`, `windows-server-2022`, `mise-a-niveau`, `in-place-upgrade`, `migration`

---

## Problème précis à résoudre

Réaliser une mise à niveau en place de Windows Server 2016 ou 2019 vers 2022 en limitant le risque.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la voie de mise à niveau supportée dans la documentation Microsoft (2016 vers 2022 et 2019 vers 2022 sont des chemins documentés, mêmes édition et langue) et la compatibilité des applications et pilotes.
   👉 Explication : la mise à niveau n'est pas permise entre toutes les éditions, ni dans tous les cas pour un DC avec rôles spécifiques ; contrôler la page officielle.
2. Prendre une sauvegarde complète et un snapshot de VM :
   ```powershell
   wbadmin start backup -backupTarget:E: -include:C: -allCritical -quiet
   ```
   👉 Explication : `E:` est un volume de sauvegarde à adapter ; vérifier la restauration avant de continuer.
3. Monter l'ISO 2022 et lancer l'installation depuis le système en cours :
   ```powershell
   Start-Process 'E:\setup.exe'
   ```
   👉 Explication : `E:` est la lettre de l'ISO monté ; choisir **Conserver les fichiers personnels et les applications**.
4. Après redémarrage, vérifier version et services :
   ```powershell
   Get-ComputerInfo -Property WindowsProductName,OsBuildNumber
   Get-Service | Where-Object {$_.StartType -eq 'Automatic' -and $_.Status -ne 'Running'}
   ```
   👉 Explication : tous les services automatiques doivent revenir ; installer ensuite les mises à jour cumulatives.

## 2. Production — Contrôles

- Mise à niveau en fenêtre de maintenance, après test sur un clone ; ordre pour AD : d'abord les DC 2022 ajoutés ou mis à niveau, ensuite les niveaux fonctionnels.
- Pour un parc critique, préférer une migration vers un nouveau serveur 2022 plutôt qu'une mise à niveau en place.

## 3. Production — Sécurité

- Appliquer les mises à jour cumulatives et le durcissement 2022 juste après l'opération ; contrôler l'antivirus et le pare-feu.

## Validation et retour arrière

- **Validation** : build 2022, rôles actifs, applications testées. **Retour arrière** : voir la fiche Retour_Arriere (snapshot ou restauration).

## Si le problème n'est pas résolu

- [Fiche d'entrée Windows Server 2016 / 2019 / 2022](../../../../Logiciels/05-Systemes-annuaires-et-services/Fiche_Logiciel_-_Windows-Server-2016-2019-2022.md)
- [Microsoft Learn — Mise à niveau de Windows Server](https://learn.microsoft.com/fr-fr/windows-server/get-started/perform-in-place-upgrade)
- [Microsoft Learn — Chemins de mise à niveau](https://learn.microsoft.com/fr-fr/windows-server/get-started/upgrade-overview)
