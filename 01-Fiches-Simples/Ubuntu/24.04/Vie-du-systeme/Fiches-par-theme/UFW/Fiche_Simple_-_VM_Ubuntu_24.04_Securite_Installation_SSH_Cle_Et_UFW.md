# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Installation_SSH_Cle_Et_UFW.md

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Installation / Sécurité / Accès distant
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[openssh]`, `[ssh]`, `[ufw]`, `[ed25519]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer OpenSSH Server sur Ubuntu Server 24.04, préparer un accès par clé Ed25519 et désactiver l'authentification SSH par mot de passe seulement après validation de la clé.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer et démarrer le service Ubuntu `ssh` :
   ```bash
   sudo apt update
   sudo apt install openssh-server
   sudo systemctl enable --now ssh
   sudo systemctl status ssh --no-pager
   ```
2. Depuis le poste client, créer une clé si nécessaire et la déployer :
   ```bash
   ssh-keygen -t ed25519
   ssh-copy-id -i ~/.ssh/id_ed25519.pub <utilisateur>@<serveur>
   ```
   👉 *Explication : La clé privée reste sur le poste client; seule la clé publique est copiée sur le serveur.*

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier qu'une connexion par clé ouvre une seconde session avant de toucher à l'authentification par mot de passe.
2. Créer un fichier de configuration local :
   ```bash
   sudo install -o root -g root -m 0644 /dev/null /etc/ssh/sshd_config.d/99-local-hardening.conf
   sudo install -o root -g root -m 0644 /dev/null /etc/ssh/sshd_config.d/00-local-hardening.conf
   sudo tee /etc/ssh/sshd_config.d/00-local-hardening.conf >/dev/null <<'EOF'
   PermitRootLogin no
   PubkeyAuthentication yes
   PasswordAuthentication no
   KbdInteractiveAuthentication no
   EOF
   ```
3. Valider la syntaxe avant rechargement :
   ```bash
   sudo sshd -t
   sudo systemctl reload ssh
   sudo sshd -T | grep -E 'permitrootlogin|pubkeyauthentication|passwordauthentication|kbdinteractiveauthentication'
   ```
   👉 *Explication : Ubuntu utilise l'unité `ssh`; le rechargement applique la configuration sans interrompre les sessions établies.*

## 🔒 3. Production — Façon Sécurisée
1. Garder la session SSH actuelle ouverte et tester un nouvel accès par clé avant de fermer cette session.
2. Si UFW est utilisé, autoriser SSH avant toute activation du pare-feu :
   ```bash
   sudo ufw app list
   sudo ufw allow OpenSSH
   sudo ufw status verbose
   ```
   N'activer UFW à distance qu'après avoir défini les règles nécessaires aux autres services et confirmé un accès console.
3. Ne jamais copier la clé privée sur le serveur. Restreindre les droits du répertoire `~/.ssh` et du fichier `authorized_keys` du compte cible.

## ✅ Validation et retour arrière
- Tester `ssh -i ~/.ssh/id_ed25519 <utilisateur>@<serveur>` depuis une nouvelle session et confirmer que l'accès root est refusé.
- En cas d'échec, corriger ou retirer le fichier `/etc/ssh/sshd_config.d/99-local-hardening.conf` depuis la console, lancer `sshd -t`, puis recharger `ssh`.
 En cas d'échec, corriger ou retirer le fichier `/etc/ssh/sshd_config.d/00-local-hardening.conf` depuis la console, lancer `sshd -t`, puis recharger `ssh`.
- Examiner les échecs avec `sudo journalctl -u ssh --since today`.

## 🔗 Si le problème n'est pas résolu
- Vérifier l'adresse Netplan, le DNS, le pare-feu UFW et les permissions du compte distant.