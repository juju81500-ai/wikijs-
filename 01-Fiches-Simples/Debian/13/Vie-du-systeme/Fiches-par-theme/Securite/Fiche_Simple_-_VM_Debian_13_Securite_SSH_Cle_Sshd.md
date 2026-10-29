# 📄 Fiche_Simple_-_VM_Debian_13_Securite_SSH_Cle_Sshd

- **Environnement** : VM ou serveur Debian 13 accessible en SSH
- **OS / Version** : Debian 13 (Trixie) - OpenSSH 10.x - Famille Debian
- **Catégorie** : Sécurité / Accès distant (SSH)
- **Tags** : `[debian13]`, `[debian]`, `[ssh]`, `[sshd]`, `[cle-ssh]`, `[hardening]`

## 🎯 Problème précis à résoudre
Remplacer l'authentification SSH par mot de passe par une authentification par clé ed25519 sur Debian 13, interdire la connexion directe de `root` et limiter l'accès SSH aux comptes autorisés, sans se verrouiller hors du serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Sur le poste d'administration, générer une paire de clés ed25519 :
   ```bash
   ssh-keygen -t ed25519 -C "<utilisateur>@<poste_admin>" -f ~/.ssh/id_ed25519_<nom_du_serveur>
   ```
   👉 Explication : Crée une clé privée (à conserver uniquement sur le poste d'administration) et une clé publique `.pub` (à déposer sur le serveur). OpenSSH 10.x de Debian 13 accepte ed25519 par défaut et refuse les algorithmes obsolètes comme DSA.

2. Déposer la clé publique sur le serveur de test :
   ```bash
   ssh-copy-id -i ~/.ssh/id_ed25519_<nom_du_serveur>.pub <utilisateur>@<ip_serveur>
   ```
   👉 Explication : Ajoute la clé dans `~/.ssh/authorized_keys` de l'utilisateur distant. Le mot de passe n'est demandé qu'une dernière fois.

3. Tester la connexion par clé depuis une nouvelle session :
   ```bash
   ssh -i ~/.ssh/id_ed25519_<nom_du_serveur> <utilisateur>@<ip_serveur> 'hostname && whoami'
   ```
   👉 Explication : Vérifie que l'authentification par clé fonctionne avant de désactiver les mots de passe. Ne pas fermer la session SSH existante tant que ce test n'a pas réussi.

---

## ⚡ 2. Production — Façon Simplifiée
1. Corriger les permissions du répertoire `.ssh` de l'utilisateur, sans quoi OpenSSH ignore la clé :
   ```bash
   sudo install -d -m 700 -o <utilisateur> -g <utilisateur> /home/<utilisateur>/.ssh
   sudo chmod 600 /home/<utilisateur>/.ssh/authorized_keys
   sudo chown <utilisateur>:<utilisateur> /home/<utilisateur>/.ssh/authorized_keys
   ```
   👉 Explication : `.ssh` doit être en `0700` et `authorized_keys` en `0600`, propriétaires de l'utilisateur. Des droits trop ouverts provoquent un refus silencieux de la clé.

2. Créer un fichier drop-in dans `/etc/ssh/sshd_config.d/`, inclus par défaut dans le `sshd_config` de Debian 13 :
   ```bash
   sudo tee /etc/ssh/sshd_config.d/10-tssr-hardening.conf >/dev/null <<'EOF'
   PermitRootLogin no
   PasswordAuthentication no
   KbdInteractiveAuthentication no
   PubkeyAuthentication yes
   MaxAuthTries 3
   AllowUsers <utilisateur>
   EOF
   ```
   👉 Explication : Ce fichier est lu avant le fichier principal `/etc/ssh/sshd_config` ; ses directives priment donc sur les valeurs par défaut. Ne pas éditer directement `sshd_config`, qui est remplacé lors des mises à jour du paquet.

3. Contrôler la syntaxe, recharger le démon et vérifier la configuration effective :
   ```bash
   sudo sshd -t && sudo systemctl reload ssh
   sudo sshd -T | grep -E '^(permitrootlogin|passwordauthentication|allowusers|pubkeyauthentication)'
   ```
   👉 Explication : `sshd -t` valide la syntaxe sans appliquer la configuration. `sshd -T` affiche la configuration réellement active. Sous Debian 13, l'unité systemd s'appelle `ssh.service`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Garder la session existante ouverte, puis valider depuis une seconde session que l'authentification par clé est seule acceptée :
   ```bash
   ssh -o PreferredAuthentications=publickey -i ~/.ssh/id_ed25519_<nom_du_serveur> <utilisateur>@<ip_serveur> 'exit'
   ```
   👉 Explication : Le test force la méthode `publickey`. Si la connexion échoue, la première session permet encore de corriger la configuration.

2. Restreindre le port SSH au réseau d'administration dans le pare-feu hôte (voir la fiche nftables de Debian 13), puis contrôler la règle active :
   ```bash
   sudo nft list ruleset | grep "dport 22"
   ```
   👉 Explication : Le port 22 ne doit accepter que le réseau d'administration (par exemple `<reseau_admin>`), jamais `0.0.0.0/0` en production.

3. Protéger la clé privée par une phrase de passe, et contrôler les connexions réussies et échouées :
   ```bash
   ssh-keygen -p -f ~/.ssh/id_ed25519_<nom_du_serveur>
   sudo journalctl -u ssh --since today --no-pager | grep -Ei "accepted|failed" | tail -n 20
   ```
   👉 Explication : La phrase de passe protège la clé si le poste est compromis. Le journal `ssh` permet de repérer des tentatives répétées, à compléter par une protection contre le brute-force (voir la fiche Fail2ban de Debian 13).
