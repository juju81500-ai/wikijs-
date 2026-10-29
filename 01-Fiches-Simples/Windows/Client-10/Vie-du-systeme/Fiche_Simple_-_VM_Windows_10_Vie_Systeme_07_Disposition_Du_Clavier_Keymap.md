# Fiche_Simple_-_VM_Windows_10_Vie_Systeme_07_Disposition_Du_Clavier_Keymap

- **Environnement** : PC Windows 10 (poste de travail)
- **OS / Version** : Windows 10; étape 07 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows10`, `vie-du-systeme`, `cycle-de-vie`, `etape-07`

---

## Problème précis à résoudre

Régler la disposition du clavier AZERTY français.

## 1. Hors-Production (Lab / Test / POC)

1. Ajouter ou choisir la disposition : **Paramètres > Heure et langue > Saisie > Paramètres avancés du clavier**, puis **Langue et région > Français > Options de langue > Claviers installés > Ajouter un clavier > Français**.
   ```powershell
   Set-WinUserLanguageList -LanguageList (New-WinUserLanguageList -Language fr-FR) -Force
   ```
   👉 Explication : garantit que la liste ne contient que le français, clavier AZERTY (`040C:0000040C`).

2. Ajouter une disposition supplémentaire si nécessaire (par exemple belge ou suisse), sans supprimer le français.
   ```powershell
   $L = Get-WinUserLanguageList
   $L[0].InputMethodTips.Add('080C:0000080C')
   Set-WinUserLanguageList $L -Force
   ```
   👉 Explication : ajoute la disposition français (Belgique) à la langue existante.

3. Changer de clavier au quotidien : **Windows + Espace**; régler le raccourci : **Paramètres > Heure et langue > Saisie > Paramètres avancés du clavier > Touches d'accès rapide de la langue de saisie**.
   👉 Explication : évite une saisie incorrecte du mot de passe.

4. Appliquer le clavier à l'écran de connexion.
   ```powershell
   Copy-UserInternationalSettingsToSystem -WelcomeScreen $true -NewUser $true
   Get-WinUserLanguageList | Select-Object LanguageTag,InputMethodTips
   ```
   👉 Explication : rend la disposition identique avant et après connexion.

## 2. Production — Contrôles

Un seul clavier par défaut pour l'ensemble du parc, défini par GPO ou profil Intune.

## 3. Production — Sécurité

Vérifier le clavier avant de saisir un mot de passe, notamment le code PIN ou BitLocker de démarrage.

## Validation et retour arrière

- **Validation** : Taper `AZERTY 123 &é"'(` dans le Bloc-notes donne les caractères attendus.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows 10](./Sommaire_-_Vie_du_systeme_Windows_10.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)
