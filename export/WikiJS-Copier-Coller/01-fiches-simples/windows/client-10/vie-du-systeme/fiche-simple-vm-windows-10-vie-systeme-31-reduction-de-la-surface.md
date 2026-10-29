# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Supprimer les composants, services et applications inutiles (débloat).

## 1. Hors-Production (Lab / Test / POC)

1. Désinstaller les applications préinstallées inutiles : **Paramètres > Applications > Applications installées > ⋯ > Désinstaller**.
   ```powershell
   Get-AppxPackage -AllUsers | Select-Object Name,PackageFullName | Sort-Object Name
   Get-AppxPackage -AllUsers *XboxApp* | Remove-AppxPackage -AllUsers
   ```
   👉 Explication : liste les applications Store puis retire l'une d'elles (exemple : Xbox).

2. Empêcher leur réinstallation sur les nouveaux profils.
   ```powershell
   Get-AppxProvisionedPackage -Online | Where-Object DisplayName -like '*Xbox*' | Remove-AppxProvisionedPackage -Online
   ```
   👉 Explication : retire l'application de l'image pour les futurs comptes.

3. Désactiver les services inutiles : **services.msc > propriétés > Type de démarrage = Désactivé**.
   ```powershell
   Get-Service | Where-Object {$_.StartType -ne 'Disabled' -and $_.Status -eq 'Running'} | Select-Object Name,DisplayName
   Set-Service -Name NOM_SERVICE -StartupType Disabled
   ```
   👉 Explication : liste les services actifs et désactive celui qui est justifié (`NOM_SERVICE`).

4. Limiter la télémétrie au niveau requis : **Paramètres > Confidentialité et sécurité > Diagnostics et commentaires**, ou GPO **Autoriser les données de diagnostic**.
   ```powershell
   Set-ItemProperty HKLM:\SOFTWARE\Policies\Microsoft\Windows\DataCollection AllowTelemetry 1 -Type DWord
   ```
   👉 Explication : fixe le niveau de diagnostic requis (valeur 1 = « Obligatoire »; vérifier la compatibilité avec la politique de l'entreprise).

## 2. Production — Contrôles

Débloat documenté et testé sur un poste pilote; ne pas utiliser de scripts anonymes trouvés en ligne.

## 3. Production — Sécurité

Chaque retrait est consigné, avec retour arrière par réinstallation depuis le Store.

## Validation et retour arrière

- **Validation** : Aucune application ou service inutile ne subsiste et le poste reste fonctionnel.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 10](/01-fiches-simples/windows/client-10/vie-du-systeme/sommaire-vie-du-systeme-windows-10)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)