# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_20_Mise_A_Jour_Initiale

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 20 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-20`

---

## Problème précis à résoudre

Appliquer toutes les mises à jour disponibles avant la mise en production.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer la recherche : **Paramètres > Windows Update > Rechercher les mises à jour**, puis **Télécharger et installer tout**.
   ```powershell
   Install-Module PSWindowsUpdate -Scope CurrentUser
   Get-WindowsUpdate
   Install-WindowsUpdate -AcceptAll -AutoReboot
   ```
   👉 Explication : installe le module communautaire PSWindowsUpdate (depuis la PowerShell Gallery) puis applique les mises à jour; en entreprise, préférer WSUS ou Intune.

2. Variante sans module : lancer le service d'analyse natif.
   ```powershell
   usoclient StartScan
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 10
   ```
   👉 Explication : déclenche l'analyse et liste les derniers correctifs installés.

3. Redémarrer puis recommencer jusqu'à ce qu'il n'y ait plus de mise à jour : **Paramètres > Windows Update > Historique des mises à jour**.
   ```powershell
   Get-WindowsUpdateLog
   (Get-ComputerInfo).OsBuildNumber
   ```
   👉 Explication : génère le journal de mise à jour (`WindowsUpdate.log` sur le bureau) et affiche le build atteint.

4. Pour Windows 10 (fin de support le 14 octobre 2025), ne recevoir les correctifs de sécurité que si le poste est inscrit aux mises à jour de sécurité étendues (ESU); sinon planifier la migration vers Windows 11.
   👉 Explication : au-delà de la fin de support, sans ESU, aucun correctif de sécurité n'est publié.

## 2. Production — Contrôles

Pour le parc, passer par WSUS, Windows Update for Business ou Intune avec des anneaux de déploiement (pilote puis généralisé).

## 3. Production — Sécurité

Mettre à jour le système avant toute exposition au réseau; sauvegarder avant les mises à jour de fonctionnalités.

## Validation et retour arrière

- **Validation** : `Paramètres > Windows Update` affiche « Vous êtes à jour ».
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
