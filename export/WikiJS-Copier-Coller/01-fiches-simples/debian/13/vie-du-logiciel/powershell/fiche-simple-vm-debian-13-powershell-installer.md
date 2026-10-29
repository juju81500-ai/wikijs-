# Fiche_Simple_-_VM_Debian_13_PowerShell_Installer

- **Environnement** : VM Debian 13 de laboratoire avec dépôts Microsoft officiels
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : shell / scripting

---

## Problème précis à résoudre

Installer PowerShell 7 à partir du dépôt Microsoft authentifié pour Debian 13.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le paquet officiel de configuration du dépôt
   ```bash
   sudo apt update
   sudo apt install -y wget ca-certificates
   wget -O /tmp/packages-microsoft-prod.deb https://packages.microsoft.com/config/debian/13/packages-microsoft-prod.deb
   dpkg-deb -I /tmp/packages-microsoft-prod.deb
   ```
   👉 Explication : vérifier métadonnées, architecture et provenance avant installation.

2. Ajouter dépôt et contrôler origine APT
   ```bash
   sudo dpkg -i /tmp/packages-microsoft-prod.deb
   sudo apt update
   apt-cache policy powershell
   ```
   👉 Explication : le candidat doit pointer sur le dépôt Microsoft attendu.

3. Installer et vérifier pwsh
   ```bash
   sudo apt install powershell
   pwsh -NoLogo -NoProfile -Command "$PSVersionTable.PSVersion.ToString()"
   ```
   👉 Explication : comparer version affichée à la stable approuvée.

4. Retirer le paquet temporaire
   ```bash
   rm -f /tmp/packages-microsoft-prod.deb
   ```
   👉 Explication : conserver les éléments de preuve de provenance selon la procédure locale.

## 2. Production — Contrôles

Tester versions et modules sur pilote, utiliser APT maîtrisé et contrôler les mises à jour Microsoft.

## 3. Production — Sécurité

- Ne pas installer depuis un miroir non autorisé.
- Ne pas lancer pwsh en root par défaut.
- Ne pas ajouter credentials dans historique ou variables persistantes.

## Validation et retour arrière

- **Validation** : `pwsh` affiche la version approuvée et APT confirme l’origine Microsoft.
- **Retour arrière** : Désinstaller via APT si aucun script ne le requiert; préserver liste modules et profils.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer Debian](https://learn.microsoft.com/powershell/scripting/install/install-debian)
- [Microsoft Learn — sécurité](https://learn.microsoft.com/powershell/scripting/security/security-features)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/powershell/fiche-simple-vm-debian-13-powershell-prerequis-limites>)