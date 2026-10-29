# Fiche_Simple_-_VM_Windows_11_Bitwarden_Installer

- **Environnement** : Poste Windows 11 géré avec compte de test
- **OS / Version** : Windows 11 Client
- **Catégorie** : gestionnaire de mots de passe / client

---

## Problème précis à résoudre

Installer client Windows Bitwarden officiel et vérifier signature Authenticode.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger depuis Bitwarden
   ```text
   Navigateur > ouvrir la documentation officielle : https://bitwarden.com/download/
   ```
   👉 Explication : ne pas utiliser un site miroir ou une publicité. Détail à confirmer dans la documentation officielle avant application : Ouvrir https://bitwarden.com/download/ et télécharger l’application Windows.

2. Vérifier signature du fichier téléchargé
   ```powershell
   Get-AuthenticodeSignature -FilePath "$HOME\Downloads\Bitwarden-Installer.exe" | Format-List Status,SignerCertificate
   ```
   👉 Explication : remplacer nom de fichier si différent; exiger signature valide de l’éditeur attendu.

3. Vérifier onglet de signature puis démarrer l’assistant
   ```text
   Explorateur > Téléchargements > clic droit > Propriétés > Signatures numériques; confirmer signature puis double-cliquer le fichier.
   ```
   👉 Explication : annuler si signature absente ou invalide.

4. Lancer client et vérifier version
   ```text
   Démarrer > Bitwarden > À propos (libellé à vérifier selon version).
   ```
   👉 Explication : ne pas se connecter avant d’avoir validé la source.

## 2. Production — Contrôles

Tester sur poste pilote, inventorier version/éditeur et contrôler mise à jour avant diffusion.

## 3. Production — Sécurité

- Ne pas contourner SmartScreen ou signature invalide.
- Ne pas saisir mot de passe via un lien reçu.
- Ne pas synchroniser sur un poste non géré.

## Validation et retour arrière

- **Validation** : Client démarre, signature est valide et version vient du canal officiel.
- **Retour arrière** : Désinstaller via Paramètres > Applications; préserver données à conserver seulement selon procédure officielle.

## Si le problème n'est pas résolu

- [Bitwarden — téléchargement officiel](https://bitwarden.com/download/)
- [Bitwarden — application bureau](https://bitwarden.com/help/desktop-app/)
- [Bitwarden — exportation](https://bitwarden.com/help/export-your-data/)
- [Bitwarden — MFA](https://bitwarden.com/help/two-step-login/)
- [Fiche connexe](</01-fiches-simples/windows/client-11/vie-du-logiciel/bitwarden/fiche-simple-vm-windows-11-bitwarden-prerequis-limites>)