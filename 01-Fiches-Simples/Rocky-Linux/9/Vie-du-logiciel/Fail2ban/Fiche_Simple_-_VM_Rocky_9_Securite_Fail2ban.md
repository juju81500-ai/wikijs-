# 📄 Fiche_Simple_-_VM_Rocky_9_Securite_Fail2ban.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 (paquet fail2ban fourni par EPEL)
- **Catégorie** : Sécurité / Protection contre le brute-force
- **Tags** : `[rocky9]`, `[rhel9]`, `[fail2ban]`, `[epel]`, `[ssh]`, `[firewalld]`

## 🎯 Problème précis à résoudre
Bloquer automatiquement les adresses IP qui échouent répétitivement à l'authentification SSH sur Rocky Linux 9, avec un blocage géré par firewalld.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer EPEL puis Fail2ban (le paquet n'est pas dans les dépôts de base) :
   ```bash
   sudo dnf install -y epel-release
   sudo dnf install -y fail2ban
   ```
   👉 Explication : Fail2ban est fourni par le dépôt EPEL sur Rocky Linux 9. Sans EPEL, `dnf` ne trouve pas le paquet.

2. Créer la configuration locale sans modifier `jail.conf` :
   ```bash
   sudo tee /etc/fail2ban/jail.local >/dev/null <<'EOF'
   [DEFAULT]
   bantime = 1h
   findtime = 10m
   maxretry = 5
   banaction = firewallcmd-rich-rules
   backend = systemd

   [sshd]
   enabled = true
   EOF
   ```
   👉 Explication : `jail.local` surcharge `jail.conf`, qui est remplacé à chaque mise à jour. `backend = systemd` lit le journal, et `firewallcmd-rich-rules` bloque via firewalld.

3. Activer le service et vérifier la prison SSH :
   ```bash
   sudo systemctl enable --now fail2ban
   sudo fail2ban-client status sshd
   ```
   👉 Explication : La commande affiche le nombre d'échecs détectés et la liste des IP actuellement bannies.

---

## ⚡ 2. Production — Façon Simplifiée
1. Ajouter l'adresse de l'administrateur dans la liste blanche, dans la section `[DEFAULT]` de `jail.local` :
   ```bash
   sudo vi /etc/fail2ban/jail.local
   sudo fail2ban-client reload
   ```
   👉 Explication : Ajouter `ignoreip = 127.0.0.1/8 ::1 <ip_administrateur>` pour éviter de se bannir soi-même. Le `reload` applique la modification sans arrêter la surveillance.

2. Tester le blocage puis le déblocage d'une adresse de test :
   ```bash
   sudo fail2ban-client set sshd banip <ip_de_test>
   sudo firewall-cmd --list-rich-rules
   sudo fail2ban-client set sshd unbanip <ip_de_test>
   ```
   👉 Explication : La règle rich-rule apparaît pendant le bannissement puis disparaît après le `unbanip`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Augmenter progressivement la durée de bannissement des récidivistes. Ajouter les deux lignes suivantes dans le bloc `[DEFAULT]` existant de `jail.local` (ne pas créer un second bloc `[DEFAULT]`) :
   ```ini
   bantime.increment = true
   bantime.maxtime = 1w
   ```
   ```bash
   sudo vi /etc/fail2ban/jail.local
   sudo fail2ban-client reload
   ```
   👉 Explication : Chaque nouveau bannissement d'une même IP double la durée, plafonnée à une semaine. Ces options sont disponibles dans Fail2ban 0.11, version fournie par EPEL pour Rocky Linux 9.

2. Surveiller les jails actives et leur statut global :
   ```bash
   sudo fail2ban-client status
   sudo journalctl -u fail2ban -p warning --no-pager -n 50
   ```
   👉 Explication : La première commande liste les jails actives. La seconde montre les avertissements du service, utiles après une modification de configuration.

3. Coupler Fail2ban à la désactivation des mots de passe SSH (voir la fiche Securite_SSH_Cle_Sshd) : une authentification par clé seule rend le brute-force inopérant.
   ```bash
   sudo sshd -T | grep -i '^passwordauthentication'
   ```
   👉 Explication : La valeur doit être `no`. Fail2ban reste un filet de sécurité, pas un remplacement du durcissement SSH.
