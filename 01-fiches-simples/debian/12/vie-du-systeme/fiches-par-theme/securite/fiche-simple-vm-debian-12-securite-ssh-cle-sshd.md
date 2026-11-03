# 📄 VM_Debian_12_Securite_SSH-Cle-Sshd.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Sécurité & Accès distant / Authentification SSH
- **Tags** : `[debian12]`, `[debian-family]`, `[ssh]`, `[sshd]`, `[ed25519]`, `[authorized-keys]`, `[hardening]`

## 🎯 Problème précis à résoudre
Passer un serveur Debian 12 à l'authentification SSH par clé cryptographique ed25519 uniquement, interdire la connexion directe de root et le mot de passe, en conservant une configuration `sshd` modulaire et validée avant rechargement.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Génération d'une paire de clés ed25519 sur le poste d'administration :
   `ssh-keygen -t ed25519 -C "<utilisateur>@<poste_administration>"`
   👉 Explication : Crée `~/.ssh/id_ed25519` (privée, à protéger par une passphrase) et `id_ed25519.pub` (publique).
2. Dépôt de la clé publique sur le serveur :
   `ssh-copy-id -i ~/.ssh/id_ed25519.pub <utilisateur>@<nom_du_serveur>`
   👉 Explication : Copie la clé publique dans `~/.ssh/authorized_keys` de l'utilisateur distant, avec les bonnes permissions.
3. Test de connexion par clé :
   `ssh -i ~/.ssh/id_ed25519 <utilisateur>@<nom_du_serveur>`
   👉 Explication : Ouvre une session sans saisir le mot de passe du compte ; garder cette session ouverte jusqu'à la fin des tests.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création d'un fichier de durcissement modulaire :
   `sudoedit /etc/ssh/sshd_config.d/10-durcissement.conf`
   👉 Explication : Debian 12 charge automatiquement `sshd_config.d/*.conf`. Y placer `PasswordAuthentication no`, `PermitRootLogin no`, `PubkeyAuthentication yes`, `KbdInteractiveAuthentication no` et `MaxAuthTries 3`.
2. Validation puis rechargement du démon SSH :
   `sudo sshd -t && sudo systemctl reload ssh`
   👉 Explication : `sshd -t` contrôle la syntaxe ; le rechargement n'est effectué que si le test réussit. Le service Debian s'appelle `ssh`.

---

## 🔒 3. Production — Façon Sécurisée (Moindre privilège & Audit)
1. Restriction des comptes autorisés à se connecter :
   `sudoedit /etc/ssh/sshd_config.d/10-durcissement.conf`
   👉 Explication : Ajouter `AllowUsers <utilisateur_admin>` pour n'autoriser que les comptes nominatifs listés ; tout autre compte est refusé.
2. Vérification de la configuration effective :
   `sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|pubkeyauthentication|allowusers) '`
   👉 Explication : Affiche les valeurs réellement appliquées par `sshd` après fusion de tous les fichiers de configuration.
3. Contrôle des permissions du répertoire SSH de l'administrateur :
   `sudo chmod 700 /home/<utilisateur_admin>/.ssh && sudo chmod 600 /home/<utilisateur_admin>/.ssh/authorized_keys`
   👉 Explication : Empêche les autres comptes de lire ou modifier les clés autorisées ; `sshd` refuse les fichiers trop permissifs.
