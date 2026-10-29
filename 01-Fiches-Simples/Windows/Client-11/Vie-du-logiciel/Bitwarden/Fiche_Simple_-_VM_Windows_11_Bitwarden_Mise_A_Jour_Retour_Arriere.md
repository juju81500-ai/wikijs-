# Fiche_Simple_-_VM_Windows_11_Bitwarden_Mise_A_Jour_Retour_Arriere

- **Environnement** : Poste Windows 11 géré avec compte de test
- **OS / Version** : Windows 11 Client
- **Catégorie** : gestionnaire de mots de passe / client
- **Tags** : `windows-11`, `bitwarden`, `mots-de-passe`, `mfa`, `securite`
---

## Problème précis à résoudre

Maintenir app/extension à jour et révoquer sessions en cas de poste remplacé.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier publication et éditeur
   ```text
   Client > À propos/Paramètres > mise à jour; comparer à la publication officielle.
   ```
   👉 Explication : libellés peuvent évoluer; ne pas utiliser de miroir.

2. Vérifier signature d’un installateur manuel
   ```powershell
   Get-AuthenticodeSignature -FilePath "$HOME\Downloads\Bitwarden-Installer.exe" | Format-List Status,SignerCertificate
   ```
   👉 Explication : remplacer le fichier à remplacer; signature doit être valide.

3. Tester MFA, verrouillage et synchronisation en pilote
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : ne pas commencer par un coffre professionnel critique. Détail à confirmer dans la documentation officielle avant application : Ouvrir coffre de test après mise à jour et vérifier session, MFA, sync et extension.

4. Révoquer session d’un appareil perdu/réinstallé
   ```text
   Portail > Paramètres > Sécurité > révoquer session/appareil selon doc officielle.
   ```
   👉 Explication : préserver accès de secours avant révocation de la session courante.

## 2. Production — Contrôles

Déployer par anneaux et disposer d’un contact support avant mise à jour généralisée.

## 3. Production — Sécurité

- Ne pas rétrograder vers version vulnérable.
- Révoquer session d’un appareil perdu ou réaffecté.
- Ne pas exporter en clair pour contourner un bug de synchronisation.

## Validation et retour arrière

- **Validation** : Version à jour, connexion/MFA/sync fonctionnent et aucun export en clair subsiste.
- **Retour arrière** : Révoquer l’appareil, réinstaller depuis canal officiel et restaurer client supporté si nécessaire.

## Si le problème n'est pas résolu

- [Bitwarden — téléchargement officiel](https://bitwarden.com/download/)
- [Bitwarden — application bureau](https://bitwarden.com/help/desktop-app/)
- [Bitwarden — exportation](https://bitwarden.com/help/export-your-data/)
- [Bitwarden — MFA](https://bitwarden.com/help/two-step-login/)
- [Fiche connexe](<Fiche_Simple_-_VM_Windows_11_Bitwarden_Prerequis_Limites.md>)
