---
title: "Fiche Simple - VM Debian 13 Securite Fail2ban"
description: "Installer Fail2ban sur Debian 13 pour bannir temporairement les adresses IP qui échouent répétitivement à s'authentifier sur SSH, en lisant les journaux systemd, sans modifier le fichier de configuration d'origine."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[debian13]", "[debian]", "[fail2ban]", "[ssh]", "[brute-force]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Securite_Fail2ban

- **Environnement** : VM ou serveur Debian 13 exposant SSH
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sécurité / Protection contre le brute-force
- **Tags** : `[debian13]`, `[debian]`, `[fail2ban]`, `[ssh]`, `[brute-force]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer Fail2ban sur Debian 13 pour bannir temporairement les adresses IP qui échouent répétitivement à s'authentifier sur SSH, en lisant les journaux systemd, sans modifier le fichier de configuration d'origine.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Fail2ban et vérifier son état par défaut :
   ```bash
   sudo apt-get update
   sudo apt-get install -y fail2ban
   sudo systemctl status fail2ban --no-pager
   sudo fail2ban-client status
   ```
   👉 Explication : Le paquet installe le démon et l'outil `fail2ban-client`. La commande `status` liste les prisons (jails) actives ; une prison `sshd` peut déjà être présente selon la configuration fournie par le paquet.

2. Provoquer volontairement des échecs d'authentification depuis un autre poste du lab :
   ```bash
   for i in 1 2 3 4 5 6; do ssh -o PubkeyAuthentication=no -o PreferredAuthentications=password utilisateur_inexistant@<ip_serveur> exit; done
   ```
   👉 Explication : Chaque tentative échoue et est journalisée. Au-delà du seuil `maxretry`, l'adresse du poste de test doit être bannie.

3. Vérifier le bannissement :
   ```bash
   sudo fail2ban-client status sshd
   ```
   👉 Explication : La ligne `Banned IP list` doit afficher l'adresse du poste de test. Le compteur `Currently failed` montre les échecs en cours.

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer une surcharge locale dans `/etc/fail2ban/jail.local` et ne jamais éditer `jail.conf` :
   ```bash
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOF'
   [DEFAULT]
   bantime = 1h
   findtime = 10m
   maxretry = 5
   ignoreip = 127.0.0.1/8 ::1 <reseau_admin>

   [sshd]
   enabled = true
   port = ssh
   backend = systemd
   EOF
   ```
   👉 Explication : `jail.local` surcharge `jail.conf` et survit aux mises à jour du paquet. `backend = systemd` lit les journaux via journald : sous Debian 13, `rsyslog` n'est pas forcément installé, et le fichier `/var/log/auth.log` peut alors être absent.

2. Contrôler la configuration puis redémarrer le service :
   ```bash
   sudo fail2ban-client -t
   sudo systemctl restart fail2ban
   sudo fail2ban-client status sshd
   ```
   👉 Explication : `fail2ban-client -t` vérifie la syntaxe avant le redémarrage. Remplacer `<reseau_admin>` par le réseau d'administration réel (par exemple `10.0.0.0/24`) pour ne jamais bannir l'équipe elle-même.

3. Consulter les actions de bannissement dans le journal :
   ```bash
   sudo journalctl -u fail2ban -n 50 --no-pager
   ```
   👉 Explication : Les lignes `Ban` et `Unban` confirment que la prison `sshd` agit réellement.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activer l'augmentation progressive de la durée de bannissement pour les récidivistes, en réécrivant `jail.local` en un seul bloc `[DEFAULT]` :
   ```bash
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOF'
   [DEFAULT]
   bantime = 1h
   bantime.increment = true
   bantime.maxtime = 1w
   findtime = 10m
   maxretry = 5
   ignoreip = 127.0.0.1/8 ::1 <reseau_admin>

   [sshd]
   enabled = true
   port = ssh
   backend = systemd
   EOF
   sudo fail2ban-client -t && sudo systemctl restart fail2ban
   ```
   👉 Explication : À chaque récidive, la durée de bannissement augmente, jusqu'à une semaine au maximum. Le fichier est réécrit entièrement pour éviter deux blocs `[DEFAULT]` dans le même fichier, ce qui peut bloquer le démarrage de Fail2ban.

2. Vérifier que `ignoreip` ne contient que le réseau d'administration, jamais `0.0.0.0/0` :
   ```bash
   sudo grep -n "ignoreip" /etc/fail2ban/jail.local
   ```
   👉 Explication : Une adresse ou un réseau trop large désactive la protection pour toutes les sources concernées.

3. Débannir une adresse légitime après une erreur de saisie, sans redémarrer le service :
   ```bash
   sudo fail2ban-client set sshd unbanip <ip_bloquee>
   ```
   👉 Explication : Libère immédiatement l'adresse indiquée. Tracer cette opération dans le registre d'exploitation.