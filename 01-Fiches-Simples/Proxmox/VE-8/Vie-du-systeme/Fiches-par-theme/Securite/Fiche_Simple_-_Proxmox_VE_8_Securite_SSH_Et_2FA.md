# 📄 Fiche_Simple_-_Proxmox_VE_8_Securite_SSH_Et_2FA.md

- **Environnement** : Hyperviseur Proxmox VE 8 (accès SSH et interface web https://<nom_de_l_hote>:8006)
- **OS / Version** : Proxmox VE 8.x - Debian 12 Bookworm
- **Catégorie** : Sécurité / Accès distant et authentification
- **Tags** : `[proxmox-ve-8]`, `[debian-bookworm]`, `[ssh]`, `[2fa]`, `[totp]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Restreindre l'accès SSH à l'authentification par clé cryptographique, interdire la connexion root par mot de passe, puis imposer un second facteur (TOTP) aux comptes administrateurs de l'interface web Proxmox.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Générer une paire de clés ed25519 sur le poste d'administration :
```bash
ssh-keygen -t ed25519 -C "admin-proxmox@<domaine>" -f ~/.ssh/id_ed25519_proxmox
```
👉 Explication : crée la clé privée `~/.ssh/id_ed25519_proxmox` (à conserver uniquement sur le poste) et la clé publique `~/.ssh/id_ed25519_proxmox.pub` à déposer sur l'hôte.

2. Déposer la clé publique sur l'hôte Proxmox :
```bash
ssh-copy-id -i ~/.ssh/id_ed25519_proxmox.pub root@<nom_de_l_hote>
```
👉 Explication : ajoute la clé publique dans `/root/.ssh/authorized_keys` sur le nœud ; le mot de passe root n'est demandé que pour cette opération.

3. Tester l'authentification par clé :
```bash
ssh -i ~/.ssh/id_ed25519_proxmox root@<nom_de_l_hote> 'pveversion'
```
👉 Explication : ouvre une session sans mot de passe et exécute `pveversion` à distance ; ce test doit réussir avant toute désactivation de l'authentification par mot de passe.

---

## ⚡ 2. Production — Façon Simplifiée
1. Désactiver l'authentification SSH par mot de passe et limiter root aux clés :
```bash
printf 'PasswordAuthentication no\nPermitRootLogin prohibit-password\n' > /etc/ssh/sshd_config.d/90-durcissement.conf
```
👉 Explication : crée un fichier de configuration inclus au début de `/etc/ssh/sshd_config`, donc prioritaire sur les valeurs par défaut de Debian.

2. Valider la syntaxe puis recharger sshd :
```bash
sshd -t && systemctl reload ssh
```
👉 Explication : `sshd -t` contrôle la syntaxe sans rien appliquer ; `systemctl reload ssh` applique la configuration sans couper les sessions ouvertes. Garder une seconde session SSH ouverte pendant ce test.

3. Vérifier les valeurs effectivement appliquées :
```bash
sshd -T | grep -E '^(passwordauthentication|permitrootlogin) '
```
👉 Explication : `sshd -T` affiche la configuration réellement active ; le résultat attendu est `passwordauthentication no` et `permitrootlogin prohibit-password`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Créer un compte Linux nominatif pour l'administration, avec droits sudo :
```bash
adduser <utilisateur_admin>
apt install -y sudo && usermod -aG sudo <utilisateur_admin>
```
👉 Explication : remplace l'usage direct de root par un compte nominatif, traçable dans les journaux ; `sudo` élève ses privilèges uniquement lorsque c'est nécessaire.

2. Déclarer le même utilisateur dans Proxmox avec le rôle Administrator :
```bash
pveum user add <utilisateur_admin>@pam --comment "Administrateur nominatif"
pveum aclmod / -user <utilisateur_admin>@pam -role Administrator
```
👉 Explication : le realm `pam` s'appuie sur les comptes Linux créés à l'étape précédente ; le rôle Administrator est accordé à la racine de l'arbre des permissions.

3. Restreindre SSH aux seuls comptes autorisés et interdire root :
```bash
printf 'PasswordAuthentication no\nPermitRootLogin no\nAllowUsers <utilisateur_admin>\n' > /etc/ssh/sshd_config.d/90-durcissement.conf
sshd -t && systemctl reload ssh
```
👉 Explication : remplace le fichier de la façon simplifiée ; seul `<utilisateur_admin>` peut ouvrir une session SSH, et uniquement par clé. Tester une connexion avec cet utilisateur avant de fermer la session root.

4. Activer le second facteur TOTP sur chaque compte administrateur :
```bash
pveum user list
```
👉 Explication : liste les comptes Proxmox à protéger. Dans l'interface web, aller dans Datacenter > Permissions > Two Factor > Add > TOTP pour chaque compte, scanner le QR code avec une application d'authentification, puis conserver les codes de secours hors de l'hôte.

5. Contrôler les facteurs d'authentification enregistrés :
```bash
pvesh get /access/tfa
```
👉 Explication : liste les facteurs à deux facteurs enregistrés (TOTP, WebAuthn, codes de secours) ; chaque compte administrateur doit y figurer avant mise en production.
