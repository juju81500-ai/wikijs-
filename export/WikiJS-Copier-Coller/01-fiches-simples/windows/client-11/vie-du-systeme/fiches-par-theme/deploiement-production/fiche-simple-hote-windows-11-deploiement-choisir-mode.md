# Fiche_Simple_-_Hote_Windows_11_Deploiement_Choisir_Mode.md

- **Environnement** : Parc de postes utilisateur: poste physique ou VM de test
- **OS / Version** : Windows 11 Pro ou Enterprise selon la gestion prévue
- **Catégorie** : déploiement de poste de travail

---

## Problème précis à résoudre

Décider comment le poste sera géré avant d'installer Windows 11.

## 1. Hors-Production (Lab / Test / POC)

1. Déterminer le mode de gestion : Autopilot/Intune, MECM, AD DS/GPO, image d'entreprise ou processus autonome.
   👉 Explication : l'enrôlement en masse dépend de la solution de parc et suit son runbook.

2. Vérifier édition et licence prévues (Pro ou Enterprise).
   👉 Explication : l'édition doit correspondre à la licence et au mode de gestion.

3. Sur un poste de test, contrôler TPM, Secure Boot et build :
   ```powershell
   Get-Tpm
   Confirm-SecureBootUEFI
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   ```
   👉 Explication : vérifie TPM 2.0, Secure Boot et l'édition (PowerShell en administrateur).

4. Vérifier stockage, pilote réseau, utilisateur assigné et compte de récupération.
   👉 Explication : évite un blocage en cours d'installation.

## 2. Production — Contrôles

Valider le mode de déploiement avec l'équipe parc et consigner la décision.

## 3. Production — Sécurité

- Préparer un compte de récupération géré; ne jamais utiliser un compte personnel.

## Validation et retour arrière

- **Validation** : mode de déploiement choisi, matériel conforme (TPM 2.0, Secure Boot).
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Microsoft Learn — Windows Autopilot](https://learn.microsoft.com/en-us/autopilot/)
- [Microsoft Learn — déployer Windows 11](https://learn.microsoft.com/en-us/windows/deployment/)
- [Guide complet](/02-fiches-completes/windows/client-11/installation-deploiement/25-deploiement-postes-windows-11-production#1-choisir-le-mode-de-deploiement)