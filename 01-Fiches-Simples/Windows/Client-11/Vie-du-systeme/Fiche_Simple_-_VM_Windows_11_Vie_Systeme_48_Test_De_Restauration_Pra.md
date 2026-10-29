# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver que les données et le poste peuvent être restaurés.

## 1. Hors-Production (Lab / Test / POC)

1. Restaurer un fichier : **Paramètres > Système > Stockage**, ou **Panneau de configuration > Historique des fichiers > Restaurer les fichiers personnels**.
   ```powershell
   Get-ChildItem "$env:USERPROFILE\Documents" | Select-Object -First 5
   ```
   👉 Explication : contrôle l'état avant la suppression de test du fichier restauré.

2. Restaurer depuis OneDrive : **Corbeille OneDrive** ou **Restaurer OneDrive** sur le portail.
   👉 Explication : récupère les fichiers supprimés ou chiffrés par erreur.

3. Restaurer l'état système : **Panneau de configuration > Récupération > Ouvrir la restauration du système**, ou **Paramètres > Système > Récupération > Réinitialiser ce PC**.
   ```powershell
   Get-ComputerRestorePoint
   Restore-Computer -RestorePoint NUMERO_POINT
   ```
   👉 Explication : liste les points de restauration puis restaure le point choisi (`NUMERO_POINT`); redémarrage automatique.

4. Mesurer le temps réel de restauration (RTO) et le comparer à l'objectif.
   ```powershell
   Measure-Command { Restore-Computer -RestorePoint NUMERO_POINT -WhatIf }
   ```
   👉 Explication : teste la commande sans l'exécuter; le RTO réel se mesure lors de l'exercice complet.

## 2. Production — Contrôles

Exercice documenté au moins une fois par an, avec comparaison du RTO/RPO réalisé et visé.

## 3. Production — Sécurité

Restaurer dans un environnement isolé avant toute restauration en production.

## Validation et retour arrière

- **Validation** : Fichier ou poste restauré et fonctionnel dans le délai visé.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows 11 Sysinternals Retour Arriere Limites](<../Vie-du-logiciel/Sysinternals/Fiche_Simple_-_VM_Windows_11_Sysinternals_Retour_Arriere_Limites.md>)
- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 11](./Sommaire_-_Vie_du_systeme_Windows_11.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
