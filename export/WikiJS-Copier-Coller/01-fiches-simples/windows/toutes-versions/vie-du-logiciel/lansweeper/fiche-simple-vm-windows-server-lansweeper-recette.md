# Fiche_Simple_-_VM_Windows_Server_Lansweeper_Recette.md

- **Environnement** : Serveur Windows x64 avec Lansweeper Classic (SQL LocalDB ou SQL Server selon l'échelle)
- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic selon la matrice officielle
- **Catégorie** : inventaire de parc / découverte réseau

---

## Problème précis à résoudre

Vérifier le fonctionnement avec un petit groupe d'actifs connus.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier le service et la base en ligne :
   ```powershell
   Get-Service | Where-Object { $_.Name -like 'Lansweeper*' } | Select-Object Name, Status
   ```
   👉 Explication : le service doit être Running; contrôler aussi que la console HTTPS répond.

2. Scanner un petit groupe d'actifs connus puis comparer modèle, OS, numéro de série et utilisateur aux données sources.
   👉 Explication : détecte les écarts d'inventaire.

3. Lire les erreurs de scan et ajuster une seule permission ou règle à la fois.
   👉 Explication : permet d'identifier la cause.

4. Vérifier la séparation des rôles, l'accès aux rapports et le journal d'audit.
   👉 Explication : garantit le moindre privilège.

5. Valider l'impact réseau avant d'ajouter d'autres plages.
   👉 Explication : évite de saturer le réseau.

## 2. Production — Contrôles

Documenter résultats et écarts avant extension.

## 3. Production — Sécurité

- Ne scanner que des actifs appartenant à l'organisation.

## Validation et retour arrière

- **Validation** : les actifs pilotes sont inventoriés correctement.
- **Retour arrière** : arrêter le scan et retirer la plage ajoutée.

## Si le problème n'est pas résolu

- [Lansweeper Classic — documentation](https://docs.lansweeper.com/classic/)
- [Lansweeper Classic — prérequis](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Guide complet](/02-fiches-completes/windows/server-2022/installation-deploiement/44-deploiement-lansweeper-classic-windows-server#5-recette)