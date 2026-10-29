# Fiche_Simple_-_VM_Rocky_9_PowerShell_Installer

- **Environnement** : VM Rocky Linux 9 de laboratoire, accès sudo, dépôt Microsoft pour RHEL 9
- **OS / Version** : Rocky Linux 9
- **Catégorie** : shell / scripting
- **Tags** : `rocky9`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Installer PowerShell 7 sur Rocky Linux 9 depuis le dépôt Microsoft.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le paquet de configuration du dépôt Microsoft pour RHEL 9 et l'inspecter :
   ```bash
   curl -sSL -o /tmp/packages-microsoft-prod.rpm https://packages.microsoft.com/config/rhel/9/packages-microsoft-prod.rpm
   rpm -qpi /tmp/packages-microsoft-prod.rpm
   ```
   👉 Explication : Rocky Linux 9 étant compatible RHEL 9, la documentation Microsoft RHEL est utilisée ; vérifier les métadonnées du paquet.

2. Enregistrer le dépôt puis contrôler l'origine du paquet :
   ```bash
   sudo rpm -i /tmp/packages-microsoft-prod.rpm
   sudo dnf makecache
   dnf info powershell
   ```
   👉 Explication : le dépôt affiché doit être celui de Microsoft.

3. Installer PowerShell et contrôler la version :
   ```bash
   sudo dnf install -y powershell
   pwsh -NoLogo -NoProfile -Command '$PSVersionTable.PSVersion.ToString()'
   ```
   👉 Explication : comparer la version affichée à celle approuvée.

4. Supprimer le fichier temporaire :
   ```bash
   rm -f /tmp/packages-microsoft-prod.rpm
   ```
   👉 Explication : nettoyage du paquet de configuration.

## 2. Production — Contrôles

Tester sur un pilote, figer la version approuvée et contrôler les mises à jour du dépôt Microsoft. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas installer depuis un miroir non autorisé.
- Contrôler la provenance du paquet de dépôt avant `rpm -i`.

## Validation et retour arrière

- **Validation** : `pwsh` affiche la version approuvée et le gestionnaire de paquets indique l'origine Microsoft.
- **Retour arrière** : désinstaller le paquet (`sudo dnf remove powershell`) puis retirer le paquet de dépôt si plus nécessaire.

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Linux](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-linux)
- [Microsoft Learn — remoting PowerShell via SSH](https://learn.microsoft.com/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Rocky_9_PowerShell_Prerequis_Limites.md)
