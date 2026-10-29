# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_07_Disposition_Du_Clavier

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Configurer la disposition de clavier correcte, y compris à l'écran de connexion.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Paramètres > Heure et langue > Langue et région > Français (France) > Options > Claviers** et choisir **Français (AZERTY)**.
   ```powershell
   Get-WinUserLanguageList
   ```
   👉 Explication : affiche la liste de langues et la disposition active.

2. Fixer le clavier français par commande :
   ```powershell
   $l = New-WinUserLanguageList fr-FR
   Set-WinUserLanguageList $l -Force
   ```
   👉 Explication : supprime les dispositions parasites (QWERTY) de la liste.

3. Appliquer à l'écran de connexion (**Paramètres de langue administratifs > Copier les paramètres**) :
   ```powershell
   Copy-UserInternationalSettingsToSystem -WelcomeScreen $true -NewUser $true
   ```
   👉 Explication : le mot de passe se saisit alors avec le même clavier avant et après ouverture de session.

## 2. Production — Contrôles

Sur une console de VM, vérifier le clavier du client (RDP, console Hyper-V) en plus du serveur.

## 3. Production — Sécurité

Un clavier incorrect fausse la saisie des mots de passe : tester avec un mot de passe temporaire avant le déploiement.

## Validation et retour arrière

- **Validation** : Les caractères `@`, `é` et `\` s'obtiennent avec les touches attendues.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2025](/01-fiches-simples/windows/server-2025/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2025)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)