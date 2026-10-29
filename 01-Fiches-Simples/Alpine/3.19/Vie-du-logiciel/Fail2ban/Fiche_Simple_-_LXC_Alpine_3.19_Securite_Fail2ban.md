# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Securite_Fail2ban.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Sécurité / Protection contre le brute-force
- **Tags** : `[alpine3.19]`, `[alpine]`, `[lxc]`, `[fail2ban]`, `[ssh]`, `[openrc]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Fail2ban sur un conteneur Alpine Linux pour bloquer temporairement les adresses qui échouent répétitivement à l'authentification SSH, sans se verrouiller soi-même hors du conteneur.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier que le dépôt community est activé, puis installer Fail2ban :
   ```sh
   grep community /etc/apk/repositories
   apk update
   apk add fail2ban
   ```
   👉 Explication : Fail2ban est fourni par le dépôt `community`. Si la ligne est absente ou commentée (`#`), l'activer dans `/etc/apk/repositories` avant l'installation.

2. Activer le service OpenRC et le démarrer :
   ```sh
   rc-update add fail2ban default
   rc-service fail2ban start
   rc-service fail2ban status
   ```
   👉 Explication : Le runlevel `default` lance Fail2ban à chaque démarrage du conteneur.

3. Vérifier que sshd journalise bien les échecs dans le fichier lu par Fail2ban :
   ```sh
   tail -n 20 /var/log/messages | grep sshd
   ```
   👉 Explication : Sous Alpine, syslog écrit dans `/var/log/messages`. Sans ces lignes, le jail `sshd` ne verra aucun échec.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer `/etc/fail2ban/jail.local` sans modifier `jail.conf` :
   ```ini
   [DEFAULT]
   bantime  = 1h
   findtime = 10m
   maxretry = 5
   ignoreip = 127.0.0.1/8 ::1 <ip_administration>

   [sshd]
   enabled  = true
   port     = ssh
   logpath  = /var/log/messages
   backend  = auto
   ```
   👉 Explication : `jail.local` surcharge `jail.conf` lors des mises à jour du paquet. `ignoreip` protège l'adresse d'administration contre un bannissement accidentel.

2. Recharger le service et contrôler le jail `sshd` :
   ```sh
   rc-service fail2ban restart
   fail2ban-client status sshd
   ```
   👉 Explication : La commande affiche le nombre de tentatives échouées et la liste des adresses bannies.

---

## 🔒 3. Production — Façon Sécurisée
1. Vérifier que le conteneur peut réellement bannir une adresse. Dans un LXC non privilégié, les règles de pare-feu peuvent être interdites :
   ```sh
   iptables -S
   ```
   👉 Explication : Si la commande échoue, le bannissement ne fonctionne pas dans le conteneur. Dans ce cas, appliquer le blocage au niveau du pare-feu Proxmox de l'hôte, et ne considérer Fail2ban que comme outil de détection.

2. Prévoir la récupération d'un accès bloqué depuis une autre adresse d'administration :
   ```sh
   fail2ban-client set sshd unbanip <ip_bannie>
   ```
   👉 Explication : Cette commande retire une adresse du jail sans redémarrer le service. Garder la console Proxmox accessible pendant les premiers tests.
