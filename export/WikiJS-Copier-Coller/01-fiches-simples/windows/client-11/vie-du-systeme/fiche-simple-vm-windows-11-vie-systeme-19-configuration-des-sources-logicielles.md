# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_19_Configuration_Des_Sources_Logicielles

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 19 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Définir les sources d'installation autorisées : Microsoft Store, WinGet, Intune, partage interne.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les sources WinGet : **Microsoft Store > Bibliothèque** (graphique) ou commande.
   ```powershell
   winget source list
   ```
   👉 Explication : affiche `winget` et `msstore` (le catalogue officiel).

2. Ajouter une source interne approuvée (`URL_SOURCE_INTERNE`) et retirer les sources non voulues.
   ```powershell
   winget source add --name Interne --arg https://URL_SOURCE_INTERNE --type Microsoft.Rest
   winget source remove --name NOM_SOURCE
   ```
   👉 Explication : n'autorise que des sources maîtrisées.

3. Restreindre le Microsoft Store par GPO ou Intune : **Configuration ordinateur > Modèles d'administration > Composants Windows > Store > Désactiver l'application Store**.
   ```powershell
   Get-AppxPackage -AllUsers Microsoft.WindowsStore | Select-Object Name,Version
   ```
   👉 Explication : contrôle la présence du Store; l'accès est ensuite filtré par stratégie.

4. Déployer via Intune les applications métier plutôt que par téléchargement manuel : **Intune > Applications > Windows > Ajouter**.
   👉 Explication : centralise le catalogue et les versions.

## 2. Production — Contrôles

Seules les sources de l'entreprise sont autorisées; catalogue d'applications validé.

## 3. Production — Sécurité

Interdire l'installation depuis des sites inconnus (SmartScreen, AppLocker).

## Validation et retour arrière

- **Validation** : `winget source list` ne montre que les sources approuvées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)