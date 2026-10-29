# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Securite_Fail2ban

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - paquet `fail2ban` depuis le dépôt universe
- **Catégorie** : Sécurité / Protection contre les intrusions et le brute-force
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[fail2ban]`, `[ssh]`, `[brute-force]`, `[jail]`, `[hardening]`

## 🎯 Problème précis à résoudre
Bloquer temporairement les adresses IP qui échouent répétitivement à s'authentifier sur SSH, sur Ubuntu Server 24.04 LTS, avec Fail2ban configuré via le journal systemd.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Fail2ban et vérifier le service :
   ```bash
   sudo apt update
   sudo apt install -y fail2ban
   systemctl status fail2ban --no-pager
   ```
   👉 *Explication : Le paquet installe l'unité `fail2ban.service` et le client `fail2ban-client`.*
2. Lister les prisons (jails) actives :
   ```bash
   sudo fail2ban-client status
   ```
   👉 *Explication : Par défaut, aucune prison n'est active tant que `jail.local` n'a pas été créé.*

## ⚡ 2. Production — Façon Simplifiée
1. Créer le fichier de configuration local, qui ne sera pas écrasé par les mises à jour :
   ```bash
   sudo install -o root -g root -m 0644 /dev/null /etc/fail2ban/jail.local
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOF'
   [DEFAULT]
   bantime  = 1h
   findtime = 10m
   maxretry = 4
   backend  = systemd
   ignoreip = 127.0.0.1/8 ::1 <reseau_admin>/24

   [sshd]
   enabled = true
   port    = ssh
   EOF
   ```
   👉 *Explication : `backend = systemd` lit le journal systemd, adapté à Ubuntu 24.04. `ignoreip` évite de bloquer le réseau d'administration ; remplacer `<reseau_admin>/24` par le réseau réel.*
2. Vérifier la configuration et recharger le service :
   ```bash
   sudo fail2ban-client -t
   sudo systemctl restart fail2ban
   sudo fail2ban-client status sshd
   ```
   👉 *Explication : `-t` contrôle la syntaxe ; la prison `sshd` doit afficher le nombre de tentatives et d'IP bannies.*

## 🔒 3. Production — Façon Sécurisée
1. Durcir la durée de bannissement pour les récidivistes avec la prison `recidive` :
   ```bash
   sudo tee -a /etc/fail2ban/jail.local >/dev/null <<'EOF'

   [recidive]
   enabled  = true
   bantime  = 1w
   findtime = 1d
   maxretry = 5
   EOF
   sudo systemctl restart fail2ban
   sudo fail2ban-client status recidive
   ```
   👉 *Explication : `recidive` surveille le journal de Fail2ban lui-même et bannit plus longtemps les IP déjà bannies plusieurs fois.*
2. Surveiller les bannissements dans le journal :
   ```bash
   sudo journalctl -u fail2ban --since today --no-pager
   ```
   👉 *Explication : Permet de détecter une attaque en cours et de vérifier que les règles se déclenchent.*

## ✅ Validation et retour arrière
- Depuis un poste de test non admin, provoquer quatre échecs d'authentification SSH et vérifier `sudo fail2ban-client status sshd`.
- Débannir une adresse : `sudo fail2ban-client set sshd unbanip <adresse_ip>`.
- Retour arrière : `sudo systemctl disable --now fail2ban` puis `sudo apt purge -y fail2ban`.
