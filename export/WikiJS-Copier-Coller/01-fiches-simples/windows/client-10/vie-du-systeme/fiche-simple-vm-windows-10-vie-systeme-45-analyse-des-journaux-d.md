# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_45_Analyse_Des_Journaux_D

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 45 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Rechercher les erreurs et avertissements après la mise en service.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir l'**Observateur d'événements > Affichages personnalisés > Événements d'administration**, ou lister les erreurs récentes.
   ```powershell
   Get-WinEvent -FilterHashtable @{LogName='System','Application';Level=1,2;StartTime=(Get-Date).AddDays(-2)} | Select-Object TimeCreated,ProviderName,Id,Message -First 30
   ```
   👉 Explication : extrait les erreurs critiques et les erreurs des 2 derniers jours.

2. Rechercher les arrêts brutaux et plantages.
   ```powershell
   Get-WinEvent -FilterHashtable @{LogName='System';Id=41,6008,1001} -MaxEvents 10 | Select-Object TimeCreated,Id,Message
   ```
   👉 Explication : 41 : redémarrage inattendu; 6008 : arrêt incorrect; 1001 : rapport de plantage.

3. Contrôler l'intégrité des fichiers système.
   ```powershell
   sfc /scannow
   DISM /Online /Cleanup-Image /ScanHealth
   ```
   👉 Explication : vérifie et détecte la corruption des fichiers (exécuter en administrateur).

4. Consulter la fiabilité : **Panneau de configuration > Sécurité et maintenance > Maintenance > Afficher l'historique des fiabilités**.
   ```powershell
   Get-CimInstance Win32_ReliabilityStabilityMetrics | Select-Object -First 5
   ```
   👉 Explication : indique l'indice de stabilité.

## 2. Production — Contrôles

Chaque erreur est classée : à corriger, à surveiller ou à ignorer avec justification.

## 3. Production — Sécurité

Ne pas diffuser les journaux bruts contenant des noms d'utilisateurs ou d'adresses à l'extérieur.

## Validation et retour arrière

- **Validation** : Aucune erreur critique non expliquée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)