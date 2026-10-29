# Fiche_Simple_-_VM_Debian_13_KeePassXC_Verifier_Mise_A_Jour.md

- **Environnement** : Poste Debian 13 amd64, KeePassXC AppImage en compte utilisateur
- **OS / Version** : Debian 13 Trixie amd64; KeePassXC 2.8.0
- **Catégorie** : gestionnaire de mots de passe local

---

## Problème précis à résoudre

Contrôler l'installation et appliquer une mise à jour sans risquer le coffre.

## 1. Hors-Production (Lab / Test / POC)

1. Revérifier signature et digest de l'AppImage installée :
   ```bash
   cd "$HOME/Téléchargements/keepassxc-2.8.0"
   gpg --verify KeePassXC-2.8.0-1-x86_64.AppImage.sig KeePassXC-2.8.0-1-x86_64.AppImage
   shasum -a 256 -c KeePassXC-2.8.0-1-x86_64.AppImage.DIGEST
   ```
   👉 Explication : confirme que le fichier n'a pas été altéré.

2. Rechercher des fichiers sensibles oubliés (exemples de motifs à adapter) :
   ```bash
   find "$HOME" -maxdepth 3 \( -name '*.csv' -o -name '*.key' \) -newer "$HOME/Téléchargements/keepassxc-2.8.0" 2>/dev/null
   ```
   👉 Explication : aucun CSV, export en clair ou fichier-clé ne doit rester dans un répertoire partagé.

3. À chaque mise à jour : télécharger les nouveaux artefacts officiels, revérifier signature et digest, puis ouvrir une copie de sauvegarde avant d'utiliser la nouvelle version avec le coffre actif.
   👉 Explication : évite de corrompre le coffre avec une version défaillante.

## 2. Production — Contrôles

Suivre les annonces de sécurité KeePassXC et planifier les mises à jour.

## 3. Production — Sécurité

- Ne mettre à jour que depuis le site ou les releases officiels.
- Ne pas laisser d'export en clair.

## Validation et retour arrière

- **Validation** : Signature, digest et version conformes; coffre de test s'ouvre et se sauvegarde.
- **Retour arrière** : Relancer l'ancienne AppImage conservée et restaurer le coffre depuis la sauvegarde.

## Si le problème n'est pas résolu

- [KeePassXC — téléchargements](https://keepassxc.org/download/)
- [KeePassXC — vérification des signatures](https://keepassxc.org/verifying-signatures/)
- [Guide complet KeePassXC 2.8.0 Debian 13](/02-fiches-completes/debian/13/installation-deploiement/79-deploiement-keepassxc-2-8-0-debian-13#7-verifications-et-mise-a-jour)