# Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Installer

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, accès sudo, dépôt Microsoft officiel
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : shell / scripting
- **Tags** : `ubuntu2404`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Installer PowerShell 7 sur Ubuntu 24.04 LTS depuis le dépôt Microsoft.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les prérequis et télécharger le paquet de configuration du dépôt Microsoft :
   ```bash
   sudo apt-get update
   sudo apt-get install -y wget apt-transport-https software-properties-common
   wget -O /tmp/packages-microsoft-prod.deb https://packages.microsoft.com/config/ubuntu/24.04/packages-microsoft-prod.deb
   dpkg-deb -I /tmp/packages-microsoft-prod.deb
   ```
   👉 Explication : le dépôt est celui indiqué par la documentation Microsoft pour Ubuntu 24.04 ; contrôler les métadonnées avant installation.

2. Enregistrer le dépôt :
   ```bash
   sudo dpkg -i /tmp/packages-microsoft-prod.deb
   sudo apt-get update
   apt-cache policy powershell
   ```
   👉 Explication : le candidat doit provenir de packages.microsoft.com.

3. Installer PowerShell et contrôler la version :
   ```bash
   sudo apt-get install -y powershell
   pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : comparer la version affichée à celle approuvée.

4. Alternative documentée par Microsoft : le paquet Snap (vérifier sa disponibilité et sa politique de mise à jour) :
   ```bash
   sudo snap install powershell --classic
   ```
   👉 Explication : le paquet Snap se met à jour automatiquement, ce qui peut gêner une version figée ; ne pas combiner avec le paquet APT.

5. Supprimer le fichier temporaire :
   ```bash
   rm -f /tmp/packages-microsoft-prod.deb
   ```
   👉 Explication : nettoyage ; conserver la preuve de provenance si la procédure locale l'exige.

## 2. Production — Contrôles

Tester sur un pilote, figer la version approuvée et contrôler les mises à jour du dépôt Microsoft. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas installer depuis un miroir non autorisé.
- Contrôler la provenance du paquet de dépôt avant `dpkg -i`.

## Validation et retour arrière

- **Validation** : `pwsh` affiche la version approuvée et le gestionnaire de paquets indique l'origine Microsoft.
- **Retour arrière** : désinstaller le paquet (`sudo apt-get remove powershell`) puis retirer le paquet de dépôt si plus nécessaire.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Linux](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-linux)
- [Microsoft Learn — remoting PowerShell via SSH](https://learn.microsoft.com/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Prerequis_Limites.md)
