# Fiche_Simple_-_VM_Windows_Server_Lansweeper_Choisir_Variante_Droits.md

- **Environnement** : Serveur Windows x64 avec Lansweeper Classic (SQL LocalDB ou SQL Server selon l'échelle)
- **OS / Version** : Windows Server 2022 recommandé; Lansweeper Classic selon la matrice officielle
- **Catégorie** : inventaire de parc / découverte réseau
- **Tags** : `lansweeper`, `windows-server-2022`, `inventaire`, `wmi`, `snmp`

---

## Problème précis à résoudre

Choisir Lansweeper Classic on-premises et vérifier la machine avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier que le besoin correspond à **Lansweeper Classic on-premises** et non à Lansweeper Platform.
   👉 Explication : ce sont deux offres distinctes; contrôler version et licence.

2. Choisir Easy (web, scan et SQL LocalDB sur une machine, base limitée à 10 Go) ou une architecture distribuée avec SQL Server.
   👉 Explication : Easy convient aux petits environnements; SQL Server au-delà.

3. Vérifier l'OS et .NET Framework :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, OsArchitecture
   Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full' | Select-Object Release
   ```
   👉 Explication : Windows 64 bits (ni Home, ni Core, ni Starter); `Release` 528040 ou plus correspond à .NET 4.8.

4. Préparer sauvegarde, DNS, certificat HTTPS et un compte d'administration nominatif.
   👉 Explication : Windows Server est recommandé au-delà de 1 000 actifs.

## 2. Production — Contrôles

Faire valider variante, licence et dimensionnement avec le propriétaire du service.

## 3. Production — Sécurité

- Compte d'administration nominatif, jamais partagé.

## Validation et retour arrière

- **Validation** : variante, licence, OS et .NET 4.8 confirmés.
- **Retour arrière** : aucune modification n'est faite par cette fiche; rien à annuler.

## Si le problème n'est pas résolu

- [Lansweeper — Platform et Classic](https://docs.lansweeper.com/classic/docs/comparing-lansweeper-platform-and-lansweeper-classic.md)
- [Lansweeper Classic — prérequis](https://docs.lansweeper.com/classic/docs/lansweeper-installation-requirements.md)
- [Guide complet](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/44_Deploiement_Lansweeper_Classic_Windows_Server.md#1-choisir-la-variante-et-preparer-les-droits)
