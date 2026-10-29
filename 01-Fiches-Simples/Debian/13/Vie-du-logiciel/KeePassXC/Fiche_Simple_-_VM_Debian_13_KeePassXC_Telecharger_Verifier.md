# Fiche_Simple_-_VM_Debian_13_KeePassXC_Telecharger_Verifier.md

- **Environnement** : Poste Debian 13 amd64, KeePassXC AppImage en compte utilisateur
- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0
- **Catégorie** : gestionnaire de mots de passe local
- **Tags** : `debian13`, `keepassxc`, `kdbx`, `argon2id`, `appimage`

---

## Problème précis à résoudre

Télécharger l'AppImage officielle et vérifier signature PGP et digest SHA-256 avant de l'exécuter.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un répertoire dédié et télécharger les trois fichiers de la release :
   ```bash
   mkdir -p "$HOME/Téléchargements/keepassxc-2.8.0"
   cd "$HOME/Téléchargements/keepassxc-2.8.0"
   curl --fail --location --proto '=https' --tlsv1.2 -O https://github.com/keepassxreboot/keepassxc/releases/download/2.8.0/KeePassXC-2.8.0-1-x86_64.AppImage
   curl --fail --location --proto '=https' --tlsv1.2 -O https://github.com/keepassxreboot/keepassxc/releases/download/2.8.0/KeePassXC-2.8.0-1-x86_64.AppImage.sig
   curl --fail --location --proto '=https' --tlsv1.2 -O https://github.com/keepassxreboot/keepassxc/releases/download/2.8.0/KeePassXC-2.8.0-1-x86_64.AppImage.DIGEST
   ```
   👉 Explication : récupère l'application, sa signature et son digest en HTTPS.

2. Importer la clé de publication et vérifier son empreinte :
   ```bash
   gpg --keyserver keys.openpgp.org --recv-keys BF5A669F2272CF4324C1FDA8CFB4C2166397D0D2
   gpg --fingerprint BF5A669F2272CF4324C1FDA8CFB4C2166397D0D2
   ```
   👉 Explication : l'empreinte doit être exactement `BF5A 669F 2272 CF43 24C1 FDA8 CFB4 C216 6397 D0D2`.

3. Vérifier la signature et le digest :
   ```bash
   gpg --verify KeePassXC-2.8.0-1-x86_64.AppImage.sig KeePassXC-2.8.0-1-x86_64.AppImage
   shasum -a 256 -c KeePassXC-2.8.0-1-x86_64.AppImage.DIGEST
   ```
   👉 Explication : la signature doit être valide et le digest afficher `OK`.

## 2. Production — Contrôles

Conserver la trace de la vérification (empreinte, date, version).

## 3. Production — Sécurité

- Ne pas exécuter le fichier si signature, empreinte ou digest ne correspondent pas.
- Un avertissement de confiance GPG n'est acceptable que si l'empreinte est celle publiée.

## Validation et retour arrière

- **Validation** : Signature valide, empreinte conforme, digest `OK`.
- **Retour arrière** : Supprimer le répertoire `$HOME/Téléchargements/keepassxc-2.8.0` et son contenu.

## Si le problème n'est pas résolu

- [KeePassXC — vérification des signatures](https://keepassxc.org/verifying-signatures/)
- [KeePassXC — téléchargements](https://keepassxc.org/download/)
- [Guide complet KeePassXC 2.8.0 Debian 13](../../../../../02-Fiches-Completes/Debian/13/Installation-Deploiement/79_Deploiement_KeePassXC_2.8.0_Debian_13.md#2-telecharger-et-verifier-lappimage)
