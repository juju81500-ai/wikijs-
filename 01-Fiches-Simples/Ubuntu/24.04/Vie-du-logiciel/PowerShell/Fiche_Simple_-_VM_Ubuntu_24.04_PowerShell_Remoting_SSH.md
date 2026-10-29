# Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Remoting_SSH

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, accès sudo, dépôt Microsoft officiel
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : shell / scripting
- **Tags** : `ubuntu2404`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Activer le remoting PowerShell via SSH sur Ubuntu 24.04 LTS (sous-système `powershell` de sshd).

## 1. Hors-Production (Lab / Test / POC)

1. Installer le serveur SSH et le démarrer :
   ```bash
   sudo apt-get install -y openssh-server
   sudo systemctl enable --now ssh
   ```
   👉 Explication : le service Ubuntu se nomme `ssh`.

2. Localiser pwsh :
   ```bash
   command -v pwsh
   ```
   👉 Explication : le chemin (normalement `/usr/bin/pwsh`) est reporté dans le sous-système ; vérifier avant d'écrire la ligne.

3. Déclarer le sous-système dans un fichier dédié et contrôler la syntaxe :
   ```bash
   echo 'Subsystem powershell /usr/bin/pwsh -sshs -NoLogo -NoProfile' | sudo tee /etc/ssh/sshd_config.d/50-powershell.conf
   sudo sshd -t
   ```
   👉 Explication : ligne documentée par Microsoft ; `sshd -t` valide avant rechargement. Si votre sshd_config n'inclut pas `sshd_config.d`, ajouter la ligne directement dans `/etc/ssh/sshd_config`.

4. Recharger SSH :
   ```bash
   sudo systemctl reload ssh
   ```
   👉 Explication : applique la configuration sans couper les sessions existantes.

5. Depuis le client PowerShell 7, ouvrir une session (HOTE et UTILISATEUR sont à remplacer) :
   ```powershell
   Enter-PSSession -HostName HOTE -UserName UTILISATEUR
   Invoke-Command -HostName HOTE -UserName UTILISATEUR -ScriptBlock { $PSVersionTable.PSVersion }
   ```
   👉 Explication : `-HostName` utilise SSH ; Windows PowerShell 5.1 ne supporte pas ce mode (il utilise `-ComputerName` / WinRM).

6. Limiter l'accès SSH au réseau d'administration :
   ```bash
   sudo ufw allow from RESEAU_ADMIN to any port 22 proto tcp
   sudo ufw status
   ```
   👉 Explication : ufw n'est actif que s'il a été activé ; adapter à votre pare-feu existant (RESEAU_ADMIN : réseau d'administration, à remplacer).

## 2. Production — Contrôles

Utiliser l'authentification par clé et restreindre les utilisateurs autorisés (`AllowUsers`/`AllowGroups`). Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Désactiver l'authentification par mot de passe une fois les clés déployées (`PasswordAuthentication no`), après test.
- Ne pas autoriser la connexion root (`PermitRootLogin no`).
- Ne jamais passer de mot de passe en clair sur la ligne de commande.

## Validation et retour arrière

- **Validation** : `Enter-PSSession -HostName` ouvre une session et `$PSVersionTable` répond.
- **Retour arrière** : supprimer `/etc/ssh/sshd_config.d/50-powershell.conf`, lancer `sudo sshd -t` puis recharger le service.

## Si le problème n'est pas résolu

- [Microsoft Learn — remoting PowerShell via SSH](https://learn.microsoft.com/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
- [sshd_config — page de manuel](https://man.openbsd.org/sshd_config)
- [Fiche connexe — Prerequis Limites](Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Prerequis_Limites.md)
